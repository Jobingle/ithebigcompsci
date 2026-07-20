import pygame
from settings import *
from game import *

class Startscr:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
        pygame.display.set_caption('Jon game')
        # Variable to keep game loop running
        self.running = True

    def play(self):
        
        
        # game loop
        while self.running:
        # for loop through the event queue  
            for event in pygame.event.get():
                # Check for QUIT event      
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        newgame = Gameygamerson()
                        newgame.run()
                        running = False
            # display image as start screen
            self.screen.fill((background_colour))
            self.screen.blit(bootupimage , (0,0))
            pygame.display.flip()
