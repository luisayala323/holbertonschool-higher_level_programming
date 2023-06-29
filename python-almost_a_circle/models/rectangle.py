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

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__y = value
