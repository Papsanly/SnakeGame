from typing import Literal

from pygame.sprite import Sprite, Group

from src.assets.asset import AssetGroup
from src.orientation import Orientation, DirectionStr, DirectionAngle
from src.tile_position import TilePosition, PositionStr
from src.utils import Utils

BodyType = Literal['end', 'turn', 'straight']


class Snake(AssetGroup):

    def __init__(self, *sprites: Group):
        super().__init__(*sprites)

        self.length = 1

        self.add(
            SnakeBody('center', 'U', 'end', *sprites),
            SnakeBody('center', 'D', 'end', *sprites, shift=(0, 1)),
        )


class SnakeBody(Sprite):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle,
                 body_type: BodyType, *groups: Group, shift=(0, 0)):
        super().__init__(*groups)

        self.position = TilePosition(position) + shift
        self.direction = Orientation(direction)
        self.body_type = body_type

        self.image = Utils.load_tile_image(f'../assets/snake_body/{body_type}_{self.direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)
