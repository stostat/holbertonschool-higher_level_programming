#!/usr/bin/python3
"""Print first and last name."""

if __name__ == "__main__":
    import doctest
    doctest.testmod()


def say_my_name(first_name, last_name=""):
    """Print first and last name."""
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
