#!/usr/bin/python3
"""
Unittests for square.py
"""
import unittest
from models.square import Square


class testSquare(unittest.TestCase):

    def test_init(self):
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_size_setter(self):
        s = Square(10)
        s.size = 20
        self.assertEqual(s.size, 20)

    def test_invalid_size_type(self):
        s = Square(10)
        with self.assertRaises(TypeError):
            s.size = "15"

    def test_invalid_size_value(self):
        s = Square(10)
        with self.assertRaises(ValueError):
            s.size = -10

    def test_area(self):
        s = Square(9)
        self.assertEqual(s.area(), 81)


if __name__ == "__main__":
    unittest.main()
