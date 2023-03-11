from gameobjects.background import Background
from gameobjects.ground import Ground
from gameobjects.player import Player

from termgame import PhysicsEngine

W = 78
H = 32

level_ground = Ground(x=0, y=H - 1, width=W, height=1)


e = PhysicsEngine(W, H, gameobjects=[level_ground, Background(W, H), Player(H)])
e.run(fps=20)
