import pygame
import random
from entities.level.level import *
from images.level.cave_images import *
from images.misc.colliders import *
from utilities.constants import *
from utilities import level_painter

class Tile(pygame.sprite.Sprite):
    def __init__(self,type,tile_index,pos,size,vicinity_matrix):
        super().__init__()
        self.type = type
        self.TYPE = TILE
        self.tile_index = tile_index
        self.position = pos
        self.map_position = round(self.tile_index[1] * level_painter.TILE_SIZE[1]+level_painter.TILE_SIZE[1]//2), round(self.tile_index[0] * level_painter.TILE_SIZE[0]+level_painter.TILE_SIZE[0]//2,2)
        self.size = size
        self.vicinity_matrix = vicinity_matrix
        self.passable = self.get_passable()
        
        self.image_surface_unscaled = self.get_tile_image()
        self.image = pygame.transform.scale(self.image_surface_unscaled, size)
        self.mask = self.get_tile_mask()
        self.rect = self.image.get_rect(center = (self.position))

    def update_position(self, vector):
        self.position = round(self.position[0] - vector[0],2), round(self.position[1] - vector[1],2)
        self.rect = self.image.get_rect(center = (self.position))

    def get_tile_image(self):
        if self.type == FLOOR:
            if self.vicinity_matrix[0][1] != ENTRANCE:
                if random.choice(range(20)) > 1:
                    return random.choice(floor_tile_images)
                else:
                    return random.choice(debree_tile_images)
            else:
                if self.vicinity_matrix[0][0] != ENTRANCE:
                    return floor_tile_entrance_images[0]
                elif self.vicinity_matrix[0][2] != ENTRANCE:
                    return floor_tile_entrance_images[2]
                else:
                    return floor_tile_entrance_images[1]
        elif self.type == WATER:
            if self.deep_water():
                return random.choice(blue_water_images)
            elif self.left_water_border():
                return blue_water_border_left
            elif self.water_top_left_convex():
                return blue_water_border_top_left_convex
            elif self.water_top_right_convex():
                return blue_water_border_top_right_convex
            elif self.water_bottom_left_convex():
                return blue_water_border_bottom_left_convex
            elif self.water_bottom_right_convex():
                return blue_water_border_bottom_right_convex
            else:
                return blank
        else:
            return blank

    def get_tile_mask(self):
        if self.passable == True:
            return pygame.mask.from_surface(empty_tile_image)
        else:
            return pygame.mask.from_surface(level_tile_collider)

    def deep_water(self):
        for row in self.vicinity_matrix:
            for cell in row:
                if cell != WATER:
                    return False
        return True

    def left_water_border(self):
        if self.vicinity_matrix[0][0] == FLOOR and self.vicinity_matrix[1][0] == FLOOR and self.vicinity_matrix[2][0] == FLOOR:
            if self.vicinity_matrix[0][1] == WATER and self.vicinity_matrix[0][2] == WATER and self.vicinity_matrix[1][2] == WATER and self.vicinity_matrix[2][1] == WATER and self.vicinity_matrix[2][2] == WATER:
                return True
        return False

    def water_top_left_convex(self):
        if self.vicinity_matrix[0][0] == FLOOR and self.vicinity_matrix[1][0] == FLOOR and self.vicinity_matrix[0][1] == FLOOR:
            if self.vicinity_matrix[1][2] == WATER and self.vicinity_matrix[2][1] == WATER:
                return True

    def water_top_right_convex(self):
        if self.vicinity_matrix[0][1] == FLOOR and self.vicinity_matrix[1][2] == FLOOR:
            if self.vicinity_matrix[1][0] == WATER and self.vicinity_matrix[2][1] == WATER:
                return True
    
    def water_bottom_right_convex(self):
        if self.vicinity_matrix[1][2] == FLOOR and self.vicinity_matrix[2][1] == FLOOR:
            if self.vicinity_matrix[0][1] == WATER and self.vicinity_matrix[1][0] == WATER:
                return True

    def water_bottom_left_convex(self):
        if self.vicinity_matrix[1][0] == FLOOR and self.vicinity_matrix[2][1] == FLOOR:
            if self.vicinity_matrix[0][1] == WATER and self.vicinity_matrix[1][2] == WATER:
                return True

    def get_passable(self):
        if self.type in IMPASSABLE_TILES:
            return False
        return True

    def get_index(self):
        return self.tile_index

# LEVEL_EXIT = "N"
# WALL = "X"
# WATER = "~"
# FLOOR = " "
# FLOOR_PIT = "O"
# SIMPLE_CRACK = "*"
# CORNER_CRACK = "`"