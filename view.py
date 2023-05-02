import pygame
import random
from abc import ABC, abstractmethod
from model import Model, SCREEN_HEIGHT, SCREEN_WIDTH
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

class View():
    def __init__(self, model):
        self._model = model
        

    def start_screen(self):
        pass

    def win_screen(self):
        pass

    def game_over(self):
        pass

    def draw_game(self):
        self._model._screen.blit(self._model.bg, (0, 0))
        for entity in self._model.all_sprites:
            self._model._screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        