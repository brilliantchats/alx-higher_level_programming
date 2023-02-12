#!/usr/bin/python3
"""
The base class of this project
"""


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise a base class object
        Attr:
            id: the unique id of individual Base objects
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
