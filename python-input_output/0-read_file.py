#!/usr/bin/python3
"""Define a function 'read_file'"""


def read_file(filename=""):
    """
    Function that reads the contents of a file and prints it to standard output

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string ("")
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
