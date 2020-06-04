#!/usr/bin/python3
"""Program that opens and counts  a file's lines using with."""
import json


def to_json_string(my_obj):
    """
    Read a json object  and represent it as string in Python.

    Args:
    my_obj- Object to be represented
    return: String
    """
    string = json.dumps(my_obj)
    return string
