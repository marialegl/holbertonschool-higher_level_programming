#!/usr/bin/python3
import roman


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    number_int = roman.fromRoman(roman_string)
    return (number_int)
