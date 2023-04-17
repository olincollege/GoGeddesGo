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
# when combined with the previous code, this should give a blank/black screen
