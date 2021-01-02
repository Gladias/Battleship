import sys

import pygame

import const
import interface

class Game:

    def __init__(self, screen):
        self.stages = iter(const.GAME_STAGES)
        self.info = ""
        self.screen = screen
        self.font = pygame.font.Font(str(const.ASSETS / "FiraCode-Medium.ttf"), const.FONT_SIZE)

    def run(self):
        icon = pygame.image.load(str(const.ASSETS / "icon.png"))
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Battleship")

        self.screen.fill((66, 135, 245))

        stage = next(self.stages)  # First stages - ship placement
        text_list = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if stage == "ship placement":
                    self.info = "Rozmieść swoje okręty na planszy 1"
                    text_list = interface.text_init(self.font)

                interface.update_screen(text_list, self.screen)
                interface.update_info(self.info, self.font, self.screen)
                pygame.display.flip()