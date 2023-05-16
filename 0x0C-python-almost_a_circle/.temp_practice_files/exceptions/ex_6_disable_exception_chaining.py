#!/usr/bin/python3
"""Disable exception chaining using ``from None``"""

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
