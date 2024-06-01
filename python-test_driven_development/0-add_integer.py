#!/usr/bin/python3
"""Integers addition module"""


def add_integer(a, b=98):
    """function that add 2 numbers"""

    if not a or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
