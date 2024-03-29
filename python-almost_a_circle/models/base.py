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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file.
        Args:
        list_objs (list): List of instances to be saved to a JSON file.
        The method creates a JSON file named after the class, containing
        the JSON string representation of the list of instances provided.
        If the list is None, an empty list is saved."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Parses a JSON string and converts it to a Python object.
         Args:
        json_string (str): A string representing a list
        of dictionaries in JSON format.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file named <Class name>.json.
        Returns:
        list: List of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                data = cls.from_json_string(json_string)
                """Use the from_json_string method of the current class"""
                instances = [cls.create(**obj) for obj in data]
                """Use the create method of the current class"""
                return instances
        except FileNotFoundError:
            return []
