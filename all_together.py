# Import the pygame module
import pygame
import random
from abc import ABC, abstractmethod

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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

# Define constants for the screen width and height
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("its_beautiful_small.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()


class PlayerController():
    def __init__(self, speed):
        self._speed = speed

    def update(self, player, pressed_keys):
        if pressed_keys[K_UP]:
            player.rect.move_ip(0, -self._speed)
        if pressed_keys[K_DOWN]:
            player.rect.move_ip(0, self._speed)
        if pressed_keys[K_LEFT]:
            player.rect.move_ip(-self._speed, 0)
        if pressed_keys[K_RIGHT]:
            player.rect.move_ip(self._speed, 0)

        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
        if player.rect.top <= 0:
            player.rect.top = 0
        if player.rect.bottom >= SCREEN_HEIGHT/2:
            player.rect.bottom = SCREEN_HEIGHT/2


class Boat(pygame.sprite.Sprite):
    def __init__(self):
        super(Boat, self).__init__()
        self.surf = pygame.image.load("holy_grail.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(100, 550))


class BoatController():
    def __init__(self, speed):
        self._speed = speed

    def update(self, boat):
        boat.rect.move_ip(self._speed, 0)

        if boat.rect.left < 0:
            boat.rect.left = 0
        if boat.rect.right > SCREEN_WIDTH:
            boat.rect.right = SCREEN_WIDTH
        if boat.rect.top <= 0:
            boat.rect.top = 0
        if boat.rect.bottom >= SCREEN_HEIGHT:
            boat.rect.bottom = SCREEN_HEIGHT


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
                random.randint(0, SCREEN_HEIGHT/2),
            )
        )
        self.speed = random.randint(2, 7)

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

    def update(self):
        def update(self):
            if self.rect.right < 0:
                self.kill()


class PlayerFinish(Finish):
    def __init__(self):
        super(PlayerFinish, self).__init__("a_plus_transparent.png")
        self.rect = self.surf.get_rect(center=(1200, 225))


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. Right now, this is just a rectangle.
player = Player()
player_controller = PlayerController(speed=4)
boat = Boat()
boat_controller = BoatController(speed=1)
player_finish = PlayerFinish()
boat_finish = BoatFinish()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
finish_lines = pygame.sprite.Group()
finish_lines.add(boat_finish)
finish_lines.add(player_finish)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(finish_lines)
all_sprites.add(boat)

# Variable to keep the main loop running
running = True

# Defines the background image
bg = pygame.image.load("final_background.JPG")

framerate = 120
ticks = 0
start = 1.5
start_ticks = start * framerate
# Start the boat in the right place
boat_controller.update(boat)
# Main loop
while running:
    screen.blit(bg, (0, 0))
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Delayed start
    if ticks > start_ticks:
        # Update the player sprite based on user keypresses
        player_controller.update(player, pressed_keys)

        #update the boat's position
        boat_controller.update(boat)

    # Update enemy position
    enemies.update()

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(
        player, enemies
    ) or pygame.sprite.spritecollideany(boat, finish_lines):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False
        print("You lose.")

    if pygame.sprite.spritecollideany(player, finish_lines):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False
        print("You Win!")

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    clock = pygame.time.Clock()
    # Update the display
    pygame.display.flip()
    # Updates game time
    ticks += 1
    # Ensure program maintains a rate of 120 frames per second
    clock.tick(120)
