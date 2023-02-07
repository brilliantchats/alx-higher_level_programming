#!/usr/bin/python3
"""
Writes an object to a file as a json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object, my_obj, to a file, filename as a JSON representation
    Args:
        my_obj: the object to write to a file
        filename: the file to write to
    """
    with open(filename, 'w', encoding="utf-8") as obj:
        obj.write(json.dumps(my_obj))
