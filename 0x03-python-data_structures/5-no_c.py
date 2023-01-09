#!/usr/bin/python3
def no_c(my_string):
    """Remove characters c and C from a given string"""
    new_str = ""
    length = len(my_string)
    if length == 0:
        return new_str
    for char in range(length):
        if my_string[char] != 'c' and my_string[char] != 'C':
            new_str += my_string[char]
    return new_str
