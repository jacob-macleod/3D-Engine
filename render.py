# Render scene
import pygame
from maths import *

distance_between_screen_and_camera = 10

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for j in range(0, 10) :
        i = 10-j
        x = find_point(100, 50, 10*j)
        y = find_point(100, 60, 10*j)
    pygame.display.update()
