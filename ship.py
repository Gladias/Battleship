class Ship:
    def __init__(self, cells):
        self.cells = cells
        self.length = len(cells)

    def is_sunk(self):
        hit_sum = 0
        for cell in self.cells:
            if cell.has_been_shot():
                hit_sum += 1

        if hit_sum == self.length:
            return True
        else:
            return False


