import pygame
import pathlib
from dataclasses import dataclass
from enums import States
from src.settings import Settings


@dataclass
class Utils:
    """Class for various utility methods and variables"""

    current_state = States.START_SCREEN
    clock = pygame.time.Clock()
    screen_surface = pygame.display.set_mode(Settings.get_resolution())
    screen_rect = screen_surface.get_rect()
    working_dir = str(pathlib.Path().resolve()) + '/'

    @classmethod
    def get_abspath(cls, name):
        return cls.working_dir + name
