#!/usr/bin/python3
"""This module define a class Student"""


class Student:
    """
    A class representing a student with attributes:
    first_name, last_name, and age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with the provided:
        first name, last name, and age

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): A list of attributes to retrieve.
            If None, all attributes are retrieved

        Returns:
            dict: A dictionary containing the requested,
            attributes of the Student
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
            }
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces the attributes of the Student instance,
        based on the provided dictionary

        Args:
            json (dict): A dictionary containing,
            new values for the Student's attributes
        """
        for key, value in json.items():
            setattr(self, key, value)
