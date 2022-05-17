import pygame

from screen import Screen
from settings import Settings as Sets
from snake_body_end import SnakeBodyEnd
from snake_body_straight import SnakeBodyStraight
from grid_position import GridPosition
from orientation import Orientation


class Snake:
    """Snake object class"""

    def __init__(self):
        """Init snake attributes and body parts"""

        # Basic attributes
        self.length = 1
        self.speed = Sets.speed

        # Body parts
        self.body_straight = pygame.sprite.Group()
        self.body_turn = pygame.sprite.Group()
        self.body_end = pygame.sprite.Group()

        # create snake of length one and center it
        center = Sets.grid_count[0] // 2, Sets.grid_count[1] // 2
        self.body_end.add(SnakeBodyEnd(
                GridPosition(center), -0.5
        ))
        self.body_end.add(SnakeBodyEnd(
            GridPosition((center[0], center[1] + self.length - 1)), 0.5
        ))
        self.body_straight.add(SnakeBodyStraight(
            GridPosition(center), self.length, orientation=Orientation('D')
        ))

    def draw(self):
        self.body_end.draw(Screen.surface)
        self.body_straight.draw(Screen.surface)
