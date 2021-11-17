import pygame
from settings import *
from utilities import game_manager
from utilities.constants import *

class Melee(pygame.sprite.Sprite):
    def __init__(self, position, sector):
        super().__init__()
        melee = pygame.image.load("images/characters/melee_range_sector_visible.png").convert_alpha()
        melee_mask = pygame.image.load("images/characters/melee_range_sector_mask.png").convert_alpha()


        self.sector = sector
        self.sprite_position = position
        self.sector_position = self.get_sector_position(self.sector)
        self.image = melee
        self.rect = self.image.get_rect(midbottom = (self.sector_position))
        self.mask = pygame.mask.from_surface(melee_mask)

    def update(self):
        self.sector_position = self.get_sector_position(self.sector)
        self.rect = self.image.get_rect(midbottom = (self.sector_position))

    def get_sector_position(self,sector):
        if sector == SECTOR_E:
            return self.sprite_position[0]+30,self.sprite_position[1]
        elif sector == SECTOR_NE:
            return self.sprite_position[0]+20,self.sprite_position[1]-13
        elif sector == SECTOR_N:
            return self.sprite_position[0],self.sprite_position[1]-20
        elif sector == SECTOR_NW:
            return self.sprite_position[0]-20,self.sprite_position[1]-13
        elif sector == SECTOR_W:
            return self.sprite_position[0]-30,self.sprite_position[1]
        elif sector == SECTOR_SW:
            return self.sprite_position[0]-20,self.sprite_position[1]+13
        elif sector == SECTOR_S:
            return self.sprite_position[0],self.sprite_position[1]+20
        elif sector == SECTOR_SE:
            return self.sprite_position[0]+20,self.sprite_position[1]+13

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0] - vector[0], self.sprite_position[1] - vector[1]