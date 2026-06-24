import pygame
from game import *
from settings import *
class Startscr:
    screen = pygame.display.set_mode((1950,1050))
    pygame.display.set_caption('Jon game')
    # Variable to keep our game loop running
    running = True
    # game loop
    while running:
    # for loop through the event queue  
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False
        # Fill the background colour to the screen
        screen.fill(background_colour)
        screen.blit(surufaceObj, (100, 100))
        pygame.display.flip()