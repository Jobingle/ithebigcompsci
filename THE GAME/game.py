import pygame
from settings import *
from LOSE import looser
from ENemy import enemyX

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,width ,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        new_size = (width,height)
        self.speed = 5
        self.xspeed = 0 
        self.yspeed = 0
        self.mask = None
        self.direction = "L"
        self.animation_count = 0
        self.animation_speed = 0.1 
        self.color = WHITE
        self.animation_framesPL = [pygame.transform.scale(pygame.image.load("images/playerWL1.png").convert_alpha(), new_size),pygame.transform.scale(pygame.image.load("images/playerWL2.png").convert_alpha(), new_size)]
        self.animation_framesPR = [pygame.transform.scale(pygame.image.load("images/playerWR1.png").convert_alpha(), new_size),pygame.transform.scale(pygame.image.load("images/playerWR2.png").convert_alpha(), new_size)]
        self.animation_framesPS = [pygame.transform.scale(pygame.image.load("images/playerstand.png").convert_alpha(), new_size)]
        self.image = self.animation_framesPS[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def animate(self):
        self.animation_count += self.animation_speed
        
        if self.direction == "L":
            if self.animation_count >= len(self.animation_framesPL):
                self.animation_count = 0
            self.image = self.animation_framesPL[int(self.animation_count)]
            
        elif self.direction == "R":
            if self.animation_count >= len(self.animation_framesPR):
                self.animation_count = 0
            self.image = self.animation_framesPR[int(self.animation_count)]
            
        elif self.direction in ("U", "D"):
            if self.animation_count >= len(self.animation_framesPS):
                self.animation_count = 0
            self.image = self.animation_framesPS[int(self.animation_count)]

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
        
#argyblargybarggg


class Gameygamerson:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
        pygame.display.set_caption('Seth the Spy')
        self.runninging = True
        self.player = Player(50,50,100,100)
        self.enemyX = enemyX(500, 500 , 100 , 100)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemyX)

    def pmove(self, player):
        keys = pygame.key.get_pressed() 
        player.xspeed = 0
        player.yspeed = 0
        if keys[pygame.K_LEFT]:
          player.moveXL(player.speed)
        elif keys[pygame.K_RIGHT]:
          player.moveXR(player.speed)
        elif keys[pygame.K_UP]:
          player.moveU(player.speed)
        elif keys[pygame.K_DOWN]:
          player.moveD(player.speed)
        screen_rect = self.screen.get_rect()
        player.rect.clamp_ip(screen_rect)

    def Emove(self, enemyX):
        for counter in range(1950):
            if self.player.x == enemyX.x + counter:
                enemyX.aggro = True

    def draw_grid(self):
        for x in range(0,screen_width,TILESIZE):
            pygame.draw.line(self.screen ,BLACK ,(x,0), (x, screen_height))
        for y in range(0,screen_height,TILESIZE):
            pygame.draw.line(self.screen ,BLACK ,(0,y), (screen_width, y))

    def run(self):
        #loop
        while self.runninging: 
            fpsClock.tick(FPS)
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.runninging = False
                if self.player.rect.x == self.enemyX.rect.x and self.player.rect.y == self.enemyX.rect.y :
                    newgame = looser()
                    newgame.run()
                    self.runninging = False
            self.screen.fill((background_colour))
            self.draw_grid()
            self.pmove(self.player)
            self.player.loop(FPS)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.update()