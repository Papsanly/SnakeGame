import pygame.sprite
from pygame.math import Vector2

from src.control.position.grid_position import GridPosition
from src.control.position.orientation import Orientation
from src.control.utils import Utils
from src.control.settings import Settings
from src.assets.snake.snake_body_end import SnakeBodyEnd
from src.assets.snake.snake_body_straight import SnakeBodyStraight
from src.assets.snake.snake_body_turn import SnakeBodyTurn


class Snake:
    """Snake object class"""

    def __init__(self):
        """Init snake attributes and body parts"""

        # Basic attributes
        self.length = 1
        self.speed = Settings.speed
        self.turning = False
        self.direction = Orientation('U')

        # Body parts pygame groups
        self.body_straight = pygame.sprite.Group()
        self.body_turn = pygame.sprite.Group()

        # create snake of length one and center it
        center = Settings.grid_count // 2
        self.body_head = SnakeBodyEnd(
            GridPosition(center, offset=(0, -0.5))
        )
        self.body_tail = SnakeBodyEnd(
            GridPosition(center, offset=(0, 0.5))
        )
        self.body_straight.add(SnakeBodyStraight(
            self.body_head, self.body_tail
        ))

    def turn(self, direction):
        direction = Orientation(direction)
        self.turning = True
        self.direction = direction

    def draw(self) -> None:
        self.body_head.draw()
        self.body_tail.draw()
        self.body_straight.draw(Utils.screen_surface)
        self.body_turn.draw(Utils.screen_surface)

    def update(self) -> None:
        """Update position and direction"""
        self.body_head.update()
        self.body_tail.update()
        self.body_straight.update()
        self.body_turn.update()

        # check if on grid and possible to turn
        if self.turning and \
                self.body_head.position.offset.length() < 0.03 and \
                abs(self.direction.get_angle() - self.body_head.direction.get_angle()) in [90, 270]:
            self.body_head.position.offset = Vector2(0, 0)
            self.direction = self.direction
            self.turning = False

            turn = SnakeBodyTurn(
                self.body_head.position,
                self.body_head.direction,
                self.direction
            )
            self.body_turn.add(turn)
            self.body_head.direction = self.direction
            self.body_straight.remove(self.body_straight.sprites()[-1])
            self.body_straight.add(SnakeBodyStraight(self.body_turn.sprites()[-1], self.body_head, 'horizontal'))
