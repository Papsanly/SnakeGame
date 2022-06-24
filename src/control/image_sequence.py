import os

import pygame
from pygame.math import Vector2

from src.control.position.grid_position import GridPosition
from src.control.utils import Utils
from src.control.settings import Settings


class ImageSequence:
    """Class to manage sequences of images for image attributes of objects"""

    def __init__(self, filename: str, position: GridPosition,
                 size: Vector2 | tuple = Settings.grid_size * Vector2(1, 1), frame_rate: int = 30):
        # get image sequence surfaces
        walked = next(os.walk(Utils.working_dir + filename))
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
        self.anim_event = pygame.event.custom_type()

    def draw(self):
        Utils.screen_surface.blit(self.image, self.rect)

    def start_anim(self):
        pygame.time.set_timer(self.anim_event, int(1000 / self.frame_rate))

    def update(self):
        """Animate image sequence"""
        if not self.anim_ended:
            self.frame += 1
            self.image = self.images[self.frame]
            if self.frame == len(self.images) - 1:
                self.anim_ended = True
                pygame.time.set_timer(self.anim_event, 0)
