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


# PYGAME_TUTORIAL
pygame.init()

screen = pygame.display.set_mode([500, 500])


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

# NEW
# fill the screen with black
screen.fill((0, 0, 0))

# draw the player on the screen
# try changing this to 'screen.blit(player.surf, player.rect)'
screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# update the display
pygame.display.flip()