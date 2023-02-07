#!/usr/bin/python3
"""
Writes to a file
"""


def write_file(filename="", text=""):
    """
    Writes to a file
    Args:
        filename: name of the file
        text: the text to write to the file
    """
    with open(filename, 'w', encoding="utf-8") as file_obj:
        num_char_written = file_obj.write(text)
        return num_char_written
