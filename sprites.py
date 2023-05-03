# sprites deals with the game design and view
# a sprite is essentially a picture
# you create a class to hold all your pictures

# (insert this code after line 18)
# define a player object by extending pygame.sprite.Sprite
# the surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    """
    A class representing a game image.

    Attributes:
        surf: the surface representing the player's sprite.
        rect: the rectangle representing the player's position.
    """
    def __init__(self):
        """
        Initialize a new Player object.

        Args:
            None
        Returns:
            None
        """
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
