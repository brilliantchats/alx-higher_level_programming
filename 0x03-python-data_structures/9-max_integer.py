#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list"""
    length = len(my_list)
    if length == 0:
        return None
    max_num = my_list[0]
    for i in range(1, length):
        if max_num < my_list[i]:
            max_num = my_list[i]
    return max_num
