"""
Description: An example of a bouncing dvd logo. 
    This shows how to manually set gameobject positioning without using the game engine.
Author: Gregory Glatzer
Date: 12/24/2022
"""

from gameobjects.background import Background
from gameobjects.logo import DVDLogo

from termgame import Engine

# define some constants
W = 32
H = 32

e = Engine(W, H, gameobjects=[Background(W, H), DVDLogo()])
e.run()
