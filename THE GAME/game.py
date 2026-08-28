import pygame
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,width ,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.speed = 5
        self.xspeed = 0 
        self.yspeed = 0
        self.mask = None
        self.direction = "L"
        self.animation_count = 0
        self.color = WHITE

    def move(self, dx , dy):
        self.rect.x += dx
        self.rect.y += dy

    def moveXL(self, speed):
        self.xspeed = -speed
        if self.direction != "L":
            self.directiom = "L"
            self.animation_count = 0
    def moveXR(self, speed):
        self.xspeed = speed
        if self.direction != "R":
            self.directiom = "R"
            self.animation_count = 0
    def loop(self):
        self.move(self.x,self.y)
    def draw(self,Gameygamerson_object_screen):
        pygame.draw.rect(Gameygamerson_object_screen, self.color, self.rect)
#argyblargybarggg


class Gameygamerson:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
        pygame.display.set_caption('Seth the Spy')
        self.runninging = True
        self.player = Player(100,100,50,50)

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
                    self.runninging = False
            self.screen.fill((background_colour))
            self.draw_grid()
            self.player.draw(self.screen)
            pygame.display.update()