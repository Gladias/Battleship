import random

import board
from ship import Ship


class Player:
    def __init__(self):
        self.ships = []
        self.is_player_turn = False

    def get_placed_ships_number(self):
        return len(self.ships)

    def place_ship(self, ship):
        self.ships.append(ship)

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
            

    def check_ships(self):
        """
        Returns number of not sunk ships
        """
        n = 0
        for ship in self.ships:
            if not ship.is_sunk():
                n += 1
        return n
