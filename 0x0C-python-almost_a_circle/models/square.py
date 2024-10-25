#!/usr/bin/python3
"""
Creates a class, Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class, Square, inherited from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square with the parameters size, x, y, and id
        Height and width to be assigned to value of size
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter function for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter function
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return [Square] (<id>) <x>/<y> - <size>
        """
        return (
                f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}"
                )

    def update(self, *args, **kwargs):
        """
        Assigns attributes to arguments

        *args:
            1st arg: id attribute
            2ns arg: size attribute
            3rd arg: x attribute
            4th arg: y attribute
        **kwargs:
            key/value pairs representing attributes
        """
        if args:
            attri = ["id", "size", "x", "y"]
            for idx, val in enumerate(args):
                if idx < len(attri):
                    setattr(self, attri[idx], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
