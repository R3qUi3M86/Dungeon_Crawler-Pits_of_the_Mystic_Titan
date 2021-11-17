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

        self.image = self.get_self_image()
        self.mask = self.get_self_mask()
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

    #Update functions    
    def update(self):
        if self.shadow_size == constants.SIZE_SMALL:
            self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        elif self.shadow_size == constants.SIZE_MEDIUM_SMALL:
            medium_shadow_sprite_position = self.get_shadow_position()
            self.rect = self.image.get_rect(midbottom = (medium_shadow_sprite_position))
        elif self.shadow_size == constants.SIZE_MEDIUM:
            medium_shadow_sprite_position = self.get_shadow_position()
            self.rect = self.image.get_rect(midbottom = (medium_shadow_sprite_position))

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0] - vector[0], self.sprite_position[1] - vector[1]

    def get_shadow_position(self):
        medium_shadow_sprite_position = self.sprite_position[0], self.sprite_position[1]+7
        return medium_shadow_sprite_position

    #Misc
    def get_self_image(self):
        if self.shadow_size == constants.SIZE_SMALL:
            if self.visible:
                return shadow_small
            else:
                return invisible_shadow_small
        
        elif self.shadow_size == constants.SIZE_MEDIUM_SMALL or self.shadow_size == constants.SIZE_MEDIUM:
            if self.visible:
                return shadow_medium
            else:
                return invisible_shadow_small
    
    def get_self_mask(self):
        if self.shadow_size == constants.SIZE_SMALL or self.shadow_size == constants.SIZE_MEDIUM_SMALL:
            return pygame.mask.from_surface(shadow_small_mask)
        elif self.shadow_size == constants.SIZE_MEDIUM:
            return pygame.mask.from_surface(shadow_medium_mask)

