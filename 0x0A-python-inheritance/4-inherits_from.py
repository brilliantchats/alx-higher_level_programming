#!/usr/bin/python3
"""
Checks if a an object is an instance of a class that
inherited from the given class or any of the given
classes base classes
"""


def inherits_from(obj, a_class):
    """Checks if obj inherits from a_class"""
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
        else:
            return False
    else:
        return False
