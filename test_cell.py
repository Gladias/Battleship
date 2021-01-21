import pygame
import unittest

from board import Board
import const


class TestCell(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

        first_board = Board(True)
        first_board.generate(const.FIRST_CELL_POSITION)
        self.cell = first_board.get_cell_by_coords(0, 0)

    def test_shoot(self):
        self.cell.put_ship()
        hit = self.cell.shoot()

        self.assertTrue(hit)
        self.assertTrue(self.cell.has_been_shot())

    def test_get_coordinates(self):
        self.assertEqual(self.cell.get_coordinates(), (0, 0))


if __name__ == '__main__':
    unittest.main()
