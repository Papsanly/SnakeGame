from __future__ import annotations

from random import choice

import pygame.event
from pygame import Vector2, Surface, BLEND_RGB_MULT, BLEND_RGB_ADD
from pygame.sprite import Sprite, Group

from src.control.direction import Direction, DirectionStr, DirectionAngle
from src.events import CustomEvents
from src.settings import Settings
from src.control.tile_position import TilePosition, PositionStr
from src.control.utils import Utils


class Snake(Group):
    """
    Snake object. Created at the center with length one
    """

    def __init__(self):
        super().__init__()

        self.direction = Direction('U')
        self.length = 1

        self.turns_list = []
        self.head = SnakeBody('center', 0, color=choice(Settings.food_colors))
        self.tail = SnakeBody('center', 1, shift=(0, 1), color=choice(Settings.food_colors))
        self.head.prev = self.tail
        self.tail.nxt = self.head
        self.add(self.tail, self.head)

        pygame.time.set_timer(CustomEvents.move_snake, int(1000 / Settings.snake_speed))

    def reset(self):
        self.empty()
        self.direction = Direction('U')
        self.turns_list = []
        self.length = 1

        self.head = SnakeBody('center', 0, color=choice(Settings.food_colors))
        self.tail = SnakeBody('center', 1, shift=(0, 1), color=choice(Settings.food_colors))
        self.head.prev = self.tail
        self.tail.nxt = self.head
        self.add(self.tail, self.head)

        pygame.time.set_timer(CustomEvents.move_snake, int(1000 / Settings.snake_speed))

    def get_body_positions(self) -> list[TilePosition]:
        positions = []
        for sprite in self.sprites():
            if hasattr(sprite, 'position'):
                positions.append(sprite.position)
        return positions

    def grow(self, foods):
        """
        Add one body sprite at the end of snake
        """
        self.length += 1
        for food in foods.sprites():
            if hasattr(food, 'position'):
                if food.position == self.head.prev.position:
                    self.add(SnakeBody(self.tail.position * 2 - self.tail.nxt.position, color=food.color))

    def draw(self, surface):
        for sprite in sorted(self.sprites(), key=lambda x: x.index, reverse=True):
            surface.blit(sprite.image, sprite.rect)

    def add(self, *sprites: Sprite):
        for sprite in sprites:
            if hasattr(sprite, 'nxt') and hasattr(sprite, 'prev'):
                if sprite is not self.head and sprite is not self.tail:
                    sprite.nxt = self.tail
                    self.tail.prev = sprite
                    self.tail = sprite
                    sprite.index = len(self)
                super().add(sprite)

    def turn(self, direction: DirectionStr | DirectionAngle | Vector2) -> None:
        """
        Turn the snake in given direction
        :param direction: Direction to turn the snake in
        """
        curr_dir = self.direction if not self.turns_list else self.turns_list[-1]
        if Direction(direction).perpendicular(curr_dir):
            self.turns_list.append(Direction(direction))

    def update(self) -> None:
        """
        Move snake parts
        """
        # get current direction
        if self.turns_list:
            self.direction = self.turns_list.pop(0)

        # move each body part to current position of the one ahead of it
        # and change image based on positions of next and previous sprite
        sprites = self.sprites()
        sprites.sort(key=lambda x: x.index, reverse=True)
        for sprite in sprites:
            if sprite is not self.head:
                sprite.update()

        # move head along current direction
        self.head.update(self.direction)

        for sprite in self.sprites():
            if hasattr(sprite, 'update_image'):
                sprite.update_image()


class SnakeBody(Sprite):

    _images_dict = Utils.preload_directory('../assets/snake_body')

    def __init__(self, position: TilePosition | PositionStr, index: int = None, color = None,
                 nxt: SnakeBody = None, prev: SnakeBody = None,
                 shift=(0, 0)):
        super().__init__()

        self.color = color
        self.index = index
        self.nxt = nxt
        self.prev = prev
        self.position = TilePosition(position) + shift

        self.image = None
        self.update_image()
        self.rect = self.image.get_rect(topleft=self.position.topleft)

    def _get_next_dir(self) -> Direction:
        if self.nxt:
            return Direction((self.nxt.position - self.position).tile)

    def _get_prev_dir(self) -> Direction:
        if self.prev:
            return Direction((self.position - self.prev.position).tile)

    def update(self, direction=None) -> None:
        if direction is None:
            direction = self._get_next_dir()
        self.position += direction.vector
        self.rect.topleft = self.position.topleft

    def update_image(self):
        next_dir = self._get_next_dir()
        prev_dir = self._get_prev_dir()

        match (prev_dir, next_dir):
            case(None, None):
                self.image = Surface(Settings.get_tile_vec())
            case (None, _):
                self.image = self._images_dict[f'end_{-next_dir}.bmp']
            case (_, None):
                self.image = self._images_dict[f'end_{prev_dir}.bmp']
            case _:
                if next_dir == prev_dir:
                    self.image = self._images_dict[f'straight_{next_dir.orientation_name}.bmp']
                else:
                    try:
                        self.image = self._images_dict[f'turn_{prev_dir}{next_dir}.bmp']
                    except KeyError:
                        self.image = self._images_dict[f'turn_{-next_dir}{-prev_dir}.bmp']
        color_image = Surface(Settings.get_tile_vec())
        white_image = Surface(Settings.get_tile_vec())

        color_image.fill(self.color)
        white_image.fill(3 * (64,))
        color_image.blit(white_image, (0, 0), special_flags=BLEND_RGB_ADD)
        color_image.blit(self.image.copy(), (0, 0), special_flags=BLEND_RGB_MULT)
        self.image = color_image
