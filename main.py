import pygame

import game
import const
from board import Board
from bot import Bot
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

    first_board = Board(True)
    second_board = Board(False)
    first_board.generate(const.FIRST_CELL_POSITION)
    second_board.generate(const.SECOND_CELL_POSITION)

    player = Player()
    bot = Bot()

    battleship = game.Game(screen, player, bot, first_board, second_board)
    battleship.run()


if __name__ == '__main__':
    main()
