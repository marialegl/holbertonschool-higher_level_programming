#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and then save them to a file
Using the "with" statement
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Script that adds all arguments to a Python list
    and then save them to a file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
