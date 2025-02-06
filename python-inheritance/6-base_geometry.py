#!/usr/bin/python3
"""
Module that defines the BaseGeometry class with an
area method that raises an exception.
"""


class BaseGeometry:
    """
    A class representing base geometry.

    Public instance method:
        - area: raises an exception if not implemented in a subclass.
    """

    def area(self):
        """
        Raises an exception because the area method is not implemented.

        Raises:
            Exception: with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
