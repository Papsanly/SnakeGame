import pygame

from src import states
from src.settings import Settings
from src.snake_game import SnakeGame
from src.states import States, CurrentState


class Screen:
    """
    Class for managing game window variables and screen rendering
    """

    # Setting up pygame window
    pygame.init()
    surface = pygame.display.set_mode(Settings.get_resolution())
    pygame.display.set_caption('Snake Game')

    def __init__(self, game: SnakeGame):
        self._game = game
        self.rect = self.surface.get_rect()

    def update(self) -> None:
        """
        Redraw and update game window surface
        """
        self.surface.fill((0, 0, 0))
        if CurrentState.current_state == States.GAME_ACTIVE:
            for obj in self._game.game_active_group:
                obj.draw(self.surface)
        elif CurrentState.current_state == States.GAME_START:
            for obj in self._game.game_start_group:
                obj.draw()
        pygame.display.update()
