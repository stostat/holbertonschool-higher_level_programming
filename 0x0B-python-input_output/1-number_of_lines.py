#!/usr/bin/python3
"""Program that opens and counts  a file's lines using with."""


def number_of_lines(filename=""):
    """
    Read a file and coubts its lines.

    Args: filename- file to open
    return: Conter
    """
    i = 0
    with open(filename) as f:
        for line in f:
            i += 1
    return i
