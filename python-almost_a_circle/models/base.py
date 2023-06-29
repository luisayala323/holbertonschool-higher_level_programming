#!/usr/bin/python3

"""" Module with class name Base"""


class Base:
    # class name base
    __nb_objects = 0

    def __init__(self, id=None):
        # constructor method
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
