from __future__ import annotations

from typing import Literal

import pygame.event
from pygame import Vector2
from pygame.sprite import Sprite, Group

from src.orientation import Orientation, DirectionStr, DirectionAngle
from src.settings import Settings
from src.tile_position import TilePosition, PositionStr
from src.utils import Utils

BodyType = Literal['end', 'turn', 'straight']


class Snake(Group):
    """
    Snake object. Created at the center with length one
    """

    def __init__(self):
        super().__init__()

        self.length = 1
        self.direction_map: dict[TilePosition, Orientation] = {}

        self.turn_dirs = []
        self.head = SnakeBodyEnd('center', 'U')
        self.tail = SnakeBodyEnd('center', 'U', shift=(0, 3), tail=True)
        self.add(self.head,
                 SnakeBodyStraight('center', 'U', shift=(0, 1)),
                 SnakeBodyStraight('center', 'U', shift=(0, 2)),
                 self.tail)

        self.move_event = pygame.event.custom_type()
        pygame.time.set_timer(self.move_event, int(1000 / Settings.snake_speed))

    def turn(self, direction: DirectionStr | DirectionAngle | Vector2) -> None:
        """
        Turn the snake in given direction
        :param direction: Direction to turn the snake in
        """
        curr_dir = self.head.direction if not self.turn_dirs else self.turn_dirs[-1]

        if (curr_dir - Orientation(direction)).angle in (90, 270):
            self.turn_dirs.append(Orientation(direction))

    def update(self) -> None:
        """
        Move snake parts according to direction map
        """
        if self.turn_dirs:
            self.direction_map[self.head.position] = self.turn_dirs.pop(0)
        for sprite in self.sprites():
            if hasattr(sprite, 'position') and \
                    hasattr(sprite, 'direction') and \
                    hasattr(sprite, 'rotate'):

                if isinstance(sprite, SnakeBodyTurn):
                    if self.tail.position == sprite.position:
                        sprite.remove(self)
                    continue

                old_position = sprite.position
                old_direction = self.direction_map.get(sprite.position)
                old_old_direction = sprite.direction

                sprite.update(old_direction)
                new_direction = self.direction_map.get(sprite.position)

                if new_direction is not None:
                    sprite.rotate(new_direction - sprite.direction)
                if sprite is self.head:
                    sprite.rotate(sprite.direction - old_old_direction)

                if sprite is self.tail and old_position in self.direction_map:
                    self.direction_map.pop(old_position)

                if old_direction is not None and sprite is self.head:
                    self.add(SnakeBodyTurn(old_position, old_old_direction, old_direction))


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

    def rotate(self, direction_diff: Orientation) -> None:
        """
        Rotate image
        """
        self.image = pygame.transform.rotate(self.image, direction_diff.angle)


class SnakeBodyEnd(SnakeBody):

    def __init__(self, position: TilePosition | PositionStr,
                 direction: Orientation | DirectionStr | DirectionAngle,
                 shift=(0, 0), tail=False):
        super().__init__(position, direction, 'end', shift=shift)

        self.tail = tail
        image_direction = -self.direction if tail else self.direction
        self.image = Utils.load_tile_image(f'../assets/snake_body/end_{image_direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)


class SnakeBodyStraight(SnakeBody):

    def __init__(self, position: TilePosition | PositionStr,
                 direction: Orientation | DirectionStr | DirectionAngle, shift=(0, 0)):
        super().__init__(position, direction, 'straight', shift=shift)

        if direction in ('U', 'D', 90, 270):
            direction = 'V'
        else:
            direction = 'H'

        self.image = Utils.load_tile_image(f'../assets/snake_body/straight_{direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)


class SnakeBodyTurn(SnakeBody):

    def __init__(self, position: TilePosition | PositionStr,
                 start_direction: Orientation | DirectionStr | DirectionAngle,
                 end_direction: DirectionStr | DirectionAngle, shift=(0, 0)):
        super().__init__(position, end_direction, 'turn', shift=shift)

        try:
            self.image = Utils.load_tile_image(f'../assets/snake_body/turn_{start_direction}{end_direction}.bmp')
        except FileNotFoundError:
            self.image = Utils.load_tile_image(f'../assets/snake_body/turn_{-end_direction}{-start_direction}.bmp')
        self.rect = self.image.get_rect(center=self.position.center)

        self.start_direction = start_direction
        self.end_direction = end_direction
