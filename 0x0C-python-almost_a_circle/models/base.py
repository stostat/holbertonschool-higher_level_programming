#!/usr/bin/python3
"""First base module."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Take Dictionary to json."""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
