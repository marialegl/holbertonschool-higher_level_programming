#!/usr/bin/python3
"""Square Class

Square Class that defines a square by
based on file 2-square
"""


class Square:
    """
    Square with size
    """
    def __init__(self, size=0):
        """Constructor of square object
        Size must  be a positive integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
