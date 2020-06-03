#!/usr/bin/python3
"""Return all attributes and methods in an object."""


def lookup(obj):
    """
    Lookup for an object and return attributes and methods.

    Args:
    obj - the object to be checkes
    Return:
    List
    """
    return dir(obj)
