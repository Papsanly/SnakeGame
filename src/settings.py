from dataclasses import dataclass
from pygame.math import Vector2


@dataclass
class Settings:
    """
    Data class for game settings
    1 unit = 1 grid square
    """
    # changeable settings by the player
    grid_count: Vector2 = Vector2(21, 21)  # units
    grid_size: int = 40  # pixels / unit
    food_radius: float = 0.5  # percentage of unit
    speed: float = 4  # unit / second
    fps: int = 30

    @classmethod
    def get_resolution(cls) -> Vector2:
        """Get pixel resolution tuple"""
        return cls.grid_count * cls.grid_size

    @classmethod
    def get_speed(cls):
        return cls.grid_size * cls.speed / cls.fps
