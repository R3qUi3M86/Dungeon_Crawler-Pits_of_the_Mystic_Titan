import pygame

class Shadow(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        shadow = pygame.image.load("images/characters/character_shadow.png").convert_alpha()

        self.image = shadow
        self.rect = self.image.get_rect(center = (position))