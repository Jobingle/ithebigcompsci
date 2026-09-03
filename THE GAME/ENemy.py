import pygame
from settings import *

class enemyX(pygame.sprite.Sprite):
    def __init__(self, x, y,width ,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        new_size = (width,height)
        self.speed = 5
        self.xspeed = 0 
        self.yspeed = 0
        self.mask = None
        self.direction = "U"
        self.aggro = False
        self.animation_count = 0
        self.animation_speed = 0.1 
        self.color = WHITE
        self.animation_framesEL = [pygame.transform.scale(pygame.image.load("images/enemyW1L.png").convert_alpha(), new_size),pygame.transform.scale(pygame.image.load("images/enemyW2L.png").convert_alpha(), new_size)]
        self.animation_framesER = [pygame.transform.scale(pygame.image.load("images/enemyW1R.png").convert_alpha(), new_size),pygame.transform.scale(pygame.image.load("images/enemyW2R.png").convert_alpha(), new_size)]
        self.animation_framesES = [pygame.transform.scale(pygame.image.load("images/enemystand.png").convert_alpha(), new_size)]
        self.animation_framesESR = [pygame.transform.scale(pygame.image.load("images/enemyfaceR.png").convert_alpha(), new_size)]
        self.animation_framesESL = [pygame.transform.scale(pygame.image.load("images/enemyfaceL.png").convert_alpha(), new_size)]
        self.animation_framesEB = [pygame.transform.scale(pygame.image.load("images/enemyBUTT.png").convert_alpha(), new_size)]
        self.image = self.animation_framesES[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def animate(self):
        self.animation_count += self.animation_speed
        
        if self.direction == "L":
            if self.animation_count >= len(self.animation_framesEL):
                self.animation_count = 0
            self.image = self.animation_framesEL[int(self.animation_count)]
            
        elif self.direction == "R":
            if self.animation_count >= len(self.animation_framesER):
                self.animation_count = 0
            self.image = self.animation_framesER[int(self.animation_count)]
            
        elif self.direction == "D":
            if self.animation_count >= len(self.animation_framesES):
                self.animation_count = 0
            self.image = self.animation_framesES[int(self.animation_count)]

        elif self.direction == "U":
            if self.animation_count >= len(self.animation_framesEB):
                self.animation_count = 0
            self.image = self.animation_framesEB[int(self.animation_count)]

    def update(self):
        self.animate()

    def move(self, dx , dy):
        self.rect.x += dx
        self.rect.y += dy

    def moveXL(self, speed):
        self.xspeed = -speed
        if self.direction != "L":
            self.direction = "L"
            self.animation_count = 0
    def moveXR(self, speed):
        self.xspeed = speed
        if self.direction != "R":
            self.direction = "R"
            self.animation_count = 0
    def moveU(self, speed):
        self.yspeed = -speed
        if self.direction != "U":
            self.direction = "U"
            self.animation_count = 0
    def moveD(self, speed):
        self.yspeed = speed
        if self.direction != "D":
            self.direction = "D"
            self.animation_count = 0

    def loop(self, fps):
        self.Lmove = (self.rect.x,self.rect.y)
        self.move(self.xspeed,self.yspeed)
