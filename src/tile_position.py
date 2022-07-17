from pygame import Vector2

from src.settings import Settings


class TilePosition:

    def __init__(self, tile):
        if isinstance(tile, str):
            if tile == 'center':
                self.tile = Settings.tiles_count // 2
        else:
            self.tile = Vector2(tile)

    def __eq__(self, other):
        return self.topleft == other.topleft

    def __hash__(self):
        return hash(tuple(self.topleft))

    @property
    def left(self):
        return round(self.tile.x * Settings.tile_size)

    @property
    def right(self):
        return round((self.tile.x + 1) * Settings.tile_size)

    @property
    def top(self):
        return round(self.tile.y * Settings.tile_size)

    @property
    def bottom(self):
        return round((self.tile.y + 1) * Settings.tile_size)

    @property
    def topleft(self):
        return Vector2(self.left, self.top)

    @property
    def center(self):
        return self.topleft + Settings.get_tile_vec() // 2

    def __add__(self, other):
        return TilePosition(self.tile + other)
