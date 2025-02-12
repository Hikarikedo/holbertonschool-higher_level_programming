#!/usr/bin/python3
"""Define a function from_json_string"""

import json


def from_json_string(my_str):
    """
    Function that converts a JSON string into a Python object

    Args:
        my_str (str): The JSON string to be converted

    Returns:
        object: A Python object corresponding to the JSON string
    """
    return json.loads(my_str)
