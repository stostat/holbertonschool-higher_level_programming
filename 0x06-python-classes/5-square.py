#!/usr/bin/python3
"""empty class defining a square."""


class Square:
    """class defining a Square."""

    def __init__(self, size=0):
        """Initialize private attributes."""
        self.size = size

    @property
    def size(self):
        """Getter for private attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for private attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of a square."""
        area = self.__size ** 2
        return area

    def my_print(self):
        """Print square with #."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
