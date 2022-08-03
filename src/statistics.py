from snake_game import SnakeGame


class Statistics:

    def __init__(self, game: SnakeGame):
        self.game = game
        self.stats = {
            'snake_length': game.snake.length
        }

    def update(self):
        self.__init__(self.game)
