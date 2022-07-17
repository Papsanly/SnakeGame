from dataclasses import dataclass
from pygame import Vector2


@dataclass
class Settings:

    tiles_count = Vector2(11, 11)
    tile_size = 70
    snake_speed = 2
    fps = 60

    @classmethod
    def get_resolution(cls):
        return cls.tiles_count * cls.tile_size

    @classmethod
    def get_tile_vec(cls):
        return cls.tile_size, cls.tile_size
