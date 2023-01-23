#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints first x elements of a list that are ints"""
    length = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            length = length + 1
        except (ValueError, TypeError):
            pass
    print()
    return length
