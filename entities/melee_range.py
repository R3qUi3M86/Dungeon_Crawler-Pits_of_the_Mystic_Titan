import pygame
from settings import *
from utilities.constants import *
from images.misc.melee_images import *

class Melee(pygame.sprite.Sprite):
    def __init__(self, position, sector):
        super().__init__()
        self.sector = sector
        self.sprite_position = position
        self.sector_position = self.get_sector_position(self.sector)
        self.image = melee
        self.rect = self.image.get_rect(midbottom = (self.sector_position))
        self.mask = pygame.mask.from_surface(melee_mask)

    #Update functions
    def update(self):
        self.sector_position = self.get_sector_position(self.sector)
        self.rect = self.image.get_rect(midbottom = (self.sector_position))

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0] - vector[0], self.sprite_position[1] - vector[1]

    #Misc
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