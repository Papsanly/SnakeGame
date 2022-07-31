class SnakeGame:
    """
    Main game class
    """
    def __init__(self) -> None:
        """
        Create objects and game rosources
        """
        # create objects
        self.snake = Snake()

        # event handler and screen manager initiation
        self.event_handler = EventHandler(self)
        self.screen_manager = ScreenManager(self)

    def run(self) -> None:
        """
        Starts the main game event loop
        """
        while True:
            self.event_handler.handle()
            self.screen_manager.update()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    from src.settings import Settings
    from src.screen import ScreenManager
    from src.events import EventHandler
    from src.control.utils import Utils
    from src.assets.snake import Snake

    snake_game = SnakeGame()
    snake_game.run()
