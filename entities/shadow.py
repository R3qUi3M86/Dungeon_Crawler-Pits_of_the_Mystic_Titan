from typing import NewType
import pygame
from utilities.constants import *
from images.misc.shadow_images import *
from images.misc.player_collision_mask_images import *

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position, id, size, mask=False, sector=None):
        super().__init__()

        self.mask = mask
        self.sector = sector
        self.shadow_size = size
        self.position = position
        self.id = id

        if mask:
            self.image = self.get_mask_image()
        else:
            self.image = self.get_normal_image()

        self.rect = self.image.get_rect(center = (self.position))
        self.mask = pygame.mask.from_surface(self.get_mask_image())

    #Update functions    
    def update_position(self,position):
        self.position = position
        self.rect = self.image.get_rect(center = (self.position))

    #Image getters
    def get_normal_image(self):
        if self.shadow_size == SIZE_SMALL:
            return shadow_small
        elif self.shadow_size == SIZE_MEDIUM:
            return shadow_medium
    
    def get_mask_image(self):
        if self.sector == None:
            if self.shadow_size == SIZE_SMALL:
                return collision_small_mask
            elif self.shadow_size == SIZE_MEDIUM:
                return collision_medium_mask
        
        else:
            if self.shadow_size == SIZE_SMALL:
                if self.sector == SECTOR_NW:
                    return collision_small_sector_nw
                elif self.sector == SECTOR_NE:
                    return collision_small_sector_ne
                elif self.sector == SECTOR_SW:
                    return collision_small_sector_sw
                elif self.sector == SECTOR_SE:
                    return collision_small_sector_se

