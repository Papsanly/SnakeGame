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

        # create objects
        self.snake = Snake()
        self.food = Food()
        self.ui = UI()

    def _handle_events(self) -> None:
        """
        Handle pygame event queue
        """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit(0)
                case self.snake.move_event:
                    self.snake.update()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            self.snake.turn('U')
                        case pygame.K_DOWN:
                            self.snake.turn('D')
                        case pygame.K_LEFT:
                            self.snake.turn('L')
                        case pygame.K_RIGHT:
                            self.snake.turn('R')

    def _update_objects(self) -> None:
        """
        Update dynamic objects
        """
        self.ui.update()

    def _update_screen(self) -> None:
        """
        Redraw and update game window surface
        """
        Utils.screen_surf.fill((0, 0, 0))
        self.snake.draw(Utils.screen_surf)
        self.food.draw(Utils.screen_surf)
        self.ui.draw(Utils.screen_surf)
        pygame.display.update()

    def run(self) -> None:
        """
        Starts the main game event loop
        """
        while True:
            self._handle_events()
            self._update_objects()
            self._update_screen()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
