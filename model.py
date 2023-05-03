import pygame
import random
from abc import ABC, abstractmethod
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

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900


class Player(pygame.sprite.Sprite):
    """
    Represents the player (Neato). Contains player coordinates and
    can update them based on keypresses using the update() method.
    Extends the pygame.sprite.Sprite class which contains the sprite
    attributes.

    Attributes:
        _speed: An int representing speed.

    """
    def __init__(self, speed):
        """
        Constructor for the Player class.

        Args:
            speed: int, represents movement speed.
        Returns:
            None
        """
        super(Player, self).__init__()
        self.surf = pygame.image.load("neato_champ.jpg").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self._speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self._speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self._speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self._speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT / 2:
            self.rect.bottom = SCREEN_HEIGHT / 2


class Boat(pygame.sprite.Sprite):
    """
    Represents John's boat. Contains player coordinates and
    can update its position using the update() method.
    Extends the pygame.sprite.Sprite class which contains
    the sprite attributes.

    Attributes:
        _speed: An int representing speed.
    """
    def __init__(self, speed):
        """
        Constructor for the Boat class.

        Args:
            speed: int, represents movement speed.
        Returns:
            None
        """
        super(Boat, self).__init__()
        self.surf = pygame.image.load("holy_grail.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
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
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the Finish object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Finish(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super(Finish, self).__init__()
        self.surf = pygame.image.load(image_path).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)


class BoatFinish(Finish):
    def __init__(self):
        super(BoatFinish, self).__init__("scotland.png")
        self.rect = self.surf.get_rect(center=(1200, 650))

class PlayerFinish(Finish):
    def __init__(self):
        super(PlayerFinish, self).__init__("a_plus_transparent.png")
        self.rect = self.surf.get_rect(center=(1200, 225))


class Model():
    def __init__(self):
        # Define constants for the screen width and height
        # Initialize pygame
        self._start_ticks = 120
        pygame.init()

        # Create the screen object
        # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


        # Create a custom event for adding a new enemy
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 60)

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
        self.bg = pygame.image.load("final_background.JPG")

        # Start the boat in the right place
        self.boat.update()
    
    def update_model(self, pressed_keys, ticks):
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
    

