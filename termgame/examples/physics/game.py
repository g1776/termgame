import random

from gameobjects.background import Background
from gameobjects.particle import Particle
from gameobjects.walls import Wall
from gameobjects.wave_manager import WaveManager

from termgame import PhysicsEngine

W = 32 * 2
H = 32
WALL_THICKNESS = 1
N_PARTICLES = 100


def create_particle() -> Particle:
    random_pos = (
        random.randint(0 + WALL_THICKNESS, W - WALL_THICKNESS),
        random.randint(0 + WALL_THICKNESS, H - WALL_THICKNESS),
    )
    random_blue = (0, 0, random.randint(100, 255))
    return Particle(*random_pos, random_blue)


e = PhysicsEngine(
    W,
    H,
    gameobjects=[
        WaveManager(),
        *[create_particle() for _ in range(N_PARTICLES)],
        Wall(0, 0, W, WALL_THICKNESS),
        Wall(0, 0, WALL_THICKNESS, H),
        Wall(0, H - WALL_THICKNESS, W, WALL_THICKNESS),
        Wall(W - WALL_THICKNESS, 0, WALL_THICKNESS, H),
        Background(W, H),
    ],
)

e.run(fps=20, ppf=10)
