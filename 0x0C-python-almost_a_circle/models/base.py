#!/usr/bin/python3
"""First base module."""


class Base:
    """Base class for this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Construct for initializing variables."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
