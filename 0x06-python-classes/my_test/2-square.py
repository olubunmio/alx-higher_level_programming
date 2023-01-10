#!/usr/bin/python3
"""Write a class Square that defines a square by:

1. Private instance attribute: ``size``
2. Instantiation with optional size: def __init__(self, size=0):
    * ``size`` must be an integer, otherwise raise TypeError exception
      with the message ``size must be an integer``
    * if size is less than 0, raise a ValueError exception with message
      ``size must be >= 0``
3. You are not allowed to import any module
"""


class Square:
    """Defines a square

    Why size is private attribute?
    The size of a square is crucial for a square, many things depend on it
    (area computation, etc.), so you as a class builder, must control the
    type and value attribute. One way to have the control is to keep it
    privately. You will wee in next tasks how to get, update and validate
    the size value.
    """
    def __init__(self, size=0):
        """Initializes Square

        Args:
            size (int, optional): the size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('must be >= 0')
        else:
            self.__size = size
