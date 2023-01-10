#!/usr/bin/python3
""" 4-print_square module

A module that contains one function ``print_square()`` that prints a square
with `#` character
"""


def print_square(size):
    """A function that prints a square made up of '#'

    ``size`` must be an integer >= 0

    Args:
        size (int): the only argument to the function

    Return:
        returns nothing
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return
    elif size >= 0:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
