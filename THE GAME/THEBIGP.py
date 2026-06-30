import pygame
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()