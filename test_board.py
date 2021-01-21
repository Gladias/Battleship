import pygame
import unittest

from board import Board
import const
from cell import Cell


class TestBoard(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

        board = Board(True)
        board.generate(const.FIRST_CELL_POSITION)
        self.board = board

    def test_generate(self):
        for row in self.board.board:
            for cell in row:
                self.assertTrue(isinstance(cell, Cell))

        self.assertEqual(len(self.board.board), 10)

    def test_check_if_edge_of_board(self):
        first_cell_coordinates = (7, 0)
        length = 2
        orientation = "Vertical"

        self.assertFalse(self.board.check_if_edge_of_board(first_cell_coordinates, length, orientation))
        length = 4
        self.assertTrue(self.board.check_if_edge_of_board(first_cell_coordinates, length, orientation))