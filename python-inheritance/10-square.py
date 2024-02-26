#!/usr/bin/python3
"""
Module based on 9-rectangle.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Instantiation size
    Args:
        Rectangle (Class): Class Parent
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
