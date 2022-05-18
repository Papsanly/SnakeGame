import pygame
from pygame.sprite import Sprite
from snake_body_end import SnakeBodyEnd
from settings import Settings


class SnakeBodyStraight(Sprite):
    """Straight body part of snake class"""

    def __init__(self, obj_1: SnakeBodyEnd, obj_2: SnakeBodyEnd):
        super().__init__()

        if obj_1.position.get_coords().y == obj_2.position.get_coords().y:
            self.orientation = 'horisontal'
        elif obj_1.position.get_coords().x == obj_2.position.get_coords().x:
            self.orientation = 'vertical'
        else:
            raise ValueError("obj_1 and obj_2 are not aligned")

        if self.orientation == 'horisontal':
            self.obj_start = obj_1 if obj_1.position.get_coords().x < obj_2.position.get_coords().x else obj_2
            self.obj_end = obj_1 if self.obj_start == obj_2 else obj_2
            left = int(self.obj_start.position.get_coords_center().x)
            top = int(self.obj_start.position.get_coords().y - Settings.get_snake_rect_offset())
            width = int(self.obj_end.position.get_coords().x - self.obj_start.position.get_coords().x)
            height = int(Settings.get_snake_width())
        elif self.orientation == 'vertical':
            self.obj_start = obj_1 if obj_1.position.get_coords().y < obj_2.position.get_coords().y else obj_2
            self.obj_end = obj_1 if self.obj_start == obj_2 else obj_2
            left = int(self.obj_start.position.get_coords().x + Settings.get_snake_rect_offset())
            top = int(self.obj_start.position.get_coords_center().y)
            width = int(Settings.get_snake_width())
            height = int(self.obj_end.position.get_coords().y - self.obj_start.position.get_coords().y)
        else:
            raise ValueError("Orientation must be either horisontal or vertical")

        self.rect = pygame.Rect(left, top, width, height)

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(3 * (255,))
