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
                                first_cell_position[1] + (row * (const.CELL_SIZE + const.CELL_GAP))), (row, column))
                line.append(element)
            self.board.append(line)

    def __str__(self):
        board_str = ""
        for row in self.board:
            for cell in row:
                board_str = board_str + str(cell) + " "
            board_str += "\n"

        return board_str

    def check_availability(self):
        #TODO sprawdzac te dwie funkcjie nizej na raz
        pass

    def check_if_edge_of_board(self, first_cell, length, horizontal: bool):
        if horizontal:
            if first_cell.coordinates[1] + length > 10:
                return True
        else:
            if first_cell.coordinates[0] + length > 10:
                return True
        return False

    def check_if_another_ship_is_placed(self, first_cell, length, horizontal: bool):
        """Checks if another ship has been placed in given cell list"""
        if horizontal:
            for i in range(length):
                if self.board[first_cell.coordinates[0]][i + first_cell.coordinates[1]].is_ship_on():
                    return True
        return False
