#!/usr/bin/python3
"""
Base class to manage all future classes
"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id: if id != None, assign the public instance attribute with
            value. if id == None __nb_objects++
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
