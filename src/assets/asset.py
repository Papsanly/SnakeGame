from typing import Sequence

from pygame.sprite import Sprite, Group


class AssetGroup(Group):
    """
    Baseclass, which is a pygame group, for any game asset
    """

    def __init__(self, *sprites: Sprite | Sequence[Sprite] | Group):
        super().__init__(*sprites)

