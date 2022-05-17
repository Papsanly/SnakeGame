import pygame.display

from settings import Settings


class Screen:
    """Class to store its screen rect and surface"""

    surface = pygame.display.set_mode(Settings.get_resolution())
    rect = surface.get_rect()
