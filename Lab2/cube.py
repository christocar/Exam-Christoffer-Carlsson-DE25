from numbers import Number
from math import pi
from shape3d import Shape3D
from utils import Utils

class Cube(Shape3D):
    """
    Cube shape class inheriting from Shape3D.

    This class represents a cube defined by its side length and bottom-left-front corner coordinates (x, y, z).
    It provides methods to calculate the surface area and volume of the cube.
    """

    def __init__(self, side_length: Number, x: Number = 0, y: Number = 0, z: Number = 0):
        """
        Initialize a Cube with a given side length and bottom-left-front corner coordinates.

        Args:
            side_length (float | int): The length of each side of the cube.
            x (float | int, optional): The x-coordinate of the cube's bottom-left-front corner. Defaults to 0.
            y (float | int, optional): The y-coordinate of the cube's bottom-left-front corner. Defaults to 0.
            z (float | int, optional): The z-coordinate of the cube's bottom-left-front corner. Defaults to 0.
        """
        Utils().validate_positive(side_length)
        super().__init__(x, y, z)
        self._side_length = side_length

    @property
    def side_length(self) -> Number:
        """Return the side length of the cube."""
        return self._side_length

    @property
    def surface_area(self) -> Number:
        """Return the surface area of the cube."""
        return 6 * self._side_length ** 2

    @property
    def volume(self) -> Number:
        """Return the volume of the cube."""
        return self._side_length ** 3
    
    def translate(self, dx: Number, dy: Number, dz: Number) -> None:
        """
        Translate the cube by given offsets.

        Args:
            dx (float | int): The offset in the x-direction.
            dy (float | int): The offset in the y-direction.
            dz (float | int): The offset in the z-direction.
        """
        super().translate(dx, dy, dz)

    def __eq__(self, other: object) -> bool:
        """
        Check equality between two cubes based on surface area and volume.

        Args:
            other (object): The other cube to compare with.
        """
        if not isinstance(other, Cube):
            return NotImplemented
        return (self.surface_area == other.surface_area and
                self.volume == other.volume)
    
    def __lt__(self, other: object) -> bool:
        """
        Check if this cube is less than another cube based on volume.

        Args:
            other (object): The other cube to compare with.
        """
        if not isinstance(other, Cube):
            return NotImplemented
        return self.volume < other.volume
    
    def __gt__(self, other: object) -> bool:
        """
        Check if this cube is greater than another cube based on volume.

        Args:
            other (object): The other cube to compare with.
        """
        if not isinstance(other, Cube):
            return NotImplemented
        return self.volume > other.volume
    
    def __le__(self, other: object) -> bool:
        """
        Check if this cube is less than or equal to another cube based on volume.

        Args:
            other (object): The other cube to compare with.
        """
        if not isinstance(other, Cube):
            return NotImplemented
        return self.volume <= other.volume

    def __ge__(self, other: object) -> bool:
        """
        Check if this cube is greater than or equal to another cube based on volume.

        Args:
            other (object): The other cube to compare with.
        """
        if not isinstance(other, Cube):
            return NotImplemented
        return self.volume >= other.volume

    def __str__(self) -> str:
        """Return a string representation of the cube."""
        return (f"Cube(side_length={self._side_length}, "
                f"corner=({self._x}, {self._y}, {self._z}))")
    
    def __repr__(self) -> str:
        """Return an official string representation of the cube."""
        return (f"Cube(side_length={self._side_length}, "
                f"x={self._x}, y={self._y}, z={self._z})")