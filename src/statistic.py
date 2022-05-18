from dataclasses import dataclass


@dataclass
class Stats:
    """Class to store if game is active and players score"""
    # Start game inactive
    game_active = False
