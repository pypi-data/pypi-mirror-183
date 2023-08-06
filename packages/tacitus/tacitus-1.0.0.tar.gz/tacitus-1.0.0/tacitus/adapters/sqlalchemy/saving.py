import collections.abc
import pickle
import operator

import sqlalchemy.dialects.postgresql
import sqlalchemy.ext.asyncio
from .registration import Many2OneLink
from ...definitions import contracts


class SqlAlchemyDataFrameSeparator(contracts.DataFrameSeparator):
    def __init__(self, registry: contracts.DataFrameRegistry):
        self._registry = registry

    def __call__(
        self,
        data: contracts.MutationData | collections.abc.Sequence[contracts.MutationData]
    ) -> dict[contracts.DataFrameName, contracts.DataFrameBucket]:
        buckets = {}
        self._resolve(data=data, buckets=buckets)
        return dict(reversed(list(buckets.items())))

    def _resolve(
        self,
        data: contracts.MutationData | collections.abc.Sequence[contracts.MutationData],
        buckets: collections.abc.MutableMapping | None = None,
        table_name: str | None = None,
        purge_key: sqlalchemy.Column | None = None
    ):

        if not isinstance(data, collections.abc.Sequence):
            data = (data,)

        bucket_data = []
        for data_row in data:
            bucket_row = {}
            for field_name, field_value in data_row.items():
                if self._registry.get_frame(field_name) is not None:
                    _purge_key = None
                    if table_name:
                        link = self._registry.get_link(field_name, table_name)
                        if isinstance(link, Many2OneLink):
                            _purge_key = link.source_key
                            if isinstance(field_value, collections.abc.Sequence):
                                field_value = [v | {_purge_key.name: data_row.get(link.target_key.name)} for v in
                                               field_value]
                            elif isinstance(field_value, collections.abc.Mapping):
                                field_value = field_value | {_purge_key.name: data_row.get(link.target_key.name)}
                    self._resolve(
                        data=field_value,
                        buckets=buckets,
                        table_name=field_name,
                        purge_key=_purge_key
                    )
                    continue
                bucket_row[field_name] = field_value
            if len(bucket_row) > 1:
                bucket_data.append(bucket_row)

        if not table_name:
            return

        bucket = buckets.get(table_name)
        if not bucket:
            bucket = contracts.DataFrameBucket(
                frame_name=table_name,
                data=[],
                purge_key=purge_key.name if purge_key is not None else None
            )
        bucket.data.extend(bucket_data)
        buckets[table_name] = bucket


class SqlAlchemyDataFrameMutator(contracts.DataFrameMutator):
    def __init__(
        self,
        registry: contracts.DataFrameRegistry,
        connection: sqlalchemy.ext.asyncio.AsyncConnection
    ):
        self._registry = registry
        self._connection = connection

    async def insert(
        self,
        bucket: contracts.DataFrameBucket
    ):
        if self._is_bucket_unprocessable(bucket):
            return

        await self._insert(
            table=self._registry.get_frame(bucket.frame_name),
            data=bucket.data
        )

    async def delete(
        self,
        filter_clause: collections.abc.Sequence[contracts.FilterClauseElement] | contracts.FilterClauseElement
    ):
        if not isinstance(filter_clause, collections.abc.Sequence):
            filter_clause = (filter_clause,)

        buckets = collections.defaultdict(list)
        for clause in filter_clause:
            buckets[clause.frame_name].append(
                clause.operator(
                    self._registry.get_column(clause.frame_name, clause.field_name),
                    clause.value
                )
            )

        for frame_name, clause in buckets.items():
            await self._delete(
                table=self._registry.get_frame(frame_name),
                filter_clause=clause
            )

    async def save(
        self,
        bucket: contracts.DataFrameBucket
    ):
        if self._is_bucket_unprocessable(bucket):
            return

        data = bucket.data
        table = self._registry.get_frame(bucket.frame_name)
        purge_key = self._registry.get_column(table, bucket.purge_key) if bucket.purge_key else None

        if not isinstance(data, collections.abc.Sequence):
            data = (data,)

        primary_key = self._registry.get_primary_key(table.name)

        if purge_key is not None:
            if ids := self._vectorize(data, purge_key.name):
                await self._delete(
                    table=table,
                    filter_clause=purge_key.in_(ids)
                )

        exists_ids = []
        if ids := self._vectorize(data, primary_key.name):
            result = await self._connection.execute(
                sqlalchemy.select([primary_key]).where(primary_key.in_(ids))
            )
            exists_ids = set((v[0] for v in result or ()))

        to_update_values = {}
        to_update_ids = collections.defaultdict(list)
        to_insert = []
        for row in data:
            if (pk := row.get(primary_key.name)) in exists_ids:
                _values = {k: v for k, v in row.items() if k != primary_key.name}
                _group_key = pickle.dumps(_values)
                to_update_values[_group_key] = _values
                to_update_ids[_group_key].append(pk)
            else:
                to_insert.append(row)

        for gk, values in to_update_values.items():
            await self._update(table, values, to_update_ids[gk])

        if to_insert:
            await self._insert(table, to_insert)

    async def _insert(
        self,
        table: sqlalchemy.Table,
        data: collections.abc.Mapping | collections.abc.Sequence[collections.abc.Mapping]
    ):
        await self._connection.execute(
            sqlalchemy.insert(
                table
            ).values(
                data
            )
        )

    async def _update(
        self,
        table: sqlalchemy.Table,
        data: collections.abc.Mapping,
        identity: collections.abc.Sequence[contracts.IdentifierType] | contracts.IdentifierType
    ):
        pk = self._registry.get_primary_key(table.name)
        await self._connection.execute(
            sqlalchemy.update(
                table
            ).values(
                data
            ).where(
                pk.in_(identity) if isinstance(identity, collections.abc.Sequence) else operator.eq(pk, identity)
            )
        )

    async def _delete(
        self,
        table: sqlalchemy.Table,
        filter_clause: sqlalchemy.sql.ClauseElement | collections.abc.Sequence[sqlalchemy.sql.ClauseElement]
    ):
        if not isinstance(filter_clause, collections.abc.Sequence):
            filter_clause = (filter_clause,)

        stmt = sqlalchemy.delete(table)
        for clause in filter_clause:
            stmt = stmt.where(clause)

        await self._connection.execute(stmt)

    @staticmethod
    def _is_bucket_unprocessable(bucket: contracts.DataFrameBucket):
        return bucket is None or bucket.data is None or bucket.frame_name is None

    @staticmethod
    def _vectorize(data: collections.abc.Sequence[collections.abc.Mapping], key: str) -> collections.abc.Sequence:
        result = []
        for r in data:
            if value := r.get(key):
                result.append(value)
        return result
