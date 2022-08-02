from random import randint, choice

from pygame import BLEND_RGB_MULT
from pygame.sprite import Sprite, Group
from pygame.surface import Surface

from src.assets.snake import Snake
from src.control.tile_position import TilePosition
from src.control.utils import Utils
from src.settings import Settings


class FoodGroup(Group):

    def __init__(self, snake: Snake, count: int):
        super().__init__()

        for _ in range(count):
            self.add_random_food(snake)

    def add_random_food(self, snake):
        while True:
            rand_pos = TilePosition(
                (randint(0, Settings.tiles_count.x - 1),
                 randint(0, Settings.tiles_count.y - 1))
            )
            if (
                rand_pos not in self.get_food_positions()
                and rand_pos not in snake.get_body_positions()
            ):
                self.add(Food(
                    position=rand_pos,
                    number=randint(0, Utils.get_food_images_count() - 1),
                    color=choice(Settings.food_colors)
                ))
                break

    def get_food_positions(self) -> list[TilePosition]:
        positions = []
        for sprite in self.sprites():
            if hasattr(sprite, 'position'):
                positions.append(sprite.position)
        return positions

    def replace_food(self, snake: Snake) -> None:
        for sprite in self.sprites():
            if hasattr(sprite, 'position'):
                if sprite.position == snake.head.prev.position:
                    self.remove(sprite)
                    self.add_random_food(snake)


class Food(Sprite):

    _images_dict = Utils.preload_directory('../assets/food')

    def __init__(self, position: TilePosition, number: int, color: tuple[int, int, int]):
        super().__init__()

        self.position = position
        self.color = color

        color_image = Surface(Settings.get_tile_vec())
        color_image.fill(color)
        color_image.blit(self._images_dict[f'{number}.bmp'].copy(), (0, 0), special_flags=BLEND_RGB_MULT)
        self.image = color_image

        self.rect = self.image.get_rect(topleft=self.position.topleft)
