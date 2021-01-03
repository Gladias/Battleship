import enum


class Cell:
    def __init__(self, position):
        self.position = position
        self.ship = False  # If ship is on this cell this is set to True
        self.sign = Sign.CLEAR

    def __str__(self):
        return self.sign.symbol()

    def has_been_shot(self):
        return self.sign != Sign.CLEAR

    def shoot(self):
        if self.ship:
            self.sign = Sign.HIT
            return True
        else:
            self.sign = Sign.MISS
            return False


class Sign(enum.Enum):
    CLEAR = "O"
    MISS = "-"
    HIT = "X"

    def symbol(self):
        return self.value

