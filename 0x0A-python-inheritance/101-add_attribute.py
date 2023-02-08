#!/usr/bin/python3
"""
adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object is possible
    Attr:
        obj: the object to add the attribute to
        attribute: the attribute to add
        value: the value of to assign to the attribute
    """
    try:
        obj.name = value
    except AttributeError:
        raise TypeError("can't add new attribute")
