"""@Author: Rayane AMROUCHE

Utils functions for controller
"""

import re
import os
import json

import __main__ as main

from dsmanager.datamanager.datastorage import DataStorage


def is_interactive() -> bool:
    """Check wether the code is runned on a notebook

    Returns:
        bool: True if runned on notebook, else False
    """
    return not hasattr(main, '__file__')


def json_to_dict(path: str) -> dict:
    """Read a json file as a dict

    Args:
        path (str, optional): Path of the json file to transform as a python
            dict

    Raises:
        FileNotFoundError: Raised if the file is not found

    Returns:
        dict: Json file as a python dict
    """
    # check if file exists
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as outfile:
            json.dump({}, outfile)

    # check if file is a json
    try:
        with open(path, encoding="utf-8") as json_file:
            file_dict = json.load(json_file, object_pairs_hook=DataStorage)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Given file is not a valid json. Details: {exc}"
        ) from exc
    return file_dict


def format_dict(dico: dict, formatting: dict) -> None:
    """Read a json file as a dict

    Args:
        dico (dict): Dict where keys have to be formated
        formatting (dict): Formatting dictionary

    """
    for key_, value_ in dico.items():
        if isinstance(value_, str) and any(k in value_ for k in formatting.keys()):
            dico[key_] = value_.format(**formatting)
        if isinstance(value_, dict):
            format_dict(value_, formatting)


def camel_to_snake(str_: str) -> str:
    """Transform a camel case name to a snake case one

    Args:
        str_ (str): String to transform

    Returns:
        str: Transformed string
    """
    str_ = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str_)
    str_ = re.sub('([a-z0-9])([A-Z])', r'\1_\2', str_).lower()
    return re.sub('_+', '_', str_)


def remove_special(str_: str) -> str:
    """Transform special characters to their meaning or to space

    Args:
        str_ (str): String to transform

    Returns:
        str: Transformed string
    """
    str_ = str_.replace("%", " Percent ")
    str_ = str_.replace("@", " At ")
    str_ = str_.replace("/w ", " With ")
    return re.sub(r'\W+', ' ', str_)


def remove_spaces(str_: str) -> str:
    """Transform spaces to simple underscore

    Args:
        str_ (str): String to transform

    Returns:
        str: Transformed string
    """
    str_ = re.sub(' +', ' ', str_)
    str_ = str_.strip(" ")
    return str_.replace(" ", "_")
