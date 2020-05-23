#!/usr/bin/python3
"""Print square, given an integer."""


def print_square(size):
    """Print square, given an integer."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
