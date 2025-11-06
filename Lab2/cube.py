from numbers import Number
from shape3d import Shape3D
from utils import Utils

class Cube(Shape3D):
    """
    Cube shape class inheriting from Shape3D.

    Represents a cube defined by its side length and position (x, y, z).
    Provides calculation of surface area and volume.
    """

    def __init__(self, side: Number, x: Number = 0, y: Number = 0, z: Number = 0):
        Utils.validate_positive(side)
        super().__init__(x, y, z)
        self._side = side

    @property
    def side(self) -> Number:
        return self._side

    @property
    def surface_area(self) -> Number:
        """Return the total surface area of the cube."""
        return 6 * (self._side ** 2)

    @property
    def volume(self) -> Number:
        """Return the volume of the cube."""
        return self._side ** 3

    def translate(self, dx: Number, dy: Number, dz: Number) -> None:
        super().translate(dx, dy, dz)

    def __str__(self) -> str:
        return f"Cube(side={self._side}, pos=({self._x}, {self._y}, {self._z}))"

    def __repr__(self) -> str:
        return f"Cube(side={self._side}, x={self._x}, y={self._y}, z={self._z})"
