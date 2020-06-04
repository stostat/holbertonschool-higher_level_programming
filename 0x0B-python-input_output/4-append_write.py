#!/usr/bin/python3
"""Program that opens and counts  a file's lines using with."""


def append_write(filename="", text=""):
    """
    Read a file and coubts its lines.

    Args:
    filename- file to open
    text: text to add
    return: Count of characters written
    """
    with open(filename, 'a') as f:
        return f.write(text)
