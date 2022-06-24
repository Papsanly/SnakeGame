import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite
from src.control.settings import Settings
from src.control.position.grid_position import GridPosition
from src.control.utils import Utils
from src.control.position.orientation import Orientation


class SnakeBodyEnd(Sprite):
    """Straight body part of snake class"""

    def __init__(self, position: GridPosition):
        super().__init__()

        self.image = pygame.image.load(Utils.working_dir + 'assets\\snake_end.bmp')
        self.image = pygame.transform.smoothscale(self.image, 2*(Settings.grid_size,))
        self.position = position
        self.direction = Orientation(Vector2(0, -1))

        # get rect for Group draw method
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position.get_coords()

    def draw(self) -> None:
        Utils.screen_surface.blit(self.image, self.rect)

    def update(self) -> None:
        """Update position"""
        move_vec = self.direction.get_vector() * Settings.get_speed()
        self.position.move(move_vec)
        self.rect.topleft = self.position.get_coords()
