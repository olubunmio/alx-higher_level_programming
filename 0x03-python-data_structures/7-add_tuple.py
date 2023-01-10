#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lst1 = [0, 0]
    lst2 = [0, 0]

    for i, item in enumerate(tuple_a):
        if i < 2:
            lst1[i] = item

    for i, item in enumerate(tuple_b):
        if i < 2:
            lst2[i] = item
    tuple_sum = (lst1[0] + lst2[0], lst1[1] + lst2[1])
    return tuple_sum
