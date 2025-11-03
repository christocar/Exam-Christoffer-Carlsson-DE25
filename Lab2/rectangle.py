from numbers import Number
from shape2d import Shape2D
from utils import Utils

class Rectangle(Shape2D):
    """
    Rectangle shape class inheriting from Shape2D.

    Represents a rectangle defined by width, height and a position (x, y).
    Provides calculation of area and perimeter and a method to check if it is a square.
    """

    def __init__(self, width: Number, height: Number, x: Number = 0, y: Number = 0):
        """
        Initialize a Rectangle with given width, height and coordinates.

        Args:
            width (float | int): The width of the rectangle.
            height (float | int): The height of the rectangle.
            x (float | int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (float | int, optional): The y-coordinate of the rectangle. Defaults to 0.
        """
        Utils.validate_positive(width)
        Utils.validate_positive(height)
        super().__init__(x, y)
        self._width = width
        self._height = height

    @property
    def width(self) -> Number:
        """Return the width of the rectangle."""
        return self._width

    @property
    def height(self) -> Number:
        """Return the height of the rectangle."""
        return self._height

    @property
    def area(self) -> Number:
        """Return the area of the rectangle."""
        return self._width * self._height

    @property
    def perimeter(self) -> Number:
        """Return the perimeter of the rectangle."""
        return 2 * (self._width + self._height)

    def is_square(self) -> bool:
        """Return True if the rectangle is a square."""
        return self._width == self._height

    def translate(self, dx: Number, dy: Number) -> None:
        """Translate the rectangle by given offsets."""
        super().translate(dx, dy)

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height}, pos=({self._x}, {self._y}))"

    def __repr__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height}, x={self._x}, y={self._y})"
