import pathlib
import pygame

from src.settings import Settings


class Utils:

    screen_surf = pygame.display.set_mode(Settings.get_resolution())
    screen_rect = screen_surf.get_rect()
    working_dir = str(pathlib.Path().resolve()) + '/'
    clock = pygame.time.Clock()

    @classmethod
    def get_abspath(cls, relative_path):
        return cls.working_dir + relative_path

    @classmethod
    def load_tile_image(cls, path):
        image = pygame.image.load(cls.get_abspath(path))
        return pygame.transform.smoothscale(image, Settings.get_tile_vec())
