#!/usr/bin/python3
"""0. Basic Serialization"""


import json


def serialize_and_save_to_file(data, filename):
    """function that serialize and save data"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """function that load and deserialize data"""
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
