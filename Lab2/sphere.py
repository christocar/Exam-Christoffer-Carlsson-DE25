from numbers import Number
from math import pi
from shape2d import Shape2D
from utils import Utils

class Sphere(Shape3D):
    """
    Sphere shape class inheriting from Shape3D.

    This class represents a sphere defined by its radius and center coordinates (x, y, z).
    It provides methods to calculate the surface area and volume of the sphere.
    """

    def __init__(self, radius: Number, x: Number = 0, y: Number = 0, z: Number = 0):
        """
        Initialize a Sphere with a given radius and center coordinates.

        Args:
            radius (float | int): The radius of the sphere.
            x (float | int, optional): The x-coordinate of the sphere's center. Defaults to 0.
            y (float | int, optional): The y-coordinate of the sphere's center. Defaults to 0.
            z (float | int, optional): The z-coordinate of the sphere's center. Defaults to 0.
        """
        Utils().validate_positive(radius)
        super().__init__(x, y, z)
        self._radius = radius

    @property
    def radius(self) -> Number:
        """Return the radius of the sphere."""
        return self._radius

    @property
    def surface_area(self) -> Number:
        """Return the surface area of the sphere."""
        return 4 * pi * self._radius ** 2

    @property
    def volume(self) -> Number:
        """Return the volume of the sphere."""
        return (4/3) * pi * self._radius ** 3
    
    def translate(self, dx: Number, dy: Number, dz: Number) -> None:
        """
        Translate the sphere by given offsets.

        Args:
            dx (float | int): The offset in the x-direction.
            dy (float | int): The offset in the y-direction.
            dz (float | int): The offset in the z-direction.
        """
        super().translate(dx, dy, dz)

    def __eq__(self, other: object) -> bool:
        """
        Check equality between two spheres based on surface area and volume.

        Args:
            other (object): The other sphere to compare with.
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        return self.surface_area == other.surface_area and self.volume == other.volume
    
    def __lt__(self, other: object) -> bool:
        """
        Check if this sphere is less than another sphere based on volume.

        Args:
            other (object): The other sphere to compare with.
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        return self.volume < other.volume
    
    def __gt__(self, other: object) -> bool:
        """
        Check if this sphere is greater than another sphere based on volume.

        Args:
            other (object): The other sphere to compare with.
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        return self.volume > other.volume
    
    def __le__(self, other: object) -> bool:
        """
        Check if this sphere is less than or equal to another sphere based on volume.

        Args:
            other (object): The other sphere to compare with.
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        return self.volume <= other.volume
    
    def __ge__(self, other: object) -> bool:
        """
        Check if this sphere is greater than or equal to another sphere based on volume.

        Args:
            other (object): The other sphere to compare with.
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        return self.volume >= other.volume

    def __str__(self) -> str:
        """Return a string representation of the sphere."""
        return (f"Sphere(radius={self._radius}, x={self._x}, y={self._y}, z={self._z})")

    def __repr__(self) -> str:
        """Return an official string representation of the sphere."""
        return (f"Sphere(radius={self._radius}, x={self._x}, y={self._y}, z={self._z})")
