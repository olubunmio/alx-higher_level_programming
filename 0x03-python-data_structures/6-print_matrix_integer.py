#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in row:
            print("{:d}".format(j), end='' if j == row[-1] else ' ')
        print()
