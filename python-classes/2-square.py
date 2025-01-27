#!/usr/bin/python3
"""
This module defines a simple Square class.
"""


class Square:
    """
    This class represents a geometric square with a given size.
    """
    def __init__(self, size=0):
        """
        Initializes the square with an optional size (the default is 0).

        Arguments:
            size (int): The size of the side of the square.

        Errors:
            TypeError: Raised if size is not an integer.

            ValueError: Raised if size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
