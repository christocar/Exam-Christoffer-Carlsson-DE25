import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(4, 6, 2, -3)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, -3)

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area, 15)

    def test_perimeter(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.perimeter, 16)

    def test_translate(self):
        r = Rectangle(2, 3, 0, 0)
        r.translate(10, -5)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, -5)

    def test_is_square_true(self):
        r = Rectangle(5, 5)
        self.assertTrue(r.is_square())

    def test_is_square_false(self):
        r = Rectangle(5, 6)
        self.assertFalse(r.is_square())

    def test_equality(self):
        r1 = Rectangle(4, 5)
        r2 = Rectangle(4, 5, 100, 100)
        r3 = Rectangle(5, 5)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_less_than(self):
        r_small = Rectangle(2, 2)
        r_big = Rectangle(10, 10)
        self.assertTrue(r_small < r_big)
        self.assertFalse(r_big < r_small)

    def test_greater_than(self):
        r_small = Rectangle(2, 2)
        r_big = Rectangle(10, 10)
        self.assertTrue(r_big > r_small)
        self.assertFalse(r_small > r_big)

    def test_less_or_equal(self):
        r1 = Rectangle(4, 4)
        r2 = Rectangle(4, 4)
        r3 = Rectangle(5, 5)
        self.assertTrue(r1 <= r2)
        self.assertTrue(r1 <= r3)
        self.assertFalse(r3 <= r1)

    def test_greater_or_equal(self):
        r1 = Rectangle(4, 4)
        r2 = Rectangle(4, 4)
        r3 = Rectangle(2, 2)
        self.assertTrue(r1 >= r2)
        self.assertTrue(r1 >= r3)
        self.assertFalse(r3 >= r1)

    def test_str(self):
        r = Rectangle(4, 5, -1, 2)
        s = str(r)
        self.assertIn("Rectangle", s)
        self.assertIn("width=4", s)
        self.assertIn("height=5", s)

    def test_repr(self):
        r = Rectangle(4, 5, -1, 2)
        rep = repr(r)
        self.assertIn("Rectangle", rep)
        self.assertIn("width=4", rep)
        self.assertIn("height=5", rep)
        self.assertIn("x=-1", rep)
        self.assertIn("y=2", rep)


if __name__ == "__main__":
    unittest.main()