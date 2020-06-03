#!/usr/bin/python3
"""Empty class."""


class BaseGeometry:
    """Raise exception."""

    def area(self):
        """Raise exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if value is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
