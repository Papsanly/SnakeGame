import pygame
import os

from src.control.settings import Settings
from src.assets.snake.snake import Snake
from src.assets.button import Button
from src.control.utils import Utils, States


class SnakeGame:
    """Main class to control game logic and manage objects"""

    def __init__(self):
        """Initiate pygame and create game objects"""
        pygame.init()

        self.foods = pygame.sprite.Group()
        self.button = Button()
        self.snake = Snake()

        pygame.display.set_caption('Snake')

    def _handle_events(self):
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
            elif event.type == self.button.image_data.anim_event:
                self.button.image_data.update()
            for sprite in self.snake.body_turn.sprites():
                if event.type == sprite.image_data.anim_event:
                    sprite.image_data.update()

    def _update_objects(self):
        """Update game objects based on active state"""
        if Utils.current_state == States.GAME_ACTIVE:
            self.snake.update()
        elif Utils.current_state == States.START_SCREEN:
            self.button.update()

    def _update_screen(self):
        """Rerender updated objects to screen"""
        # debugging tools
        # src.debug.fill_bg()
        # src.debug.draw_grid()

        # draw game objects based on states
        if Utils.current_state == States.GAME_ACTIVE:
            self.snake.draw()
        elif Utils.current_state == States.START_SCREEN:
            self.button.draw()

        # update screen
        pygame.display.update()

    def run(self):
        """Run main game loop"""
        while True:
            self._handle_events()
            self._update_objects()
            self._update_screen()
            Utils.clock.tick(Settings.fps)


if __name__ == '__main__':
    # change working directory for launching through shortcuts
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    snake_game = SnakeGame()
    snake_game.run()
