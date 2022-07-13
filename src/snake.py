import pygame.sprite
from pygame.math import Vector2

from src.settings import Settings
from src.utils import Utils, Groups


class Snake(pygame.sprite.Sprite):
    """Snake object class"""

    def __init__(self, *groups: pygame.sprite.Group) -> None:
        """Init snake attributes and body parts"""
        super().__init__(*groups)

        # Basic attributes
        self.length = 1
        self.speed = Settings.speed

        # create body
        self.body_head = SnakeBodyEnd(
            Vector2(0, -1),
            Settings.get_resolution() // 2,
            Groups.visible_sprites, Groups.dynamic_sprites
        )
        self.body_tail = SnakeBodyEnd(
            Vector2(0, -1),
            Settings.get_resolution() // 2 + Vector2(0, Settings.grid_size),
            Groups.visible_sprites, Groups.dynamic_sprites
        )


class SnakeBodyEnd(pygame.sprite.Sprite):

    def __init__(self, direction: Vector2, position: Vector2,
                 *groups: pygame.sprite.Group) -> None:
        super().__init__(*groups)

        self.direction = direction
        self.position = position
        self.image = Utils.load_asset_image('snake_end.bmp')
        self.rect = self.image.get_rect(center=position)

    def update(self):
        """Move along direction with snake speed"""

        self.position += self.direction * Settings.get_speed()
        self.rect.center = self.position


class SnakeBodyStraight(pygame.sprite.Sprite):

    def __init__(self, direction: Vector2, start_position: Vector2,
                 end_position: Vector2, *groups: pygame.sprite.Group):
        super().__init__(*groups)

        self.direction = direction
        self.start_position = start_position
        self.end_position = end_position

        match self.direction:
            case (1, 0):
                self.rect = pygame.Rect(
                    self.start_position,
                    top, width, height)
