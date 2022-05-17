from collections import namedtuple

import pygame.image
from pygame.sprite import Sprite
from orientation import Orientation
from settings import Settings

vec2 = namedtuple('vec2', 'x y')


class SnakeBodyEnd(Sprite):
    """Stright body part of snake class"""

    def __init__(self, position, fraction=0, orientation=Orientation('U')):
        super().__init__()

        self.image = pygame.image.load('../resources/snake_end.bmp')
        self.image = pygame.transform.smoothscale(self.image, 2*(Settings.grid_size,))
        self.orientation = orientation
        self.fraction = fraction
        self.position = position

        # get rect for draw method in pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = self.get_position().x
        self.rect.y = self.get_position().y

    def get_position(self):
        """Get pixel position"""
        if self.orientation.name == 'U':
            fraction_x = 0
            fraction_y = self.fraction
        elif self.orientation.name == 'D':
            fraction_x = 0
            fraction_y = -self.fraction
        elif self.orientation.name == 'R':
            fraction_x = self.fraction
            fraction_y = 0
        elif self.orientation.name == 'L':
            fraction_x = -self.fraction
            fraction_y = 0
        else:
            raise ValueError("Orientation.name must return 'U', 'D', 'R' or 'L'")
        return vec2(self.position.get().x + fraction_x * Settings.grid_size,
                    self.position.get().y + fraction_y * Settings.grid_size)
