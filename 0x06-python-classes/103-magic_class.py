#!/usr/bin/python3
"""Define circle."""


import math


class MagicClass:
    """Define circle."""

    def __init__(self, radius=0):
        """Init a circumference."""
        self._MagicClass__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Return area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Return radius."""
        return 2 * math.pi * self._MagicClass__radius
