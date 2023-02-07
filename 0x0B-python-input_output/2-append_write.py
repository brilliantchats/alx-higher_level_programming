#!/usr/bin/python3
"""
Appends to the end of a file
"""


def append_write(filename="", text=""):
    """
    Appends to the end of a file
    Args:
        filename: name of the file to append to
        text: text to append to file
    """
    with open(filename, 'a', encoding="utf-8") as file_obj:
        chars = file_obj.write(text)
        return chars
