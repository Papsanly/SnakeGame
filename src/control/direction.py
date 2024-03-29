from __future__ import annotations
from typing import Literal
from pygame import Vector2

DirectionStr = Literal['U', 'D', 'R', 'L']
DirectionAngle = Literal[0, 90, 180, 270]


class Direction:
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

        self.__dir_internal = direction

    def perpendicular(self, other: Direction):
        """
        :param other: Other orientation
        :return: True if orientations are perpendicular , false otherwise
        """
        return (self - other).angle in (90, 270)

    def __add__(self, other: Direction) -> Direction:
        """
        Add angles mod 360
        :param other: Another Orientation object
        :return: Another Orientation object
        """
        return Direction((self.angle + other.angle) % 360)

    def __sub__(self, other: Direction) -> Direction:
        """
        Subtract angles mod 360
        :param other: Another Orientation object
        :return: Another Direction object
        """
        return Direction((self.angle - other.angle) % 360)

    @property
    def orientation_name(self):
        if self.name in ('U', 'D'):
            return 'V'
        elif self.name in ('R', 'L'):
            return 'H'
        else:
            raise ValueError('Invalid direction!')

    @property
    def name(self):
        try:
            if isinstance(self.__dir_internal, str):
                return self.__dir_internal
            elif isinstance(self.__dir_internal, (Vector2, tuple)):
                return self.__vector_name_dict[tuple(self.__dir_internal)]
            elif isinstance(self.__dir_internal, (int, float)):
                return self.__angle_name_dict[self.__dir_internal]
            elif isinstance(self.__dir_internal, Direction):
                return self.__dir_internal.name
            else:
                raise KeyError
        except KeyError:
            raise ValueError('Invalid direction!')

    @property
    def vector(self):
        try:
            if isinstance(self.__dir_internal, str):
                return Vector2(self.__name_vector_dict[self.__dir_internal])
            elif isinstance(self.__dir_internal, (Vector2, tuple)):
                return Vector2(self.__dir_internal)
            elif isinstance(self.__dir_internal, (int, float)):
                return Vector2(self.__angle_vector_dict[int(self.__dir_internal)])
            elif isinstance(self.__dir_internal, Direction):
                return self.__dir_internal.vector
            else:
                raise KeyError
        except KeyError:
            raise ValueError('Invalid direction!')

    @property
    def angle(self):
        try:
            if isinstance(self.__dir_internal, str):
                return self.__name_angle_dict[self.__dir_internal]
            elif isinstance(self.__dir_internal, (Vector2, tuple)):
                return self.__vector_angle_dict[tuple(self.__dir_internal)]
            elif isinstance(self.__dir_internal, (int, float)):
                return int(self.__dir_internal)
            elif isinstance(self.__dir_internal, Direction):
                return self.__dir_internal.angle
            else:
                raise KeyError
        except KeyError:
            raise ValueError('Invalid direction!')

    def __repr__(self) -> str:
        """
        :return: Name attribute
        """
        return self.name

    def __eq__(self, other: Direction) -> bool:
        """
        :param other: Another Orientation object
        :return: True if names are equal
        """
        return self.name == other.name

    def __neg__(self) -> Direction:
        """
        :return: New Orientation object with opposite direction
        """
        return Direction(-self.vector)

    def __ne__(self, other: Direction) -> bool:
        """
        :param other: Another Orientation object
        :return: True if names are not equal
        """
        return self.name != other.name
