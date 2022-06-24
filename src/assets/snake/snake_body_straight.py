import pygame
from pygame.sprite import Sprite

from src.control.settings import Settings
from src.assets.snake.snake_body_end import SnakeBodyEnd
from src.assets.snake.snake_body_turn import SnakeBodyTurn


class SnakeBodyStraight(Sprite):
    """Straight body part of snake class"""

    def __init__(self, obj_start: SnakeBodyEnd | SnakeBodyTurn | Sprite, obj_end: SnakeBodyEnd | SnakeBodyTurn | Sprite,
                 orientation=None):
        super().__init__()

        self.obj_start = obj_start
        self.obj_end = obj_end

        if not orientation:
            if obj_start.position.get_coords().y == obj_end.position.get_coords().y:
                self.orientation = 'horizontal'
            elif obj_start.position.get_coords().x == obj_end.position.get_coords().x:
                self.orientation = 'vertical'
            else:
                raise ValueError("obj_1 and obj_2 are not aligned")
        else:
            self.orientation = orientation

        if self.orientation == 'horizontal':
            left = self.obj_start.position.get_coords_center().x
            top = self.obj_start.position.get_coords().y + Settings.get_snake_rect_offset()
            width = self.obj_end.position.get_coords().x - self.obj_start.position.get_coords().x
            height = Settings.get_snake_width()
        elif self.orientation == 'vertical':
            left = self.obj_start.position.get_coords().x + Settings.get_snake_rect_offset()
            top = self.obj_start.position.get_coords_center().y
            width = Settings.get_snake_width()
            height = self.obj_end.position.get_coords().y - self.obj_start.position.get_coords().y
        else:
            raise ValueError("Orientation must be either horizontal or vertical")

        self.rect = pygame.Rect(left, top, width, height)

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(3 * (255,))

    def update(self):
        """Update position according to obj_start and obj_end"""
        if self.orientation == 'horizontal':
            x_start = self.obj_start.position.get_coords_center().x
            x_end = self.obj_end.position.get_coords_center().x
            self.rect.left = x_start
            self.rect.width = x_end - x_start
        elif self.orientation == 'vertical':
            y_start = self.obj_start.position.get_coords_center().y
            y_end = self.obj_end.position.get_coords_center().y
            self.rect.top = y_start
            self.rect.height = y_end - y_start
        else:
            raise ValueError("Orientation must be either horizontal or vertical")
