#!/usr/bin/python3
"""empty class defining a square."""


class Square:
    """class defining a Square."""

    def __init__(self, size=0):
        """Initialize private attributes."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of a square."""
        area = self.__size ** 2
        return area
