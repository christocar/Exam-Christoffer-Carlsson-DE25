from abc import ABC, abstractmethod
from numbers import Number

class Shape2D(ABC):
    """
    Abstract base class for 2D shapes.

    This class defines the interface for 2D shapes, requiring subclasses to implement
    methods for calculating area and perimeter. Translation method is also provided.
    """

    def __init__(self, x: Number, y: Number):
        """
        Initialize a 2D shape with x and y coordinates.

        Args:
            x (Number): The x-coordinate of the shape.
            y (Number): The y-coordinate of the shape.
        """
        self._x = x
        self._y = y

    @property
    def x(self) -> Number:
        return self._x

    @property
    def y(self) -> Number:
        return self._y

    @property
    @abstractmethod
    def area(self) -> Number:
        """Return the area of the shape (must be implemented by subclass)."""
        pass

    @property
    @abstractmethod
    def perimeter(self) -> Number:
        """Return the perimeter of the shape (must be implemented by subclass)."""
        pass

    def translate(self, dx: Number, dy: Number) -> None:
        """
        Translate the shape by given numeric offsets.

        Args:
            dx (Number): Offset in the x-direction.
            dy (Number): Offset in the y-direction.
        """
        self._x += dx
        self._y += dy

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area == other.area and self.perimeter == other.perimeter
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area < other.area
    
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area > other.area

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area <= other.area
    
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area >= other.area
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(area={self.area}, perimeter={self.perimeter})"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"
