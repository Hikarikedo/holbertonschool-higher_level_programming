#!/usr/bin/python3
"""Define a function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file using a JSON representation

    Args:
        my_obj: The Python object to be saved
        filename (str): The name of the file where the JSON,
        data will be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
