#!/usr/bin/python3

"""
Imports a function that reads a text file (UTF8)
and prints it
"""


def reading(filename=""):
    """
    read and prints  UTF8 text file
    Args: filename (string): name of the file

    """

    with open(filename, 'r') as file:
        print(file.read(), end="")
