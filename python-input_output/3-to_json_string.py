#!/usr/bin/python3
"""Define a function to_json_string"""

import json


def to_json_string(my_obj):
    """
    Function that converts a Python object to a JSON string

    Args:
        my_obj: The Python object to convert to a JSON string

    Returns:
        str: A JSON-formatted string representation of the object
    """
    return json.dumps(my_obj)
