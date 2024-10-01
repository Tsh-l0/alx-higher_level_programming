#!/usr/bin/python3
"""Defines a class, Square"""


class Square:

    def __init__(self, size=0):

        """Initializes the class, Square.
        Args:
            size: Represents the size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculates the area of the classm Square
        Returns: The size of the class, Square
        """

        return self.__size ** 2
