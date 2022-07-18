import pygame

from src.settings import Settings
from src.snake import Snake
from src.food import Food
from src.ui import UI
from src.utils import Utils


class SnakeGame:

    def __init__(self) -> None:

        # basic pygame setup
        pygame.init()
        pygame.display.set_caption('Snake Game')

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
            Utils.screen_surf.fill((0, 0, 0))
            self.visible_sprites.draw(Utils.screen_surf)
            pygame.display.update()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
