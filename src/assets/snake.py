from typing import Sequence

from pygame.sprite import Sprite, Group

from src.assets.asset import AssetGroup
from src.tile_position import TilePosition


class Snake(AssetGroup):

    def __init__(self, *sprites: Sprite | Sequence[Sprite] | Group):
        super().__init__(*sprites)

        self.length = 1

        self.add(
            SnakeBody(position='center', direction='U', body_type='end'),
            SnakeBody(position=TilePosition('center') + (0, 1), direction='D', body_type='end'),
        )


class SnakeBody(Sprite):
    pass