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
        x = (-find_point(distance_between_screen_and_camera, 1, 5, 200+(100*i)))*1000
        y = (-find_point(distance_between_screen_and_camera, 170, 5, 200+(100*i)))*1000
        pygame.draw.rect(gameDisplay, (255/i,20*i,0), (x,y,20,20))
    pygame.display.update()
