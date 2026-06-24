import pygame

from settings import *
class Startscr:
    screen = pygame.display.set_mode((300, 300))

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

        # Update the display using flip
        pygame.display.flip()