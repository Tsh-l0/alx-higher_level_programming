#!/usr/bin/python3
"""
Unittests for the function def max_integer(list=[]):
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define unittest
    """

    def max_at_end(self):
        self.assertEqual(max_integer([2, 4, 6, 8]), 4)

    def max_at_middle(self):
         self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_str(self):
        """Test an empty str"""
        self.assertEqual(max_integer(""), None)

    def test_list_str(self):
        """Tests a list of str"""
        sentence = ["python", "is", "my", "favourite"]
        self.assertEqual(max_integer(sentence), "favourite")

    def test_str(self):
        """Tests for a str"""
        word = "python"
        self.assertEqual(max_integer(word), "p")

    def test_float(self):
        """Tests for floats"""
        float = [1.12, 2.24, 3.14, 4.45. 5.56]
        self.assertEqual(max_intetger(float), 3.14)
