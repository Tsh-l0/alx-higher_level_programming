#!/usr/bin/python3
"""
A function that prints a square using the character #
"""


def print_square(size):
    """
    Args:
        size: The size length of the square

    Raises:
        TypeError: If size is not an int
        ValueError: If size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for char in range(size):
        print("#" * size)
