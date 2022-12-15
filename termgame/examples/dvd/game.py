"""
Description: An example of a bouncing dvd logo
Author: Gregory Glatzer
Date: 10/24/2022
"""

from gameobjects.background import Background
from gameobjects.logo import DVDLogo

from termgame import PhysicsEngine

# define some constants
W = 32
H = 32

e = PhysicsEngine(W, H, gameobjects=[Background(W, H), DVDLogo()])
e.run(fps=10)
