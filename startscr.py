import pygame
from game import *
from settings import *
class Startscr:
    screen = pygame.display.set_mode((1950,1050))
    pygame.display.set_caption('Jon game')
    # Variable to keep game loop running
    running = True
    # game loop
    while running:
    # for loop through the event queue  
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False
        # Fill the background colour to the screen
        # add text
        screen.fill(background_colour)
        screen.blit(startscreentext1, (500, 100))
        screen.blit(startscreentext2, (10, 500))
        pygame.display.flip()