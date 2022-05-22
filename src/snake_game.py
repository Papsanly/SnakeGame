import pygame
import os

from src.settings import Settings
from src.snake import Snake
from src.button import Button
from src.screen import Screen
from src.custom_events import ANIMATE_BUTTON, ANIMATE_SNAKE_BODY_TURN
from src.states import States, GAME_ACTIVE, START_SCREEN
from src.time_control import clock
import src.debug

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
            # handle quit event
            if event.type == pygame.QUIT:
                exit(0)

            # handle user input events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.button.check_clicked(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.turn('U')
                elif event.key == pygame.K_DOWN:
                    self.snake.turn('D')
                elif event.key == pygame.K_LEFT:
                    self.snake.turn('L')
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn('R')

            # handle custom events
            elif event.type == ANIMATE_BUTTON:
                self.button.image_data.update()
            elif event.type == ANIMATE_SNAKE_BODY_TURN:
                for sprite in self.snake.body_turn.sprites():
                    if not sprite.image_data.anim_ended:
                        sprite.image_data.update()

    def _update_objects(self):
        """Update game objects based on active state"""
        if States.current_state == GAME_ACTIVE:
            self.snake.update()
        elif States.current_state == START_SCREEN:
            self.button.update()

    def _update_screen(self):
        """Rerender updated objects to screen"""
        # debugging tools
        src.debug.fill_bg()
        src.debug.draw_grid()

        # draw game objects based on states
        if States.current_state == GAME_ACTIVE:
            self.snake.draw()
        elif States.current_state == START_SCREEN:
            self.button.draw()

        # update screen
        pygame.display.update()

    def run(self):
        """Run main game loop"""
        while True:
            self._check_events()
            self._update_objects()
            self._update_screen()
            clock.tick(Settings.fps)


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
