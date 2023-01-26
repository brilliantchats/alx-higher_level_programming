#!/usr/bin/python3
"""
'Square' a class of a square
"""


class Square:
    """
    A class about a square
    Attribute:
        size: size of the square
    """
    def __init__(self, size):
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

    @property
    def size(self):
        """
        Gets size of the square
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
        Returns the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the '#' symbol
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
