#!/usr/bin/python3
"""Write a class Square that defines a square by:

Private instace attribute: ``size``
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""


class Square:
    """Defines a square

    Why size is private attribute?
    The size of a square is crucial for a square, many things depend on it
    (area computation, etc.), so you as a class builder, must control the
    type and value attribute. One way to have the control is to keep it
    privately. You will wee in next tasks how to get, update and validate
    the size value.

    Attributes:
    __size (int): private attribute (won't permit display next time)
    """
    def __init__(self, size):
        """Initializes Square

        Args:
            size (int): the size of the square
        """
        self.__size = size

# d = Square(3)
# print(d.__dict__)  # private attributes are shown using __dict__
