from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """
    Data class for game settings
    1 unit = 1 grid square
    """
    resolution = (15, 15)  # units
    grid_size = 75  # pixels / unit
    snake_width = 0.625  # amount of grid square coverage
    food_radius = 0.5  # amount of grid square coverage
    speed = 1  # unit / second
