import pygame

from src.settings import Settings
from src.snake import Snake


class SnakeGame:

    def __init__(self):

        self.screen_surf = pygame.display.set_mode(Settings.get_resolution())
        pygame.display.set_caption('Snake Game')
        self.screen_rect = self.screen_surf.get_rect()
        self.clock = pygame.time.Clock()

        self.snake = Snake()

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit(0)

                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            self.snake.turn((0, -1))
                        case pygame.K_DOWN:
                            self.snake.turn((0, 1))
                        case pygame.K_LEFT:
                            self.snake.turn((-1, 0))
                        case pygame.K_RIGHT:
                            self.snake.turn((1, 0))

                case self.snake.movement_event:
                    self.snake.body_group.update()

    def update_screen(self):
        self.screen_surf.fill((0, 0, 0))
        self.snake.draw(self.screen_surf)
        pygame.display.update()

    def run(self):
        while True:
            self.handle_events()
            self.update_screen()
            for position, direction in self.snake.body_group.direction_map.items():
                print(f'{position.tile}: {tuple(direction)}', end=', ')
            print()
            self.clock.tick(Settings.fps)


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
