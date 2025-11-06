"""
Unit tests for Cube.

This test suite verifies that the Cube class behaves correctly and fulfills
the requirements of the Shape3D contract.

Tests included:
- initialization and value validation
- volume and surface area calculations
- translation of x/y/z position
- comparison operators (>, <, ==, >=, <=) based on volume
- string representations (__str__ and __repr__)
"""

import unittest
from cube import Cube

class TestCube(unittest.TestCase):

    def test_init(self):
        c = Cube(4, 1, -2, 3)
        self.assertEqual(c.side, 4)
        self.assertEqual(c._x, 1)
        self.assertEqual(c._y, -2)
        self.assertEqual(c._z, 3)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Cube(-1)
        with self.assertRaises(TypeError):
            Cube("a")

    def test_surface_area(self):
        c = Cube(3)
        expected = 6 * (3 ** 2)
        self.assertEqual(c.surface_area, expected)

    def test_volume(self):
        c = Cube(2)
        expected = 2 ** 3
        self.assertEqual(c.volume, expected)

    def test_translate(self):
        c = Cube(1, 0, 0, 0)
        c.translate(4, -1, 2)
        self.assertEqual(c._x, 4)
        self.assertEqual(c._y, -1)
        self.assertEqual(c._z, 2)

    def test_equality(self):
        c1 = Cube(3)
        c2 = Cube(3, 10, 10, 10)  # same side, different position
        c3 = Cube(4)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)

    def test_less_than(self):
        c_small = Cube(2)
        c_big = Cube(5)
        self.assertTrue(c_small < c_big)
        self.assertFalse(c_big < c_small)

    def test_greater_than(self):
        c_small = Cube(2)
        c_big = Cube(5)
        self.assertTrue(c_big > c_small)
        self.assertFalse(c_small > c_big)

    def test_less_or_equal(self):
        c1 = Cube(3)
        c2 = Cube(3)
        c3 = Cube(4)
        self.assertTrue(c1 <= c2)  # equal sides
        self.assertTrue(c1 <= c3)  # strictly less
        self.assertFalse(c3 <= c1)

    def test_greater_or_equal(self):    
        c1 = Cube(3)
        c2 = Cube(3)
        c3 = Cube(2)
        self.assertTrue(c1 >= c2)  # equal sides
        self.assertTrue(c1 >= c3)  # strictly greater
        self.assertFalse(c3 >= c1)

    def test_str(self):
        c = Cube(2, 1, 2, 3)
        self.assertEqual(str(c), "Cube(side=2, pos=(1, 2, 3))")

    def test_repr(self):
        c = Cube(3, -1, -2, -3)
        self.assertEqual(repr(c), "Cube(side=3, x=-1, y=-2, z=-3)")

if __name__ == '__main__':
    unittest.main()