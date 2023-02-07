#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry():
    """
    Defines two instance methods
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        Attr:
            name: a string
            value: should be an int > 0
        """
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
