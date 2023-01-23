#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements from mylist"""
    length = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            length = length + 1
        except IndexError:
            break
    print()
    return length
