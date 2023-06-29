#!/usr/bin/python3

"""Module contains Base class"""

from models.base import Base


class Rectangle(Base):

    """Class Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int, optional): x of the Rectangle. Defaults to 0.
            y (int, optional): y of the Rectangle. Defaults to 0.
            id (int, optional): id of the Rectangle. Default
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
