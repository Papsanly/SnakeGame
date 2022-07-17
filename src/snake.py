from pygame import Vector2
from pygame.sprite import Group, Sprite

from src.tile_position import TilePosition
from src.utils import Utils


class Snake:

    def __init__(self):

        self.length = 1
        self.direction_map = {}
        self.snake_body_group = Group(
            SnakeBody(TilePosition('center')),
            SnakeBody(TilePosition('center') + Vector2(0, 1))
        )


class SnakeBody(Sprite):

    def __init__(self, position, *groups):
        super().__init__(*groups)

        self.position = position
        self.image = Utils.load_tile_image('../assets/snake_end.bmp').convert()
        self.rect = self.image.get_rect(topleft=position.topleft)
