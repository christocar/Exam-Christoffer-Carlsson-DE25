from numbers import Number
from math import pi
from shape2d import Shape2D
from utils import Utils

class Rectangle(Shape2D):
    """
    Rectangle shape class inheriting from Shape2D.

    This class represents a rectangle defined by its width, height, and bottom-left corner coordinates (x, y).
    It provides methods to calculate the area and perimeter of the rectangle.
    """

    def __init__(self, width: Number, height: Number, x: Number = 0, y: Number = 0):
        """
        Initialize a Rectangle with a given width, height, and bottom-left corner coordinates.

        Args:
            width (float | int): The width of the rectangle.
            height (float | int): The height of the rectangle.
            x (float | int, optional): The x-coordinate of the rectangle's bottom-left corner. Defaults to 0.
            y (float | int, optional): The y-coordinate of the rectangle's bottom-left corner. Defaults to 0.
        """
        Utils().validate_positive(width)
        Utils().validate_positive(height)
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
        """Check if the rectangle is a square (width == height)."""
        return self._width == self._height
    
    def translate(self, dx: Number, dy: Number) -> None:
        """
        Translate the rectangle by given offsets.

        Args:
            dx (float | int): The offset in the x-direction.
            dy (float | int): The offset in the y-direction.
        """
        super().translate(dx, dy)

    def __eq__(self, other: object) -> bool:
        """
        Check equality between two rectangles based on area and perimeter.

        Args:
            other (object): The other rectangle to compare with.
        """
        return super().__eq__(other)
    
    def __lt__(self, other: object) -> bool:
        """
        Check if this rectangle is less than another rectangle based on area.

        Args:
            other (object): The other rectangle to compare with.
        """
        return super().__lt__(other)
    
    def __gt__(self, other: object) -> bool:
        """
        Check if this rectangle is greater than another rectangle based on area.

        Args:
            other (object): The other rectangle to compare with.
        """
        return super().__gt__(other)
    
    def __le__(self, other: object) -> bool:
        """
        Check if this rectangle is less than or equal to another rectangle based on area.

        Args:
            other (object): The other rectangle to compare with.
        """
        return super().__le__(other)

    def __ge__(self, other: object) -> bool:
        """
        Check if this rectangle is greater than or equal to another rectangle based on area.

        Args:
            other (object): The other rectangle to compare with.
        """
        return super().__ge__(other)

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return (f"Rectangle(width={self._width}, height={self._height}, "
                f"x={self._x}, y={self._y})")

    def __repr__(self) -> str:
        """Return an official string representation of the rectangle."""
        return (f"Rectangle(width={self._width}, height={self._height}, "
                f"x={self._x}, y={self._y})")
