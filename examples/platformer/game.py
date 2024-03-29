"""
Description: An example of moving a player back and forth using keyboard arrows.
Author: Gregory Glatzer
Date: 12/24/2022
"""

from gameobjects.background import Background
from gameobjects.ground import Ground
from gameobjects.player import Player

from termgame import PhysicsEngine
from termgame.settings import Settings

W = 72
H = 40
GROUND_HEIGHT = 2

level_ground = Ground(x=0, y=H - GROUND_HEIGHT, width=W, height=GROUND_HEIGHT)

p1 = Player(H, GROUND_HEIGHT, lru=["left", "right", "up"], name="Player 1")
p2 = Player(H, GROUND_HEIGHT, lru=["a", "d", "w"], name="Player 2")

e = PhysicsEngine(W, H, gameobjects=[level_ground, Background(W, H), p1, p2])

Settings.runtime_settings.headless = False
e.run()
