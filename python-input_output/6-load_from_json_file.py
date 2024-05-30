#!/usr/bin/python3
"""
Function that creates an Object
from a “JSON file”
Using the "with" statement
"""


import json


def load_from_json_file(filename):
    """
    Function that hat creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_string = file.read()
        obj = json.loads(json_string)
        return obj
