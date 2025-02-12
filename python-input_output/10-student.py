#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instantiate the Student class with:
        first_name, last_name, and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}
