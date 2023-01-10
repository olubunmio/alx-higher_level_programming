#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: Computes and sets/returns the size."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """int: Computes and returns the area of self.__size."""
        return self.__size ** 2
