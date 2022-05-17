class Orientation:
    """Class to handle orientation or rotation of objects"""

    def __init__(self, name):
        """Init class by orientation name: 'U'-up, 'D'-down, ets."""
        self.name = name

    def get_angle(self):
        """
        Return angle of rotation for given orientation name.
        Rotation origin is set to 'U'
        """
        if self.name == 'U':
            return 0
        elif self.name == 'L':
            return 90
        elif self.name == 'D':
            return 180
        elif self.name == 'R':
            return -90
        else:
            raise ValueError()
