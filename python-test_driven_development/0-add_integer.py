#!/usr/bin/python3
"""Module 
to add 
2 integers
123
"""
def add_integer(a, b=98):
    """
    comentar
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
