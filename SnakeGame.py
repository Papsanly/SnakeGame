import pygame

from settings import Settings


class SnakeGame:
    """Main class to control game logic and manage objects"""

    def __init__(self):
        """Initiate pygame and create game objects"""
        pygame.init()

        # create screen
        pygame.display.set_mode(Settings.resolution)


    def run(self):
        """Run main game loop"""
        while True:
            pygame.display.update()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
