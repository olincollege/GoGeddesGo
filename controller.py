# put this after the handling loop (events.py)

# get the set of keys pressed and check for user input
pressed_keys = pygame.key.get_pressed()

# move the sprite based on user keypresses
def update(self, pressed_keys):
    if pressed_keys[K-UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)