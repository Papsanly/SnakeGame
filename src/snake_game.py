import pygame

from src.settings import Settings
from src.assets.snake import Snake
from src.assets.food import Food
from src.assets.ui import UI
from src.utils import Utils


class SnakeGame:
    """
    Main game class
    """
    def __init__(self) -> None:
        """
        Initiate pygame, create objects and groups
        """

        # pygame setup
        pygame.init()
        pygame.display.set_caption('Snake Game')

        # create groups
        self.visible_sprites = pygame.sprite.Group()
        self.dynamic_sprites = pygame.sprite.Group()

        # create objects
        self.snake = Snake(self.visible_sprites, self.dynamic_sprites)
        self.food = Food(self.visible_sprites)
        self.ui = UI(self.visible_sprites, self.dynamic_sprites)

    def run(self) -> None:
        """
        Starts the main game event loop
        """

        while True:
            # handle quiting
            if pygame.event.get(pygame.QUIT):
                return

            # update objects
            self.dynamic_sprites.update()

            # update screen
            Utils.screen_surf.fill((0, 0, 0))
            self.visible_sprites.draw(Utils.screen_surf)
            pygame.display.update()

            # set fps
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
