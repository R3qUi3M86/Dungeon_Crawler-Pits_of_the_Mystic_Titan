import pygame

class Cursor(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        attack_cursor = pygame.image.load('images/attack_cursor.png').convert_alpha()
        self.image = attack_cursor
        self.position = position
        self.rect = self.image.get_rect(center = (position))

    def update(self):
        self.rect = self.image.get_rect(center = (pygame.mouse.get_pos()))

cursor = pygame.sprite.GroupSingle()
cursor.add(Cursor(pygame.mouse.get_pos()))