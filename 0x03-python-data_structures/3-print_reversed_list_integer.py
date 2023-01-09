#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints the integers of a list in reverse order"""
    length = len(my_list)
    if length == 0:
        print()
        return
    for i in range(length - 1, -1, -1):
        print("{:d}".format(my_list[i]))
