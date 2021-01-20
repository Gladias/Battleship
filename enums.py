import enum


class Sign(enum.Enum):
    CLEAR = "O"
    MISS = "-"
    HIT = "X"
    SUNK = "S"

    def symbol(self):
        return self.value


class Direction(enum.Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Orientation(enum.Enum):
    Horizontal = 0
    Vertical = 1


