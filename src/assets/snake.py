from typing import Sequence

from pygame.sprite import Sprite, Group

from src.assets.asset import AssetGroup


class Snake(AssetGroup):

    def __init__(self, *sprites: Sprite | Sequence[Sprite] | Group):
        super().__init__(*sprites)

        self.length = 1
