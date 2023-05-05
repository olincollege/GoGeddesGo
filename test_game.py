"""
Pytests for the game. Tests the three main components of the
MVC framework
properly initialize
"""

from model import Model
from view import View
from controller import Controller


def test_init_model():
    """
    It is hard to unit test this game because everything is tied together
    by pygame.
    The best we can do is test if each component of the MVC framework
    initializes
    without errors. This tests the model component
    """
    model = Model()
    assert isinstance(model, Model)


def test_init_view():
    """
    This unit test tests if the view component of our framework
    initializes without
    errors by creating a view object and testing if it is of type View.
    """
    model = Model()
    view = View(model)
    assert isinstance(view, View)


def test_init_controller():
    """
    This unit test tests if the controller component of our framework
    initializes without
    errors by creating a controller object and testing if it is of
    type Controller.
    """
    model = Model()
    controller = Controller(model)
    assert isinstance(controller, Controller)
