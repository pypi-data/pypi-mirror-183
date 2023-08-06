import decimal
import sys
from typing import TypedDict, Callable, TypeVar
from datetime import date, datetime
import asyncio

from graphql import GraphQLError
from graphql.type.definition import GraphQLObjectType, GraphQLEnumType, get_named_type, is_list_type, is_non_null_type
from ariadne import UnionType
from ariadne.types import GraphQLResolveInfo
from sqlalchemy import MetaData, ColumnElement, select, Executable, cast, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.exc import MultipleResultsFound
from pyparsing import ParseException

from .auth_utils import User
from .graphql_app import check_permission, HideResult
from .filter_parser import number_filter_parser, date_filter_parser, datetime_filter_parser, boolean_filter_parser


M = TypeVar('M', bound=DeclarativeBase)
nulldate = date(1753, 1, 1)  # For Incadea Tables


class FieldFilter(TypedDict):
    field_name: str
    value: str


model_types = UnionType('ModelTypes')

@model_types.type_resolver
def resolve_model_types(obj, *_):
    return obj['__typename']


# Shortcuts

def get_table_primary_keys(model: type[M]) -> list[ColumnElement]:
    return [col for col in model.__mapper__.columns if col.primary_key]


def filter_primary_key(q: Executable, model: type[M], primary_key_values: list[str]):
    pk_cols = get_table_primary_keys(model)
    try:
        for i, pk_val in enumerate(primary_key_values):
            q = q.where(pk_cols[i] == pk_val)
    except IndexError:
        raise GraphQLError(f"You have specified more primary keys values than there are columns for model {model.__name__}")
    return q


def get_user(info: GraphQLResolveInfo) -> User:
    return info.context['request'].user


def get_db(info) -> AsyncConnection:
    return info.context['request'].state.db


async def get_or_none(db: AsyncConnection, model: type[M], primary_keys: list, column: ColumnElement | None = None) -> M | None:
    result = await db.execute(filter_primary_key(select(column or model), model, primary_keys))
    if column is not None:
        return result.scalar_one_or_none()
    else:
        return result.one_or_none()


async def get_or_error(db: AsyncConnection, model: type[M], primary_keys: list, column: ColumnElement | None = None) -> M:
    try:
        row: M | None = await get_or_none(db, model, primary_keys, column)
    except MultipleResultsFound:
        raise GraphQLError(f"Primary keys: {primary_keys} returned more than one row")
    if row is None:
        raise GraphQLError(f"Could not find {model.name}: {primary_keys}")
    return row


# Resover Tools

def separate_filters(filters: list[FieldFilter], field_names_to_separate: list[str]):
    """ When some filters are automatically handled, and others you need to write custom SQLAlchemy queries """
    newfilters = []
    separated = []
    for f in filters:
        if f['field_name'] in field_names_to_separate:
            separated.append(f)
        else:
            newfilters.append(f)
    return newfilters, separated


def model_to_dict(model, remove_fields: list[str] = None):  # Todo: Maybe remove since switching to core
    if remove_fields is None:
        remove_fields = []
    return {
        field: getattr(model, field)
        for field in model.__mapper__.column_attrs.keys()
        if field not in remove_fields
    }


# Complete Resolvers

def resolve_type_inspector_factory(table_metadata: MetaData):
    tables_dict = {table.name: table for table in table_metadata.tables.values()}

    def resolve_type_inspector(_, info: GraphQLResolveInfo, type_name: str):
        gqltype = info.schema.get_type(type_name)
        if gqltype is None or not isinstance(gqltype, GraphQLObjectType):
            return None

        #Primary Keys
        if hasattr(gqltype, '__tablename__'):
            table: Table | None = tables_dict.get(gqltype.__tablename__)
            if table is None:
                raise GraphQLError(f"Could not find table with name{gqltype.__tablename__}")
            primary_keys = [col.name for col in get_table_primary_keys(table)]
        else:
            primary_keys = None

        # Filters
        all_filter = hasattr(gqltype, '__all_filter__')
        field_details = []
        for field_name, field in gqltype.fields.items():
            has_filter = False
            if hasattr(field, '__filter__'):
                if getattr(field, '__filter__'):
                    has_filter = True
            elif all_filter:
                has_filter = True

            field_filter_type = None
            if has_filter:
                field_type = get_named_type(field.type)
                if field_type is None:
                    raise Exception('Can only filter on Named Types')
                # Deducing filter type by GraphQL type. Contrary to simple_table_resolver
                if is_list_type(field.type) or (is_non_null_type(field.type) and is_list_type(field.type.of_type)):
                    field_filter_type = 'LIST'  # If list, it means it's a postgresql array and only = comparator works
                elif field_type.name == 'String':
                    field_filter_type = 'STRING'
                elif field_type.name in ['Int', 'Float']:
                    field_filter_type = 'NUMBER'
                elif field_type.name in ['Date', 'DateTime']:
                    field_filter_type = 'DATE'
                elif field_type.name == 'Boolean':
                    field_filter_type = 'BOOLEAN'
                elif isinstance(field_type, GraphQLEnumType):
                    field_filter_type = 'STRING'  # Consider Enum as strings
                else:
                    raise GraphQLError(f'Type {field_type.name} cannot support filtering on field {field_name}')

            # Todo: implement editable
            field_details.append({'field_name': field_name, 'filter_type': field_filter_type, 'editable': False})

        return {'field_details': field_details, 'primary_keys': primary_keys}
    return resolve_type_inspector


def load_from_table_query(model: type[M], filters: list[FieldFilter], limit: int | None, offset: int | None,
                          query_modifier: Callable[[Executable], Executable] | None = None, init_query: Executable | None = None) -> Executable:
    q = select(model) if init_query is None else init_query

    for f in filters:
        full_name = f['field_name']
        value = f['value']

        # field_name, *relation_names = full_name.split('.')[::-1]
        # current_model = table
        # for relation_name in relation_names:
        #     # Get Relation model and alias it
        #     current_model = aliased(getattr(current_model, relation_name).mapper.class_)
        #     q = q.join(current_model)
        #
        # field = getattr(current_model, field_name)
        # Todo: fix above
        field = getattr(model, full_name)
        field_type = field.type.python_type

        # Deducing filter type by model column type. Contrary to resolve_type_inspector.
        try:
            if field_type is str:
                q = q.where(cast(field, String).ilike(value))  # cast used to make Enum behave like strings.
            elif field_type in [int, float, decimal.Decimal]:
                q = number_filter_parser(q, field, value)
            elif field_type is date:
                q = date_filter_parser(q, field, value)
            elif field_type is datetime:
                q = datetime_filter_parser(q, field, value)
            elif field_type is bool:
                q = boolean_filter_parser(q, field, value)
            elif field_type is list:
                q = q.where(field.any_() == value)
            else:
                raise GraphQLError(f'Cannot filter on column type {field_type}')
        except ParseException as e:
            raise GraphQLError(f'Cannot parse value: {value} for field {field} of type {field_type} [{e}]')

    if query_modifier is not None:
        q = query_modifier(q)

    return q.limit(limit).offset(offset)


def resolve_type_loader_factory(table_metadata: MetaData):
    tables_dict = {table.name: table for table in table_metadata.tables.values()}

    async def resolve_type_loader(_, info, type_name, filters: list[FieldFilter], limit: int, offset: int):
        gqltype = info.schema.get_type(type_name)
        if gqltype is None:  # Check if Type exists in GQL
            raise GraphQLError(f'Type {type_name} does not exist')
        table_name = getattr(gqltype, '__tablename__', None)
        if table_name is None:  # Check if GQL type is configured
            raise GraphQLError(f'Type {type_name} is linked to a DB Table')

        table = tables_dict.get(table_name)
        if table is None:  # Check if model is found
            raise GraphQLError(f"Could not find {table_name} is database metadata")

        q = load_from_table_query(table, filters, limit, offset)
        rows = []
        for rowm in (await get_db(info).execute(q)).mappings().all():
            row = dict(rowm)
            row['__typename'] = type_name
            rows.append(row)
        return rows

    return resolve_type_loader


def simple_table_resolver_factory(model: type[M], query_modifiers=None):
    async def simple_table_resolver(_, info, filters: list[FieldFilter], limit: int, offset: int) -> list[M]:
        q = load_from_table_query(model, filters, limit, offset, query_modifiers)
        return (await get_db(info).execute(q)).all()
    return simple_table_resolver


async def external_module_executor(module_name, *args: str):
    proc = await asyncio.create_subprocess_exec(sys.executable, '-u', '-m', f'scripts.{module_name}', *args,
                                                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    while not proc.stdout.at_eof():
        data = await proc.stdout.readline()
        yield data.decode().rstrip()

    error = await proc.stderr.read()
    if error:
        raise GraphQLError(error.decode().rstrip())


def subscription_permission_check(generator):
    async def new_generator(obj, info, *args, **kwargs):
        try:
            check_permission(info)
        except HideResult:
            yield None
            return

        async for res in generator(obj, info, *args, **kwargs):
            yield res

    return new_generator
