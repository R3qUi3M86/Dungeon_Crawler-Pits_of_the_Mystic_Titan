import pygame
from settings import *

central_light1 = pygame.image.load("images/ui/light_source1.png").convert_alpha()
central_light2 = pygame.image.load("images/ui/light_source2.png").convert_alpha()
central_light3 = pygame.image.load("images/ui/light_source3.png").convert_alpha()
central_light4 = pygame.image.load("images/ui/light_source4.png").convert_alpha()
central_light5 = pygame.image.load("images/ui/light_source5.png").convert_alpha()
central_light6 = pygame.image.load("images/ui/light_source6.png").convert_alpha()

wall_hider_mask = pygame.image.load("images/ui/wall_hider_mask.png").convert_alpha()
wall_hider_mask2 = pygame.image.load("images/ui/wall_hider_mask2.png").convert_alpha()

health_bar_empty = pygame.image.load("images/ui/health_bar/empty_bar.png").convert_alpha()
health_bar_health = pygame.image.load("images/ui/health_bar/health.png").convert_alpha()
health_bar_health_mask = pygame.image.load("images/ui/health_bar/health_mask.png").convert_alpha()
inner_shadow = pygame.image.load("images/ui/health_bar/inner_shadow.png").convert_alpha()