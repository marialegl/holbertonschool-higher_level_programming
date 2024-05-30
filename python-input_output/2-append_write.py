#!/usr/bin/python3
"""Function that appends a string
at the end of a text file (UTF8)
Using the "with" statement
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written
