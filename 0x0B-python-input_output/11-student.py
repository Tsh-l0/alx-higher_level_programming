#!/usr/bin/python3
"""
A class that defines a student using attributes
"""


class Student:
    """
    Class, Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the class student using the attributes in the args
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the class, Student
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if
                    hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes from the class, Student

        Args:
            json: A dictionary with the attributes to be used
        """
        for k, value in json.items():
            setattr(self, k, value)
