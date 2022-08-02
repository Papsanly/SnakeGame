import pathlib
from os import walk

import pygame
from pygame.surface import Surface

from src.settings import Settings


class Utils:
    """
    Class with convinient and important constants, variables and methods
    """

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
    def load_tile_image(cls, relative_path: str) -> Surface:
        """
        Returns scaled to fit a tile pygame surface with loaded image

        :param relative_path: Relative path from current working directory to asset image
        """
        image = pygame.image.load(cls.get_abspath(relative_path)).convert_alpha()
        return pygame.transform.smoothscale(image, Settings.get_tile_vec())

    @classmethod
    def preload_directory(cls, relative_directory: str) -> dict[str, Surface]:
        """
        :param relative_directory: Relative path to
        :return: Dictionary of file names and surfaces created from all images in directory
        """
        result = {}
        for _, _, files in walk(Utils.get_abspath(relative_directory)):
            for filename in files:
                try:
                    image = Utils.load_tile_image(relative_directory + '/' + filename)
                    result[filename] = image
                except pygame.error:
                    pass
        return result

    @classmethod
    def get_food_images_count(cls) -> int:
        """
        :return: Amount of food images stored in assets/food directory
        """
        return len(list(walk(cls.get_abspath('../assets/food')))[0][2])
