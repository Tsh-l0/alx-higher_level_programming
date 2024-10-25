#!/usr.bin/python3
"""
Unittests for rectangle.py
"""
import unittest
from models.rectangle import Rectangle
import io
import unittest.mock


class TestRectangleInstantiation(unittest.TestCase):
    """
    Testing the class, Rectangle
    """

    def test_init_no_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_init_with_id(self):
        r1 = Rectangle(10, 3, 1, 1, 95)
        self.assertEqual(r1.id, 95)

    def test_width_getter(self):
        r = Rectangle(25, 17)
        self.assertEqual(r.width, 25)

    def test_height_getter(self):
        r = Rectangle(25, 17)
        self.assertEqual(r.width, 25)

    def test_x_getter(self):
        r = Rectangle(25, 10, 20)
        self.assertEqual(r.x, 20)

    def test_y_getter(self):
        r = Rectangle(10, 2, 0, 4)
        self.assertEqual(r.y, 4)

    def test_width_setter_invalid_type(self):
        r = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            r.width = "10"

    def test_width_setter_invalid_type(self):
        r = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height_setter_invalid_type(self):
        r = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            r.height = "5"

    def test_height_setter_invalid_value(self):
        r = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            r.height = -5

    def test_x_setter_invalid_type(self):
        r = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            r.x = "2"

    def test_x_setter_invalid_value(self):
        r = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            r.x = -2

    def test_y_setter_invalid_type(self):
        r = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            r.y = "2"

    def test_y_setter_invalid_value(self):
        r = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            r.y = -2


class TestRectangleMethods(unittest.TestCase):
    """
    Unittests for testing rectangle class methods
    """

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
