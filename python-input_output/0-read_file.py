#!/usr/bin/python3

"""Defines a text file-reading functionality"""


def reading(filename=""):
    """
    read and prints  UTF8 text file
    Args: filename (string): name of the file

    """

    with open(filename, 'r') as file:
        print(file.read(), end="")
