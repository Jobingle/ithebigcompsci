import pygame
from settings import *

class Gameygamerson:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
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
            self.screen.fill((background_colour))
            def draw_grid(self):
                for x in range(0,self.screen_width,TILESIZE):
                    pygame.draw.line(self.screen ,BLACK ,(x,0), (x, screen_height))
                for y in range(0,self.screen_width,TILESIZE):
                    pygame.draw.line(self.screen ,BLACK ,(0,y), (screen_width, y))
            pygame.display.flip()