import pathlib
import pygame

from src.settings import Settings


class Utils:
    """
    Class with convinient and important constants, variables and methods
    """

    screen_surf = pygame.display.set_mode(Settings.get_resolution())
    screen_rect = screen_surf.get_rect()
    working_dir = str(pathlib.Path().resolve()) + '/'
    clock = pygame.time.Clock()

    @classmethod
    def get_abspath(cls, relative_path: str) -> str:
        """
        Returns absolute path from relative one

        :param relative_path: Relative path from current working directory to asset image
        """
        return cls.working_dir + relative_path

    @classmethod
    def load_tile_image(cls, relative_path: str):
        """
        Returns scaled to fit a tile pygame surface with loaded image

        :param relative_path: Relative path from current working directory to asset image
        """
        image = pygame.image.load(cls.get_abspath(relative_path))
        return pygame.transform.smoothscale(image, Settings.get_tile_vec())
