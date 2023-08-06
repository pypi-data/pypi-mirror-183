"""@Author: Rayane AMROUCHE

Utils for DataManager
"""

import os

from typing import Any

import pandas as pd  # type: ignore

from dotenv import load_dotenv  # type: ignore

from dsmanager.datamanager.datastorage import DataStorage

from dsmanager.controller.utils import StaticMethod
from dsmanager.controller.logger import make_logger

from dsmanager.datamanager.utils._df_info import unique
from dsmanager.datamanager.utils._df_info import describe

from dsmanager.datamanager.utils._df_transform import clean_column

from dsmanager.datamanager.utils._column_transform import create_category
from dsmanager.datamanager.utils._column_transform import as_category
from dsmanager.datamanager.utils._column_transform import bin_column
from dsmanager.datamanager.utils._column_transform import onehot_encode
from dsmanager.datamanager.utils._column_transform import onehot_decode
from dsmanager.datamanager.utils._column_transform import column_spliter

from dsmanager.datamanager.utils._plotting import scatter_matrix
from dsmanager.datamanager.utils._plotting import displot
from dsmanager.datamanager.utils._plotting import corr

from dsmanager.datamanager.utils._pandas_object import to_datamanager
from dsmanager.datamanager.utils._pandas_object import pipe_sklearn
from dsmanager.datamanager.utils._pandas_object import pipe_steps
from dsmanager.datamanager.utils._pandas_object import pipe_leaf


class Utils:
    """Utils class brings utils tools for the data manager
    """

    unique = StaticMethod(unique)
    describe = StaticMethod(describe)

    clean_column = StaticMethod(clean_column)

    create_category = create_category
    as_category = as_category
    bin_column = bin_column
    onehot_encode = StaticMethod(onehot_encode)
    onehot_decode = StaticMethod(onehot_decode)
    column_spliter = StaticMethod(column_spliter)

    scatter_matrix = StaticMethod(scatter_matrix)
    displot = StaticMethod(displot)
    corr = StaticMethod(corr)

    def __init__(self,
                 dm_: Any,
                 logger_path: str = "/tmp/logs",
                 verbose: int = 0
                 ) -> None:
        """Init class Utils with an empty local storage
        """
        self.dm_ = dm_
        self.logger = make_logger(
            os.path.join(logger_path, "datamanager"),
            "utils",
            verbose=verbose
        )
        self.categories = DataStorage()

    def copy_as(self,
                df_: pd.DataFrame,
                name: str) -> pd.DataFrame:
        """Copy a pandas DataFrame in the datamanager with a given name

            Args:
                df_ (pd.DataFrame): DataFrame to save
                name (str): Alias of the DataFrame in the DataStorage of the
                    DataManager

            Returns:
                pd.DataFrame: Returns original DataFrame to keep chaining
        """
        self.dm_.datas[name] = df_
        return df_

    def load_env(self,
                 env_path: str = "",
                 ) -> None:
        """Load env file from a given path or from the datamanager

        Args:
            env_path (str, optional): Path of the env file. Defaults to "".
        """
        if env_path:
            load_dotenv(env_path)
        elif self.dm_.env_path:
            load_dotenv(self.dm_.env_path)


pd.core.base.PandasObject.to_datamanager = to_datamanager
pd.core.base.PandasObject.pipe_sklearn = pipe_sklearn
pd.core.base.PandasObject.pipe_leaf = pipe_leaf
pd.core.base.PandasObject.pipe_steps = pipe_steps
