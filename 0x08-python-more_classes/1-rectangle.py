#!/usr/bin/python3
"""
A class about a rectangle with width and height attributes
"""


class Rectangle():
    """
    Class about a Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialise a Rectangle instance
        Args:
            width: the smaller of the two sides
            height: the larger of the two sides
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        Args:
            value: the value to set for width
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        Args:
            value: the value to set for height
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
