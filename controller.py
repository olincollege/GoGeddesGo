import pygame
class Controller:
    def __init__(self, model):
        self._model = model

    def keyboard(self):
        return pygame.key.get_pressed()