import pygame
from settings import *

class Game:
    a = "b"


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
            if event.type == pygame.K_KP_ENTER:
                event.key == pygame.K_KP_ENTER
                running = False
                game = Game()
        # display image as start screen
        screen.fill((background_colour))
        screen.blit(bootupimage , (0,0))
        pygame.display.flip()
