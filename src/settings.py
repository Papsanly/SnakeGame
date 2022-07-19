from dataclasses import dataclass
from pygame import Vector2


@dataclass
class Settings:
    """
    Dataclass that stores all game constants
    """

    tiles_count = Vector2(11, 11)  # amount of tiles on x and y-axis
    tile_size = 70  # pixel size of one tile
    snake_speed = 4.0  # amount of tiles snake goes through per second
    fps = 60

    @classmethod
    def get_resolution(cls) -> Vector2:
        """
        Returns pixel resolution tuple of entire game window
        """
        return cls.tiles_count * cls.tile_size

    @classmethod
    def get_tile_vec(cls) -> Vector2:
        """
        Returns vector representing 1 tile
        """
        return Vector2(cls.tile_size, cls.tile_size)
