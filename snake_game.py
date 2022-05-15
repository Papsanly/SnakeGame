import pygame

from settings import Settings
from snake import Snake
from button import Button
from food import Food

class SnakeGame:
    """Main class to control game logic and manage objects"""

    def __init__(self):
        """Initiate pygame and create game objects"""
        pygame.init()

        # start game active
        self.is_active = True

        # create game objects
        self.foods = pygame.sprite.Group()
        self.button = Button('Play')
        self.snake = Snake()

        # create screen
        pygame.display.set_mode(Settings.resolution)
        pygame.display.set_caption('Snake')

    def _check_events(self):
        """Check user input and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

    def _update_screen(self):
        """Update rendered objects"""
        pygame.display.update()

    def run(self):
        """Run main game loop"""
        while True:
            self._check_events()
            if self.is_active:
                self._update_screen()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
