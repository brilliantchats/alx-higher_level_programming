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
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
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

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns a new string object representation of this class"""
        result = ""
        if self.width == 0 or self.height == 0:
            return result
        for i in range(self.height):
            for j in range(self.width):
                result = result + "#"
            if i < self.height - 1:
                result = result + "\n"
        return result

    def __repr__(self):
        """
        Returns a string representation which can be evaluated back to
        a Rectangle object using the eval object
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Is invoked when an instance is deleted"""
        print("Bye rectangle...")
