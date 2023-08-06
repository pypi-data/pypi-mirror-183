import typing
import orjson
import sqlalchemy.ext.asyncio


def default_serializer(obj):
    return orjson.dumps(obj, option=orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_NAIVE_UTC).decode()


def default_deserializer(obj):
    return orjson.loads(obj)


class SqlalchemyConnectionPool:
    def __init__(
        self,
        dsn: str,
        echo: bool = True,
        auto_commit: bool = False,
        json_serializer: typing.Callable = default_serializer,
        json_deserializer: typing.Callable = default_deserializer
    ):
        self._engine = sqlalchemy.ext.asyncio.create_async_engine(
            dsn,
            echo=echo,
            json_serializer=json_serializer,
            json_deserializer=json_deserializer
        )
        self._auto_commit = auto_commit

    async def get_connection(self):
        connection = sqlalchemy.ext.asyncio.AsyncConnection(self._engine)
        await connection.start()
        if self._auto_commit:
            await connection.begin()
        return connection

    async def commit(
        self,
        connection: sqlalchemy.ext.asyncio.AsyncConnection
    ):
        if self._auto_commit:
            await connection.commit()
        await connection.close()

    async def rollback(
        self,
        connection: sqlalchemy.ext.asyncio.AsyncConnection,
        exc_type: typing.Any | None = None
    ):
        if self._auto_commit:
            await connection.rollback()
        await connection.close()
