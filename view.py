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


class View:
    """
    Handles the visuals and displays of the game.
    Attributes:
        _model: A Model instance representing the model state to display.
    """

    def __init__(self, model):
        """
        Constructor for the View class.

        Args:
            _model: A Model instance representing the model state to display.
        Returns:
            None
        """
        self._model = model

    def draw_game(self):
        """
        Renders the current frame of the game based on the
        state contained in the model

        Args:
            None
        Returns:
            None
        """
        self._model._screen.blit(self._model.bg, (0, 0))
        for entity in self._model.all_sprites:
            self._model._screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
