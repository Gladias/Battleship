import enum


class Sign(enum.Enum):
    CLEAR = "O"
    MISS = "-"
    HIT = "X"

    def symbol(self):
        return self.value



