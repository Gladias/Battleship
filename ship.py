class Ship:
    def __init__(self, cells, orientation):
        self.cells = cells
        self.length = len(cells)
        self.orientation = orientation

    def is_sunk(self):
        hit_sum = 0
        for cell in self.cells:
            if cell.has_been_shot():
                hit_sum += 1

        if hit_sum == self.length:
            for cell in self.cells:
                cell.mark_sunk()
            return True
        else:
            return False


