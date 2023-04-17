# this line says "draw surf onto the screen at the center"
screen.blit(surf, (SCREENWIDTH/2, SCREENHEIGHT/2))
pygame.display.flip()

# this doesn't look like the center because .blit() 
# uses the top left corner of surf at the given location

# put the center of surf at the center of display
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2, 
    (SCREEN_HEIGHT-surf.get_height())/2
)

# draw surf at the new coordinates
screen.blit(surf, surf_center)
pygame.display.flip()
