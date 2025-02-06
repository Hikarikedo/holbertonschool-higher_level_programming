#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list
    in sorted order.
    """

    def print_sorted(self):
        print(sorted(self))
