import unittest
from math import pi
from sphere import Sphere

class TestSphere(unittest.TestCase):
    def test_init(self):
        s = Sphere(5, 2, -3, 7)
        self.assertEqual(s.radius, 5)
        self.assertEqual(s._x, 2)
        self.assertEqual(s._y, -3)
        self.assertEqual(s._z, 7)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Sphere(-1)
        with self.assertRaises(TypeError):
            Sphere("a")

    def test_surface_area(self):
        s = Sphere(3)
        expected = 4 * pi * (3 ** 2)
        self.assertAlmostEqual(s.surface_area, expected, places=9)

    def test_volume(self):
        s = Sphere(2)
        expected = (4/3) * pi * (2 ** 3)
        self.assertAlmostEqual(s.volume, expected, places=9)

    def test_translate(self):
        s = Sphere(1, 0, 0, 0)
        s.translate(5, -3, 2)
        self.assertEqual(s._x, 5)
        self.assertEqual(s._y, -3)
        self.assertEqual(s._z, 2)

    def test_is_unit_sphere_true(self):
        self.assertTrue(Sphere(1).is_unit_sphere())

    def test_is_unit_sphere_false(self):
        self.assertFalse(Sphere(4).is_unit_sphere())

    def test_equality(self):
        s1 = Sphere(3)
        s2 = Sphere(3, 10, 10, 10)  # same radius, different position
        s3 = Sphere(4)
        self.assertTrue(s1 == s2)
        self.assertFalse(s1 == s3)

    def test_less_than(self):
        s_small = Sphere(2)
        s_big = Sphere(5)
        self.assertTrue(s_small < s_big)
        self.assertFalse(s_big < s_small)

    def test_greater_than(self):
        s_small = Sphere(2)
        s_big = Sphere(5)
        self.assertTrue(s_big > s_small)
        self.assertFalse(s_small > s_big)

    def test_less_or_equal(self):
        s1 = Sphere(3)
        s2 = Sphere(3)
        s3 = Sphere(4)
        self.assertTrue(s1 <= s2)  # equal radii
        self.assertTrue(s1 <= s3)  # strictly less
        self.assertFalse(s3 <= s1)

    def test_greater_or_equal(self):
        s1 = Sphere(3)
        s2 = Sphere(3)
        s3 = Sphere(2)
        self.assertTrue(s1 >= s2)  # equal radii
        self.assertTrue(s1 >= s3)  # strictly greater
        self.assertFalse(s3 >= s1)

    def test_str(self):
        s = Sphere(4, -1, 2, 3)
        self.assertEqual(str(s), "Sphere(radius=4, pos=(-1, 2, 3))")

    def test_repr(self):
        s = Sphere(4, -1, 2, 3)
        self.assertEqual(repr(s), "Sphere(radius=4, x=-1, y=2, z=3)")

if __name__ == '__main__':
    unittest.main()