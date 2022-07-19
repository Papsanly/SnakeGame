from typing import Literal

import pygame.event
from pygame.sprite import Sprite

from src.assets.asset import AssetGroup
from src.orientation import Orientation, DirectionStr, DirectionAngle
from src.settings import Settings
from src.tile_position import TilePosition, PositionStr
from src.utils import Utils

BodyType = Literal['end', 'turn', 'straight']


class Snake(AssetGroup):

    def __init__(self):
        super().__init__()

        self.length = 1
        self.direction_map: dict[TilePosition, Orientation] = {}

        self.add(
            SnakeBodyEnd('center', 'U'),
            SnakeBodyEnd('center', 'U', shift=(0, 1), tail=True),
        )

        self.move_event = pygame.event.custom_type()
        pygame.time.set_timer(self.move_event, int(1000 / Settings.snake_speed))

    def update(self) -> None:
        for sprite in self.sprites():
            if hasattr(sprite, 'position'):
                new_direction = self.direction_map.get(sprite.position)
                sprite.update(new_direction)


class SnakeBody(Sprite):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle,
                 body_type: BodyType, shift=(0, 0)):
        super().__init__()

        self.position = TilePosition(position) + shift
        self.direction = Orientation(direction)
        self.body_type = body_type

    def update(self, direction) -> None:
        if direction is not None:
            self.direction = direction
        self.position += self.direction.vector
        self.rect.center = self.position.center


class SnakeBodyEnd(SnakeBody):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle,
                 shift=(0, 0), tail=False):
        super().__init__(position, direction, 'end', shift=shift)

        image_direction = -self.direction if tail else self.direction
        self.image = Utils.load_tile_image(f'../assets/snake_body/end_{image_direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)


class SnakeBodyStraight(SnakeBody):

    def __init__(self, position: PositionStr, direction: DirectionStr | DirectionAngle, shift=(0, 0)):
        super().__init__(position, direction, 'straight', shift=shift)

        if direction in ('U', 'D', 90, 270):
            direction = 'V'
        else:
            direction = 'H'

        self.image = Utils.load_tile_image(f'../assets/snake_body/straight_{direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)


class SnakeBodyTurn(SnakeBody):

    def __init__(self, position: PositionStr, start_direction: DirectionStr | DirectionAngle,
                 end_direction: DirectionStr | DirectionAngle, shift=(0, 0)):
        super().__init__(position, end_direction, 'turn', shift=shift)

        self.image = Utils.load_tile_image(f'../assets/snake_body/turn_{start_direction}{end_direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)
