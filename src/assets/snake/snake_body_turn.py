import pygame
from pygame.sprite import Sprite

from src.control.position.grid_position import GridPosition
from src.control.image_sequence import ImageSequence
from src.control.position.orientation import Orientation
from src.control.settings import Settings


class SnakeBodyTurn(Sprite):
    """Turning body part of snake class"""

    def __init__(self, position: GridPosition, start_direction: Orientation, end_direction: Orientation):
        super().__init__()
        # set basic attributes
        self.position = position
        self.start_direction = start_direction
        self.end_direction = end_direction

        # load image data
        self.image_data = ImageSequence(
            '../assets/body_turn',
            self.position,
            frame_rate=int(60 * Settings.speed)
        )
        self.image = self.image_data.image
        self.rect = self.image_data.rect

        # start animation right after creation
        self.image_data.start_anim()

        # rotate image based on start and end direction
        angle = self.start_direction.get_angle()
        flip = self.end_direction.get_vector() != self.start_direction.get_vector().rotate(90)
        flip_x = self.start_direction.get_name() in ['U', 'D']
        flip_y = not flip_x
        for i, image in enumerate(self.image_data.images):
            self.image_data.images[i] = pygame.transform.rotate(image, angle)
            if flip:
                self.image_data.images[i] = pygame.transform.flip(self.image_data.images[i], flip_x, flip_y)

    def update(self) -> None:
        self.image = self.image_data.image
        self.rect = self.image_data.rect
