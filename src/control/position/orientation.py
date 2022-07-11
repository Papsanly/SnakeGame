from __future__ import annotations
from pygame.math import Vector2


class Orientation:
    """Class to manage object orientation in a grid"""

    def __init__(self, direction: str | Vector2 | int | float):
        # set initial direction attribute
        self.direction = direction

        # check if valid for all types of direction
        self.get_name()

    def __eq__(self, other):
        return self.get_name() == other.get_name()

    def __neg__(self) -> Orientation:
        return Orientation(-self.get_vector())

    def __ne__(self, other):
        return self.get_name() != other.get_name()

    def get_name(self) -> str:
        """Convert direction to name: 'U', 'R", 'L' or 'D'"""
        if isinstance(self.direction, str):
            if self.direction in ['U', 'D', 'L', 'R']:
                return self.direction
        elif isinstance(self.direction, Vector2):
            direction = tuple(self.direction)
            match direction:
                case (1, 0): return 'R'
                case (-1, 0): return 'L'
                case (0, 1): return 'D'
                case (0, -1): return 'U'
        elif isinstance(self.direction, (int, float)):
            direction = int(self.direction) % 360
            match direction:
                case 0: return 'U'
                case 90: return 'R'
                case 180: return 'D'
                case 270: return 'L'
        else:
            raise ValueError('Invalid direction')

    def get_vector(self) -> Vector2:
        self.direction = self.get_name()
        if self.direction == 'U':
            return Vector2(0, -1)
        elif self.direction == 'D':
            return Vector2(0, 1)
        elif self.direction == 'R':
            return Vector2(1, 0)
        elif self.direction == 'L':
            return Vector2(-1, 0)

    def get_angle(self) -> int:
        self.direction = self.get_name()
        if self.direction == 'U':
            return 0
        elif self.direction == 'D':
            return 180
        elif self.direction == 'R':
            return 270
        elif self.direction == 'L':
            return 90
