from cell import Cell
import const


class Board:
    def __init__(self, is_visible):
        self.is_visible = is_visible
        self.board = []

    def generate(self, first_cell_position):
        for row in range(10):
            line = []
            for column in range(10):
                element = Cell((first_cell_position[0] + (column * (const.CELL_SIZE + const.CELL_GAP)),
                                first_cell_position[1] + (row * (const.CELL_SIZE + const.CELL_GAP))))
                line.append(element)
            self.board.append(line)

    def __str__(self):
        board_str = ""
        for row in self.board:
            for cell in row:
                board_str = board_str + str(cell) + " "
            board_str += "\n"

        return board_str

    def check_for_another_ship(self, cell_list):
        """Checks if another ship has been placed in given cell list"""
