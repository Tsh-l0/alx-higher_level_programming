#!/usr/bin/python3
"""
unittests for base.py
"""


import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the class, Base
    """

    def test_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        b1 = Base(23)
        self.assertEqual(b1.id, 23)

    def test_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_json_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file_none(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as my_file:
            self.assertEqual(my_file.read(), "[]")

    def test_load_from_no_file(self):
        self.assertEqual(Base.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
