#!/usr/bin/python3
"""
Adds all command line args to a list, then saves it to a json file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_to_file():
    """
    Adds all command line args to a list, then saves to a json file
    """
    filename = "add_item.json"
    try:
        data = load_from_json_file(filename)
        for i in range(1, len(sys.argv)):
            data.append(sys.argv[i])
        save_to_json_file(data, filename)
    except Exception:
        save_to_json_file([], filename)

add_to_file()
