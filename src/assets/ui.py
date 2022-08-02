from pygame import Rect
from pygame.sprite import Group

from src.settings import Settings
from src.snake_game import SnakeGame


class UIElement:
    """TODO"""
    pass


class UIElementText(UIElement):
    """TODO"""
    pass


class UIElementImage(UIElement):
    """TODO"""
    pass


class UI(Group):

    def __init__(self, game: SnakeGame):
        super().__init__()

        self.length_counter = UIElementText(
            # rect=Rect((0, 0), (50, Settings.get_resolution().y)),
            # size=50,
            # attributes=[game.snake.length],
            # alligment='midleft',
            # text='Score: {a0}',
        )
        self.start_button = UIElementImage(
            # path='../assets/ui/play.bmp',
            # center=game.screen.rect.center
        )
        self.end_button = UIElementImage(
            # path='../assets/ui/again.bmp',
            # center=game.screen.rect.center
        )

    def draw(self, surface):
        """TODO"""
        pass

    def update(self):
        """TODO"""
        pass
