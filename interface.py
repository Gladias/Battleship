import pygame

import const


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


class Text(GameObject):
    """Represents text object."""
    def __init__(self, text, font, position=const.INFO_POSITION, rect=None):
        super().__init__(rect, text, font)
        self.text_rect.center = position

def text_init(font):
    ships_caption = Text("Twoje okręty:", font, const.SHIPS_CAPTION_POSITION)
    first_board_caption = Text("Plansza 1", font, const.FIRST_BOARD_CAPTION_POSITION)
    return [ships_caption, first_board_caption]


def update_info(info, font, screen):
    text = Text(info, font, const.INFO_POSITION)
    screen.blit(text.rendered_text, text.text_rect)


def update_screen(text_list, screen):
    for text in text_list:
        screen.blit(text.rendered_text, text.text_rect)
