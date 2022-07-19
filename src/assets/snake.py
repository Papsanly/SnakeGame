from typing import Literal

import pygame.event
from pygame import Vector2
from pygame.sprite import Sprite

from src.assets.asset import AssetGroup
from src.orientation import Orientation, DirectionStr, DirectionAngle
from src.settings import Settings
from src.tile_position import TilePosition, PositionStr
from src.utils import Utils

BodyType = Literal['end', 'turn', 'straight']


class Snake(AssetGroup):
    """
    Snake object. Created at the center with length one
    """

    def __init__(self):
        super().__init__()

        self.length = 1
        self.direction_map: dict[TilePosition, Orientation] = {}

        self.head = SnakeBodyEnd('center', 'U')
        self.tail = SnakeBodyEnd('center', 'U', shift=(0, 1), tail=True)
        self.add(self.head, self.tail)

        self.move_event = pygame.event.custom_type()
        pygame.time.set_timer(self.move_event, int(1000 / Settings.snake_speed))

    def turn(self, direction: DirectionStr | DirectionAngle | Vector2) -> None:
        """
        Turn the snake in given direction
        :param direction: Direction to turn the snake to
        """
        self.direction_map[self.head.position] = Orientation(direction)
        self.add(SnakeBodyTurn(self.head.position, self.head.direction, direction))

    def update(self) -> None:
        """
        Move snake parts according to direction map
        """
        for sprite in self.sprites():
            if hasattr(sprite, 'position') and hasattr(sprite, 'direction') and hasattr(sprite, 'tail'):
                old_direction = sprite.direction
                new_direction = self.direction_map.get(sprite.position)
                sprite.update(new_direction)
                if sprite.tail:
                    self.direction_map.pop(old_direction)


class SnakeBody(Sprite):

    def __init__(self, position: TilePosition | PositionStr,
                 direction: Orientation | DirectionStr | DirectionAngle,
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

    def rotate(self, direction):

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
