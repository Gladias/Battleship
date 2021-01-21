import random
import time

import const
from enums import Sign, Direction
from player import Player
from ship import Ship


class Bot(Player):
    def __init__(self):
        super().__init__()
        self.random_shots = True
        self.last_shots = const.BOT_SHOOTS
        self.first_accurate_shot_pos = (0, 0)  # First accurate shot made with random shot
        self.last_accurate_shot_pos = (0, 0)
        self.horizontal_shooting = True

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

    def shoot(self, game_board):
        # time.sleep(2)
        if self.random_shots:
            self.make_random_shot(game_board)
        else:
            x, y = self.last_accurate_shot_pos
            direction = Direction.LEFT

            if self.last_shots[Direction.LEFT] == Sign.CLEAR and x > 0:
                self.make_directional_shot(game_board, Direction.LEFT)
                direction = Direction.LEFT

            elif self.last_shots[Direction.RIGHT] == Sign.CLEAR and x < 9:
                self.make_directional_shot(game_board, Direction.RIGHT)
                direction = Direction.RIGHT

            elif self.last_shots[Direction.UP] == Sign.CLEAR and y > 0:
                self.make_directional_shot(game_board, Direction.UP)
                direction = Direction.UP

            elif self.last_shots[Direction.DOWN] == Sign.CLEAR and y < 9:
                self.make_directional_shot(game_board, Direction.DOWN)
                direction = Direction.DOWN

            new_x, new_y = self.last_accurate_shot_pos

            # Miss case
            if new_x == x and new_y == y:
                self.last_shots[direction] = Sign.MISS
                self.last_accurate_shot_pos = self.first_accurate_shot_pos

    def make_directional_shot(self, game_board, direction):
        x, y = self.last_accurate_shot_pos

        if direction == Direction.LEFT:
            if game_board.get_cell_by_coords(x - 1, y).shoot():
                self.last_accurate_shot_pos = (x - 1, y)
        elif direction == Direction.RIGHT:
            if game_board.get_cell_by_coords(x + 1, y).shoot():
                self.last_accurate_shot_pos = (x + 1, y)
        elif direction == Direction.UP:
            if game_board.get_cell_by_coords(x, y - 1).shoot():
                self.last_accurate_shot_pos = (x, y - 1)
        else:
            if game_board.get_cell_by_coords(x, y + 1).shoot():
                self.last_accurate_shot_pos = (x, y + 1)

    def make_random_shot(self, game_board):
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        while game_board.get_cell_by_coords(x, y).has_been_shot():
            x = random.randint(0, 9)
            y = random.randint(0, 9)

        if game_board.get_cell_by_coords(x, y).shoot():
            self.random_shots = False
            self.first_accurate_shot_pos = (x, y)
            self.last_accurate_shot_pos = (x, y)
        else:
            self.random_shots = True

    def last_shot_sunk_enemy_ship(self):
        self.random_shots = True

        self.last_shots[Direction.LEFT] = Sign.CLEAR
        self.last_shots[Direction.RIGHT] = Sign.CLEAR
        self.last_shots[Direction.UP] = Sign.CLEAR
        self.last_shots[Direction.DOWN] = Sign.CLEAR
