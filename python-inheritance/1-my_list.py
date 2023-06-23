#!/usr/bin/python3

"""Class MyList that inherits list."""


class MyList(list):
    """Class print list ascended order."""

    def print_sorted(self):
        """Print list in ascended order."""
        if isinstance(self, list):
            ascend = sorted(self)
            print(ascend)
