#!/usr/bin/python3

"""class BaseGeometry"""


class BaseGeometry:
    """exception error area() not implemented"""

    def area(self):
        """Public instance method: def area(self):
          that raises an Exception with the message
            area() is not implemented"""
        raise Exception('area() is not implemented')
