#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples together"""
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    x = 0
    y = 0
    # Test how long tuple a is
    if len_a == 0:
        new_a = 0, 0
    elif len_a == 1:
        new_a = tuple_a[0], 0
    else:
        new_a = tuple_a[0], tuple_a[1]
    # Test how long tuple b is
    if len_b == 0:
        new_b = 0, 0
    elif len_b == 1:
        new_b = tuple_b[0], 0
    else:
        new_b = tuple_b[0], tuple_b[1]

    x += (new_a[0] + new_b[0])
    y += (new_a[1] + new_b[1])
    return x, y
