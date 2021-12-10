import pygame
from utilities.constants import *
from utilities import entity_manager
from images.misc.shadow_images import *

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position, map_position, id, size, tile_index=None, glow=None):
        super().__init__()
        self.TYPE = SHADOW
        self.shadow_size = size
        self.position = position
        self.map_position = map_position
        self.id = id
        self.tile_index=tile_index
        self.glow = glow

        self.image = self.get_image()
        self.rect = self.image.get_rect(center = (self.position))
        self.mask = pygame.mask.from_surface(self.image)

    #Update functions    
    def update_position(self,position):
        self.position = position
        self.rect = self.image.get_rect(center = (self.position))

    #Image getters
    def get_image(self):
        if not self.glow:
            if self.shadow_size == SIZE_TINY:
                return shadow_tiny
            elif self.shadow_size == SIZE_SMALL:
                return shadow_small
            elif self.shadow_size == SIZE_MEDIUM:
                return shadow_medium
            elif self.shadow_size == SIZE_LARGE:
                return shadow_large

        elif self.glow == RED_GLOW:
            if self.shadow_size == SIZE_TINY:
                return shadow_tiny_red
            elif self.shadow_size == SIZE_SMALL:
                return shadow_small_red
            elif self.shadow_size == SIZE_MEDIUM:
                return shadow_medium_red
            elif self.shadow_size == SIZE_LARGE:
                return shadow_large_red

        elif self.glow == GREEN_GLOW:
            if self.shadow_size == SIZE_TINY:
                return shadow_tiny_green
            elif self.shadow_size == SIZE_SMALL:
                return shadow_small_green
            elif self.shadow_size == SIZE_MEDIUM:
                return shadow_medium_green
            elif self.shadow_size == SIZE_LARGE:
                return shadow_large_green

        elif self.glow == BLUE_GLOW:
            if self.shadow_size == SIZE_TINY:
                return shadow_tiny_blue
            elif self.shadow_size == SIZE_SMALL:
                return shadow_small_blue
            elif self.shadow_size == SIZE_MEDIUM:
                return shadow_medium_blue
            elif self.shadow_size == SIZE_LARGE:
                return shadow_large_blue


