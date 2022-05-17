from settings import Settings
from collections import namedtuple

vec2 = namedtuple('vec2', 'x y')


class GridPosition:
    """Class to manage coordinates of game objects on grid"""

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def get(self):
        """Get exact pixel position on upper right corner of the grid square"""
        return vec2(self.x * Settings.grid_size, self.y * Settings.grid_size)
