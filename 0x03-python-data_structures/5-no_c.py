#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for letter in my_string:
        if letter not in 'Cc':
            new_str = new_str + letter
    return new_str
