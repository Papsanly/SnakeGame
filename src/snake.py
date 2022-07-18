import pygame
from pygame import Vector2
from pygame.sprite import Group, Sprite

from src.orientation import Orientation
from src.settings import Settings
from src.tile_position import TilePosition
from src.utils import Utils


class Snake:

    def __init__(self):

        self.length = 1

        self.head = SnakeBody(TilePosition('center'), body_type='end')
        self.tail = SnakeBody(TilePosition('center') + Vector2(0, 4), body_type='end', tail=True, end_direction=(0, 1))
        self.body_group = SnakeBodyGroup(
            self.head, self.tail,
        )

        self.movement_event = pygame.event.custom_type()
        pygame.time.set_timer(self.movement_event, 1000 // Settings.snake_speed)

    def turn(self, direction):
        if direction in self.body_group.possible_turning_directions[tuple(self.head.direction.get_vector())]:
            self.body_group.direction_map[self.head.position] = Vector2(direction)

    def draw(self, surface):
        self.body_group.draw(surface)


class SnakeBodyGroup(Group):

    def __init__(self, *sprites):
        super().__init__(*sprites)

        self.possible_turning_directions = {
            (0, 1): ((1, 0), (-1, 0)),
            (0, -1): ((1, 0), (-1, 0)),
            (1, 0): ((0, 1), (0, -1)),
            (-1, 0): ((0, 1), (0, -1))
        }
        self.direction_map = {}

    def update(self):
        for sprite in self.sprites():
            if hasattr(sprite, 'tail') and hasattr(sprite, 'position'):
                old_position = sprite.position
                sprite.update(self.direction_map.get(sprite.position))
                if sprite.tail and old_position in self.direction_map:
                    self.direction_map.pop(old_position)


class SnakeBody(Sprite):

    def __init__(self, position, body_type, *groups, tail=False, start_direction='', end_direction=(0, -1)):
        super().__init__(*groups)

        self.tail = tail
        self.body_type = body_type
        self.position = position
        self.direction = Orientation(end_direction)
        self.start_direction = start_direction
        self.image = Utils.load_tile_image(
            f'../assets/body_{body_type}/snake_{body_type}_{start_direction}{self.direction}.bmp'
        ).convert()
        self.rect = self.image.get_rect(topleft=position.topleft)

    def update(self, direction):
        self.direction = direction if direction else self.direction
        if hasattr(self.direction, 'get_vector'):
            self.position += self.direction.get_vector()
        else:
            self.position += self.direction
        self.rect.topleft = self.position.topleft
