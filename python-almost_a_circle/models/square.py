#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): length of one side of the square..
            x (int): The x coordinate of the new square.
            y (int): The y coordinate of the new square.
            id (int): The identity of the new square.
        """
        super().__init__(size, size, x, y, id)
        """calling the constructor of the base class
        (Rectangle) and passing its parameters to it"""

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for the size property.
         Returns:
        int: The size of the square, which is equivalent to its width.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size property.
        Args:
        value (int): The size to set for the square,
        which will be assigned to both width and height.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute: id, size, x and y"""
        if args and len(args) > 0:
            """If args exists and is not empty, updates the attributes
            according to the order of the arguments."""
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            """If args is empty or does not exist, update
            attributes according to kwargs"""
            for key, value in kwargs.items():
                setattr(self, key, value)
