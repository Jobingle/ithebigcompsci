import pygame
from settings import *
from game import *

class THEWALL(pygame.sprite.Sprite):
    def __init__(self, x, y,width ,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        new_size = (width,height)
        self.animation_framesST = [pygame.transform.scale(pygame.image.load("images/obj.png").convert_alpha(), new_size)]
        self.image = self.animation_framesST[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)