import pathlib

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

ASSETS = pathlib.Path("assets/")

GAME_STAGES = ["ship placement", "shooting", "end"]

FIRST_CELL_POSITION = (240, 240)
SECOND_CELL_POSITION = (1000, 400)
CELL_SIZE = 30
CELL_GAP = 2

CELL_COLOR = (255, 255, 255)
SHIP_COLOR = (138, 138, 138)
HIT_COLOR = (255, 54, 54)
BACKGROUND_COLOR = (66, 135, 245)

# SHIP PLACEMENT
SHIPS_BUTTONS = [(30, 360, 5 * CELL_SIZE, CELL_SIZE),
                 (30, 400, 4 * CELL_SIZE, CELL_SIZE),
                 (30, 440, 3 * CELL_SIZE, CELL_SIZE),
                 (30, 480, 3 * CELL_SIZE, CELL_SIZE),
                 (30, 520, 2 * CELL_SIZE, CELL_SIZE)]

CONFIRM_BUTTON = (325, 160, 140, 40)

# TEXT
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 20

INFO_POSITION = (WINDOW_WIDTH / 2, 100)

SHIPS_CAPTION_POSITION = (120, 300)

FIRST_BOARD_CAPTION_POSITION = (400, 650)
SECOND_BOARD_CAPTION_POSITION = (1000, 650)


