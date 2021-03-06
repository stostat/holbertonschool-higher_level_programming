#!/usr/bin/python3
"""Program that opens and counts  a file's lines using with."""
import json


def save_to_json_file(my_obj, filename):
    """
    Read a json object  and represent it as string in Python.

    Args:
    my_obj- Object to be represented
    return: String
    """
    with open(filename, 'w') as fp:
        json.dump(my_obj, fp)
