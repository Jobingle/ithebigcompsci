import pygame
from settings import *

class Gameygamerson:
    screen = pygame.display.set_mode((1950,1050))
    pygame.display.set_caption('Seth the Spy')
    # Variable to keep game loop running
    runninging = True
    # game loop
    while runninging:
    # for loop through the event queue  
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                runninging = False



