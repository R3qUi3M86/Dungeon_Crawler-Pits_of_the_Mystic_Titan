import pygame
from utilities import constants

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position, id, size):
        super().__init__()
        shadow_small = pygame.image.load("images/characters/character_shadow_small.png").convert_alpha()
        shadow_small_mask = pygame.image.load("images/characters/character_shadow_mask_small.png").convert_alpha()
        shadow_medium = pygame.image.load("images/characters/character_shadow_medium.png").convert_alpha()
        shadow_medium_mask = pygame.image.load("images/characters/character_shadow_mask_medium.png").convert_alpha()

        self.shadow_size = size
        self.sprite_position = position
        self.id = id

        if size == constants.SIZE_SMALL:
            self.image = shadow_small
            self.mask = pygame.mask.from_surface(shadow_small_mask)
        elif size == constants.SIZE_MEDIUM:
            self.image = shadow_medium
            self.mask = pygame.mask.from_surface(shadow_medium_mask)
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        
    
    def update(self):
        if self.shadow_size == constants.SIZE_SMALL:
            self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        elif self.shadow_size == constants.SIZE_MEDIUM:
            medium_shadow_sprite_position = self.get_shadow_position()
            self.rect = self.image.get_rect(midbottom = (medium_shadow_sprite_position))

    def get_shadow_position(self):
        medium_shadow_sprite_position = self.sprite_position[0], self.sprite_position[1]+7
        return medium_shadow_sprite_position

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0] - vector[0], self.sprite_position[1] - vector[1]