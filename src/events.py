from enum import Enum
from typing import Callable, Any

import pygame
from pygame import USEREVENT
from pygame.event import Event

from src.snake_game import SnakeGame


class CustomEvents(int, Enum):
    """
    Enum of all custom events used in game
    """
    move_snake = USEREVENT + 1
    snake_eats_food = USEREVENT + 2


class _EventMethod:
    """
    Class to store method and its arguments for handling events
    """
    def __init__(self, method: Callable, use_event=True, **kwargs: Any):
        self.method = method
        self.kwargs = kwargs
        self.use_event = use_event

    def __call__(self, event: Event = None):
        if self.use_event:
            self.method(event, **self.kwargs)
        else:
            self.method(**self.kwargs)


class EventHandler:
    """
    Class for handling all pygame events
    """

    def __init__(self, game: SnakeGame):
        # instance of game class for accessing game resources
        self._game = game

        # dictionary of event types and methods that are to be called when this event occurs
        self._events_dict = {
            pygame.QUIT: [
                _EventMethod(exit, code=0, use_event=False)
            ],
            CustomEvents.move_snake: [
                _EventMethod(self._game.snake.update, use_event=False)
            ],
            CustomEvents.add_snake: [
                _EventMethod(self._game.snake.grow, use_event=False)
            ],
            pygame.KEYDOWN: [
                _EventMethod(self._snake_turn)
            ],
        }

    def _snake_turn(self, event: Event):
        """
        Turn the snake in given direction
        """
        match event.key:
            case pygame.K_UP:
                self._game.snake.turn('U')
            case pygame.K_DOWN:
                self._game.snake.turn('D')
            case pygame.K_LEFT:
                self._game.snake.turn('L')
            case pygame.K_RIGHT:
                self._game.snake.turn('R')

    def handle(self) -> None:
        """
        Handle all events from pygame event queue
        """
        for event in pygame.event.get():
            try:
                for method in self._events_dict[event.type]:
                    method(event)
            except KeyError:
                pass
