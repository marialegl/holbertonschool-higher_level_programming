#!/usr/bin/python3
"""
Function that returns an object
(Python data structure) represented by a JSON string
Importing the 'json' module.
"""


import json


def from_json_string(my_str):
    """
    Function that returns an object
    represented by a JSON string
    """
    json_string = json.loads(my_str)
    return json_string
