#!/usr/bin/python3
"""Define a function load_from_json_file"""

import json


def load_from_json_file(filename):
    """
    Function that reads a JSON file and converts its content,
    back into a Python object

    Args:
        filename (str): The name of the file to read,
        and load the JSON data from

    Returns:
        object: The Python object corresponding to the JSON data in the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
