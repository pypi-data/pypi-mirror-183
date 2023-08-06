"""@Author: Rayane AMROUCHE

Local Sources Handling
"""

from typing import Any

from dsmanager.datamanager.datasources.datasource import DataSource
from dsmanager.datamanager.utils._func import find_type


class LocalSource(DataSource):
    """Inherited Data Source Class for local sources
    """

    @staticmethod
    def read_source(path: str, **kwargs: Any) -> Any:
        """Local source reader

        Args:
            path (str): Path or Uri of the datasource

        Returns:
            Any: Data from source
        """
        if "file_type" not in kwargs:
            kwargs["file_type"] = find_type(path)

        data = super(LocalSource, LocalSource).encode_files(
            path,
            **kwargs
        )
        return data

    def read(self, source_info: dict, **kwargs: Any) -> Any:
        """Handle source and returns the source data

        Args:
            source_info (dict): Source metadatas

        Returns:
            Any: Source datas
        """
        args = self.setup_fileinfo(source_info, **kwargs)

        path = source_info["path"]

        data = self.read_source(
            path,
            **args
        )

        self.logger.info(
            "Read data from '%s'",
            source_info["path"]
        )
        return data
