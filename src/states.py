from dataclasses import dataclass

# available game states
GAME_ACTIVE = 'GAME_ACTIVE'
START_SCREEN = 'GAME_NOT_ACTIVE'


@dataclass
class States:
    """Data class to store active game state"""

    current_state: str = START_SCREEN
