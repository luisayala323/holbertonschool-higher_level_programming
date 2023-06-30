#!/usr/bin/python3

"""
Module contains Base class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherited from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance

        Args:
            size (int): size of the Square (both width and height)
            x (int, optional): The x of the Square. Defaults to 0.
            y (int, optional): THe y of the Square. Defaults to 0.
            id (int, optional): The id of the Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Args:
            value (int): value to set size to
        """
        self.width = self.height = value

    def __str__(self):
        """
        Print the string representation of the Square method.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Accept both positional arguments and keyword arguments.
        """
        num_args = len(args)
        if num_args == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.size = args[1]
            if num_args > 2:
                self.x = args[2]
            if num_args > 3:
                self.y = args[3]
