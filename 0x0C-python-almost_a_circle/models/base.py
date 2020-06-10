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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file."""
        empty_list = []
        if list_objs is not None:
            for i in list_objs:
                empty_list.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """Json to string."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                tup = cls(1, 1)
            elif cls.__name__ == "Square":
                tup = cls(1)
            tup.update(**dictionary)
            return tup

    @classmethod
    def load_from_file(cls):
        """Load from file."""
        file_to_load = str(cls.__name__) + ".json"
        try:
            with open(file_to_load, "r") as f:
                data = cls.from_json_string(f.read())
                return [cls.create(**i) for i in data]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to file."""
        list_to_save = []
        if len(list_objs) is not 0:
            for i in list_objs:
                list_to_save.append(i.to_dictionary())
        with open(cls.__name__ + ".csv", "w+") as f:
            f.write(cls.to_json_string(list_to_save))

    @classmethod
    def load_from_file_csv(cls):
        """Load from file."""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                cvs = Base.from_json_string(f.read())
                list_to_load = []
                for i in cvs:
                    list_to_load.append(cls.create(**i))
                return list_to_load
        except IOError:
            return []
