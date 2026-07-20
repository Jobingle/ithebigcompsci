import pygame
from settings import *

class Gameygamerson:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
        pygame.display.set_caption('Seth the Spy')
        self.runninging = True
    def draw_grid(self):
        for x in range(0,screen_width,TILESIZE):
            pygame.draw.line(self.screen ,BLACK ,(x,0), (x, screen_height))
        for y in range(0,screen_height,TILESIZE):
            pygame.draw.line(self.screen ,BLACK ,(0,y), (screen_width, y))
    
    def run(self):
        #loop
        while self.runninging: 
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    runninging = False
            self.screen.fill((background_colour))
            self.draw_grid()
            pygame.display.update()