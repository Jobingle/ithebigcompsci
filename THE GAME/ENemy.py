import pygame
from settings import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from game import *

class enemyX(pygame.sprite.Sprite):
    def __init__(self, x, y,width ,height,matrix,face, player):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.grid_width = 1950 // TILESIZE
        self.grid_height = 1050 // TILESIZE
        self.sneaky = True
        self.matrix = matrix
        self.player = player
        new_size = (width,height)
        self.speed = 2
        self.xspeed = 0 
        self.yspeed = 0
        self.mask = None
        self.direction = face
        self.aggro = False
        self.animation_count = 0
        self.animation_speed = 0.1 
        self.color = WHITE
        self.animation_framesER= [pygame.transform.scale(pygame.image.load("images/enemyW1L.png").convert_alpha(), new_size),pygame.transform.scale(pygame.image.load("images/enemyW2L.png").convert_alpha(), new_size)]
        self.animation_framesEL = [pygame.transform.scale(pygame.image.load("images/enemyW1R.png").convert_alpha(), new_size),pygame.transform.scale(pygame.image.load("images/enemyW2R.png").convert_alpha(), new_size)]
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


    def movetoplayer(self, player, enemyX):
        mapX = self.grid_width
        mapY = self.grid_height
        matrix = self.matrix
        grid = Grid(matrix=matrix)
        start_x = self.rect.x // TILESIZE
        start_y = self.rect.y // TILESIZE
        end_x = self.player.rect.x // TILESIZE
        end_y = self.player.rect.y // TILESIZE
        start_x =max(0, min(start_x, mapX - 1))
        start_y = max(0, min(start_y, mapY - 1))
        end_x = max(0, min(end_x, mapX - 1))
        end_y = max(0, min(end_y, mapY - 1))
        start = grid.node(start_x, start_y)
        end = grid.node(end_x, end_y)
        finder = AStarFinder()
        path, runs = finder.find_path(start, end, grid)
        if len(path) > 1:
            next_node = path[1]
            self.xspeed = 0
            self.yspeed = 0
            #gracias hasattr absolute legend
            if hasattr(next_node, 'x'):
                nx, ny = next_node.x, next_node.y
            else:
                nx, ny = next_node[0], next_node[1]
            if (nx, ny) == (start_x + 1, start_y):
                self.moveXR(self.speed)
            elif (nx, ny) == (start_x - 1, start_y):
                self.moveXL(self.speed)
            elif (nx, ny) == (start_x, start_y + 1):
                self.moveD(self.speed)
            elif (nx, ny) == (start_x, start_y - 1):
                self.moveU(self.speed)
            self.move(self.xspeed, self.yspeed)

    def loop(self, fps):
        self.Lmove = (self.rect.x,self.rect.y)
        self.move(self.xspeed,self.yspeed)
