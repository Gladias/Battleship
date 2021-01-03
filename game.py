import sys

import pygame

import const
import interface
from ship import Ship


class Game:
    def __init__(self, screen, player, bot, first_board, second_board):
        self.stages = iter(const.GAME_STAGES)
        self.player = player
        self.bot = bot
        self.first_board = first_board
        self.second_board = second_board
        self.info = ""
        self.screen = screen
        self.font = pygame.font.Font(str(const.ASSETS / "FiraCode-Medium.ttf"), const.FONT_SIZE)
        self.active_ship = 0  # len of active ship

    def run(self):
        icon = pygame.image.load(str(const.ASSETS / "icon.png"))
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Battleship")

        self.screen.fill(const.BACKGROUND_COLOR)

        stage = next(self.stages)  # First stage - ship placement
        text_list = interface.text_init(self.font)
        ships = interface.ships_init()
        active_ship_orientation = "Horizontal"   # Can be Horizontal or Vertical

        buttons = [interface.Button(pygame.Rect(const.CONFIRM_BUTTON), "Potwierdź", self.font, const.CELL_COLOR)]

        #TODO change cursor image after clicking on ship
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if stage == "ship placement":
                    self.info = "Rozmieść swoje okręty na planszy 1"

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        if active_ship_orientation == "Horizontal":
                            active_ship_orientation = "Vertical"
                        else:
                            active_ship_orientation = "Horizontal"

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

                        if self.active_ship == 0:
                            for ship in ships:
                                if ship.collidepoint(mouse_pos):
                                    self.active_ship = int(ship.width / const.CELL_SIZE)
                                    ships.remove(ship)
                        else:
                            for row in self.first_board.board:
                                for cell in row:
                                    if cell.rect.collidepoint(mouse_pos):
                                        """Checking if ship can be placed"""
                                        if self.first_board.is_place_ok(cell.coordinates, self.active_ship, active_ship_orientation):
                                            cell_list = []

                                            for i in range(self.active_ship):
                                                if active_ship_orientation == "Horizontal":
                                                    cell_list.append(self.first_board.board[cell.coordinates[0]][i + cell.coordinates[1]])
                                                else:
                                                    cell_list.append(self.first_board.board[i + cell.coordinates[0]][cell.coordinates[1]])
                                                cell_list[i].put_ship()

                                            new_ship = Ship(cell_list, active_ship_orientation)
                                            self.player.place_ship(new_ship)
                                            self.active_ship = 0
                                            active_ship_orientation = "Horizontal"

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

                        if buttons[0].rect.collidepoint(mouse_pos):
                            print(self.player.get_placed_ships_number())
                            if self.player.get_placed_ships_number() < 5:
                                self.info = "Nie rozmieszczono wszystkich okrętów na planszy"
                            else:
                                print("Next stage")
                                self.bot.place_random_ships(self.second_board)
                                stage = next(self.stages)

                if stage == "shooting":
                    pass

                interface.update_screen(text_list, ships, buttons, self.first_board, self.second_board, self.screen)
                interface.update_info(self.info, self.font, self.screen)
                pygame.display.flip()
