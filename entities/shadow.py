from typing import NewType
import pygame
from utilities.constants import *
from images.misc.shadow_images import *
from images.misc.player_collision_mask_images import *

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position, id, size, visible, sector=None):
        super().__init__()

        self.visible = visible
        self.sector = sector
        self.shadow_size = size
        self.position = position
        self.id = id

        self.image = self.get_self_image()
        self.rect = self.image.get_rect(center = (self.position))
        self.mask = self.get_self_mask()

    #Update functions    
    def update(self):
        self.rect = self.image.get_rect(center = (self.position))

    def update_position(self,vector):
        self.position = self.position[0] - vector[0], self.position[1] - vector[1]
        self.rect = self.image.get_rect(center = (self.position))

    #Misc
    def get_self_image(self):
        if self.shadow_size == SIZE_SMALL:
            if self.visible:
                return shadow_small
            else:
                return invisible_shadow_small
        
        elif self.shadow_size == SIZE_MEDIUM:
            if self.visible:
                return shadow_medium
            else:
                return invisible_shadow_medium
    
    def get_self_mask(self):
        if self.sector == None:
            if self.shadow_size == SIZE_SMALL:
                return pygame.mask.from_surface(shadow_small_mask)
            elif self.shadow_size == SIZE_MEDIUM:
                return pygame.mask.from_surface(shadow_medium_mask)
        
        elif self.sector == SECTOR_NW:
            return pygame.mask.from_surface(collision_sector_nw)
        elif self.sector == SECTOR_NE:
            return pygame.mask.from_surface(collision_sector_ne)
        elif self.sector == SECTOR_SW:
            return pygame.mask.from_surface(collision_sector_sw)
        elif self.sector == SECTOR_SE:
            return pygame.mask.from_surface(collision_sector_se)

