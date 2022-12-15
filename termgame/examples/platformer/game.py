from termgame import PhysicsEngine
from gameobjects.player import Player
from gameobjects.background import Background
from gameobjects.ground import Ground

W = 32
H = 32

level_ground = Ground(x=0, y=H - 1, width=W, height=1)


e = PhysicsEngine(W, H, gameobjects=[Background(W, H), Player(H)])
e.run(fps=20)
