#!/usr/bin/python3
"""Program that opens and counts  a file's lines using with."""


def read_lines(filename="", nb_lines=0):
    """
    Read a file and coubts its lines.

    Args:
    filename- file to open
    nb_lines: number of lines to be printed
    return: Conter
    """
    i = 0
    with open(filename) as f:
        if nb_lines == 0:
            print(f.read())
        else:
            while i < nb_lines:
                print(f.readline(), end='')
                i += 1
