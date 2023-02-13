#!/usr/bin/python3
"""
A Rectangle class that inherits from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise the Rectangle class
        Attrs:
            width: shorter side of the rectangle
            height: longer side of the rectangle
            x: x
            y: y
            id: id of the unique rectangle object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value for width"""
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x"""
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y"""
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the area using '#' symbol"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Overriding the inbuilt str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
