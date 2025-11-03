from math import pi
from numbers import Number
from shape3d import Shape3D
from utils import Utils

class Sphere(Shape3D):
    """
    Sphere shape class inheriting from Shape3D.

    Represents a sphere defined by its radius and position (x, y, z).
    Provides calculation of surface area and volume.
    """

    def __init__(self, radius: Number, x: Number = 0, y: Number = 0, z: Number = 0):
        Utils.validate_positive(radius)
        super().__init__(x, y, z)
        self._radius = radius

    @property
    def radius(self) -> Number:
        """Return the radius of the sphere."""
        return self._radius

    @property
    def surface_area(self) -> Number:
        """Return the total surface area of the sphere."""
        return 4 * pi * (self._radius ** 2)

    @property
    def volume(self) -> Number:
        """Return the volume of the sphere."""
        return (4/3) * pi * (self._radius ** 3)

    def is_unit_sphere(self) -> bool:
        """Return True if the sphere is a unit sphere (radius == 1)."""
        return self._radius == 1

    def translate(self, dx: Number, dy: Number, dz: Number) -> None:
        """Translate the sphere by given offsets."""
        super().translate(dx, dy, dz)

    def __str__(self) -> str:
        return f"Sphere(radius={self._radius}, pos=({self._x}, {self._y}, {self._z}))"

    def __repr__(self) -> str:
        return f"Sphere(radius={self._radius}, x={self._x}, y={self._y}, z={self._z})"
