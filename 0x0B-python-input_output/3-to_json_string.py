#!/usr/bin/python3
"""
Returns JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of my_obj
    Args:
        my_obj: the object
    """
    my_obj_str = json.dumps(my_obj)
    return my_obj_str
