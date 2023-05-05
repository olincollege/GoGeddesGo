"""
The main game file. Run this by typing `python3 game.py` to play our game. 
"""

import pygame
from model import Model
from view import View
from controller import Controller

# Ignored error because its wrong, there very much is a member
# and it is critical to any pygame.
pygame.init()  # pylint: disable=no-member
clock = pygame.time.Clock()
model = Model()
view = View(model)
controller = Controller(model)

TICKS = 0
RUNNING = True

while RUNNING:
    view.draw_game()
    STATUS = model.update_model(controller.keyboard(), TICKS)
    if STATUS == "W":
        RUNNING = False
    elif STATUS == "L":
        RUNNING = False
    # Updates game time
    TICKS += 1
    clock.tick(60)
