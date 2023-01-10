#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """A class Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter and setter function."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """int: Computes and Returns area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character `#`.

        If size == 0 print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
