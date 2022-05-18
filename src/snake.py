import pygame

from screen import Screen
from settings import Settings
from snake_body_end import SnakeBodyEnd
from snake_body_straight import SnakeBodyStraight
from grid_position import GridPos
from pygame.math import Vector2


class Snake:
    """Snake object class"""

    def __init__(self):
        """Init snake attributes and body parts"""

        # Basic attributes
        self.length = 1
        self.speed = Settings.speed

        # Body parts pygame groups
        self.body_straight = pygame.sprite.Group()
        self.body_turn = pygame.sprite.Group()

        # create snake of length one and center it
        center = Settings.grid_count // 2
        self.body_head = (SnakeBodyEnd(
            GridPos(center, offset=(0, -0.5))
        ))
        self.body_tail = (SnakeBodyEnd(
            GridPos(center, offset=(0, 0.5))
        ))
        self.body_straight.add(SnakeBodyStraight(
            self.body_head, self.body_tail
        ))

    def draw(self) -> None:
        self.body_head.draw()
        self.body_tail.draw()
        self.body_straight.draw(Screen.surface)

    def update(self):
        """Update position"""
        self.body_head.update()
        self.body_tail.update()
        self.body_straight.update()
