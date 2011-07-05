import pygame, random, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Mechi Pygame & Eclipse')

# set up colors
WHITE = (255, 255, 255)
BLUE = (5, 5, 255)

# set up fonts
basicFont = pygame.font.SysFont("Corpse", 48)

# set up the text
text = basicFont.render('Isaac Mechi', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

windowSurface.blit(text, textRect)

pygame.display.update()