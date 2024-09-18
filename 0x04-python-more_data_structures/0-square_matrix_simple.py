#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    for sqr_root in matrix:
        sqr_num = list(map(lambda x: x**2, sqr_root))
        new_matrix.append(sqr_num)
    return new_matrix
