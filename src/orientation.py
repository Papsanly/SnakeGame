from pygame import Vector2


class Orientation:

    def __init__(self, direction):
        self.direction = direction
        self.get_name()

    def __repr__(self):
        return self.get_name()

    def __eq__(self, other):
        return self.get_name() == other.get_name()

    def __neg__(self):
        return Orientation(-self.get_vector())

    def __ne__(self, other):
        return self.get_name() != other.get_name()

    def get_name(self):
        if isinstance(self.direction, str):
            if self.direction in ['U', 'D', 'L', 'R']:
                return self.direction
        elif isinstance(self.direction, (Vector2, tuple)):
            direction = tuple(self.direction)
            match direction:
                case (1, 0): return 'R'
                case (-1, 0): return 'L'
                case (0, 1): return 'D'
                case (0, -1): return 'U'
        elif isinstance(self.direction, (int, float)):
            direction = int(self.direction) % 360
            match direction:
                case 0: return 'U'
                case 90: return 'R'
                case 180: return 'D'
                case 270: return 'L'
        else:
            raise ValueError('Invalid direction')

    def get_vector(self):
        self.direction = self.get_name()
        match self.direction:
            case 'U': return Vector2(0, -1)
            case 'D': return Vector2(0, -1)
            case 'R': return Vector2(0, -1)
            case 'L': return Vector2(-1, 0)

    def get_angle(self) -> int:
        self.direction = self.get_name()
        match self.direction:
            case 'U': return 0
            case 'D': return 180
            case 'R': return 270
            case 'L': return 90
