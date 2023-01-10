#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A square class with private attributes

    Instantiation with optional arg ``size``
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('must be >= 0')
        else:
            self.__size = size

    def area(self):
        """int: Computes the area of the square
        """
        return self.__size ** 2
