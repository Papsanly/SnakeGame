from enum import Enum
from typing import Callable, Any

import pygame
from pygame import USEREVENT
from pygame.event import Event

from src.snake_game import SnakeGame
from src.states import States, CurrentState


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
    def __init__(self, method: Callable, use_event=False, indices: list[int] = None, **kwargs: Any):
        self.method = method
        self.kwargs = kwargs
        self.use_event = use_event
        self.indices = [0] if indices is None else indices

    def __repr__(self):
        return f'EventMethod(method={self.method})'

    def __call__(self, events: list[Event] = None):
        if self.use_event:
            used_events = []
            for index in self.indices:
                used_events.append(list(events)[index])
            self.method(*used_events, **self.kwargs)
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
            (pygame.QUIT,):
            {
                'methods': [_EventMethod(exit, code=0)],
                'states': [States.GAME_ACTIVE, States.GAME_START, States.GAME_END]
            },
            (CustomEvents.move_snake,):
            {
                'methods': [_EventMethod(self._game.snake.update)],
                'states': [States.GAME_ACTIVE]
            },
            (pygame.KEYDOWN,):
            {
                'methods': [_EventMethod(self._snake_turn, use_event=True)],
                'states': [States.GAME_ACTIVE]
            },
            (CustomEvents.snake_eats_food, CustomEvents.move_snake):
            {
                'methods': [
                    _EventMethod(self._game.snake.grow, foods=self._game.foods),
                    _EventMethod(self._game.foods.replace_food, snake=self._game.snake)
                ],
                'states': [States.GAME_ACTIVE]
            },
            (pygame.MOUSEBUTTONUP,):
            {
                'methods': [
                    _EventMethod(self._game.ui.check_clicks)
                ],
                'states': [States.GAME_END, States.GAME_START]
            }
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
        all_events: dict[int, Event] = {event.type: event for event in pygame.event.get()}
        for events, methods in self._events_dict.items():
            set_intersection = set(events) & set(all_events)
            if set_intersection == set(events):
                if CurrentState.current_state in methods['states']:
                    for method in methods['methods']:
                        method([all_events[event_type] for event_type in set_intersection])
