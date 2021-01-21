import pygame

from enums import Sign
import const


class Cell:
    def __init__(self, position, coordinates):
        self.screen_position = position
        self.coordinates = coordinates
        self.ship_on = False  # If ship is on this cell this is set to True
        self.sign = Sign.CLEAR
        self.rect = pygame.Rect((self.screen_position + (const.CELL_SIZE, const.CELL_SIZE)))

    def __str__(self):
        return self.sign.symbol()

    def has_been_shot(self):
        return self.sign != Sign.CLEAR

    def put_ship(self):
        self.ship_on = True

    def is_ship_on(self):
        return self.ship_on

    def get_coordinates(self):
        return self.coordinates

    def mark_sunk(self):
        self.sign = Sign.SUNK

    def shoot(self):
        if self.ship_on:
            self.sign = Sign.HIT
            return True
        else:
            if self.sign != Sign.SUNK:
                self.sign = Sign.MISS
                return False
            else:
                return None

