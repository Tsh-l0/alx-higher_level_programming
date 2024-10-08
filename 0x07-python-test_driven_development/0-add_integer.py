#!/usr/bin/python3
"""
A function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Returns the sum of 2 ints

    Args:
        a: First integer
        b: Second integer

    Raises:
        TypeError: If either a or b is not an int or float
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
