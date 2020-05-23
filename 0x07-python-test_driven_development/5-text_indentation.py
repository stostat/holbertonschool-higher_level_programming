#!/usr/bin/python3
"""Indents text after special characters."""


def text_indentation(text):
    """Indents text after special characters."""
    chars = ['.', ':', '?']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in chars:
            print(i)
        else:
            print(i, end='')
