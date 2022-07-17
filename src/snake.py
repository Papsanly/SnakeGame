import pygame.event
from pygame import Vector2
from pygame.sprite import Group, Sprite

from src.settings import Settings
from src.tile_position import TilePosition
from src.utils import Utils


class Snake:

    def __init__(self):

        self.length = 1

        self.head = SnakeBody(TilePosition('center'))
        self.b1 = SnakeBody(TilePosition('center') + Vector2(0, 1))
        self.b2 = SnakeBody(TilePosition('center') + Vector2(0, 2))
        self.b3 = SnakeBody(TilePosition('center') + Vector2(0, 3))
        self.tail = SnakeBody(TilePosition('center') + Vector2(0, 4), tail=True)
        self.body_group = SnakeBodyGroup(
            self.head, self.tail,
            self.b1, self.b2, self.b3
        )

        self.movement_event = pygame.event.custom_type()
        pygame.time.set_timer(self.movement_event, 1000 // Settings.snake_speed)

    def turn(self, direction):
        if direction not in self.body_group.possible_turning_directions[tuple(self.head.direction)]:
            return
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

    def __init__(self, position, tail = False, *groups):
        super().__init__(*groups)

        self.tail = tail
        self.position = position
        self.direction = Vector2(0, -1)
        self.image = Utils.load_tile_image('../assets/snake_end.bmp').convert()
        self.rect = self.image.get_rect(topleft=position.topleft)

    def update(self, direction):
        self.direction = direction if direction else self.direction
        self.position += self.direction
        self.rect.topleft = self.position.topleft
