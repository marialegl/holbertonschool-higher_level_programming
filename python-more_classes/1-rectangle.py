#!/usr/bin/python3
"""Rectangle Class

This class represents a square.
"""


class Rectangle:
    """
    Rectangle that defines a square
    """
    def __init__(self, width=0, heigth=0):
         self.__width = width
         self.__heigth = heigth

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
