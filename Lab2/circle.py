from numbers import Number
from math import pi
from shape2d import Shape2D
from utils import Utils

class Circle(Shape2D):
    """
    Circle shape class inheriting from Shape2D.

    Represents a circle defined by its radius and center (x, y).
    Provides calculation of area and perimeter and a method to check if it is a unit circle.
    """

    def __init__(self, radius: Number, x: Number = 0, y: Number = 0):
        """
        Initialize a Circle with given radius and coordinates.

        Args:
            radius (Number): The radius of the circle.
            x (Number, optional): The x-position of the circle. Defaults to 0.
            y (Number, optional): The y-position of the circle. Defaults to 0.
        """
        Utils.validate_positive(radius)
        super().__init__(x, y)
        self._radius = radius

    @property
    def radius(self) -> Number:
        """Return the radius of the circle."""
        return self._radius

    @property
    def area(self) -> Number:
        """Return the area of the circle."""
        return pi * (self._radius ** 2)

    @property
    def perimeter(self) -> Number:
        """Return the circumference (perimeter) of the circle."""
        return 2 * pi * self._radius

    def is_unit_circle(self) -> bool:
        """Return True if the circle is a unit circle (radius == 1)."""
        return self._radius == 1

    def translate(self, dx: Number, dy: Number) -> None:
        """
        Translate the circle by given numeric offsets.

        Args:
            dx (Number): Offset in the x-direction.
            dy (Number): Offset in the y-direction.
        """
        super().translate(dx, dy)

    def __str__(self) -> str:
        return f"Circle(radius={self._radius}, center=({self._x}, {self._y}))"

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius}, x={self._x}, y={self._y})"
