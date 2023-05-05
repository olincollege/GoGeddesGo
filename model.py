"""
Contains many helper classes for our game as well as
the Model class. Helper classes are intended for internal
use only.
"""

import random
import pygame
from pygame.locals import (  # pylint: disable=no-name-in-module
    RLEACCEL,  # pylint: disable=no-name-in-module
)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900


class Player(pygame.sprite.Sprite):  # pylint: disable=too-few-public-methods
    """
    Represents the player (Neato). Contains player coordinates and
    can update them based on keypresses using the update() method.
    Extends the pygame.sprite. Sprite class which contains the sprite
    attributes.

    Attributes:
        _speed: An int representing speed.
        surf: The sprite surface
        rect: The sprite rect

    """

    def __init__(self, speed):
        """
        Constructor for the Player class.

        Args:
            speed: int, represents movement speed.
        Returns:
            None
        """
        super(Player, self).__init__()  # pylint: disable=super-with-arguments
        self.surf = pygame.image.load("neato_champ.jpg").convert()
        self.surf.set_colorkey(
            (255, 255, 255), RLEACCEL
        )  # pylint: disable=no-member
        self.rect = self.surf.get_rect()
        self._speed = speed

    def update(self, pressed_keys):
        """
        Updates the player's position based on which keypress was
        passed into it.

        Args:
            pressed_keys: dict, holds which keys were pressed
        Returns:
            None
        """
        if pressed_keys[pygame.locals.K_UP]:  # pylint: disable=no-member
            self.rect.move_ip(0, -self._speed)
        if pressed_keys[pygame.locals.K_DOWN]:  # pylint: disable=no-member
            self.rect.move_ip(0, self._speed)
        if pressed_keys[pygame.locals.K_LEFT]:  # pylint: disable=no-member
            self.rect.move_ip(-self._speed, 0)
        if pressed_keys[pygame.locals.K_RIGHT]:  # pylint: disable=no-member
            self.rect.move_ip(self._speed, 0)

        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, SCREEN_WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT/2)


class Boat(pygame.sprite.Sprite):  # pylint: disable=too-few-public-methods
    """
    Represents John's boat. Contains player coordinates and
    can update its position using the update() method.
    Extends the pygame.sprite.Sprite class which contains
    the sprite attributes.

    Attributes:
        _speed: An int representing speed.
        surf: The sprite surface.
        rect: The sprite rect.
    """

    def __init__(self, speed):
        """
        Constructor for the Boat class.

        Args:
            speed: int, represents movement speed.
        Returns:
            None
        """
        super(Boat, self).__init__()  # pylint: disable=super-with-arguments
        self.surf = pygame.image.load("holy_grail.png").convert()
        self.surf.set_colorkey(
            (255, 255, 255), RLEACCEL
        )  # pylint: disable=no-member
        self.rect = self.surf.get_rect(center=(100, 550))
        self._speed = speed

    def update(self):
        """
        Updates the position by moving _speed steps to the right
        each time the method is called.

        Args:
            None
        Returns:
            None
        """
        self.rect.move_ip(self._speed, 0)

        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, SCREEN_WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT)


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):  # pylint: disable=too-few-public-methods
    """
    The enemy class, extends pygame.sprite.Sprite.
    Little white bullets that fly from left to right.

    Attributes:
        _speed: An int representing speed.
        surf: The sprite surface.
        rect: The sprite rect.
    """

    def __init__(self):
        """
        Constructor for the Boat class.

        Args:
            speed: int, represents movement speed.
        Returns:
            None
        """
        super(Enemy, self).__init__()  # pylint: disable=super-with-arguments
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT / 2),
            )
        )
        self.speed = random.randint(2, 14)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        """
        Updates the position by moving _speed steps to the left
        each time the method is called.

        Args:
            None
        Returns:
            None
        """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the Finish object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Finish(pygame.sprite.Sprite):  # pylint: disable=too-few-public-methods
    """
    Finish line superclass, extended by the two finish classes.

    Attributes:
        surf: The sprite surface
    """

    def __init__(self, image_path):
        super(Finish, self).__init__()  # pylint: disable=super-with-arguments
        self.surf = pygame.image.load(image_path).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  # pylint: disable=no-member


class BoatFinish(Finish):  # pylint: disable=too-few-public-methods
    """
    Finish line for John's boat. Extends the Finish class

    Attributes:
        rect: The sprite rect
    """

    def __init__(self):
        super(BoatFinish, self).__init__( # pylint: disable=super-with-arguments
            "scotland.png"
        )
        self.rect = self.surf.get_rect(center=(1200, 650))


class PlayerFinish(Finish):  # pylint: disable=too-few-public-methods
    """
    Finish line for the player. Extends the Finish class

    Attributes:
        rect: The sprite rect
    """

    def __init__(self):
        super( # pylint: disable=super-with-arguments
            PlayerFinish, self
        ).__init__(  # pylint: disable=super-with-arguments
            "a_plus_transparent.png"
        )
        self.rect = self.surf.get_rect(center=(1200, 225))


class Model:  # pylint: disable=(too-many-instance-attributes, too-few-public-methods)
    """
    Model for our game, part of the MVC framework.
    Represents game state and has an update function
    that updates the game state via the controller.
    """

    def __init__(self):
        """
        Constructor for the Model class.

        Attributes:
            _start_ticks: start delay to allow enemies to spawn
            _screen: the game display
            ADDENEMY: an event used for spawning our enemies
            player: an instance of the Player class
            boat: an instance of the Boat class
            player_finish: an instance of the PlayerFinish class
            boat_finish: an instance of the BoatFinish class
            enemies: a sprite group of the enemies
            finish_lines: a sprite group of the finish lines
            all_sprites: a sprite group that contains all the game's sprites.
            bg: the background image
        """
        # Define constants for the screen width and height
        # Initialize pygame
        self._start_ticks = 120
        pygame.init()  # pylint: disable=no-member

        # Create the screen object
        # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create a custom event for adding a new enemy
        self.ADDENEMY = (  # pylint: disable=(invalid-name, no-member)
            pygame.USEREVENT + 1  # pylint: disable=(invalid-name, no-member)
        )
        pygame.time.set_timer(self.ADDENEMY, 180)

        # Instantiate player. Right now, this is just a rectangle.
        self.player = Player(speed=8)
        self.boat = Boat(speed=1)
        self.player_finish = PlayerFinish()
        self.boat_finish = BoatFinish()

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        self.enemies = pygame.sprite.Group()
        self.finish_lines = pygame.sprite.Group()
        self.finish_lines.add(self.boat_finish)
        self.finish_lines.add(self.player_finish)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.finish_lines)
        self.all_sprites.add(self.boat)

        # Defines the background image
        self.bg = pygame.image.load(  # pylint: disable=invalid-name
            "final_background.JPG"
        )

        # Start the boat in the right place
        self.boat.update()

    def update_model(self, pressed_keys, ticks):
        """
        Updates the game state, a single cycle of the control logic.
        Requires pressed_keys which is generated by the Controller class
        The player and boat can't move while ticks is below _start_ticks

        Args:
            pressed_keys: A dictionary representing the keypresses
            ticks: An int used to delay the start of the game
        Returns:
            A string representing if we won, lost, or nothing happened.
        """
        if pygame.sprite.spritecollideany(
            self.player, self.enemies
        ) or pygame.sprite.spritecollideany(self.boat, self.finish_lines):
            # If so, then remove the player and stop the loop
            self.player.kill()
            print("You lose.")
            return "L"

        if pygame.sprite.spritecollideany(self.player, self.finish_lines):
            # If so, then remove the player and stop the loop
            self.player.kill()
            print("You Win!")
            return "W"

        for event in pygame.event.get():
            # Add a new enemy
            if event.type == self.ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)

        self.enemies.update()
        if ticks > self._start_ticks:
            # Update the player based on user keypresses
            self.player.update(pressed_keys)

            # Update the boat's position
            self.boat.update()
        return "fuck it we ball"
