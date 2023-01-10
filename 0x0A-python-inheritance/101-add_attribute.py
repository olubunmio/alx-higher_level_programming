#!/usr/bin/python3
"""A module that contains a function that trys adds attributes to an object.
"""


def add_attribute(obj, attr, val):
    """A function that trys to add attributes to an object.
    """

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, val)
