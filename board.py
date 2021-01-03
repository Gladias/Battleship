from cell import Cell
import const


class Board:
    def __init__(self, visible):
        self.visible = visible
        self.board = []

    def generate(self, first_cell_position):
        for row in range(10):
            line = []
            for column in range(10):
                element = Cell((first_cell_position[0] + (column * (const.CELL_SIZE + const.CELL_GAP)),
                                first_cell_position[1] + (row * (const.CELL_SIZE + const.CELL_GAP))), (row, column))
                line.append(element)
            self.board.append(line)

    def is_visible(self):
        return self.visible

    def __str__(self):
        board_str = ""
        for row in self.board:
            for cell in row:
                board_str = board_str + str(cell) + " "
            board_str += "\n"

        return board_str

    def get_cell_by_coords(self, x, y):
        return self.board[x][y]

    def is_place_ok(self, first_cell_coordinates, length, orientation):
        return not self.check_if_edge_of_board(first_cell_coordinates, length, orientation) and not self.check_if_another_ship_is_placed(first_cell_coordinates, length, orientation)

    def check_if_edge_of_board(self, first_cell_coordinates, length, orientation):
        if orientation == "Horizontal":
            if first_cell_coordinates[1] + length > 10:
                return True
        else:
            if first_cell_coordinates[0] + length > 10:
                return True
        return False

    def check_if_another_ship_is_placed(self, first_cell_coordinates, length, orientation):
        """Checks if another ship has been placed in given cell list"""
        if orientation == "Horizontal":
            for i in range(length):
                if self.board[first_cell_coordinates[0]][i + first_cell_coordinates[1]].is_ship_on():
                    return True
        else:
            for i in range(length):
                if self.board[first_cell_coordinates[0] + i][first_cell_coordinates[1]].is_ship_on():
                    return True
        return False
