import collections.abc
import typing
import dataclasses

IdentifierType = typing.Any

DataFrame = typing.Any
DataFrameColumn = typing.Any

DataFrameName = str
DataFrameFieldName = str
DataFrameFieldValue = typing.Any

FilterClause = collections.abc.Mapping
FilterClauseOperation = typing.Callable

SortDirection = typing.Literal['asc', 'desc']
SortClause = collections.abc.Mapping[DataFrameFieldName, SortDirection]

FilterClauseElement = tuple[DataFrameFieldName, FilterClauseOperation, DataFrameFieldValue]

ConnectionData = typing.Any
MutationData = collections.abc.Mapping[str, typing.Any]


class DataFrameLink(typing.Protocol):
    source_key: DataFrameColumn
    target_key: DataFrameColumn


@dataclasses.dataclass
class FilterClauseElement:
    frame_name: DataFrameName
    field_name: DataFrameFieldName
    operator: FilterClauseOperation
    value: DataFrameFieldValue


@dataclasses.dataclass(eq=True)
class Field:
    name: str
    alias: str | None = None
    relation: str | None = None
    expression: str | None = None


@dataclasses.dataclass
class Node:
    relation: str
    fields: collections.abc.MutableSequence[Field]
    name: str | None = None
    filter: FilterClause | None = None
    sort: SortClause | None = None
    limit: int | None = None
    offset: int | None = None
    modifier: typing.Callable = None

    @property
    def qualified_name(self):
        return self.name or self.relation


@dataclasses.dataclass
class Query:
    root_node: Node
    with_total: bool = False


class DataFrameRegistry(typing.Protocol):
    def get_link(
        self,
        source_frame: str,
        target_frame: str
    ) -> DataFrameLink: ...

    def get_column(
        self,
        frame_name: str,
        field_name: str,
        prefix: str | None = None,
        alias: str | None = None
    ) -> DataFrameColumn:
        ...

    def get_frame(self, frame_name: str) -> DataFrame:
        ...

    def get_primary_key(self, frame_name: str) -> DataFrameColumn | None:
        ...


class QueryResultProxy(typing.Protocol):
    def get_all(self): ...

    def get_one(self): ...

    def get_total(self): ...


class DataVendor(typing.Protocol):
    async def get(self, query: Query | None = None) -> QueryResultProxy | None: ...

    async def save(
        self,
        data: MutationData | collections.abc.Sequence[MutationData]
    ) -> typing.NoReturn: ...

    async def insert(
        self,
        data: MutationData | collections.abc.Sequence[MutationData]
    ) -> typing.NoReturn: ...

    async def delete(
        self,
        filter_clause: FilterClause
    ) -> typing.NoReturn: ...


class DataVendorConnection(typing.Protocol):
    async def execute(self, data: ConnectionData): ...


class DataVendorConnectionPool(typing.Protocol):
    async def get_connection(self) -> DataVendorConnection: ...

    async def close_connection(self, connection: DataVendorConnection): ...


class DataFilterBuilder(typing.Protocol):
    def __call__(self, clause: FilterClause): ...


@dataclasses.dataclass
class DataFrameBucket:
    frame_name: str
    data: collections.abc.Sequence[MutationData] | MutationData
    purge_key: str | None = None


class DataFrameSeparator(typing.Protocol):
    def __call__(self, data: collections.abc.Mapping) -> collections.abc.Mapping[DataFrameName, DataFrameBucket]: ...


class DataFrameMutator(typing.Protocol):
    async def insert(
        self,
        bucket: DataFrameBucket
    ): ...

    async def delete(
        self,
        filter_clause: collections.abc.Sequence[FilterClauseElement] | FilterClauseElement
    ): ...

    async def save(
        self,
        bucket: DataFrameBucket
    ): ...
