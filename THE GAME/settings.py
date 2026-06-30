import pygame, sys, random
pygame.init()
#colour
background_colour = (143,143,143)
screen_width = 700
screen_height = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
TEXTCOLOUR = (171,55,87)
#time
FPS = 60
fpsClock = pygame.time.Clock()
font = pygame.font.Font(None, 100)
#startscreen
fontObjfirst = pygame.font.SysFont('impact', 100)
fontObjsecond = pygame.font.SysFont('impact', 50)
startscreentext1 = fontObjfirst.render('Are you ready . . .', True, TEXTCOLOUR, None)
startscreentext2 = fontObjsecond.render('press enter to start mission', True, TEXTCOLOUR, None)
bootupimage = pygame.image.load('startscreen.png')
#sizes
scX = (1950)
scY = (1050)