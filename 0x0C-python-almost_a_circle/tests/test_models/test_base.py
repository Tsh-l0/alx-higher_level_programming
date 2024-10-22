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
