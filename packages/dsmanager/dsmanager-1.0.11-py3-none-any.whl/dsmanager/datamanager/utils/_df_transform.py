"""@Author: Rayane AMROUCHE

DataFrame transformation methods for the Utils class for the DataManager
"""

from typing import List, Callable

import pandas as pd  # type: ignore

from dsmanager.controller.utils import camel_to_snake
from dsmanager.controller.utils import remove_special
from dsmanager.controller.utils import remove_spaces


@staticmethod
def clean_column(df_: pd.DataFrame, new_steps: List[Callable] = None) -> pd.DataFrame:
    """Transform the columns names of a given dataframe

    Args:
        df_ (pd.DataFrame): DataFrame which columns are to be cleaned
        new_steps (List[Callable], optional): List of functions to apply on
            columns names. Defaults to None.

    Returns:
        pd.DataFrame: Returns original DataFrame to keep chaining
    """
    if new_steps is None:
        new_steps = []
    new_cols = {}  # type: dict
    for col in df_.columns:
        cur_col = camel_to_snake(remove_spaces(remove_special(col)))
        for step in new_steps:
            cur_col = step(cur_col)
        while cur_col in new_cols.values():
            cur_col += "_"
        new_cols[col] = cur_col

    return (
        df_
        .rename(columns=new_cols)
    )
