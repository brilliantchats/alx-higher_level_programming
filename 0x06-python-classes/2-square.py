#!/usr/bin/python3
"""
'Square' class for a square
"""


class Square:
    """
    A class for a square
    Attributes:
        size: size of a square
    """
    def __init__(self, size=0):
        """
        init method for the square class
        Args:
            size: size of the the square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
