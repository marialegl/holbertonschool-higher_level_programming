#!/usr/bin/python3
"""
Function that write a text file (UTF8)
Using the "with" statement
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that write a text file
    returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written
