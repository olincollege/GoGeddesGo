# fill the screen with white
screen.fill((255, 255, 255))

# create a surface and pass in a touple containing its length and width
surf = pygame.Surface((50, 50))

# give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()
