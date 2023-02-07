#!/usr/bin/python3
"""
Inherits from another base class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square that inherits from Rectangle class
    """
    def __init__(self, size):
        """
        Instantiates the square class
        Attr:
            size: size of the sides of the square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size
