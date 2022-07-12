import pygame
import os

from src.settings import Settings
from src.utils import Utils


class SnakeGame:
    """Main class to control game logic and manage objects"""

    def __init__(self):
        """Initiate pygame and create game objects"""
        pygame.init()

        # TODO: create game objects

        pygame.display.set_caption('Snake')

    def _handle_events(self):
        """Check user input and other events"""
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                exit(0)

    def _update_objects(self):
        """Update game objects based on active state"""
        pass

    def _update_screen(self):
        """Rerender updated objects to screen"""

        # update screen
        pygame.display.update()

    def run(self):
        """Run main game loop"""
        while True:
            self._handle_events()
            self._update_objects()
            self._update_screen()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    # change working directory for launching through shortcuts
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    snake_game = SnakeGame()
    snake_game.run()
