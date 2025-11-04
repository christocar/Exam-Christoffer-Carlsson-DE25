"""
Unit tests for the Circle class.

This file verifies:
- initialization and validation
- area and perimeter calculations
- translation (movement)
- unit circle detection
- rich comparisons: ==, <, >, <=, >=
- string representations: __str__, __repr__
"""

import unittest
from math import pi
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_init(self):
        c = Circle(5, 2, 3)
        self.assertEqual(c.radius, 5)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 3)

    def test_area(self):
        c = Circle(3)
        self.assertAlmostEqual(c.area, pi * 9, places=9)

    def test_perimeter(self):
        c = Circle(2)
        self.assertAlmostEqual(c.perimeter, 4 * pi, places=9)

    def test_translate(self):
        c = Circle(1, 0, 0)
        c.translate(10, -5)
        self.assertEqual(c.x, 10)
        self.assertEqual(c.y, -5)

    def test_is_unit_circle_true(self):
        self.assertTrue(Circle(1).is_unit_circle())

    def test_is_unit_circle_false(self):
        self.assertFalse(Circle(3).is_unit_circle())

    def test_equality(self):
        c1 = Circle(4)
        c2 = Circle(4, 10, 10)  # same area, different position
        c3 = Circle(5)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)

    def test_less_than(self):
        c_small = Circle(2)
        c_big = Circle(5)
        self.assertTrue(c_small < c_big)
        self.assertFalse(c_big < c_small)

    def test_greater_than(self):
        c_small = Circle(2)
        c_big = Circle(5)
        self.assertTrue(c_big > c_small)
        self.assertFalse(c_small > c_big)

    def test_less_or_equal(self):
        c1 = Circle(3)
        c2 = Circle(3)
        c3 = Circle(4)
        self.assertTrue(c1 <= c2)  # equal areas
        self.assertTrue(c1 <= c3)  # strictly less
        self.assertFalse(c3 <= c1)

    def test_greater_or_equal(self):
        c1 = Circle(3)
        c2 = Circle(3)
        c3 = Circle(2)
        self.assertTrue(c1 >= c2)  # equal areas
        self.assertTrue(c1 >= c3)  # strictly greater
        self.assertFalse(c3 >= c1)

    def test_str(self):
        c = Circle(5, -1, 2)
        s = str(c)
        self.assertIn("Circle", s)
        self.assertIn("radius=5", s)
        self.assertIn("center=(-1, 2)", s)

    def test_repr(self):
        c = Circle(5, -1, 2)
        r = repr(c)
        self.assertIn("Circle", r)
        self.assertIn("radius=5", r)
        self.assertIn("x=-1", r)
        self.assertIn("y=2", r)


if __name__ == "__main__":
    unittest.main()
