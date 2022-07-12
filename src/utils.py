import pygame
import pathlib
from dataclasses import dataclass
from enum import Enum
from src.settings import Settings


class States(Enum):
    """Enumeration of game states"""

    GAME_ACTIVE = 'game active'
    START_SCREEN = 'start screen'


@dataclass
class Utils:
    """Class for various utility methods and variables"""

    current_state = States.START_SCREEN
    clock = pygame.time.Clock()
    screen_surface = pygame.display.set_mode(Settings.get_resolution())
    screen_rect = screen_surface.get_rect()
    working_dir = str(pathlib.Path().resolve()) + '/'
