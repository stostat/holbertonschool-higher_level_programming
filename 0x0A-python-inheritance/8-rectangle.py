#!/usr/bin/python3
"""Empty class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class rectangle(BaseGeometry):
    """Raise exception."""

    def __init__(self, width, height):
        """Instatiate width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
