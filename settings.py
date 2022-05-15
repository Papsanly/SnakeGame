from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    resolution = (1000, 1000)