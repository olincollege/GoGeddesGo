"""
controller module, contains the Controller class
"""
import pygame


class Controller:
    """
    Controller class. Contains the method keyboard
    which is a key listener that just passes out what
    keys it reads in dictionary form.
    """

    def __init__(self, model):
        """
        Constructor for the Controller class

        Args:
            None
        Returns:
            None
        """
        self._model = model

    def keyboard(self):
        """
        Key listener. Returns a dictionary of the keys
        pressed. Nothing else.

        Args:
            None
        Returns:
            A dictionary of the pressed keys
        """
        return pygame.key.get_pressed()

    def mouse(self):
        """
        Placeholder for futher enhancement
        Intended to read mouse input
        """
        return
