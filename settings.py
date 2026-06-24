import pygame, sys, random
pygame.init()
background_colour = (143,143,143)
screen_width = 700
screen_height = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
TEXTCOLOUR = (200, 100, 0)
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300#
font = pygame.font.Font(None, 50)
fontObj = pygame.font.SysFont('courier', 35)
surufaceObj = fontObj.render('Are you ready...', True, TEXTCOLOUR, None)
