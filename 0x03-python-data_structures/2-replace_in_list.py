#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an elem index idx in my_list with element"""
    length = len(my_list)
    if idx >= length or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
