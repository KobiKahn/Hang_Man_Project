import pygame, sys
import random
pygame.init()




SCREEN_W = 700
SCREEN_H = 800
FPS = 60
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


