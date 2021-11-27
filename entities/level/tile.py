import pygame
import random
from entities.level.level import *
from images.level.cave_images import *
from images.misc.colliders import *
from utilities.constants import *
from utilities import level_painter
from utilities import entity_manager

class Tile(pygame.sprite.Sprite):
    def __init__(self,type,tile_index,pos,size,vicinity_matrix):
        super().__init__()
        self.TYPE = type
        self.tile_index = tile_index
        self.position = pos
        self.map_position = int(self.tile_index[1] * level_painter.TILE_SIZE[1]+level_painter.TILE_SIZE[1]//2+screen_width//2), int(self.tile_index[0] * level_painter.TILE_SIZE[0]+level_painter.TILE_SIZE[0]//2 + screen_height//2)
        self.size = size
        self.vicinity_matrix = vicinity_matrix
        self.passable = self.get_passable()
        
        self.image_surface_unscaled = self.get_tile_image()
        self.image = pygame.transform.scale(self.image_surface_unscaled, size)
        self.cluster_x_y = self.get_cluster_x_y()
        self.mask = self.get_tile_mask()
        self.rect = self.image.get_rect(center = (self.position))

    def update_position(self):
        self.position = self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0], self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1]
        self.rect = self.image.get_rect(center = (self.position))

    def get_tile_image(self):
        if self.TYPE == FLOOR:
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
        elif self.TYPE == WATER:
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
        elif self.image_surface_unscaled in blue_water_border_convex_images[0] or self.image_surface_unscaled in blue_water_border_convex_images[1]:
            return pygame.mask.from_surface(blue_water_border_convex_colliders[self.cluster_x_y[0]][self.cluster_x_y[1]])
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
        if self.vicinity_matrix[1][0] == FLOOR and self.vicinity_matrix[0][1] == FLOOR:
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

    def get_cluster_x_y(self):
        if self.image_surface_unscaled in blue_water_border_convex_images[0] or self.image_surface_unscaled in blue_water_border_convex_images[1]:
            for i in range(2):
                for j in range(2):
                    if blue_water_border_convex_images[i][j] == self.image_surface_unscaled:
                        return i,j


    def get_passable(self):
        if self.TYPE in IMPASSABLE_TILES:
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