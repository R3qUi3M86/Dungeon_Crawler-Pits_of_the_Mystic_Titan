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

        self.is_convex = False

    def update_position(self):
        self.position = self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0], self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1]
        self.rect = self.image.get_rect(center = (self.position))

    def get_tile_image(self):
        if self.TYPE in PASSABLE_TILES:
            
            if self.TYPE == FLOOR:
                if self.vicinity_matrix[0][1] != ENTRANCE:
                    if random.choice(range(10)) > 0:
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
            
            elif self.TYPE is SIMPLE_CRACK:
                return random.choice(simple_crack_images)

            elif self.TYPE is CORNER_CRACK:
                if self.top_left_corner_crack():
                    return corner_crack_images[0][0]
                elif self.top_right_corner_crack():
                    return corner_crack_images[0][1]
                elif self.bottom_left_corner_crack():
                    return corner_crack_images[1][0]
                elif self.bottom_right_corner_crack():
                    return corner_crack_images[1][1]
        
        elif self.TYPE in IMPASSABLE_TILES:
            
            if self.TYPE is FLOOR_PIT:
                return random.choice(pit_tile_images)
            
            elif self.TYPE is WATER:
                if self.deep_water():
                    return random.choice(blue_water_images)
                elif self.water_under_wall():
                    if self.water_under_wall_middle():
                        return random.choice(blue_water_under_wall_images)
                    elif self.water_under_wall_left():
                        return blue_water_under_wall_left
                    elif self.water_under_wall_right():
                        return blue_water_under_wall_right
                elif self.left_water_border():
                    return blue_water_border_left
                elif self.right_water_border():
                    return blue_water_border_right
                elif self.top_water_border():
                    return random.choice(blue_water_border_top_images)
                elif self.bottom_water_border():
                    return random.choice(blue_water_border_bottom_images)
                elif self.water_top_left_convex():
                    self.is_convex = True
                    return blue_water_border_top_left_convex
                elif self.water_top_right_convex():
                    self.is_convex = True
                    return blue_water_border_top_right_convex
                elif self.water_bottom_left_convex():
                    self.is_convex = True
                    return blue_water_border_bottom_left_convex
                elif self.water_bottom_right_convex():
                    self.is_convex = True
                    return blue_water_border_bottom_right_convex
                elif self.water_top_left_concave():
                    return blue_water_border_top_left_concave
                elif self.water_top_right_concave():
                    return blue_water_border_top_right_concave
                elif self.water_bottom_left_concave():
                    return blue_water_border_bottom_left_concave
                elif self.water_bottom_right_concave():
                    return blue_water_border_bottom_right_concave
                else:
                    return blank
            
            elif self.TYPE is WALL:
                if self.wall_bottom_lower_wall_section():
                    return self.get_bottom_lower_wall_section_image()
                elif self.wall_bottom_middle_wall_section():
                    return self.get_bottom_middle_wall_section_image()
                elif self.wall_bottom_upper_wall_section():
                    return self.get_bottom_upper_wall_section_image()
            else:
                return blank

    def get_tile_mask(self):
        if self.passable == True:
            return pygame.mask.from_surface(empty_tile_image)
        else:
            if self.TYPE in IMPASSABLE_TILES:
                if self.TYPE is FLOOR_PIT:
                    return pygame.mask.from_surface(floor_pit_collider)
                if self.TYPE is WATER:
                    if self.image_surface_unscaled is blue_water_border_right:
                        return pygame.mask.from_surface(blue_water_border_right_collider)
                    elif self.image_surface_unscaled is blue_water_border_left:
                        return pygame.mask.from_surface(blue_water_border_left_collider)
                    elif self.image_surface_unscaled in blue_water_border_top_images:
                        return pygame.mask.from_surface(blue_water_border_top_collider)
                    elif self.image_surface_unscaled in blue_water_border_bottom_images:
                        return pygame.mask.from_surface(blue_water_border_bottom_collider)
                    elif self.image_surface_unscaled in blue_water_border_convex_images[0] or self.image_surface_unscaled in blue_water_border_convex_images[1]:
                        return pygame.mask.from_surface(blue_water_border_convex_colliders[self.cluster_x_y[0]][self.cluster_x_y[1]])
                    elif self.image_surface_unscaled in blue_water_border_concave_images[0] or self.image_surface_unscaled in blue_water_border_concave_images[1]:
                        return pygame.mask.from_surface(blue_water_border_concave_colliders[self.cluster_x_y[0]][self.cluster_x_y[1]])
                else:         
                    return pygame.mask.from_surface(level_tile_collider)

    ######################
    ##### CONDITIONS #####
    ######################
    ### Corner cracks
    def top_left_corner_crack(self):
        if self.vicinity_matrix[1][0] is not CORNER_CRACK and self.vicinity_matrix[0][1] is not CORNER_CRACK:
            return corner_crack_images[0][0]

    def top_right_corner_crack(self):
        if self.vicinity_matrix[1][2] is not CORNER_CRACK and self.vicinity_matrix[0][1] is not CORNER_CRACK:
            return corner_crack_images[0][1]
                
    def bottom_left_corner_crack(self):
        if self.vicinity_matrix[1][0] is not CORNER_CRACK and self.vicinity_matrix[2][1] is not CORNER_CRACK:
            return corner_crack_images[1][0]

    def bottom_right_corner_crack(self):
        if self.vicinity_matrix[1][2] is not CORNER_CRACK and self.vicinity_matrix[2][1] is not CORNER_CRACK:
            return corner_crack_images[1][1]

    ### Water tiles
    def deep_water(self):
        for row in self.vicinity_matrix:
            for cell in row:
                if cell not in IMPASSABLE_TILES:
                    return False
        if self.vicinity_matrix[0][1] is WALL:
            return False
        return True

    def water_under_wall(self):
        for row in self.vicinity_matrix:
            for cell in row:
                if cell not in IMPASSABLE_TILES:
                    return False
        if self.vicinity_matrix[0][1] is WALL:
            return True
        return False

    def water_under_wall_middle(self):
        if self.vicinity_matrix[0][0] is WALL and self.vicinity_matrix[0][1] is WALL and self.vicinity_matrix[0][2] is WALL:
            return True
        return False

    def water_under_wall_left(self):
        if self.vicinity_matrix[0][0] is WATER:
            return True
        return False
    
    def water_under_wall_right(self):
        if self.vicinity_matrix[0][2] is WATER:
            return True
        return False

    def left_water_border(self):
        if self.vicinity_matrix[1][0] in PASSABLE_TILES:
            if self.vicinity_matrix[0][1] == WATER and self.vicinity_matrix[2][1] == WATER:
                return True
        return False

    def right_water_border(self):
        if self.vicinity_matrix[1][2] in PASSABLE_TILES:
            if self.vicinity_matrix[0][1] == WATER and self.vicinity_matrix[2][1] == WATER:
                return True
        return False
    
    def top_water_border(self):
        if self.vicinity_matrix[0][1] in PASSABLE_TILES:
            if (self.vicinity_matrix[1][0] == WATER or self.vicinity_matrix[1][0] == WALL) and (self.vicinity_matrix[1][2] == WATER or self.vicinity_matrix[1][2] == WALL):
                return True
        return False
    
    def bottom_water_border(self):
        if self.vicinity_matrix[2][1] in PASSABLE_TILES:
            if (self.vicinity_matrix[1][0] == WATER or self.vicinity_matrix[1][0] == WALL) and (self.vicinity_matrix[1][2] == WATER or self.vicinity_matrix[1][2] == WALL):
                return True
        return False

    def water_top_left_convex(self):
        if self.vicinity_matrix[1][0] in PASSABLE_TILES and self.vicinity_matrix[0][1] in PASSABLE_TILES:
            return True

    def water_top_right_convex(self):
        if self.vicinity_matrix[0][1] in PASSABLE_TILES and self.vicinity_matrix[1][2] in PASSABLE_TILES:
            return True
    
    def water_bottom_right_convex(self):
        if self.vicinity_matrix[1][2] in PASSABLE_TILES and self.vicinity_matrix[2][1] in PASSABLE_TILES:
            return True

    def water_bottom_left_convex(self):
        if self.vicinity_matrix[1][0] in PASSABLE_TILES and self.vicinity_matrix[2][1] in PASSABLE_TILES :
            return True

    def water_top_left_concave(self):
        if self.vicinity_matrix[0][0] in PASSABLE_TILES :
            if self.vicinity_matrix[1][0] in IMPASSABLE_TILES and self.vicinity_matrix[0][1] in IMPASSABLE_TILES:
                return True

    def water_top_right_concave(self):
        if self.vicinity_matrix[0][2] in PASSABLE_TILES :
            if self.vicinity_matrix[0][1] in IMPASSABLE_TILES and self.vicinity_matrix[1][2] in IMPASSABLE_TILES:
                return True
    
    def water_bottom_right_concave(self):
        if self.vicinity_matrix[2][2] in PASSABLE_TILES :
            if self.vicinity_matrix[1][2] in IMPASSABLE_TILES and self.vicinity_matrix[2][1] in IMPASSABLE_TILES:
                return True

    def water_bottom_left_concave(self):
        if self.vicinity_matrix[2][0] in PASSABLE_TILES :
            if self.vicinity_matrix[1][0] in IMPASSABLE_TILES and self.vicinity_matrix[2][1] in IMPASSABLE_TILES:
                return True

    ### Walls
    def wall_bottom_lower_wall_section(self):
        if self.vicinity_matrix[2][1] in PASSABLE_TILES or self.vicinity_matrix[2][1] is FLOOR_PIT or self.vicinity_matrix[2][1] is WATER:
            return True
        return False

    def wall_bottom_middle_wall_section(self):
        grid_two_squares_south = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]]
        if (grid_two_squares_south in PASSABLE_TILES or grid_two_squares_south is FLOOR_PIT or grid_two_squares_south is WATER) and (self.vicinity_matrix[0][1] is WALL):
            return True
        return False

    def wall_bottom_upper_wall_section(self):
        grid_three_squares_south = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]]
        if (grid_three_squares_south in PASSABLE_TILES or grid_three_squares_south is FLOOR_PIT or grid_three_squares_south is WATER) and (self.vicinity_matrix[0][1] is WALL):
            return True
        return False

    def get_bottom_lower_wall_section_image(self):
        if self.vicinity_matrix[1][0] in PASSABLE_TILES or self.vicinity_matrix[1][0] is FLOOR_PIT:
            return wall_corner_bottom_left_lower
        elif self.vicinity_matrix[1][2] in PASSABLE_TILES or self.vicinity_matrix[1][2] is FLOOR_PIT:
            return wall_corner_bottom_right_lower
        
        elif self.vicinity_matrix[1][0] is WATER:
            if self.vicinity_matrix[0][0] in PASSABLE_TILES or self.vicinity_matrix[0][0] is FLOOR_PIT:
                return None
            elif self. vicinity_matrix[0][0] is WATER:
                return None
        elif self.vicinity_matrix[1][2] is WATER:
            if self.vicinity_matrix[0][2] in PASSABLE_TILES or self.vicinity_matrix[0][2] is FLOOR_PIT:
                return None
            elif self. vicinity_matrix[0][2] is WATER:
                return None

    def get_bottom_middle_wall_section_image(self):
        pass

    def get_bottom_upper_wall_section_image(self):
        pass

    def get_cluster_x_y(self):
        if self.TYPE is WATER:
            if self.image_surface_unscaled in blue_water_border_convex_images[0] or self.image_surface_unscaled in blue_water_border_convex_images[1]:
                for i in range(2):
                    for j in range(2):
                        if blue_water_border_convex_images[i][j] == self.image_surface_unscaled:
                            return i,j
            
            elif self.image_surface_unscaled in blue_water_border_concave_images[0] or self.image_surface_unscaled in blue_water_border_concave_images[1]:
                for i in range(2):
                    for j in range(2):
                        if blue_water_border_concave_images[i][j] == self.image_surface_unscaled:
                            return i,j
        
        elif self.TYPE is CORNER_CRACK:
            if self.image_surface_unscaled in corner_crack_images[0] or self.image_surface_unscaled in corner_crack_images[1]:
                for i in range(2):
                    for j in range(2):
                        if corner_crack_images[i][j] == self.image_surface_unscaled:
                            return i,j


    def get_passable(self):
        if self.TYPE in IMPASSABLE_TILES:
            return False
        return True

    def get_index(self):
        return self.tile_index
