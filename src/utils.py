import pygame
import pathlib
from dataclasses import dataclass
from src.settings import Settings
from enum import Enum


class States(Enum):
    """Enumeration of game states"""

    GAME_ACTIVE = 'game active'
    START_SCREEN = 'start screen'


@dataclass
class Groups:
    """Dataclass of all sprite groups"""

    visible_sprites = pygame.sprite.Group()
    dynamic_sprites = pygame.sprite.Group()
    snake_body_straight_sprites = pygame.sprite.Group()


@dataclass
class Utils:
    """Class for various utility methods and variables"""

    current_state: States = States.START_SCREEN
    clock = pygame.time.Clock()
    screen_surface: pygame.Surface = pygame.display.set_mode(Settings.get_resolution())
    screen_rect: pygame.Rect = screen_surface.get_rect()
    working_dir = str(pathlib.Path().resolve()) + '/'

    @classmethod
    def get_abspath(cls, path) -> str:
        """Get absolute path from relative"""
        return cls.working_dir + path

    @classmethod
    def load_asset_image(cls, path):
        """Load image of the grid square and scale"""
        image = pygame.image.load(Utils.get_abspath('../assets/' + path))
        scaled_image = pygame.transform.smoothscale(image, Settings.get_grid_square())
        return scaled_image
