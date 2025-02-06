#!/usr/bin/python3
"""
Module that defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or an instance of a class
    that inherited from a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class or
        a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
