import os
import pygame
from timeit import default_timer as time

from settings import Settings
from grid_position import GridPos
from screen import Screen


class ImageSequence:
    """Class to manage sequences of images for image attributes of objects"""

    def __init__(self, filename: str, position: GridPos,
                 size: tuple=(Settings.grid_size, Settings.grid_size), frame_rate: int=24):
        # get image sequence surfaces
        walked = next(os.walk(filename))
        files = [walked[0] + '/' + file
                 for file in sorted(walked[2], key=lambda x: int(x[:-4]))]
        self.images = [pygame.transform.smoothscale(pygame.image.load(file), size=size)
                       for file in files]

        # set first image
        self.frame = 0
        self.frame_rate = frame_rate

        self.image = self.images[self.frame]

        # get image rect and set position
        self.rect = self.image.get_rect()
        self.rect.topleft = position.get_coords()

        # timer for image animation
        self.timer = time()

        # animation end indicator
        self.ended = False

    def draw(self):
        Screen.surface.blit(self.image, self.rect)

    def update(self):
        """Animate image sequence"""
        if time() - self.timer >= 1 / self.frame_rate and not self.ended:
            self.timer = time()
            self.frame += 1
            if self.frame == len(self.images) - 1:
                self.ended = True
