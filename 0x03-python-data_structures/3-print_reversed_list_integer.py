#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints the integers of a list in reverse order"""
    my_list.reverse()
    for intgr in my_list:
        print("{:d}".format(intgr))
