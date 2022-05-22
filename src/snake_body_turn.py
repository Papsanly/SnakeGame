import time

import pygame
from pygame.sprite import Sprite

from src.grid_position import GridPos
from src.image_sequence import ImageSequence
from src.orientation import Orientation
from src.settings import Settings
from src.custom_events import ANIMATE_SNAKE_BODY_TURN


class SnakeBodyTurn(Sprite):
    """Turning body part of snake class"""

    def __init__(self, position: GridPos, start_direction: Orientation, end_direction: Orientation):
        super().__init__()
        # set basic attributes
        self.position = position
        self.start_direction = start_direction
        self.end_direction = end_direction

        # load image data
        self.image_data = ImageSequence(
            '../resources/body_turn',
            self.position,
            ANIMATE_SNAKE_BODY_TURN,
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
