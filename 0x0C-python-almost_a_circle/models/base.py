#!/usr/bin/python3
"""
Base class to manage all future classes
"""
import json
import os


class Base:
    """
    Represents the base model

    This is tge base classe for all classes in the project
    Manages the id to avoid repeating the same code
    """

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of list_dictionaries

        args:
            A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of all instances
        """
        file_name = cls.__name__ + ".json"
        list_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, "r") as my_file:
                str = my_file.read()
                list_dictionaries = cls.from_json_string(str)
                for dictionary in list_dictionaries:
                    list_instances.append(cls.create(**dictionary))
        return list_instances
