#!/usr/bin/python3
"""Class for rectangle."""


class Rectangle:
    """Rectangle class."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """Return string of symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        return (self.__height * ((self.__width * str(self.print_symbol)) +
                '\n'))[:-1]

    def __repr__(self):
        """Return string of #."""

        return ("Rectangle({}, {})".format(self.__width, self.height))

    def __del__(self):
        """Delete rectangle."""

        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles by area."""

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """create square."""

        return cls(size, size)
