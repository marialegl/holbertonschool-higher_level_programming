#!/usr/bin/python3
"""Defines a base model class.
"""


import json
"""Import the json module to work with JSON
"""


class Base:
    """Base model.
    This Represents the "base" for all other classes in project 0x0C*.
    Private Class Attributes:
    __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.
        Args:
        id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Define a static to_json_string method in the Base class
        that takes list_dictionaries as an argument."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            """If the list contains dictionaries, json.dumps()
            is used to convert the list of dictionaries to
            a JSON string and returned."""
            return "[]"
        else:
            return json.dumps(list_dictionaries)
