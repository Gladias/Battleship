class Player:
    def __init__(self):
        self.ships = []
        self.is_player_turn = False

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
