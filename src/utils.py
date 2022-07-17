import pathlib
import pygame

from src.settings import Settings


class Utils:

    working_dir = str(pathlib.Path().resolve()) + '/'

    @classmethod
    def get_abspath(cls, relative_path):
        return cls.working_dir + relative_path

    @classmethod
    def load_tile_image(cls, path):
        image = pygame.image.load(cls.get_abspath(path))
        return pygame.transform.smoothscale(image, Settings.get_tile_vec())
