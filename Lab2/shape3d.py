from abc import ABC, abstractmethod
from numbers import Number

class Shape3D(ABC):
    """
    Abstract base class for 3D shapes.

    This class defines the interface for 3D shapes, requiring subclasses to implement
    methods for calculating volume and surface area. Translation method is also provided.
    """

    def __init__(self, x: Number, y: Number, z: Number):
        """
        Initialize a 3D shape with x, y, and z coordinates.

        Args:
            x (float): The x-coordinate of the shape.
            y (float): The y-coordinate of the shape.
            z (float): The z-coordinate of the shape.
        """
        self._x = x
        self._y = y
        self._z = z

    @property
    @abstractmethod
    def volume(self) -> Number:
        """Return the volume of the shape (must be implemented by subclass)."""
        pass

    @property
    @abstractmethod
    def surface_area(self) -> Number:
        """Return the surface area of the shape (must be implemented by subclass)."""
        pass

    def translate(self, dx: Number, dy: Number, dz: Number) -> None:
        """Translate the shape by given offsets."""
        self._x += dx
        self._y += dy
        self._z += dz

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shape3D):
            return NotImplemented
        return self.volume == other.volume and self.surface_area == other.surface_area
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Shape3D):
            return NotImplemented
        return self.volume < other.volume
    
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Shape3D):
            return NotImplemented
        return self.volume > other.volume
    
    def __le__(self, other: object) -> bool:
        if not isinstance(other, Shape3D):
            return NotImplemented
        return self.volume <= other.volume

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Shape3D):
            return NotImplemented
        return self.volume >= other.volume

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(volume={self.volume}, surface_area={self.surface_area})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x}, y={self._y}, z={self._z})"
