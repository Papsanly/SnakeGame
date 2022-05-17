from dataclasses import dataclass
from collections import namedtuple

vec2 = namedtuple('vec2', 'x y')


@dataclass(frozen=True)
class Settings:
    """
    Data class for game settings
    1 unit = 1 grid square
    """
    grid_count = vec2(15, 15)  # units
    grid_size = 75  # pixels / unit
    food_radius = 0.5  # amount of grid square coverage
    speed = 1  # unit / second

    @classmethod
    def get_resolution(cls):
        """Get pixel resolution tuple"""
        return vec2(cls.grid_size * cls.grid_count.x, cls.grid_size * cls.grid_count.y)

    @classmethod
    def get_snake_rect_offset(cls):
        """Get offset for SnakeBodyStraight rect position"""
        return int(cls.grid_size * 0.1875)
