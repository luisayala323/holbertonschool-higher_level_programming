#!/usr/bin/python3

""" Defines  a class-checking function"""


def is_same_class(obj, a_class):
    """Check if he object is exactly an instance
      of the specified class otherwise return True or False"""

    return type(obj) is a_class
