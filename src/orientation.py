from pygame.math import Vector2


class Orienatation:
    """Class to manage object orienation in a grid"""

    def __init__(self, direction: str | Vector2 | int | float):
        # set initial direction attribute
        self.direction = direction

        # check if valid for all types of direction
        self.get_name()

    def get_name(self) -> str:
        """Convert direction to name: 'U', 'R", 'L' or 'D'"""
        if isinstance(self.direction, str):
            if self.direction in ['U', 'D', 'L', 'R']:
                return self.direction
            else:
                raise ValueError('Invalid direction')
        elif isinstance(self.direction, Vector2):
            direction = tuple(self.direction)
            if direction == (1, 0):
                return 'R'
            elif direction == (-1, 0):
                return 'L'
            elif direction == (0, 1):
                return 'D'
            elif direction == (0, -1):
                return 'U'
            else:
                raise ValueError('Invalid direction')
        elif isinstance(self.direction, (int, float)):
            direction = int(self.direction) % 360
            if direction == 0:
                return 'U'
            elif direction == 90:
                return 'R'
            elif direction == 180:
                return 'D'
            elif direction == 270:
                return 'L'
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
            return 90
        elif self.direction == 'L':
            return 270
