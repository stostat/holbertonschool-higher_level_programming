#!/usr/bin/python3
"""Program that loads json file to object in python."""
import json


def load_from_json_file(filename):
    """
    Load json file to object in python.

    Args:
    filename - File to be opened
    return: None
    """
    with open(filename) as fp:
        json.load(fp)
