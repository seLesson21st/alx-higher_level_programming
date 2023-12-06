#!/usr/bin/python3
'''function that computes the square value of all integers of a matrix'''


def square_matrix_simple(matrix=[]):
    n_matrix = []
    for column in matrix:
        result = list(map(lambda i: i**2, column))
        n_matrix.append(result)
    return n_matrix
