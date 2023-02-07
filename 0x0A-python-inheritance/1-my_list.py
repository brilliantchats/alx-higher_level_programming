#!/usr/bin/python3
"""
Prints a list in sorted ascending order
"""


class MyList(list):
    """
    A class that inherits from the super class list
    """
    def print_sorted(self):
        """
        Prints a sorted ascending list
        """
        print(sorted(self))
