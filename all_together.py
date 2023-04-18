# INTRO_GAME_STEPS
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# SPRITES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # put this after the handling loop (events.py)

    # move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# PYGAME_TUTORIAL
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


# NEW
# Instantiate player. This is currently just a rectangle. 
player = Player()


# EVENTS
# Variable to keep the main loop running
running = True

# Main loop
while running:
    # look at every event in the queue
    for event in pygame.event.get():
        # did the user hit a key?
        if event.type == KEYDOWN:
            # if it was the escape key, stop the loop
            if event.key == K_ESCAPE:
                # to exit the loop and game use 'running = False'
                running = False

        # if the user hit the window close button, stop the loop
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # NEW
    # fill the screen with black
    screen.fill((0, 0, 0))

    # draw the player on the screen
    # try changing this to 'screen.blit(player.surf, player.rect)'
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    # update the display
    pygame.display.flip()