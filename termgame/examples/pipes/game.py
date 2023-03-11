from gameobjects.background import Background

from termgame import Engine

W = 8
H = 8
GRID_WIDTH = 1
CELL_THICKNESS = 3

bg = Background(W, H, GRID_WIDTH, CELL_THICKNESS)

e = Engine(
    bg.screen_width,
    bg.screen_height,
    gameobjects=[
        bg,
    ],
)

e.run(fps=20)
