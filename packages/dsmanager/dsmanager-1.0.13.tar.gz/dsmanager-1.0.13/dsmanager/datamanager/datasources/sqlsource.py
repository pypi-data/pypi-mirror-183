"""@Author: Rayane AMROUCHE

Local Sources Handling
"""

import os

from urllib.parse import quote
from typing import Any

import pandas as pd  # type: ignore
import sqlalchemy  # type: ignore

from dsmanager.datamanager.datasources.datasource import DataSource


class SqlSource(DataSource):
    """Inherited Data Source Class for sql sources
    """

    @staticmethod
    def read_source(
            uri: str,
            query: str = "",
            table_name: str = "",
            **kwargs: Any) -> Any:
        """Sql source reader

        Args:
            uri (str): Sqlalchemy format URI
            query (str, optional): Sql query. Defaults to "".
            table_name (str, optional): Table name to query. Defaults to "".

        Returns:
            Any: Data from source
        """
        engine = sqlalchemy.create_engine(uri)
        if query:
            conn = engine.connect()
            data = pd.read_sql_query(query, conn, **kwargs)
            conn.close()
        elif table_name:
            conn = engine.connect()
            data = pd.read_sql_table(table_name, conn, **kwargs)
            conn.close()
        else:
            data = engine

        return data

    def read(self, source_info: dict, **kwargs: Any) -> Any:
        """Handle source and returns the source data

        Args:
            source_info (dict): Source metadatas

        Returns:
            Any: Source datas
        """
        args = source_info["args"] if "args" in source_info else {}

        self.load_source(source_info, **kwargs)

        dialect = source_info["dialect"]
        database = source_info["database"]
        user = os.environ.get(source_info["username_env_name"], "")
        pswd = os.environ.get(source_info["password_env_name"], "")
        address = source_info["address"]

        data = self.read_source(
            uri=f"{dialect}://{user}:{quote(pswd)}@{address}/{database}",
            query=source_info["query"] if
            "query" in source_info else "",
            table_name=source_info["table_name"] if
            "table_name" in source_info else "",
            **args
        )

        self.logger.info(
            "Read data from '%s'",
            f"{address}/{database}"
        )

        return data

    def read_db(self, source_info: dict, **kwargs: Any) -> Any:
        """Read source and returns a source engine

        Args:
            source_info (dict): Source metadatas

        Returns:
            Any: Source engine
        """
        self.load_source(source_info, **kwargs)
        args = source_info["args"] if "args" in source_info else {}

        dialect = source_info["dialect"]
        database = source_info["database"]
        user = os.environ.get(source_info["username_env_name"], "")
        pswd = os.environ.get(source_info["password_env_name"], "")
        address = source_info["address"]

        engine = self.read_source(
            uri=f"{dialect}://{user}:{quote(pswd)}@{address}/{database}",
            **args
        )

        self.logger.info(
            "Connect to database '%s'",
            f"{address}/{database}"
        )

        return engine
