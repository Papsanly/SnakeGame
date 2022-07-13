from __future__ import annotations
from pygame import Vector2

from src.settings import Settings


class GridPosition:
    """Class to manage positioning of objects on grid"""

    def __init__(self, grid_square: Vector2 | tuple | str,
                 offset: Vector2 | tuple = (0, 0)):

        int_offset = Vector2(int(offset[0]), int(offset[1]))
        nonint_offset = offset - int_offset

        if isinstance(grid_square, str):
            if grid_square == 'center':
                self.grid_square = int_offset + Settings.grid_count // 2
        else:
            self.grid_square = Vector2(grid_square) + int_offset

        self.offset = Vector2(nonint_offset)

    def __add__(self, other: GridPosition) -> GridPosition:
        return GridPosition(self.grid_square + other.grid_square,
                            self.offset + other.offset)

    def __sub__(self, other: GridPosition) -> GridPosition:
        return GridPosition(self.grid_square - other.grid_square,
                            self.offset - other.offset)

    @property
    def left(self) -> int:
        return round((self.grid_square.x + self.offset.x) * Settings.grid_size)

    @property
    def right(self) -> int:
        return round((self.grid_square.x + 1 + self.offset.x) * Settings.grid_size)

    @property
    def top(self) -> int:
        return round((self.grid_square.y + self.offset.y) * Settings.grid_size)

    @property
    def bottom(self) -> int:
        return round((self.grid_square.y + 1 + self.offset.y) * Settings.grid_size)

    @property
    def topleft(self) -> Vector2:
        return Vector2(self.left, self.top)

    @property
    def center(self) -> Vector2:
        return self.topleft + Vector2(Settings.get_grid_square()) // 2

    def moved(self, move_vec: Vector2 | tuple) -> GridPosition:
        return self + GridPosition((0, 0), move_vec)
