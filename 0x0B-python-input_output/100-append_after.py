#!/usr/bin/python3
"""
Appends a line of text after occurence of a particular string on each line
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text after occurence of a particular string
    on each line of a file
    Args:
        filename: the name of the file to work on
        search_string: the string to search for on each line
        new_string: the string to append
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        f.seek(0)
        file_strings = f.readlines()
        i = 0
        for string in file_strings:
            if search_string in string:
                file_strings[i] = string + new_string
            i = i + 1
        result_str = "".join(file_strings)
        f.seek(0)
        f.write(result_str)
