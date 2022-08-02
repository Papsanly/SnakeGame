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
        self.foods = FoodGroup(self.snake, Settings.food_count)

        self.statistics = Statistics(self)
        self.screen = Screen(self)

        self.ui = UI(self)

        # create states group
        self.game_active_group = [self.foods, self.snake, self.ui]
        self.game_start_group = [self.ui]
        self.game_end_group = [self.ui]

        # event handler, screen manager and statistics initiation
        self.event_handler = EventHandler(self)

    def _check_snake_food_intersection(self):
        food_positions = self.foods.get_food_positions()
        if self.snake.head.position in food_positions:
            pygame.event.post(Event(CustomEvents.snake_eats_food))

    def _check_snake_collisions(self):
        snake_head_position = self.snake.head.position
        snake_positions = self.snake.get_body_positions()
        snake_positions.remove(snake_head_position)
        if (
            snake_head_position in snake_positions or
            not self.screen.rect.collidepoint(snake_head_position.topleft)
        ):
            CurrentState.current_state = States.GAME_END

    def run(self) -> None:
        """
        Starts the main game event loop
        """
        while True:
            self._check_snake_food_intersection()
            self._check_snake_collisions()

            self.statistics.update()
            self.ui.update(self)

            self.event_handler.handle()
            self.screen.update()

            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    import pygame
    from pygame.event import Event
    from src.states import States, CurrentState
    from src.settings import Settings
    from src.screen import Screen
    from src.events import EventHandler, CustomEvents
    from src.control.utils import Utils
    from src.statistics import Statistics
    from src.assets.snake import Snake
    from src.assets.food import FoodGroup
    from src.assets.ui import UI

    snake_game = SnakeGame()
    snake_game.run()
