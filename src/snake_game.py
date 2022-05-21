import pygame
import os

from snake import Snake
from button import Button
from screen import Screen
from custom_events import ANIMATE
from time_control import clock
from statistic import Stats
import debug

# change working directory for launching through shortcuts
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class SnakeGame:
    """Main class to control game logic and manage objects"""

    def __init__(self):
        """Initiate pygame and create game objects"""
        pygame.init()

        # create game objects
        self.foods = pygame.sprite.Group()
        self.button = Button()
        self.snake = Snake()

        # create screen
        self.screen_rect = Screen.rect
        pygame.display.set_caption('Snake')

    def _check_events(self):
        """Check user input and other events"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.button.check_clicked(mouse_pos)

            if event.type == ANIMATE:
                self.button.anim_data.update()

    def _update_screen(self):
        """Update rendered objects"""
        # debugging tools
        debug.fill_bg()
        debug.draw_grid()

        # draw game objects
        self.snake.draw()
        if not Stats.game_active:
            self.button.draw()

        # update screen
        pygame.display.update()

    def run(self):
        """Run main game loop"""
        while True:
            self._check_events()

            if Stats.game_active:
                self.snake.update()
            else:
                self.button.update()

            self._update_screen()
            clock.tick()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
