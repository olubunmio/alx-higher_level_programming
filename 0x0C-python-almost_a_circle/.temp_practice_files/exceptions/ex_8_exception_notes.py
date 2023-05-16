#!/usr/bin/python3

# ExecptionGroup not supported in python3.9
# `add_note()` exception method also not supported in python3.9 (new in 3.11)

try:
    raise TypeError("bad type")
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
