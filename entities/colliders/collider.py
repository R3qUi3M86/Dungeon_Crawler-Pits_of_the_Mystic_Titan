import pygame
from utilities.constants import *
from images.misc.colliders import *
from utilities import entity_manager

class Collider(pygame.sprite.Sprite):
    def __init__(self, map_position, id, type, sector=None, size=SIZE_SMALL, image=None):
        super().__init__()
        self.map_position = map_position
        self.position = None
        self.id = id
        self.sector = sector
        self.size = size
        self.TYPE = type

        if image == None:
            self.image = self.get_image()
        else:
            self.image = image

        self.rect = self.image.get_rect(center = (self.map_position))
        #self.screen_rect = self.image.get_rect(center = (self.map_position))
        self.mask = pygame.mask.from_surface(self.image)

    #Update functions
    # def update_position(self,position): #Old method not used
    #     self.position = position
    #     self.rect.center = self.position

    def update_position(self, map_pos):
        self.map_position = map_pos
        self.rect.center = map_pos
        #self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        #self.screen_rect = self.image.get_rect(center = (self.position))

    #Misc
    def get_image(self):
        if self.TYPE == ENTITY_OMNI:
            if self.size == SIZE_TINY:
                return entity_collider_tiny
            elif self.size == SIZE_SMALL:
                return entity_collider_small
            elif self.size == SIZE_MEDIUM:
                return entity_collider_medium
        
        elif self.TYPE == ENTITY_SECTOR:
            if self.size == SIZE_SMALL:
                if self.sector == SECTOR_NW:
                    return entity_collider_sector_nw
                elif self.sector == SECTOR_NE:
                    return entity_collider_sector_ne
                elif self.sector == SECTOR_SW:
                    return entity_collider_sector_sw
                elif self.sector == SECTOR_SE:
                    return entity_collider_sector_se

        elif self.TYPE == SQUARE:
            if self.size == SIZE_SMALL:
                return small_square_collider
            elif self.size == SIZE_MEDIUM:
                return medium_square_collider

        elif self.TYPE == WALL_HIDER1:
            return wall_hider_coolider_primary

        elif self.TYPE == WALL_HIDER2:
            return wall_hider_coolider_secondary

        elif self.TYPE == WALL_HIDER3:
            return wall_hider_coolider_tertiary

        elif self.TYPE == PROJECTILE:
            return projectile_collider
