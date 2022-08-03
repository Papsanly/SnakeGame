from dataclasses import dataclass
from pygame import Vector2


@dataclass
class Settings:
    """
    Dataclass that stores all game constants
    """

    tiles_count = Vector2(51, 31)  # amount of tiles on x and y-axis
    tile_size = 25  # pixel size of one tile
    snake_speed = 9.0  # amount of tiles snake goes through per second
    fps = 30  # main loop iterations per second
    food_colors = [
        (209, 42, 72),
        (114, 237, 169),
        (227, 187, 30),
        (196, 117, 235),
        (250, 164, 72)
    ]  # variations of food colors
    food_count = 5  # maximum amount of food at any time

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
