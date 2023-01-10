#!/usr/bin/python3
"""This is the integer addition module

A module that contains a function that adds two integers ``add_integer()``
The two numbers must be integers
"""


def add_integer(a, b=98):
    """add_integer

    A function that adds two integers
    The both numbers must be of type int or float else an exception is
    raised.

    Args:
        a (int): The first argument to the function
        b (:obj:`int`: optional): the second argument to the function
            Defaults to 98.
    Return:
        int: returns the sum of `a` and `b`.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a+1 == a:
        raise OverflowError("a is too large")
    if b+1 == b:
        raise OverflowError("b is too large")

    return int(a) + int(b)
