#!/usr/bin/python3
"""
Function to check if an obj is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """checks if obj is an exact instance of a_class"""
    if type(obj) is a_class:
        return True
    else:
        return False
