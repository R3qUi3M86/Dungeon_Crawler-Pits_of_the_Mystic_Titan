import pygame
from images.misc.cursors import *

class Cursor(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = attack_cursor
        self.position = position
        self.rect = self.image.get_rect(center = (position))

    def update(self):
        self.rect = self.image.get_rect(center = (pygame.mouse.get_pos()))

cursor = pygame.sprite.GroupSingle()
cursor.add(Cursor(pygame.mouse.get_pos()))