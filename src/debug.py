import pygame

from screen import Screen
from settings import Settings


def draw_grid():
    width = 5
    for x, y in zip(range(Settings.grid_count.x), range(Settings.grid_count.y)):
        rect_horisontal = pygame.Rect(0, x * Settings.grid_size, Settings.get_resolution().y, width)
        rect_vertical = pygame.Rect(y * Settings.grid_size, 0, width, Settings.get_resolution().x)
        pygame.draw.rect(Screen.surface, 3*(150,), rect_horisontal)
        pygame.draw.rect(Screen.surface, 3*(150,), rect_vertical)


def fill_bg():
    Screen.surface.fill(3 * (50,))
