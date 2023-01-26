#!/usr/bin/python3
"""
'Square' a class for a Square
"""


class Square:
    """
    A class of a Square
    Attributes:
        size: size of a square
    """
    def __init__(self, size=0):
        """
        init method for the class
        Args:
            size: size of the square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        area method to get the area for the square
        """
        return self.__size * self.__size
