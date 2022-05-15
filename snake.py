import pygame

from settings import Settings


class Snake:
    """Snake object class"""

    def __init__(self):
        """Init snake attributes and body parts"""
        # Basic attributes
        self.length = 1
        self.speed = Settings.speed
        self.width = Settings.snake_width

        # Body parts
        self.body_straight = pygame.sprite.Group()
        self.body_turn = pygame.sprite.Group()
        self.body_end = pygame.sprite.Group()
