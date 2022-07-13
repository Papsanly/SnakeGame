import pygame

from src.utils import Utils
from src.settings import Settings


def draw_grid() -> None:
    width = 5
    for x, y in zip(range(int(Settings.grid_count.x)), range(int(Settings.grid_count.y))):
        rect_horizontal = pygame.Rect(0, x * Settings.grid_size, Settings.get_resolution().y, width)
        rect_vertical = pygame.Rect(y * Settings.grid_size, 0, width, Settings.get_resolution().x)
        pygame.draw.rect(Utils.screen_surface, 3*(150,), rect_horizontal)
        pygame.draw.rect(Utils.screen_surface, 3*(150,), rect_vertical)


def fill_bg() -> None:
    Utils.screen_surface.fill(3 * (50,))
