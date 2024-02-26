#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """Public instance method that prints the list, but sorted (ascending sort)

    Args:
        self: list
    """

    def print_sorted(self):
        list_order = sorted(self)
        print(list_order)
