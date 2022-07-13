import pygame
from pygame import Vector2

from src.grid_position import GridPosition
from src.settings import Settings
from src.utils import Utils, Groups


class Snake(pygame.sprite.Sprite):
    """Snake object class"""

    def __init__(self, *groups: pygame.sprite.Group) -> None:
        """Init snake attributes and body parts"""
        super().__init__(*groups)

        # Basic attributes
        self.length = 1
        self.speed = Settings.snake_speed

        # assign body groups
        self.body_straight = Groups.snake_body_straight_sprites

        # create body
        self.body_head = SnakeBodyEnd(
            Vector2(0, -1),
            GridPosition('center'),
            Groups.visible_sprites, Groups.dynamic_sprites
        )
        self.body_tail = SnakeBodyEnd(
            Vector2(0, -1),
            GridPosition('center', (0, 1)),
            Groups.visible_sprites, Groups.dynamic_sprites
        )
        self.body_straight_first = self.body_straight_last = SnakeBodyStraight(
            Vector2(0, -1),
            self.body_head.position,
            self.body_tail.position,
            Groups.visible_sprites, Groups.snake_body_straight_sprites
        )


class SnakeBodyEnd(pygame.sprite.Sprite):

    def __init__(self, direction: Vector2, position: GridPosition,
                 *groups: pygame.sprite.Group) -> None:
        super().__init__(*groups)

        self.direction = direction
        self.position = position
        self.image = Utils.load_asset_image('snake_end.bmp')
        self.rect = self.image.get_rect(center=position.center)

    def update(self):
        """Move along direction with snake speed"""

        self.position = self.position.moved(self.direction * Settings.get_snake_speed() / Settings.grid_size)
        self.rect.center = self.position.center


class SnakeBodyStraight(pygame.sprite.Sprite):

    def __init__(self, direction: Vector2, grid_square_1: GridPosition,
                 grid_square_2: GridPosition, *groups: pygame.sprite.Group) -> None:
        super().__init__(*groups)

        self.direction = direction
        self.square_1 = grid_square_1
        self.square_2 = grid_square_2

        self.rect = None
        self.update_rect()
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((255, 255, 255))

    def update_rect(self) -> None:
        """
        Get snake body straight rect from direction and end points
        """
        match tuple(self.direction):
            case (1, 0) | (-1, 0):
                self.rect = pygame.Rect(
                    min(self.square_1.center.x, self.square_2.center.x),
                    self.square_1.top + Settings.get_snake_width_offset(),
                    abs(self.square_2.left - self.square_1.left),
                    Settings.get_snake_width()
                )
            case (0, 1) | (0, -1):
                self.rect = pygame.Rect(
                    self.square_1.left + Settings.get_snake_width_offset(),
                    min(self.square_1.center.y, self.square_2.center.y),
                    Settings.get_snake_width(),
                    abs(self.square_2.top - self.square_1.top),
                )
            case _:
                raise ValueError('Impossible direction!')

    def update(self, pos_1: GridPosition, pos_2: GridPosition) -> None:
        """Move rect endpoints according to pos_1 and pos_2"""
        self.square_1 = pos_1
        self.square_2 = pos_2
        self.update_rect()
