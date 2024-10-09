#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: A list of lists including ints or floats
        div: The divisor to be used. Can be int/float

    Raises:
        TypeError: Matrix contains non ints
        TypeError: Matrix has rows of different sizes
        TypeError: Div is not int/float
        ZeroDivisionError: Div == 0

    Returns:
        A matrix with the result of the divided matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for
                                               row in matrix):
        raise TypeError("matrix must be a matrix "
                        " (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el
               in row):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the"
                        " same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
