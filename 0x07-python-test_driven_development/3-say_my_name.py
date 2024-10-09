#!/usr/bin/python3
"""
Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: Must be a str
        last_name: Must be a str

    Raises:
        TypeError: If first_name / last_name are not str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")

    print(f"My name is {first_name} {last_name}")
