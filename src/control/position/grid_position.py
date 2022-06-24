from src.control.settings import Settings
from pygame.math import Vector2


class GridPosition:
    """Class to manage coordinates of game objects on grid"""

    def __init__(self, grid_square: Vector2 | tuple, offset: Vector2 | tuple = Vector2(0, 0)):
        self.xy = Vector2(grid_square)
        self.x = self.xy.x
        self.y = self.xy.y
        self.offset = Vector2(offset)

    def get_coords(self) -> Vector2:
        """Get exact pixel position on upper right corner of the object"""
        return (self.xy + self.offset) * Settings.grid_size

    def tuple(self) -> tuple:
        return int(self.x), int(self.y)

    def get_coords_center(self) -> Vector2:
        """Get center of specified grid square in pixels"""
        return self.get_coords() + Vector2(Settings.grid_size, Settings.grid_size) / 2

    def set_xy(self, value: Vector2) -> None:
        self.xy = value
        self.x = value.x
        self.y = value.y

    def set_x(self, value):
        self.x = value
        self.xy.x = self.x

    def set_y(self, value):
        self.y = value
        self.xy.y = self.y

    def move(self, move_vec: Vector2) -> None:
        """Move along Vector2"""
        if move_vec.length() != 0:
            move_vec /= Settings.grid_size
            if (self.offset + move_vec).length() < 1:
                self.offset += move_vec
            else:
                self.set_xy(self.xy + move_vec.normalize())
                self.offset += move_vec - move_vec.normalize()
