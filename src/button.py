from pygame.math import Vector2

from src.settings import Settings
from src.grid_position import GridPos
from src.image_sequence import ImageSequence
from src.states import States, GAME_ACTIVE
from src.custom_events import ANIMATE_BUTTON


class Button:
    """Startup button class"""

    def __init__(self):
        """Init button attributes"""
        # get all images and set current image to the first one
        self.image_data = ImageSequence(
            '../resources/start',
            GridPos(
                Settings.grid_count // 2 - Vector2(1, 1),
                (0.5, 0)
            ),
            ANIMATE_BUTTON,
            tuple(Vector2(2, 2.5) * Settings.grid_size),
        )

        # get button center for checking if clicked
        self.center = Settings.get_resolution() // 2 + Vector2(0, -0.5) * Settings.grid_size

    def check_clicked(self, mouse_pos):
        """Check if button is clicked to start animation"""
        if self.center.distance_to(mouse_pos) < Settings.grid_size:
            self.image_data.start_anim()

    def draw(self):
        self.image_data.draw()

    def update(self):
        """Activate game when animation ended"""
        if self.image_data.anim_ended:
            States.current_state = GAME_ACTIVE
