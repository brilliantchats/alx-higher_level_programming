#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return the square of all values of integrs in a matrix"""
    return [[x**2 for x in row] for row in matrix]
