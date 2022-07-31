import pygame
from pygame.surface import Surface

from src.settings import Settings
from src.snake_game import SnakeGame


class ScreenManager:
    """
    Class for managing game window variables and screen rendering
    """

    # Setting up pygame window
    pygame.init()
    screen_surf = pygame.display.set_mode(Settings.get_resolution())
    pygame.display.set_caption('Snake Game')

    def __init__(self, game: SnakeGame):
        self._game = game
        self.screen_rect = self.screen_surf.get_rect()

    def update(self) -> None:
        """
        Redraw and update game window surface
        """
        self.screen_surf.fill((0, 0, 0))
        self._game.snake.draw(self.screen_surf)
        pygame.display.update()
