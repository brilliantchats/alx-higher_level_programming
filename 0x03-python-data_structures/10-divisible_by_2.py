#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    length = len(my_list)
    new_cpy = []
    for i in range(length):
        if my_list[i] % 2 == 0:
            new_cpy.append(True)
        else:
            new_cpy.append(False)
    return new_cpy
