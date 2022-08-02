from enum import Enum


class States(Enum):

    GAME_ACTIVE = 'game active'
    GAME_START = 'game start'
    GAME_END = 'game end'


class CurrentState:
    current_state = States.GAME_ACTIVE
