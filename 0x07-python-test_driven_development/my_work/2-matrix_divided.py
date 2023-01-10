#!/usr/bin/python3
"""Matrix division module

A module that contains only one function that divides a given list of lists
"""


def matrix_divided(matrix, div):
    """A function that divides a matrix by `div`

    Please refer to the inline documentation for more details as to
    the usage of the function.

    Args:
        matrix (:obj:`list of lists`): the first argument to the function
        div (:obj:`int/float`): the second argument to the function

    Return:
        returns a new matrix containing the result of the divided elements
        of ``matrix``.
    """
    # --------------------- Test for Edge Cases -----------------------
    # --> 1. check if matrix is a list of list of ints/floats
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(message1)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(message1)

    for row in matrix:
        for i in range(len(row)):
            if type(row[i]) not in [int, float]:
                raise TypeError(message1)

    # --> 2. check if rows are of the same size
    message2 = "Each row of the matrix must have the same size"
    for i in range(len(matrix)):
        j = i + 1
        if j < len(matrix):
            if len(matrix[i]) != len(matrix[j]):
                raise TypeError(message2)

    # --> 3. check if div is an integer/float
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    # --> 4. check division by 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # --> 5. check if matrix is empty
    if len(matrix) == 0:
        return matrix

    # --------------------- All edge cases passed ------------------------

    # function init
    new_matx = []
    for row in matrix:
        new_row = []
        for i in range(len(row)):
            val = round(row[i] / div, 2)
            new_row.append(val)
        new_matx.append(new_row)

    return new_matx
