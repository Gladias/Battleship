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

    def shoot(self, clicked_cell, second_board):
        return clicked_cell.shoot()

    def count_not_sunk_ships(self):
        n = 0
        for ship in self.ships:
            if not ship.is_sunk():
                n += 1
        return n
