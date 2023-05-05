"""
This module contains the View class for our game
"""
import pygame


class View:  # pylint: disable=too-few-public-methods
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
        self._model._screen.blit( # pylint: disable=protected-access
            self._model.bg, (0, 0)
        )
        for entity in self._model.all_sprites:
            self._model._screen.blit(entity.surf, entity.rect) # pylint: disable=protected-access
        pygame.display.flip()
