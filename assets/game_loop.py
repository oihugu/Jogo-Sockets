import assets
import pygame

def game_loop(done, clock, screen, p1, p2):
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if not(assets.controls.capture_buttons(event, p1)):
                done = True
                return False

        # --- Game logic should go here
        if pygame.time.get_ticks() % 30 == 0:
            p1.io()
            p2.io()
            
        # --- Screen-clearing code goes here
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((255, 255, 255))
        # --- Drawing code should go here
        p1.draw()
        p2.draw()
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)