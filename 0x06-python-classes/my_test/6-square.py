#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """A class square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is tuple) and (len(value) == 2) and \
           (type(value[0]) is int and type(value[1]) is int) and \
           (value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """int: Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character `#`.

        If size == 0, prints an empty line
        position should be used by using space - Don't fill lines by spaces
        when position[1] > 0
        """
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
