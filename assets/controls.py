import pygame

def capture_buttons(event, p1):
    if event.type == pygame.QUIT:
        return False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            p1.move(0, -5)
        if event.key == pygame.K_s:
            p1.move(0, 5)
        if event.key == pygame.K_a:
            p1.move(-5, 0)
        if event.key == pygame.K_d:
            p1.move(5, 0)
    
    return True