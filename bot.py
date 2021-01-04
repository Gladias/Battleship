import random

from player import Player
from ship import Ship


class Bot(Player):
    def __init__(self):
        super().__init__()
        self.last_turn_hit = False

    def place_random_ships(self, game_board):
        lengths = [2, 3, 3, 4, 5]

        for length in lengths:
            k = random.randint(0, 1)
            a = random.randint(0, 9)
            b = random.randint(0, 9)

            if k == 0:
                orientation = "Horizontal"
            else:
                orientation = "Vertical"

            while not game_board.is_place_ok((a, b), length, orientation):
                a = random.randint(0, 9)
                b = random.randint(0, 9)

            cell_list = []
            for i in range(length):
                if orientation == "Horizontal":
                    cell_list.append(game_board.board[a][i + b])
                else:
                    cell_list.append(game_board.board[i + a][b])

                cell_list[i].put_ship()

            new_ship = Ship(cell_list, orientation)
            self.place_ship(new_ship)



    def make_random_shot(self, game_board):
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        while not game_board.get_cell_by_coords(x, y).has_been_shot():
            x = random.randint(0, 9)
            y = random.randint(0, 9)

        if game_board.get_cell_by_coords(x, y).shoot():
            self.last_turn_hit = True
        else:
            self.last_turn_hit = False
