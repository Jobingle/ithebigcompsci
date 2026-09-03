import pygame
from settings import *
from LOSE import *
from ENemy import enemyX
from win import *
import math
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

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
mapx = 1950
mapy = 1050
#ergyblergyblerggg

class Gameygamerson:
    def __init__(self):
        self.screen = pygame.display.set_mode((1950,1050))
        pygame.display.set_caption('Seth the Spy')
        self.runninging = True
        self.player = Player(50,50,100,100)
        self.enemyX = enemyX(500, 500 , 100 , 100, "U")
        self.enemyX2 = enemyX(750, 750 , 100 , 100, "D")
        self.enemyX3 = enemyX(1000, 1000 , 100 , 100, "L")
        self.enemyX4 = enemyX(250, 250 , 100 , 100, "R")
        self.door = theD_O_R_E(1000, 650 , 100 , 100)
        self.walls = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemyX)
        self.all_sprites.add(self.door)
        self.grid_width = 1950 // TILESIZE
        self.grid_height = 1050 // TILESIZE

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
        self.movetoplayer(self.player, enemyX)

    def movetoplayer(self, player, enemyX):
        mapX = self.grid_width
        mapY = self.grid_height
        matrix = [[1 for _ in range(mapX)] for _ in range(mapY)]
        grid = Grid(matrix=matrix)
        start_x = enemyX.rect.x // TILESIZE
        start_y = enemyX.rect.y // TILESIZE
        end_x = player.rect.x // TILESIZE
        end_y = player.rect.y // TILESIZE
        start_x = max(0, min(start_x, mapX - 1))
        start_y = max(0, min(start_y, mapY - 1))
        end_x = max(0, min(end_x, mapX - 1))
        end_y = max(0, min(end_y, mapY - 1))
        start = grid.node(start_x, start_y)
        end = grid.node(end_x, end_y)
        finder = AStarFinder()
        path, runs = finder.find_path(start, end, grid)
        if len(path) > 1:
            next_node = path[1]
            enemyX.xspeed = 0
            enemyX.yspeed = 0
#gracias hasattr absolute legend
            if hasattr(next_node, 'x'):
                nx, ny = next_node.x, next_node.y
            else:
                nx, ny = next_node[0], next_node[1]
            if (nx, ny) == (start_x + 1, start_y):
                enemyX.moveXR(enemyX.speed)
            elif (nx, ny) == (start_x - 1, start_y):
                enemyX.moveXL(enemyX.speed)
            elif (nx, ny) == (start_x, start_y + 1):
                enemyX.moveD(enemyX.speed)
            elif (nx, ny) == (start_x, start_y - 1):
                enemyX.moveU(enemyX.speed)
            enemyX.move(enemyX.xspeed, enemyX.yspeed)

    def draw_grid(self):
        for x in range(0,screen_width,TILESIZE):
            pygame.draw.line(self.screen ,BLACK ,(x,0), (x, screen_height))
        for y in range(0,screen_height,TILESIZE):
            pygame.draw.line(self.screen ,BLACK ,(0,y), (screen_width, y))

    def run(self):
        while self.runninging: 
            fpsClock.tick(FPS)
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.runninging = False

            self.screen.fill((background_colour))
            self.draw_grid()

            self.pmove(self.player)
            self.player.loop(FPS)

            self.Emove(self.enemyX)
            self.enemyX.loop(FPS)

            if self.player.rect.colliderect(self.enemyX.rect):
                newgame = looser()
                newgame.play()
                self.runninging = False

            if self.player.rect.colliderect(self.enemyX2.rect):
                newgame = looser()
                newgame.play()
                self.runninging = False

            if self.player.rect.colliderect(self.enemyX3.rect):
                newgame = looser()
                newgame.play()
                self.runninging = False

            if self.player.rect.colliderect(self.enemyX4.rect):
                newgame = looser()
                newgame.play()
                self.runninging = False

            if self.player.rect.colliderect(self.door.rect):
                newgame = winscr()
                newgame.play()
                self.runninging = False

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.update()