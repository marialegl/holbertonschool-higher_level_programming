#!/usr/bin/python3
"""Square Class

Square Class that defines a square by
based on file 3-square
"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """Constructor of square object
        Size must  be a positive integer"""
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
