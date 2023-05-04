import pygame
import random
from abc import ABC, abstractmethod
from model import Model
from view import View
from controller import Controller
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
clock = pygame.time.Clock()
model = Model()
view = View(model)
controller = Controller(model)

ticks = 0
running = True

while running:
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    view.draw_game()
    status = model.update_model(controller.keyboard(), ticks)
    if status == "W":
        view.win_screen()
        running = False
    elif status == "L":
        view.game_over()
        running = False
    # Updates game time
    ticks += 1
    clock.tick(60)

pygame.quit()
