#!/usr/bin/python3
"""
Function which opens, reads and prints a file to stdout
"""


def read_file(filename=""):
    """
    Opens and reads a file
    """
    with open(filename, 'r', encoding="utf-8") as file_obj:
        print(file_obj.read(), end="")
