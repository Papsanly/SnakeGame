from dataclasses import dataclass
from pygame.math import Vector2
from time_control import clock


@dataclass
class Settings:
    """
    Data class for game settings
    1 unit = 1 grid square
    """
    # changeable settings by the player
    grid_count = Vector2(15, 15)  # units
    grid_size = 75  # pixels / unit
    food_radius = 0.5  # persentage of grid square size
    speed = 2  # unit / second

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

    @classmethod
    def set_fps(cls, fps):
        """Set current fps based on iteration time taken by main while loop"""
        cls.fps = fps

    @classmethod
    def get_speed(cls):
        fps = clock.get_fps()
        return cls.grid_size * cls.speed / fps
