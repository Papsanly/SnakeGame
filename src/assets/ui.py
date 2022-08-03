import pygame.font
from pygame import BLEND_RGB_ADD
from pygame.math import Vector2
from pygame.sprite import Group, Sprite

from src.control.utils import Utils
from src.states import States, CurrentState


class UI(Group):
    """
    Managing all the UI in the game
    """
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.length_counter = UIElementText(
            game,
            size=30,
            attributes={'a0': 'snake_length'},
            text='Score: {a0}',
            topleft=(20, 10),
        )
        self.start_button = UIElementStateButton(
            path='../assets/ui/play.bmp',
            state=States.GAME_ACTIVE,
            width=300,
            center=game.screen.rect.center
        )
        self.restart_button = UIElementStateButton(
            path='../assets/ui/restart.bmp',
            state=States.GAME_ACTIVE,
            width=300,
            center=Vector2(game.screen.rect.center) - Vector2(200, 0)
        )
        self.end_button = UIElementStateButton(
            path='../assets/ui/quit.bmp',
            state=States.GAME_ACTIVE,
            width=300,
            center=Vector2(game.screen.rect.center) + Vector2(200, 0)
        )

        self.elements_dict = {
            self.restart_button: [States.GAME_END],
            self.end_button: [States.GAME_END],
            self.start_button: [States.GAME_START],
            self.length_counter: [States.GAME_ACTIVE, States.GAME_END]
        }

    def draw(self, surface):
        for sprite, states in self.elements_dict.items():
            if CurrentState.current_state in states:
                surface.blit(sprite.image, sprite.rect, special_flags=BLEND_RGB_ADD)

    def check_clicks(self):
        for sprite, states in self.elements_dict.items():
            if isinstance(sprite, UIElementStateButton):
                if CurrentState.current_state in states:
                    updated = sprite.update()
                    if sprite is self.restart_button and updated:
                        self.game.snake.reset()
                        self.game.foods.reset()
                    elif sprite is self.end_button and updated:
                        exit(0)

    def update(self, game):
        for sprite, states in self.elements_dict.items():
            if isinstance(sprite, UIElementText):
                if CurrentState.current_state in states:
                    sprite.update(game)


class UIElementText(Sprite):

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


class UIElementStateButton(Sprite):

    def __init__(self, path, width, state, **position):
        super().__init__()
        self.state = state
        self.image = pygame.image.load(Utils.get_abspath(path))

        scalar = width / self.image.get_width()
        height = scalar * self.image.get_height()

        self.image = pygame.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect(**position)

    def update(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if (Vector2(self.rect.center) - Vector2(mouse_pos)).length() < self.rect.width // 2:
            pygame.mouse.set_visible(False)
            CurrentState.current_state = self.state
            return True
        return False
