import pygame
from settings import *

class Melee(pygame.sprite.Sprite):
    def __init__(self, position, sector_position):
        super().__init__()
        melee = pygame.image.load("images/characters/melee_range_sector_visible.png").convert_alpha()
        melee_mask = pygame.image.load("images/characters/melee_range_sector_mask.png").convert_alpha()

        self.sprite_position = position
        self.sector_position = sector_position
        self.image = melee
        self.rect = self.image.get_rect(center = (self.sector_position))
        self.mask = pygame.mask.from_surface(melee_mask)

    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.sector_position))

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0] - vector[0], self.sprite_position[1] - vector[1]
        self.sector_position = self.sector_position[0] - vector[0], self.sector_position[1] - vector[1]