import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite
from settings import Settings
from grid_transformation import GridTransformation


class SnakeBodyEnd(Sprite):
    """Straight body part of snake class"""

    def __init__(self, position: GridTransformation):
        super().__init__()

        self.image = pygame.image.load('../resources/snake_end.bmp')
        self.image = pygame.transform.smoothscale(self.image, 2*(Settings.grid_size,))
        self.position = position
        self.direction = Vector2(0, -1)
        self.speed = Settings.speed

        # get rect for draw method in pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = self.position.get_coords().x
        self.rect.y = self.position.get_coords().y

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

    def update(self) -> None:
        """Update position"""
        move_vec = self.direction * Settings.get_speed()
        self.position.move(move_vec)
        self.rect.x = self.position.get_coords().x
        self.rect.y = self.position.get_coords().y
