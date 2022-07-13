from dataclasses import dataclass
from pygame.math import Vector2


@dataclass
class Settings:
    """
    Data class for game settings
    1 unit = 1 grid square
    """
    # changeable settings by the player
    grid_count = Vector2(13, 13)  # units
    grid_size = 58  # pixels / unit
    snake_speed = 1.0  # unit / second
    fps = 60  # frames per second

    @classmethod
    def get_grid_square(cls) -> tuple[int, int]:
        """Returns tuple with values of grid size"""
        return Settings.grid_size, Settings.grid_size

    @classmethod
    def get_resolution(cls) -> Vector2:
        """Get pixel resolution tuple"""
        return cls.grid_count * cls.grid_size

    @classmethod
    def get_snake_speed(cls) -> float:
        """Get amount of pixels that snake moves per frame"""
        return cls.grid_size * cls.snake_speed / cls.fps

    @classmethod
    def get_snake_width(cls) -> int:
        """Returns width of snake in pixels"""
        return cls.grid_size - 2 * cls.get_snake_width_offset()

    @classmethod
    def get_snake_width_offset(cls) -> int:
        """
        Returns pixel offset from the topleft of a square
        to the topleft of snake straight body part
        """
        return round(cls.grid_size * 3 / 16)
