#!/usr/bin/python3
"""Rectangle module module."""
from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits from base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Construct attributes of sub class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return attribute."""
        return(self.__width)

    @width.setter
    def width(self, value):
        pass

    @property
    def height(self):
        """Return attribute."""
        return(self.__height)

    @height.setter
    def height(self, value):
        pass

    @property
    def x(self):
        """Return attribute."""
        return(self.__x)

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        """Return attribute."""
        return(self.__y)

    @y.setter
    def y(self, value):
        pass
