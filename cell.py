import pygame

from enums import Sign
import const


class Cell:
    def __init__(self, position, coordinates):
        self.position = position
        self.coordinates = coordinates
        self.ship = False  # If ship is on this cell this is set to True
        self.sign = Sign.CLEAR
        self.rect = pygame.Rect((position + (const.CELL_SIZE, const.CELL_SIZE)))

    def __str__(self):
        return self.sign.symbol()

    def has_been_shot(self):
        return self.sign != Sign.CLEAR

    def put_ship(self):
        self.ship = True

    def is_ship_on(self):
        return self.ship

    def get_coordinates(self):
        return self.coordinates

    def shoot(self):
        if self.ship:
            self.sign = Sign.HIT
            return True
        else:
            self.sign = Sign.MISS
            return False

