import pygame
from pygame.sprite import Sprite

from src.settings import Settings
from src.snake_body_end import SnakeBodyEnd
from src.snake_body_turn import SnakeBodyTurn


class SnakeBodyStraight(Sprite):
    """Straight body part of snake class"""

    def __init__(self, obj_start: SnakeBodyEnd | SnakeBodyTurn, obj_end: SnakeBodyEnd | SnakeBodyTurn):
        super().__init__()

        self.obj_start = obj_start
        self.obj_end = obj_end

        if obj_start.position.get_coords().y == obj_end.position.get_coords().y:
            self.orientation = 'horizontal'
        elif obj_start.position.get_coords().x == obj_end.position.get_coords().x:
            self.orientation = 'vertical'
        else:
            raise ValueError("obj_1 and obj_2 are not aligned")

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

    def set_obj_end(self, obj_end):
        self.obj_end = obj_end

    def update(self):
        """Update position according to obj_start and obj_end"""
        if self.orientation == 'horizontal':
            self.rect.x = self.obj_start.position.get_coords_center().x
            self.rect.width = self.obj_end.position.get_coords_center().x - self.rect.x
        elif self.orientation == 'vertical':
            self.rect.y = self.obj_start.position.get_coords_center().y
            self.rect.height = self.obj_end.position.get_coords_center().y - self.rect.y
        else:
            raise ValueError("Orientation must be either horizontal or vertical")
