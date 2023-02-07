#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Defines a class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    Defines its own constructor with attributes validated by
    the BaseGeometry integer validator
    """
    def __init__(self, width, height):
        """
        Instantiates a Rectangle object with the following attributes
        Attr:
            width: width of the rectangle
            height: height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
