#!/usr/bin/python3

"""Function that returns True if the object is
 an instance of a class that inherited
   (directly or indirectly) from the specified class"""


def inherit_from(obj, a_class):
    """Method that returns True if the object is an
 instance of a class that inherited"""
    return issubclass(obj, a_class)
