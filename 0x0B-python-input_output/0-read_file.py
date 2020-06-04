#!/usr/bin/python3
"""Program that opens and prints a file using with."""


def read_file(filename=""):
    """
    Read a file and prints it.

    Args: filename- file to open
    return: Nothing
    """
    with open(filename) as f:
        for line in f:
            print(line, end='')
