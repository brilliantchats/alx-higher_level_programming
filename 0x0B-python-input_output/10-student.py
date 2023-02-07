#!/usr/bin/python3
"""
A class that defines a student
"""


class Student():
    """
    Class about Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates the Student class
        Attr:
            first_name: First name of Student
            last_name: Last name of Student
            age: Age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs:
            data = dict()
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
                if attr in self.__dict__.keys():
                    data[attr] = self.__dict__[attr]
            return data
        else:
            return self.__dict__
