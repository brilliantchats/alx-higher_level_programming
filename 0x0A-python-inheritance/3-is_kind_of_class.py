#!/usr/bin/python3
"""
Returns true if the given obj is an instance of a given class
"""


def is_kind_of_class(obj, a_class):
    """
    Is obj an instance of a_class or any of base classes
    of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
