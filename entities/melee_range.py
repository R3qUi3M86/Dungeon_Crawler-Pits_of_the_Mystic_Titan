import pygame
from settings import *
from utilities.constants import *
from images.misc.melee_images import *

class Melee(pygame.sprite.Sprite):
    def __init__(self, position, sector):
        super().__init__()
        self.position = position
        self.sector = sector
        self.image = self.get_sector_image()
        self.rect = self.image.get_rect(center = (self.position))
        self.mask = pygame.mask.from_surface(self.image)

    #Update functions
    def update(self):
        self.rect = self.image.get_rect(center = (self.position))

    def update_position(self,position):
        self.position = position
        self.rect = self.image.get_rect(center = (self.position))

    #Misc
    def get_sector_image(self):
        if self.sector == SECTOR_E:
            return melee_mask_e
        elif self.sector == SECTOR_NE:
            return melee_mask_ne
        elif self.sector == SECTOR_N:
            return melee_mask_n
        elif self.sector == SECTOR_NW:
            return melee_mask_nw
        elif self.sector == SECTOR_W:
            return melee_mask_w
        elif self.sector == SECTOR_SW:
            return melee_mask_sw
        elif self.sector == SECTOR_S:
            return melee_mask_s
        elif self.sector == SECTOR_SE:
            return melee_mask_se