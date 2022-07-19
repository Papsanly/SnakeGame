from typing import Literal

from pygame.sprite import Sprite, Group

from src.assets.asset import AssetGroup
from src.orientation import Orientation, DirectionStr, DirectionAngle
from src.tile_position import TilePosition, PositionStr
from src.utils import Utils

BodyType = Literal['end', 'turn', 'straight']


class Snake(AssetGroup):

    def __init__(self, *groups: Group):
        super().__init__(*groups)

        self.length = 1

        self.add(
            SnakeBodyTurn('center', 'U', 'L', 'end', *groups),
            SnakeBodyEnd('center', 'D', 'end', *groups, shift=(0, 1)),
        )


class SnakeBody(Sprite):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle,
                 body_type: BodyType, *groups: Group, shift=(0, 0)):
        super().__init__(*groups)

        self.position = TilePosition(position) + shift
        self.direction = Orientation(direction)
        self.body_type = body_type


class SnakeBodyEnd(SnakeBody):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle,
                 *groups: Group, shift=(0, 0)):
        super().__init__(position, direction, 'end', *groups, shift=shift)

        self.image = Utils.load_tile_image(f'../assets/snake_body/end_{self.direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)


class SnakeBodyStraight(SnakeBody):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle,
                 *groups: Group, shift=(0, 0)):
        super().__init__(position, direction, 'straight', *groups, shift=shift)

        if direction in ('U', 'D', 90, 270):
            direction = 'V'
        elif direction in ('R', 'L', 0, 180):
            direction = 'H'

        self.image = Utils.load_tile_image(f'../assets/snake_body/straight_{direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)


class SnakeBodyTurn(SnakeBody):

    def __init__(self, position: PositionStr, start_direction: DirectionStr | DirectionAngle,
                 end_direction: DirectionStr | DirectionAngle,
                 *groups: Group, shift=(0, 0)):
        super().__init__(position, end_direction, 'turn', *groups, shift=shift)

        self.image = Utils.load_tile_image(f'../assets/snake_body/turn_{start_direction}{end_direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)
