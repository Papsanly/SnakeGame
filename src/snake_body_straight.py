import pygame
from pygame.sprite import Sprite

from settings import Settings
from orientation import Orientation


class SnakeBodyStraight(Sprite):
    """Stright body part of snake class"""

    def __init__(self, position, length, fraction=0, orientation=Orientation('U')):
        super().__init__()

        self.length = length
        self.orientation = orientation
        self.fraction = fraction
        self.position = position

        # get coordinates for Rect object
        if orientation.name == 'U':
            left = Settings.get_snake_rect_offset()
            top = -Settings.grid_size * (length - 1)
            width = Settings.grid_size - 2 * Settings.get_snake_rect_offset()
            height = Settings.grid_size * length
        elif orientation.name == 'D':
            left = Settings.get_snake_rect_offset()
            top = 0
            width = Settings.grid_size - 2 * Settings.get_snake_rect_offset()
            height = Settings.grid_size * length
        elif orientation.name == 'R':
            left = -Settings.grid_size * (length - 1)
            top = Settings.get_snake_rect_offset()
            width = Settings.grid_size * length
            height = Settings.grid_size - 2 * Settings.get_snake_rect_offset()
        elif orientation.name == 'L':
            left = 0
            top = Settings.get_snake_rect_offset()
            width = Settings.grid_size * length
            height = Settings.grid_size - 2 * Settings.get_snake_rect_offset()
        else:
            raise ValueError("orientation argument takes 'U', 'D', 'R' or 'L'")

        self.rect = pygame.Rect(
            position.get().x + left,
            position.get().y + top,
            width,
            height,
        )

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(3 * (255,))
