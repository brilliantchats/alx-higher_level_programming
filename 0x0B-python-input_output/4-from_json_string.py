#!/usr/bin/python3
"""
Returns an object from a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object from JSON string, my_str
    Args:
        my_str: JSON string representing a Python object
    """
    return json.loads(my_str)
