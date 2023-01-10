#!/usr/bin/python3
"""A module that contains a class BaseGeometry.
"""


class BaseGeometry:
    """A class BaseGeometry that raises an Exception with the message area()
    is not yet implemented.

    Public instance method: def area(self): that raises an Exception with the
    message area() is not implemented

    Public instance method: def integer_validator(self, name, value): that
    validates value:
        - you can assume name is always a string
        - if value is not an integer: raise a TypeError exception, with the
          message <name> must be an integer
        - if value is less or equal to 0: raise a ValueError exception with
          the message <name> must be greater than 0
    """
    def area(self):
        """raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates ``value``
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
