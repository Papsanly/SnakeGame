import pygame
import os

from src.settings import Settings
from src.utils import Utils, Groups
from src.snake import Snake


class SnakeGame:
    """Main class to control game logic and manage objects"""

    def __init__(self):
        """Initiate pygame and create game objects"""
        pygame.init()
        pygame.display.set_caption('Snake')

        # create game objects
        self.snake = Snake()

    def handle_events(self):
        """Check user input and other events"""
        for event in pygame.event.get():
            match event.type:

                # handle quit event
                case pygame.QUIT:
                    exit(0)

    def update_objects(self):
        """Update game objects based on active state"""
        Groups.dynamic_sprites.update()

    def update_screen(self):
        """Rerender updated objects to screen"""
        Groups.visible_sprites.draw(Utils.screen_surface)

        # update screen
        pygame.display.update()

    def run(self):
        """Run main game loop"""
        while True:
            self.handle_events()
            self.update_objects()
            self.update_screen()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    # change working directory for launching through shortcuts
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    snake_game = SnakeGame()
    snake_game.run()
