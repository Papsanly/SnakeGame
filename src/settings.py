from dataclasses import dataclass
from pygame.math import Vector2


@dataclass(frozen=True)
class Settings:
    """
    Data class for game settings
    1 unit = 1 grid square
    """
    grid_count = Vector2(15, 15)  # units
    grid_size = 75  # pixels / unit
    food_radius = 0.5  # amount of grid square coverage
    speed = 1  # unit / second

    @classmethod
    def get_resolution(cls) -> Vector2:
        """Get pixel resolution tuple"""
        return cls.grid_count * cls.grid_size

    @classmethod
    def get_snake_rect_offset(cls) -> int:
        """Get offset for SnakeBodyStraight rect position"""
        return int(cls.grid_size * 0.1875)

    @classmethod
    def get_snake_width(cls) -> int:
        """get snake width in pixels"""
        return cls.grid_size - 2 * cls.get_snake_rect_offset()