#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes in class."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Override of the str method."""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                    self.__y, self.__width)

    def update(self, *args, **kwargs):
        """Update that receives args."""
        measures = ['id', 'width', 'height' 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, measures[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Update to dictionary."""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
