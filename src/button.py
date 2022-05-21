from pygame.math import Vector2

from settings import Settings
from grid_position import GridPos
from screen import Screen
from image_sequence import ImageSequence
from statistic import Stats


class Button:
    """Startup button class"""

    def __init__(self):
        """Init button attributes"""
        # get all images and set current image to the first one
        self.anim_data = ImageSequence(
            '../resources/start',
            GridPos(
                Settings.grid_count // 2 - Vector2(1, 1),
                (0.5, 0)
            ),
            tuple(Vector2(2, 2.5) * Settings.grid_size),
            30
        )

        # Start button unclicked
        self.is_clicked = False

        # get button center for checking if clicked
        self.center = Settings.get_resolution() // 2 + Vector2(0, -0.5) * Settings.grid_size

    def check_clicked(self, mouse_pos):
        """Check if button is clicked to start animation"""
        if self.center.distance_to(mouse_pos) < Settings.grid_size:
            self.is_clicked = True
            self.anim_data.set_timer()

    def draw(self):
        Screen.surface.blit(self.anim_data.image, self.anim_data.rect)

    def update(self):
        """Activate game when animation ended"""
        if self.anim_data.ended:
            Stats.game_active = True
