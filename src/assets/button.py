from pygame.math import Vector2

from src.control.settings import Settings
from src.control.position.grid_position import GridPosition
from src.control.image_sequence import ImageSequence
from src.control.utils import States, Utils


class Button:
    """Startup button class"""

    def __init__(self):
        """Init button attributes"""
        # get all images and set current image to the first one
        self.image_data = ImageSequence(
            'assets\\start',
            GridPosition(
                Settings.grid_count // 2 - Vector2(1, 1),
                (0.5, 0)
            ),
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
            Utils.current_state = States.GAME_ACTIVE
