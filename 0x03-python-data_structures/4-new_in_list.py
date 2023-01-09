#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Repalce an elem of a copy of my_list at index idx"""
    length = len(my_list)
    my_list_cpy = my_list.copy()
    if idx >= length or idx < 0:
        return my_list_cpy
    my_list_cpy[idx] = element
    return my_list_cpy
