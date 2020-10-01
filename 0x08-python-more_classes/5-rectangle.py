#!/usr/bin/python3
"""Class for rectangle."""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private attribute for width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private attribute for height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle."""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return perimeter."""
        if self.__width == 0 or self.__height == 0:
            perim = 0
        else:
            perim = (self.__width * 2) + (self.__height * 2)
        return perim

    def __str__(self):
        """Return string of #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        return (self.__height * ((self.__width * '#') + '\n'))[:-1]

    def __repr__(self):
        """Return string of #."""

        return ("Rectangle({}, {})".format(self.__width, self.height))

    def __del__(self):
        """Delete rectangle."""

        print('Bye rectangle...')
