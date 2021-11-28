import pygame
from images.ui import ui
from settings import *

DARK_COLOR = (30,30,30)
fog = pygame.Surface((screen_width,screen_height))
fog.fill(DARK_COLOR)
light_mask = ui.central_light5
light_rect = light_mask.get_rect()
fog.blit(light_mask,light_rect)