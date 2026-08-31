import pygame
from settings import *
from game import *

class theD_O_R_E:
    def __init__(self, x, y,width ,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        new_size = (width,height)
        self.animation_framesBD = [pygame.transform.scale(pygame.image.load("images/door.png").convert_alpha(), new_size)]
        self.image = self.animation_framesBD[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class winscr:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
        pygame.display.set_caption('you win')
        self.running = True
    def play(self):
        while self.running:
            for event in pygame.event.get():     
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((background_colour))
            self.screen.blit(winimage , (0,0))
            pygame.display.flip()
