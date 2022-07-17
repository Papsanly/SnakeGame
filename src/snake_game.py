import pygame

from src.settings import Settings
from src.snake import Snake


class SnakeGame:

    def __init__(self):

        self.screen_surf = pygame.display.set_mode(Settings.get_resolution())
        pygame.display.set_caption('Snake Game')
        self.screen_rect = self.screen_surf.get_rect()

        self.snake = Snake()

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit(0)

    def run(self):
        while True:
            self.handle_events()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
