from abc import ABC, abstractmethod
from numbers import Number

class Shape2D(ABC):
    """
    Abstract base class for 2D shapes.

    This class defines the interface for 2D shapes, requiring subclasses to implement
    methods for calculating area and perimeter. Translation method is also provided.
    """

    def __init__(self, x: float, y: float):
        """
        Initialize a 2D shape with x and y coordinates.

        Args:
            x (float): The x-coordinate of the shape.
            y (float): The y-coordinate of the shape.
        """
        self._x = x
        self._y = y

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

    def translate(self, dx: float, dy: float) -> None:
        """
        Translate the shape by given offsets.

        Args:
            dx (float | int): The offset in the x-direction.
            dy (float | int): The offset in the y-direction.
        """
        self._x += dx
        self._y += dy

    def __eq__(self, other: object) -> bool:
        """
        Check equality between two shapes based on area and perimeter.

        Args:
            other (object): The other shape to compare with.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area == other.area and self.perimeter == other.perimeter
    
    def __lt__(self, other: object) -> bool:
        """
        Check if this shape is less than another shape based on area.

        Args:
            other (object): The other shape to compare with.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area < other.area
    
    def __gt__(self, other: object) -> bool:
        """
        Check if this shape is greater than another shape based on area.

        Args:
            other (object): The other shape to compare with.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area > other.area

    def __le__(self, other: object) -> bool:
        """
        Check if this shape is less than or equal to another shape based on area.

        Args:
            other (object): The other shape to compare with.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area <= other.area
    
    def __ge__(self, other: object) -> bool:
        """
        Check if this shape is greater than or equal to another shape based on area.

        Args:
            other (object): The other shape to compare with.
        """
        if not isinstance(other, Shape2D):
            return NotImplemented
        return self.area >= other.area
    
    def __str__(self) -> str:
        """
        Return a string representation of the shape.

        Returns:
            str: A string describing the shape's type, area, and perimeter.
        """
        return f"{self.__class__.__name__}(area={self.area}, perimeter={self.perimeter})"
    
    def __repr__(self) -> str:
        """
        Return a detailed string representation of the shape.

        Returns:
            str: A string with the class name and its attributes.
        """
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"