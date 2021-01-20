import pygame

import const
from enums import Sign


class GameObject:
    """Base class for game objects."""
    def __init__(self, rect, text, font):
        self.rect = rect

        self.text = text
        self.font = font
        self.rendered_text = self.render_text(text)
        self.text_rect = self.rendered_text.get_rect()

    def render_text(self, text, color=const.FONT_COLOR):
        """Renders Pygame text object with given text value."""
        return self.font.render(text, True, color)

    def update_text(self, new_text):
        """Updates text value and invokes render_text method."""
        self.text = new_text
        self.rendered_text = self.render_text(new_text)

    def update_rect_position(self, is_center_update, x, y):
        """Updates object's rect position."""
        if is_center_update:
            self.rect.center = (x, y)
        else:
            self.rect.x = x
            self.rect.y = y


class Button(GameObject):
    """Represents button with position, centered caption, color and border."""
    def __init__(self, rect, text, font, bg_color):
        super().__init__(rect, text, font)
        self.text_rect.center = (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2)
        self.bg_color = bg_color

    def has_been_clicked(self, click):
        pass

class Text(GameObject):
    """Represents text object."""
    def __init__(self, text, font, position=const.INFO_POSITION, rect=None):
        super().__init__(rect, text, font)
        self.text_rect.center = position

def text_init(font):
    ships_caption = Text("Twoje okręty:", font, const.SHIPS_CAPTION_POSITION)
    first_board_caption = Text("Plansza 1", font, const.FIRST_BOARD_CAPTION_POSITION)
    return [first_board_caption, ships_caption]

def ships_init():
    ships = []
    for button in const.SHIPS_BUTTONS:
        ships.append(pygame.Rect(button))
    return ships

def update_info(info, font, screen):
    text = Text(info, font, const.INFO_POSITION)
    screen.blit(text.rendered_text, text.text_rect)

def update_screen(text_list, ships, buttons, first_board, second_board, screen):
    screen.fill(const.BACKGROUND_COLOR)

    for text in text_list:
        screen.blit(text.rendered_text, text.text_rect)

    for ship in ships:
        pygame.draw.rect(screen, const.SHIP_COLOR, ship)

    for button in buttons:
        pygame.draw.rect(screen, button.bg_color, button.rect)
        screen.blit(button.rendered_text, button.text_rect)

    if first_board.is_visible():
        for row in first_board.board:
            for cell in row:
                if cell.is_ship_on():
                    pygame.draw.rect(screen, const.SHIP_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                if cell.sign == Sign.CLEAR and not cell.is_ship_on():
                    pygame.draw.rect(screen, const.CELL_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                elif cell.sign == Sign.MISS:
                    pygame.draw.rect(screen, const.MISS_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                elif cell.sign == Sign.HIT:
                    pygame.draw.rect(screen, const.HIT_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                elif cell.sign == Sign.SUNK:
                    draw_sunken_ship(screen, cell)


    if second_board.is_visible():
        for row in second_board.board:
            for cell in row:
                if cell.sign == Sign.CLEAR:
                    pygame.draw.rect(screen, const.CELL_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                elif cell.sign == Sign.MISS:
                    pygame.draw.rect(screen, const.MISS_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                elif cell.sign == Sign.HIT:
                    pygame.draw.rect(screen, const.HIT_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))
                else:
                    draw_sunken_ship(screen, cell)


def draw_sunken_ship(screen, cell):
    pygame.draw.rect(screen, const.HIT_COLOR, cell.screen_position + (const.CELL_SIZE, const.CELL_SIZE))

    pygame.draw.line(screen, const.SUNK_LINES_COLOR,
                     cell.screen_position,
                     (cell.screen_position[0] + const.CELL_SIZE, cell.screen_position[1] + const.CELL_SIZE), 3)

    pygame.draw.line(screen, const.SUNK_LINES_COLOR,
                     (cell.screen_position[0], cell.screen_position[1] + const.CELL_SIZE),
                     (cell.screen_position[0] + const.CELL_SIZE, cell.screen_position[1]), 3)


def draw_finish_menu(screen, font, win: bool):
    if win:
        result_caption = Text("Wygrana!", font, const.RESULT_POSITION)
    else:
        result_caption = Text("Przegrana!", font, const.RESULT_POSITION)

    play_again_button = Button(pygame.Rect(const.PLAY_AGAIN_BUTTON), "Zagraj ponownie!", font, const.PLAY_AGAIN_COLOR)
    exit_button = Button(pygame.Rect(const.EXIT_BUTTON), "Wyjdź", font, const.EXIT_COLOR)

    background = pygame.Rect(const.FINISH_SQUARE)

    # Drawing
    pygame.draw.rect(screen, const.FINISH_BACKGROUND_COLOR, background)
    screen.blit(result_caption.rendered_text, result_caption.text_rect)

    pygame.draw.rect(screen, play_again_button.bg_color, play_again_button.rect)
    screen.blit(play_again_button.rendered_text, play_again_button.text_rect)

    pygame.draw.rect(screen, exit_button.bg_color, exit_button.rect)
    screen.blit(exit_button.rendered_text, exit_button.text_rect)

    return (play_again_button, exit_button)