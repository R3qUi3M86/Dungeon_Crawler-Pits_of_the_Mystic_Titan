import pygame
from settings import *
from sys import exit
from entities import player
from entities import level


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill([25, 23, 22])
    #screen.blit(level.test_surface_scaled,(-800,0))
    player.hero.draw(screen)
    player.hero.update()
    
    pygame.display.update()
    clock.tick(60)