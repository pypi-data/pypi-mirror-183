import json
from typing import List, Optional, Union

import pandas as pd
from redis.client import Redis
from sqlalchemy import Column

from datapipe.store.database import MetaKey
from datapipe.store.table_store import TableStore
from datapipe.types import (DataDF, DataSchema, IndexDF, MetaSchema,
                            data_to_index)


def _serialize(values):
    return json.dumps(values)


def _deserialize(bytestring):
    return json.loads(bytestring)


def _to_itertuples(df: DataDF, colnames):
    return tuple(df[colnames].itertuples(index=False, name=None))


class RedisStore(TableStore):
    def __init__(
        self,
        connection: Union[Redis, str],
        name: str,
        data_sql_schema: List[Column]
    ) -> None:

        if isinstance(connection, str):
            self.redis_connection = Redis.from_url(connection, decode_responses=True)
        else:
            self.redis_connection = connection
        self.name = name
        self.data_sql_schema = data_sql_schema
        self.prim_keys = [column.name for column in self.data_sql_schema if column.primary_key]
        self.value_cols = [column.name for column in self.data_sql_schema if not column.primary_key]

    def insert_rows(self, df: DataDF) -> None:
        if df.empty:
            return

        # get rows as Iter[Tuple]
        key_rows = _to_itertuples(df, self.prim_keys)
        value_rows = _to_itertuples(df, self.value_cols)
        redis_pipe = self.redis_connection.pipeline()
        for keys, values in zip(key_rows, value_rows):
            redis_pipe.hset(self.name, _serialize(keys), _serialize(values))
        redis_pipe.execute()

    def update_rows(self, df: DataDF) -> None:
        # удаляем существующие ключи
        if df.empty:
            df = pd.DataFrame(columns=[column.name for column in self.data_sql_schema])
        self.delete_rows(data_to_index(df, self.prim_keys))
        self.insert_rows(df)

    def read_rows(self, df_keys: Optional[IndexDF] = None) -> DataDF:
        if df_keys is not None:
            if df_keys.empty:
                return pd.DataFrame(columns=[column.name for column in self.data_sql_schema])

            keys = _to_itertuples(df_keys, self.prim_keys)
            keys_json = [_serialize(key) for key in keys]
            values = self.redis_connection.hmget(self.name, keys_json)
            values = [_deserialize(val) for val in values if val]
        else:
            pairs = self.redis_connection.hgetall(self.name)
            keys = [_deserialize(key) for key in pairs.keys()]
            values = [_deserialize(val) for val in pairs.values()]

        result_df = pd.concat([
            pd.DataFrame.from_records(keys, columns=self.prim_keys),
            pd.DataFrame.from_records(values, columns=self.value_cols)
        ], axis=1)
        if values:
            return result_df
        else:
            return result_df.iloc[:0]

    def delete_rows(self, df_keys: IndexDF) -> None:
        if df_keys.empty:
            return
        keys = _to_itertuples(df_keys, self.prim_keys)
        keys = [_serialize(key) for key in keys]
        self.redis_connection.hdel(self.name, *keys)

    def get_primary_schema(self) -> DataSchema:
        return [column for column in self.data_sql_schema if column.primary_key]

    def get_meta_schema(self) -> MetaSchema:
        meta_key_prop = MetaKey.get_property_name()
        return [column for column in self.data_sql_schema if hasattr(column, meta_key_prop)]
