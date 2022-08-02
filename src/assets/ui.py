import time

import pygame.font
from pygame import BLEND_RGB_ADD, BLEND_RGB_MULT
from pygame.sprite import Group, Sprite
from pygame.surface import Surface

from src.control.utils import Utils
from src.snake_game import SnakeGame
from src.states import States, CurrentState


class UI(Group):
    """
    Managing all the UI un the game
    """
    def __init__(self, game):
        super().__init__()

        self.length_counter = UIElementText(
            game,
            size=50,
            attributes={'a0': 'snake_length'},
            text='Score: {a0}',
            topleft=(0, 0),
        )
        self.start_button = UIElementImage(
            path='../assets/ui/play.bmp',
            width=300,
            center=game.screen.rect.center
        )
        self.end_button = UIElementImage(
            path='../assets/ui/again.bmp',
            width=300,
            center=game.screen.rect.center
        )

        self.elements_dict = {
            self.end_button: [States.GAME_END],
            self.start_button: [States.GAME_ACTIVE],
            self.length_counter: [States.GAME_ACTIVE]
        }

    def draw(self, surface):
        for sprite, states in self.elements_dict.items():
            if CurrentState.current_state in states:
                surface.blit(sprite.image, sprite.rect, special_flags=BLEND_RGB_ADD)

    def update(self, game):
        for sprite, states in self.elements_dict.items():
            if CurrentState.current_state in states:
                sprite.update(game)


class UIElement(Sprite):
    pass


class UIElementText(UIElement):

    def __init__(self, game, size, attributes, text, **position):
        super().__init__()

        if len(position) > 1:
            raise ValueError('Too many position specifiers')

        self.size = size
        self.attributes = attributes
        self.text = text

        self.font = pygame.font.Font(Utils.get_abspath('../assets/Bauhaus 93 Regular.ttf'), self.size)
        self.image = None
        self.update(game)
        self.rect = self.image.get_rect(**position)

    def update(self, game):
        attrs = {attr_name: game.statistics.stats[attr_val] for attr_name, attr_val in self.attributes.items()}
        text = self.text.format(**attrs)
        self.image = self.font.render(text, True, (255, 255, 255), (0, 0, 0))


class UIElementImage(UIElement):

    def __init__(self, path, width, **position):
        super().__init__()
        self.image = Surface((0, 0))
        self.rect = self.image.get_rect()
        