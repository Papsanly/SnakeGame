from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    resolution = (15, 15)
    grid_size = 75
    snake_width = 0.625
    food_radius = 0.5
    speed = 1
