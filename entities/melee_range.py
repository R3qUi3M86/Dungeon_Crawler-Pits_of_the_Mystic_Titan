import pygame
from settings import *

class Melee(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        melee = pygame.image.load("images/characters/melee_range_sector_visible.png").convert_alpha()

        self.image = melee
        self.rect = self.image.get_rect(center = (position))