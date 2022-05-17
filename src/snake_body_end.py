import pygame
from pygame.sprite import Sprite
from settings import Settings
from grid_transformation import GridTransformation


class SnakeBodyEnd(Sprite):
    """Stright body part of snake class"""

    def __init__(self, position: GridTransformation):
        super().__init__()

        self.image = pygame.image.load('../resources/snake_end.bmp')
        self.image = pygame.transform.smoothscale(self.image, 2*(Settings.grid_size,))
        self.position = position

        # get rect for draw method in pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = self.position.get_coords().x
        self.rect.y = self.position.get_coords().y

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)
