import random

import board
from ship import Ship

class Player:
    def __init__(self):
        self.ships = []
        self.player_turn = False

    def get_placed_ships_number(self):
        return len(self.ships)

    def is_player_turn(self):
        return self.player_turn

    def place_ship(self, ship):
        self.ships.append(ship)

    def check_ships(self):
        """
        Returns number of not sunk ships
        """
        n = 0
        for ship in self.ships:
            if not ship.is_sunk():
                n += 1
        return n
