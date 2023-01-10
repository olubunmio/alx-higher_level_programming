#!/usr/bin/python3
"""A module that contains a class ``MyInt`` that inherits from int
"""


class MyInt(int):
    """A class that inherits from int.
    """
    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    def __eq__(self, other):
        return False if self.__num == other else True

    def __ne__(self, other):
        return False if self.__num != other else True
