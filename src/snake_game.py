import pygame

from src.settings import Settings
from src.snake import Snake
from src.food import Food
from src.ui import UI


class SnakeGame:

    def __init__(self) -> None:

        # basic pygame setup
        pygame.init()
        self.screen_surf = pygame.display.set_mode(Settings.get_resolution())
        pygame.display.set_caption('Snake Game')
        self.screen_rect = self.screen_surf.get_rect()
        self.clock = pygame.time.Clock()

        # create groups
        self.visible_sprites = pygame.sprite.Group()
        self.dynamic_sprites = pygame.sprite.Group()

        # object creation
        self.snake = Snake()
        self.food = Food()
        self.ui = UI()

    def run(self) -> None:
        while True:
            self.dynamic_sprites.update()
            self.screen_surf.fill((0, 0, 0))
            self.visible_sprites.draw(self.screen_surf)
            pygame.display.update()
            self.clock.tick(Settings.fps)


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
