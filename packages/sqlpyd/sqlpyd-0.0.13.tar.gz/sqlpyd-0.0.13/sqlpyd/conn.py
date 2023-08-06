import sqlite3
from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from pydantic import BaseSettings, Field
from sqlite_utils import Database
from sqlite_utils.db import Table

from .tableconfig import TableConfig


class Connection(BaseSettings):
    """Thin wrapper over sqlite-utils `Database` (which itself wraps around sqlite3.connect) with some convenience methods."""

    DatabasePath: str | None = Field(
        None,
        env="DB_FILE",
        description="Intended / existing path to the database from the present working directory.",
    )
    WAL: bool | None = Field(False, title="Write Ahead Logging.")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def path_to_db(self) -> Path | None:
        if self.DatabasePath:
            return Path().cwd().joinpath(self.DatabasePath)
        return None

    @property
    def db(self) -> Database:
        if self.path_to_db:
            obj = Database(self.path_to_db, use_counts_table=True)
            if self.WAL:
                obj.enable_wal()
            return obj
        return Database(filename_or_conn=None, memory=True)

    @property
    @contextmanager
    def session(self) -> Iterator[sqlite3.Cursor]:
        conn = self.db.conn
        cur = conn.cursor()
        yield cur
        conn.commit()
        conn.close()

    def tbl(self, table_name: str) -> Table:
        """Should use string represented by kls.__tablename__ to retrieve the table instance."""
        tbl = self.db.table(table_name)
        if isinstance(tbl, Table):
            return tbl
        raise Exception(f"No {tbl=}")

    def table(self, kls) -> Table:
        """Using the TableConfig kls to retrieve the table instance."""
        if not issubclass(kls, TableConfig):
            raise NotImplementedError(f"{kls} must be a TableConfig.")
        tbl_obj = self.db.table(kls.__tablename__)
        if tbl_obj.exists() and isinstance(tbl_obj, Table):
            return tbl_obj
        raise Exception(f"No {tbl_obj=}")

    def create_table(self, kls: Any) -> Table:
        """Create a TableConfig table, if it doesn't exist yet, having attributes declared in the `kls`."""
        if not issubclass(kls, TableConfig):
            raise NotImplementedError(f"{kls} must be a TableConfig.")
        return kls.config_tbl(self.tbl(kls.__tablename__))

    def add_record(self, kls, item: dict) -> Table:
        """With a TableConfig `kls` (that is representing or should represent an sqlite database), add a record which will be cleaned via Pydantic prior to being inserted by sqlite-utils."""
        return self.create_table(kls).insert(
            kls(**item).dict(exclude_none=True)
        )

    def add_records(
        self, kls, items: Iterable[dict] | Iterator[dict]
    ) -> Table:
        """With a TableConfig-enabled `kls` (that is representing or should represent an sqlite database), records which will be cleaned via Pydantic prior to being bulk inserted via sqlite-utils."""
        return self.create_table(kls).insert_all(
            kls(**item).dict(exclude_none=True) for item in items
        )

    def add_cleaned_records(
        self, kls, items: Iterable[Any] | Iterator[Any]
    ) -> Table:
        """Previously validated records can be inserted without requiring a deserialization step."""
        return self.create_table(kls).insert_all(
            i.dict(exclude_none=True) for i in items
        )
