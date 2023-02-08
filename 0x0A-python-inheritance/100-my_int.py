#!/usr/bin/python3
"""
A class that inherits from int but overrides the __eq__
and __ne__ methods
"""


class MyInt(int):
    """
    Inherits from int and then overrides the __eq__
    and __ne__ methods
    """
    def __init__(self, value):
        """
        Instantiates the class
        Attr:
            value: value of MyInt
        """
        self.value = value
        super().__init__()

    def __eq__(self, other):
        """
        Flips the equality operator - ==
        """
        return self.value != other

    def __ne__(self, other):
        """
        Flips the inequality operator - !=
        """
        return self.value == other
