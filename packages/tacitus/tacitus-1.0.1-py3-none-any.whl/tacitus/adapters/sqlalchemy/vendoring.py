import collections.abc
import functools
import typing

from .obtaining import SqlAlchemyQueryResolver, QueryResultProxy
from .saving import SqlAlchemyDataFrameMutator, SqlAlchemyDataFrameSeparator
from .building import FilterBuilder
from ...definitions import contracts


class SqlAlchemyVendor(contracts.DataVendor):
    def __init__(
        self,
        registry: contracts.DataFrameRegistry,
        connection: contracts.DataVendorConnection
    ):
        self._registry = registry
        self._connection = connection

    @functools.cached_property
    def _query_resolver(self):
        return SqlAlchemyQueryResolver(
            registry=self._registry,
            connection=self._connection
        )

    @functools.cached_property
    def _data_frame_separator(self):
        return SqlAlchemyDataFrameSeparator(
            registry=self._registry,
        )

    @functools.cached_property
    def _data_frame_mutator(self):
        return SqlAlchemyDataFrameMutator(
            registry=self._registry,
            connection=self._connection
        )

    async def get(self, query: contracts.Query | None = None) -> QueryResultProxy | None:
        if query is None:
            return

        data = await self._query_resolver.resolve_query(query)
        total = None

        if query.with_total:
            data, total = data

        return QueryResultProxy(
            data=data,
            total=total
        )

    async def insert(
        self,
        data: contracts.MutationData | collections.abc.Sequence[contracts.MutationData]
    ) -> typing.NoReturn:
        if data:
            buckets = self._data_frame_separator(data)
            for bucket in buckets.values():
                await self._data_frame_mutator.insert(bucket)

    async def save(
        self,
        data: contracts.MutationData | collections.abc.Sequence[contracts.MutationData]
    ) -> typing.NoReturn:
        if data:
            buckets = self._data_frame_separator(data)
            for bucket in buckets.values():
                await self._data_frame_mutator.save(bucket)

    async def delete(
        self,
        filter_clause: contracts.FilterClause
    ) -> typing.NoReturn:
        if filter_clause:
            await self._data_frame_mutator.delete(filter_clause=FilterBuilder().__call__(filter_clause))
