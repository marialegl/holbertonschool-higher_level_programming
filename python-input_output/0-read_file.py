#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
and prints it to stdout
Using the "with" statement.
"""


def read_file(filename=""):
    """
    Function that reads a text file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
