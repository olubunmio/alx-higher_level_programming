#!/usr/bin/python3
"""0-lookup

A module that contains one function that returns a list of available
attributes in a module
"""


def lookup(obj):
    """A function that returns list of available attributes"""
    return list(dir(obj))
