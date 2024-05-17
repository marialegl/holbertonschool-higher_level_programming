#!/usr/bin/python3
def raise_exception():
    try:
        x = 5 + "Hello"
    except TypeError as e:
        raise e
