#!/usr/bin/python3
"""
Class BaseGeometry whit two methods
"""


class BaseGeometry:
    """Class with two methods, area and integer_validation
    """

    def area(self):
        """
        Public instance method
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method:
        Args:
            name (string)
            value (int)
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
