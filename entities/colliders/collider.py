import pygame
from utilities.constants import *
from images.misc.colliders import *

class Collider(pygame.sprite.Sprite):
    def __init__(self, position, id, type, sector=None, size=SIZE_SMALL):
        super().__init__()
        self.position = position
        self.id = id
        self.sector = sector
        self.size = size
        self.type = type

        self.image = self.get_image()
        self.rect = self.image.get_rect(center = (self.position))
        self.mask = pygame.mask.from_surface(self.image)

    #Update functions
    def update_position(self,position):
        self.position = position
        self.rect = self.image.get_rect(center = (self.position))

    #Misc
    def get_image(self):
        if self.type == ENTITY_OMNI:
            if self.size == SIZE_SMALL:
                return entity_collider_small
            elif self.size == SIZE_MEDIUM:
                return entity_collider_medium
        
        elif self.type == ENTITY_SECTOR:
            if self.size == SIZE_SMALL:
                if self.sector == SECTOR_NW:
                    return entity_collider_sector_nw
                elif self.sector == SECTOR_NE:
                    return entity_collider_sector_ne
                elif self.sector == SECTOR_SW:
                    return entity_collider_sector_sw
                elif self.sector == SECTOR_SE:
                    return entity_collider_sector_se

        elif self.type == SQUARE:
            if self.size == SIZE_SMALL:
                return small_square_collider
            elif self.size == SIZE_MEDIUM:
                return medium_square_collider

        elif self.type == WALL_HIDER:
            return wall_hider_coolider

        elif self.type == CROSSBOW_BOLT:
            return bolt_collider

