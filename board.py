from cell import Cell
import const

class Board:
    def __init__(self, board_number, is_visible):
        is_visible = is_visible
        self.board = []
        for row in range(10):
            line = []
            for column in range(10):
                if board_number == 1:
                    element = Cell((const.FIRST_CELL_POSITION[0] + (column * (const.CELL_SIZE + const.CELL_GAP)),
                                   const.FIRST_CELL_POSITION[1] + (row * (const.CELL_SIZE + const.CELL_GAP))))
                else:
                    element = Cell((const.SECOND_CELL_POSITION[0] + (column * const.CELL_SIZE),
                                    const.SECOND_CELL_POSITION[1] + (row * const.CELL_SIZE)))

                line.append(element)
            self.board.append(line)
