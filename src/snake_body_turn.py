import os

import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite

from grid_position import GridPos
from settings import Settings


class SnakeBodyTurn(Sprite):
    """Turning body part of snake class"""

    def __init__(self, position: GridPos, start_direction: Vector2, end_direction: Vector2):
        super().__init__()
        # set basic attributes
        self.position = position
        self.start_direction = start_direction
        self.end_direction = end_direction

        # get images
        walked = next(os.walk('../resources/turn'))
        files = [walked[0] + '/' + file
                 for file
                 in sorted(walked[2], key=lambda x: int(x[:-4]))]
        size = (2 * Settings.grid_size, 2.5 * Settings.grid_size)
        self.images = [pygame.transform.smoothscale(pygame.image.load(file), size=size)
                       for file in files]
        self.frame = 0
        self.image = self.images[self.frame]

        # get rect
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position.get_coords()

        # rotate based on start and end direction
        pygame.transform.rotate()