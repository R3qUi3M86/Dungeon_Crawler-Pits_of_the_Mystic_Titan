import pygame
import random
from entities.level.level import *
from images.level.cave_images import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,type,pos,size,vicinity_matrix):
        super().__init__()
        self.type = type
        self.position = pos
        self.size = size
        self.vicinity_matrix = vicinity_matrix
        self.passable = self.get_passable()
        
        self.image_surface_unscaled = self.get_tile_image()
        self.image = pygame.transform.scale(self.image_surface_unscaled, size)
        self.rect = self.image.get_rect(center = (self.position))

    def update_position(self, vector):
        self.position = self.position[0] - vector[0], self.position[1] - vector[1]
        self.rect = self.image.get_rect(center = (self.position))

    def get_tile_image(self):
        if self.type == FLOOR:
            if self.vicinity_matrix[0][1] != ENTRANCE:
                return random.choice(floor_tile_images)
            else:
                if self.vicinity_matrix[0][0] != ENTRANCE:
                    return floor_tile_entrance_images[0]
                elif self.vicinity_matrix[0][2] != ENTRANCE:
                    return floor_tile_entrance_images[2]
                else:
                    return floor_tile_entrance_images[1]
        
        else:
            return blank


    def get_passable(self):
        if self.type in IMPASSABLE_TILES:
            return False
        return True

# LEVEL_EXIT = "N"
# WALL = "X"
# WATER = "~"
# FLOOR = " "
# FLOOR_PIT = "O"
# SIMPLE_CRACK = "*"
# CORNER_CRACK = "`"