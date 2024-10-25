#!/usr/bin/python3
"""
Class, Rectangle, that inherits from Base
"""


from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints the class, Rectangle using the character #
        """
        for aa in range(self.y):
            print("")
        for row in range(self.__height):
            for ac in range(self.x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Overrides the __str__ method so that it returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>
        """
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.height}"
                )

    def update(self, *args):
        """
        Assigns an argument to every attribute
        1st arg: id attribute
        2nd arg: width attribute
        3rd arg: height attribute
        4th arg: x atribute
        5th arg: y attribute
        """
        attri = ["id", "width", "height", "x", "y"]
        for idx, val in enumerate(args):
            if idx < len(attri):
                setattr(self, attri[idx], val)
