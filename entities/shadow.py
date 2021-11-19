import pygame
from utilities import constants
from images.misc.shadow_images import *

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position, id, size, visible):
        super().__init__()

        self.visible = visible
        self.shadow_size = size
        self.position = position
        self.id = id

        self.image = self.get_self_image()
        self.rect = self.image.get_rect(center = (self.position))
        self.mask = self.get_self_mask()

    #Update functions    
    def update(self):
        self.rect = self.image.get_rect(center = (self.position))

    #Misc
    def get_self_image(self):
        if self.shadow_size == constants.SIZE_SMALL:
            if self.visible:
                return shadow_small
            else:
                return invisible_shadow_small
        
        elif self.shadow_size == constants.SIZE_MEDIUM:
            if self.visible:
                return shadow_medium
            else:
                return invisible_shadow_medium
    
    def get_self_mask(self):
        if self.shadow_size == constants.SIZE_SMALL:
            return pygame.mask.from_surface(shadow_small_mask)
        elif self.shadow_size == constants.SIZE_MEDIUM:
            return pygame.mask.from_surface(shadow_medium_mask)

