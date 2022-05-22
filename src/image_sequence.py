import os

import pygame
from pygame.math import Vector2

from src.grid_position import GridPos
from src.screen import Screen
from src.settings import Settings


class ImageSequence:
    """Class to manage sequences of images for image attributes of objects"""

    def __init__(self, filename: str, position: GridPos, anim_event: int,
                 size: Vector2 | tuple = Settings.grid_size * Vector2(1, 1), frame_rate: int = 30):
        # get image sequence surfaces
        walked = next(os.walk(filename))
        files = [walked[0] + '/' + file
                 for file in sorted(walked[2], key=lambda x: int(x[:-4]))]
        self.images = [pygame.transform.smoothscale(pygame.image.load(file), size=size)
                       for file in files]

        # set current frame and frame rate
        self.frame = 0
        self.frame_rate = frame_rate
        self.image = self.images[self.frame]

        # get image rect and set position
        self.rect = self.image.get_rect()
        self.rect.topleft = position.get_coords()

        # animation end indicator
        self.anim_ended = False

        # set animation event
        self.anim_event = anim_event

    def draw(self):
        Screen.surface.blit(self.image, self.rect)

    def start_anim(self):
        pygame.time.set_timer(self.anim_event, int(1000 / self.frame_rate))

    def update(self):
        """Animate image sequence"""
        self.frame += 1
        self.image = self.images[self.frame]
        if self.frame == len(self.images) - 1:
            self.anim_ended = True
            pygame.time.set_timer(self.anim_event, 0)
