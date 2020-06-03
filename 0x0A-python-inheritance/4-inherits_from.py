#!/usr/bin/python3
"""CHeck class."""


def inherits_from(obj, a_class):
    """Check inheritance."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
