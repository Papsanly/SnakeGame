class SnakeGame:
    """
    Main game class
    """
    def __init__(self, screen) -> None:
        """
        Initiate pygame, create objects and groups
        """

        # add length to snake event for debug
        # self.add_snake = pygame.event.custom_type()
        # pygame.time.set_timer(self.add_snake, 1, loops=600)

        # create objects
        self.snake = Snake()

        # event handler and screen manager initiation
        self.event_handler = EventHandler(self)
        self.screen_manager = ScreenManager(self, screen)

    def run(self) -> None:
        """
        Starts the main game event loop
        """
        while True:
            self.event_handler.handle()
            self.screen_manager.update()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    import pygame
    from src.settings import Settings

    pygame.init()
    screen = pygame.display.set_mode(Settings.get_resolution())
    pygame.display.set_caption('Snake Game')

    from src.screen import ScreenManager
    from src.events import EventHandler

    from src.assets.snake import Snake
    from src.control.utils import Utils

    snake_game = SnakeGame(screen)
    snake_game.run()
