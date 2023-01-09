#!/usr/bin/python3
def element_at(my_list, idx):
    """Returns the elem at index idx in my_list"""
    length = len(my_list)
    if idx >= length or idx < 0:
        return None
    return my_list[idx]
