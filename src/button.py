import os
import pygame
import time

from pygame.math import Vector2

from settings import Settings
from grid_position import GridPos
from screen import Screen
from statistic import Stats


class Button:
    """Startup button class"""

    def __init__(self):
        """Init button attributes"""
        # get all images and set current image to the first one
        walked = next(os.walk('../resources/start'))
        files = [walked[0] + '/' + file
                 for file
                 in sorted(walked[2], key=lambda x: int(x[:-4]))]
        size = (2 * Settings.grid_size, 2.5 * Settings.grid_size)
        self.images = [pygame.transform.smoothscale(pygame.image.load(file), size=size)
                       for file in files]
        self.frame = 0
        self.image = self.images[self.frame]

        # Start button unclicked
        self.is_clicked = False

        # create and center button rect
        self.rect = self.image.get_rect()
        grid_square = Vector2(Settings.grid_count // 2) - Vector2(1, 1)
        self.rect.topleft = GridPos(grid_square=grid_square, offset=(0.5, 0)).get_coords()

        # get button center for checking if clicked
        self.center = Settings.get_resolution() // 2 + Vector2(0, -0.5) * Settings.grid_size

    def check_clicked(self, mouse_pos):
        """Check if button is clicked to set game_active to True"""
        if self.center.distance_to(mouse_pos) < Settings.grid_size:
            self.is_clicked = True

    def draw(self):
        Screen.surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.images[self.frame]
        if self.is_clicked:
            if self.frame != len(self.images) - 1:
                self.frame += 1
                if Settings.fps:
                    time.sleep(max(1 / 24 - 1 / Settings.fps, 0))
            else:
                Stats.game_active = True
