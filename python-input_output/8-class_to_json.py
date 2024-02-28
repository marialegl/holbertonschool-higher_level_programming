#!/usr/bin/python3
"""
Function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure
    """
    description = {}
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            description[attr_name] = attr_value
