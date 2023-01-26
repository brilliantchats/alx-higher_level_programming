#!/usr/bin/python3
"""
'Square' a class for a Square
"""


class Square:
    """
    A class about a Square
    Attributes:
        size: size of the square
    """
    def __init__(self, size=0):
        """
        init method of the square
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

    @property
    def size(self):
        """
        Gets the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        returns area of the square
        """
        return self.__size * self.__size
