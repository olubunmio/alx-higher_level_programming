#!/usr/bin/python3
"""A module that contains a class BaseGeometry.
"""


class BaseGeometry:
    """A class BaseGeometry that raises an Exception with the message area()
    is not yet implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")
