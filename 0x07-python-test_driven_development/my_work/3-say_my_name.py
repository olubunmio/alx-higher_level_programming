#!/usr/bin/python3
"""say_my_name module

A module that contains only one function ``say_my_name()`` that prints
someone's name.
"""


def say_my_name(first_name, last_name=""):
    """A function that prints someones name.

    Args:
        first_name (str): the first argument to the string
        last_name (str): the second argument to the string

    Return:
        returns "My name is {first_name} {last_name}"
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    fullname = "{:s} {:s}".format(first_name, last_name)
    print("My name is {}".format(fullname))


if __name__ == "__main__":
    say_my_name = __import__('3-say_my_name').say_my_name

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
