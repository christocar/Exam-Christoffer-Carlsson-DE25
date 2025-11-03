from numbers import Number
from math import pi
from shape2d import Shape2D
from utils import Utils

def Circle(Shape2D):
    """
    Circle shape class inheriting from Shape2D.

    This class represents a circle defined by its radius and center coordinates (x, y).
    It provides methods to calculate the area and perimeter of the circle.
    """

    def __init__(self, radius: Number, x: Number = 0, y: Number = 0):
        """
        Initialize a Circle with a given radius and center coordinates.

        Args:
            radius (float | int): The radius of the circle.
            x (float | int, optional): The x-coordinate of the circle's center. Defaults to 0.
            y (float | int, optional): The y-coordinate of the circle's center. Defaults to 0.
        """
        Utils().validate_positive(radius)
        super().__init__(x, y)
        self._radius = radius

    @property
    def radius(self) -> Number:
        """Return the radius of the circle."""
        return self._radius

    @property
    def area(self) -> Number:
        """Return the area of the circle."""
        return pi * self._radius ** 2

    @property
    def perimeter(self) -> Number:
        """Return the perimeter (circumference) of the circle."""
        return 2 * pi * self._radius
    
    def is_unit_circle(self) -> bool:
        """Check if the circle is a unit circle (radius == 1)."""
        return self._radius == 1
    
    def translate(self, dx: Number, dy: Number) -> None:
        """
        Translate the circle by given offsets.

        Args:
            dx (float | int): The offset in the x-direction.
            dy (float | int): The offset in the y-direction.
        """
        super().translate(dx, dy)

    def __eq__(self, other: object) -> bool:
        """
        Check equality between two circles based on area and perimeter.

        Args:
            other (object): The other circle to compare with.
        """
        return super().__eq__(other)
    
    def __lt__(self, other: object) -> bool:
        """
        Check if this circle is less than another circle based on area.

        Args:
            other (object): The other circle to compare with.
        """
        return super().__lt__(other)

    def __gt__(self, other: object) -> bool:
        """
        Check if this circle is greater than another circle based on area.

        Args:
            other (object): The other circle to compare with.
        """
        return super().__gt__(other)

    def __le__(self, other: object) -> bool:
        """
        Check if this circle is less than or equal to another circle based on area.

        Args:
            other (object): The other circle to compare with.
        """
        return super().__le__(other)

    def __ge__(self, other: object) -> bool:
        """
        Check if this circle is greater than or equal to another circle based on area.

        Args:
            other (object): The other circle to compare with.
        """
        return super().__ge__(other)
    
    def __str__(self) -> str:
        """
        Return a string representation of the circle.
        """
        return f"Circle(radius={self._radius}, center=({self._x}, {self._y}))"
    
    def __repr__(self) -> str:
        """
        Return an official string representation of the circle.
        """
        return f"Circle(radius={self._radius}, x={self._x}, y={self._y})"
