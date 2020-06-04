#!/usr/bin/python3
"""Program that opens and counts  a file's lines using with."""
import json


def from_json_string(my_str):
    """
    Read a json object  and represent it as string in Python.

    Args:
    my_obj- Object to be represented
    return: String
    """
    obj = json.loads(my_str)
    return obj
