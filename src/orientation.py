from __future__ import annotations
from typing import Literal
from pygame import Vector2

DirectionStr = Literal['U', 'D', 'R', 'L']
DirectionAngle = Literal[0, 90, 180, 270]


class Orientation:
    """
    Class for managing sprite orientation
    """

    __name_vector_dict = {
        'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    __name_angle_dict = {
        'U': 90,
        'D': 270,
        'R': 0,
        'L': 180
    }
    __angle_vector_dict = {
        0: (1, 0),
        90: (0, -1),
        180: (-1, 0),
        270: (0, 1)
    }
    __vector_name_dict = {v: k for k, v in __name_vector_dict.items()}
    __angle_name_dict = {v: k for k, v in __name_angle_dict.items()}
    __vector_angle_dict = {v: k for k, v in __angle_vector_dict.items()}

    def __init__(self, direction: DirectionStr | Vector2 | DirectionAngle | tuple) -> None:
        """
        :param direction: Vector or tuple that points to coresponding direction or
                          string: 'U' - up, 'D' - down, 'R' - right, 'L' - left or
                          rotation angle: 0 - 'R', 90 - 'U', 180 - 'L', 270 - 'D'
        """

        try:
            if isinstance(direction, str):
                self.name = direction
                self.vector = Vector2(self.__name_vector_dict[direction])
                self.angle = self.__name_angle_dict[direction]
            elif isinstance(direction, (Vector2, tuple)):
                self.name = self.__vector_name_dict[tuple(direction)]
                self.vector = Vector2(direction)
                self.angle = self.__vector_angle_dict[tuple(direction)]
            elif isinstance(direction, (int, float)):
                self.name = self.__angle_name_dict[int(direction)]
                self.vector = Vector2(self.__angle_vector_dict[int(direction)])
                self.angle = int(direction)
        except KeyError:
            raise ValueError('Invalid direction!')

    def __repr__(self) -> str:
        """
        :return: Name attribute
        """
        return self.name

    def __eq__(self, other: Orientation) -> bool:
        """
        :param other: Another Orientation object
        :return: True if names are equal
        """
        return self.name == other.name

    def __neg__(self) -> Orientation:
        """
        :return: New Orientation object with opposite direction
        """
        return Orientation(-self.vector)

    def __ne__(self, other: Orientation) -> bool:
        """
        :param other: Another Orientation object
        :return: True if names are not equal
        """
        return self.name != other.name
