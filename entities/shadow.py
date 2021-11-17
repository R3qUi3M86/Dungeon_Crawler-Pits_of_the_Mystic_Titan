import pygame
from utilities import constants
from images.misc.shadow_images import *

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position, id, size, visible):
        super().__init__()

        self.visible = visible
        self.shadow_size = size
        self.sprite_position = position
        self.id = id

        if size == constants.SIZE_SMALL:
            if visible:
                self.image = shadow_small
            else:
                self.image = invisible_shadow_small
            self.mask = pygame.mask.from_surface(shadow_small_mask)
        elif size == constants.SIZE_MEDIUM_SMALL:
            if visible:
                self.image = shadow_medium
            else:
                self.image = invisible_shadow_small
            self.mask = pygame.mask.from_surface(shadow_small_mask)
        elif size == constants.SIZE_MEDIUM:
            if visible:
                self.image = shadow_medium
            else:
                self.image = invisible_shadow_medium
            self.mask = pygame.mask.from_surface(shadow_medium_mask)
        
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        
    def update(self):
        if self.shadow_size == constants.SIZE_SMALL:
            self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        elif self.shadow_size == constants.SIZE_MEDIUM_SMALL:
            medium_shadow_sprite_position = self.get_shadow_position()
            self.rect = self.image.get_rect(midbottom = (medium_shadow_sprite_position))
        elif self.shadow_size == constants.SIZE_MEDIUM:
            medium_shadow_sprite_position = self.get_shadow_position()
            self.rect = self.image.get_rect(midbottom = (medium_shadow_sprite_position))

    def get_shadow_position(self):
        medium_shadow_sprite_position = self.sprite_position[0], self.sprite_position[1]+7
        return medium_shadow_sprite_position

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0] - vector[0], self.sprite_position[1] - vector[1]