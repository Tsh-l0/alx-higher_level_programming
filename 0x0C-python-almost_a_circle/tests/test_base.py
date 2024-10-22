#!/usr/bin/python3
"""
unittests for base.py
"""


import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the class, Base
    """
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(23, Base(23).id)
