#!/usr/bin/python3
"""Print sorted list."""


class MyList(list):
    """Subclass of list that receives a list."""

    def print_sorted(self):
        """Sort list."""
        print(sorted(self))
