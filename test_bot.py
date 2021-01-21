import unittest
import pygame

import const
from board import Board
from bot import Bot


class TestBot(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

        self.bot = Bot()

    def test_place_random_ships(self):
        board = Board(True)
        board.generate(const.FIRST_CELL_POSITION)

        self.bot.place_random_ships(board)
        self.assertEqual(self.bot.get_placed_ships_number(), 5)


if __name__ == '__main__':
    unittest.main()