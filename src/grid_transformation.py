from settings import Settings
from pygame.math import Vector2


class GridTransformation:
    """Class to manage coordinates and rotation of game objects on grid"""

    def __init__(self, grid_square: Vector2, offset=Vector2(0, 0)):
        self.xy = grid_square
        self.x = grid_square.x
        self.y = grid_square.y
        self.offset = offset

    def get_coords(self) -> Vector2:
        """Get exact pixel position on upper right corner of the object"""
        return (self.xy + self.offset) * Settings.grid_size

    def tuple(self) -> tuple:
        return int(self.x), int(self.y)

    def get_coords_center(self) -> Vector2:
        """Get center of specified grid square in pixels"""
        return self.get_coords() + Vector2(Settings.grid_size, Settings.grid_size) / 2

    def move(self, move_vec: Vector2) -> None:
        """Move along Vector2"""
        self.xy += move_vec
