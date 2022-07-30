from __future__ import annotations
from typing import Literal
from pygame import Vector2
from src.settings import Settings

PositionStr = Literal['center', 'topleft', 'topright', 'bottomleft', 'bottomright']


class TilePosition:
    """
    Class to manage object positioning on grid
    """

    def __init__(self, tile: TilePosition | PositionStr | Vector2 | tuple) -> None:
        """
        :param tile: Vector or tuple representing tile position or string 'center'
        """
        if isinstance(tile, str):
            match tile:
                case 'center': self.tile = Settings.tiles_count // 2
                case 'topleft': self.tile = Vector2(0, 0)
                case 'topright': self.tile = Vector2(Settings.tiles_count.x, 0)
                case 'bottomleft': self.tile = Vector2(0, Settings.tiles_count.x)
                case 'bottomright': self.tile = Settings.tiles_count
        elif isinstance(tile, TilePosition):
            self.tile = tile.tile
        else:
            self.tile = Vector2(tile)

    def __repr__(self):
        return str(self.topleft)

    def __eq__(self, other: TilePosition) -> bool:
        """
        :param other: Another TilePosition object
        :return: True if tile attribute matches
        """
        return self.tile == other.tile

    def __hash__(self) -> hash:
        """
        :return: Hash value
        """
        return hash(tuple(self.topleft))

    @property
    def left(self) -> int:
        """
        :return: Pixel y-coordinate of the left side of the tile
        """
        return round(self.tile.x * Settings.tile_size)

    @property
    def right(self) -> int:
        """
        :return: Pixel y-coordinate of the right side of the tile
        """
        return round((self.tile.x + 1) * Settings.tile_size)

    @property
    def top(self) -> int:
        """
        :return: Pixel x-coordinate of the top side of the tile
        """
        return round(self.tile.y * Settings.tile_size)

    @property
    def bottom(self) -> int:
        """
        :return: Pixel x-coordinate of the bottom side of the tile
        """
        return round((self.tile.y + 1) * Settings.tile_size)

    @property
    def topleft(self) -> Vector2:
        """
        :return: Vector with pixel coords of the left and top side of the tile - Vector2(left, top)
        """
        return Vector2(self.left, self.top)

    @property
    def center(self) -> Vector2:
        """
        :return: Vector with pixel coords of the center of the tile - Vector2(centerx, centery)
        """
        return self.topleft + Settings.get_tile_vec() // 2

    def __mul__(self, other: int) -> TilePosition:
        """
        Multiply tile coordinates by number
        :param other: Integer to multiply by
        :return: Another tileimage object
        """
        return TilePosition(self.tile * other)

    def __add__(self, other: TilePosition | Vector2 | tuple) -> TilePosition:
        """
        Adds coresponding coordinates of tile attribute

        :param other: Vector or tuple with amount of tile coordinates to add
        :return: Another TilePosition object with new tile coords
        """
        if isinstance(other, TilePosition):
            return TilePosition(self.tile + other.tile)
        else:
            return TilePosition(self.tile + Vector2(other))

    def __sub__(self, other: TilePosition | Vector2 | tuple) -> TilePosition:
        """
        Subtracts coresponding coordinates of tile attribute

        :param other: Vector or tuple with amount of tile coordinates to subtract
        :return: Another TilePosition object
        """
        if isinstance(other, TilePosition):
            return TilePosition(self.tile - other.tile)
        else:
            return TilePosition(self.tile - Vector2(other))
