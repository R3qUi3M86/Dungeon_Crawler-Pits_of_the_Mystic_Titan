import pygame
import random
from entities.level.level import *
from images.level.cave_images import *
from images.misc.colliders import *
from utilities.constants import *
from utilities import level_painter
from utilities import entity_manager

class Tile(pygame.sprite.Sprite):
    def __init__(self,type,tile_index,pos,size,vicinity_matrix, wall_mode = HIDDEN):
        super().__init__()
        self.TYPE = type
        self.tile_index = tile_index
        self.position = pos
        self.map_position = int(self.tile_index[1] * level_painter.TILE_SIZE[1]+level_painter.TILE_SIZE[1]//2+screen_width//2), int(self.tile_index[0] * level_painter.TILE_SIZE[0]+level_painter.TILE_SIZE[0]//2 + screen_height//2)
        self.size = size
        self.vicinity_matrix = vicinity_matrix
        self.passable = self.get_passable()
        self.wall_mode = wall_mode
        
        self.is_convex = False
        self.image_unscaled = self.get_tile_image()
        self.image = pygame.transform.scale(self.image_unscaled, size)
        self.cluster_x_y = self.get_cluster_x_y()
        self.mask = self.get_tile_mask()
        self.rect = self.image.get_rect(center = (self.position))


    def update_position(self):
        self.position = self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0], self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1]
        self.rect = self.image.get_rect(center = (self.position))

    ###############
    ### Getters ###
    ###############
    #General
    def get_tile_image(self):
        if self.wall_mode is HIDDEN:
            if self.TYPE in PASSABLE_TILES:
                
                if self.TYPE is FLOOR:
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
                    if self.bottom_lower_wall_section():
                        return self.get_bottom_lower_wall_hidden_section_image()
                    elif self.side_wall_hidden_section() and not self.wall_section_concave_hidden():
                        return self.get_side_wall_hidden_section_image()
                    elif self.top_wall_section():
                        return self.get_top_wall_hidden_section_image()
                    elif self.wall_section_concave_hidden():
                        return self.get_side_wall_hidden_concave_image()
                        
                    else:
                        return blank

                elif self.TYPE is ENTRANCE:
                    return self.get_level_entrance_hidden_image()

                elif self.TYPE is EXIT:
                    return self.get_level_exit_hidden_image()
                
                else:
                    return empty_tile_image
        
        elif self.wall_mode is PRIMARY_OVERLAY:
            if self.TYPE is WALL:
                if self.bottom_lower_wall_section():
                    if self.vicinity_matrix[1][0] not in WALL_LIKE:
                        return wall_corner_bottom_left_lower_overlay
                    elif self.vicinity_matrix[1][2] not in WALL_LIKE:
                        return wall_corner_bottom_right_lower_overlay
                    else:
                        return random.choice(wall_bottom_lower_overlay)
                
                elif self.bottom_middle_wall_section():
                    if self.vicinity_matrix[0][1] not in WALL_LIKE:
                        if self.vicinity_matrix[1][0] not in WALL_LIKE or self.vicinity_matrix[2][0] not in WALL_LIKE:
                            return wall_bottom_middle_left_primary
                        elif self.vicinity_matrix[1][2] not in WALL_LIKE or self.vicinity_matrix[2][2] not in WALL_LIKE:
                            return wall_bottom_middle_right_primary
                        else:
                            return random.choice(wall_bottom_middle_primary_overlay)
                    else:
                        if self.vicinity_matrix[1][0] not in WALL_LIKE or self.vicinity_matrix[2][0] not in WALL_LIKE: 
                            return wall_bottom_middle_left_overlay
                        elif self.vicinity_matrix[1][2] not in WALL_LIKE or self.vicinity_matrix[2][2] not in WALL_LIKE:
                            return wall_bottom_middle_right_overlay
                        else:
                            return random.choice(wall_bottom_middle_overlay)
                
                elif self.bottom_upper_wall_section():
                    if self.vicinity_matrix[2][1] in WALL_LIKE and self.TYPE is WALL:
                        if self.bottom_upper_left_corner_section():
                            if self.vicinity_matrix[0][1] not in WALL_LIKE:
                                return wall_bottom_left_upper_primary
                            else:
                                return wall_bottom_left_upper_overlay
                        elif self.bottom_upper_right_corner_section():
                            if self.vicinity_matrix[0][1] not in WALL_LIKE:
                                return wall_bottom_right_upper_primary
                            else:
                                return wall_bottom_right_upper_overlay
                        else:
                            return random.choice(wall_bottom_upper_primary)
                    else:
                        return empty_tile_image

                elif self.side_wall_primary_section():
                    return self.get_side_wall_primary_image()
                
                elif self.side_wall_concave_section():
                    return self.get_side_wall_concave_primary_image()

                else:
                    return empty_tile_image

            elif self.TYPE is ENTRANCE:
                return self.get_level_entrance_primary_image()

            elif self.TYPE is EXIT:
                return self.get_level_exit_primary_image()
            
            else:
                return empty_tile_image
        
        elif self.wall_mode is SECONDARY_OVERLAY:
            if True:
                return empty_tile_image
        
        else:
            return blank

    def get_tile_mask(self):
        if self.passable == True:
            return pygame.mask.from_surface(empty_tile_image)
        else:
            if self.TYPE in IMPASSABLE_TILES:
                if self.TYPE is FLOOR_PIT:
                    return pygame.mask.from_surface(floor_pit_collider)
                elif self.TYPE is WATER:
                    if self.image_unscaled is blue_water_border_right:
                        return pygame.mask.from_surface(blue_water_border_right_collider)
                    elif self.image_unscaled is blue_water_border_left:
                        return pygame.mask.from_surface(blue_water_border_left_collider)
                    elif self.image_unscaled in blue_water_border_top_images:
                        return pygame.mask.from_surface(blue_water_border_top_collider)
                    elif self.image_unscaled in blue_water_border_bottom_images:
                        return pygame.mask.from_surface(blue_water_border_bottom_collider)
                    elif self.image_unscaled in blue_water_border_convex_images[0] or self.image_unscaled in blue_water_border_convex_images[1]:
                        return pygame.mask.from_surface(blue_water_border_convex_colliders[self.cluster_x_y[0]][self.cluster_x_y[1]])
                    elif self.image_unscaled in blue_water_border_concave_images[0] or self.image_unscaled in blue_water_border_concave_images[1]:
                        return pygame.mask.from_surface(blue_water_border_concave_colliders[self.cluster_x_y[0]][self.cluster_x_y[1]])
                elif self.TYPE is WALL:
                    if self.image_unscaled in wall_bottom_lower_hidden or self.image_unscaled is wall_corner_bottom_lower_left_water_bottom_border_hidden or self.image_unscaled is wall_corner_bottom_lower_right_water_bottom_border_hidden:
                        return pygame.mask.from_surface(wall_bottom_mid_floor_collider)
                    elif self.image_unscaled is wall_corner_bottom_lower_left_hidden:
                        return pygame.mask.from_surface(wall_corner_bottom_left_floor_collider)
                    elif self.image_unscaled is wall_corner_bottom_lower_right_hidden:
                        return pygame.mask.from_surface(wall_corner_bottom_right_floor_collider)
                    elif self.image_unscaled is wall_corner_bottom_lower_left_water_left_border_hidden:
                        return pygame.mask.from_surface(wall_corner_bottom_left_water_left_border_collider)
                    elif self.image_unscaled is wall_corner_bottom_lower_right_water_right_border_hidden:
                        return pygame.mask.from_surface(wall_corner_bottom_right_water_right_border_collider)
                    elif self.image_unscaled is wall_corner_bottom_lower_left_water_top_border_hidden:
                        return pygame.mask.from_surface(small_collider_top_left)
                    elif self.image_unscaled is wall_corner_bottom_lower_right_water_top_border_hidden:
                        return pygame.mask.from_surface(small_collider_top_right)
                    elif self.image_unscaled is wall_corner_bottom_lower_left_floor_convex_hidden or self.image_unscaled is wall_bottom_lower_left_water_border_hidden or self.image_unscaled is wall_corner_bottom_lower_right_water_left_border_hidden:
                        return pygame.mask.from_surface(small_collider_bottom_left)
                    elif self.image_unscaled is wall_corner_bottom_lower_left_water_right_border_hidden or self.image_unscaled is wall_corner_bottom_lower_right_floor_convex_hidden or self.image_unscaled is wall_bottom_lower_right_water_border_hidden:
                        return pygame.mask.from_surface(small_collider_bottom_right)
                    elif self.image_unscaled is wall_corner_bottom_lower_right_water_convex_hidden:
                        return pygame.mask.from_surface(small_dual_collider_ne_sw)
                    elif self.image_unscaled is wall_corner_bottom_lower_left_water_convex_hidden:
                        return pygame.mask.from_surface(small_dual_collider_nw_se)
                    elif self.image_unscaled in wall_left:
                        return pygame.mask.from_surface(wall_left_collider)
                    elif self.image_unscaled in wall_right:
                        return pygame.mask.from_surface(wall_right_collider)
                    elif self.image_unscaled in wall_top_floor or self.image_unscaled is wall_top_left_convex_water_top_border or self.image_unscaled is wall_top_right_convex_water_top_border:
                        return pygame.mask.from_surface(wall_top_floor_collider)
                    elif self.image_unscaled is wall_top_left_convex_floor:
                        return pygame.mask.from_surface(wall_top_left_convex_floor_collider)
                    elif self.image_unscaled is wall_top_right_convex_floor:
                        return pygame.mask.from_surface(wall_top_right_convex_floor_collider)
                    elif self.image_unscaled is wall_top_left_convex_water_left_border:
                        return pygame.mask.from_surface(wall_top_left_convex_water_left_border_collider)
                    elif self.image_unscaled is wall_top_right_convex_water_right_border:
                        return pygame.mask.from_surface(wall_top_right_convex_water_right_border_collider)
                    elif self.image_unscaled is wall_top_left_convex_water_floor_convex or self.image_unscaled is wall_top_right_convex_water_left_border or self.image_unscaled in wall_top_water_left_border:
                        return pygame.mask.from_surface(wall_top_small_left_collider)
                    elif self.image_unscaled is wall_top_left_convex_water_right_border or self.image_unscaled is wall_top_right_convex_water_floor_convex or self.image_unscaled in wall_top_water_right_border:
                        return pygame.mask.from_surface(wall_top_small_right_collider)
                    elif self.image_unscaled is wall_top_left_convex_water_convex:
                        return pygame.mask.from_surface(wall_top_left_convex_water_convex_collider)
                    elif self.image_unscaled is wall_top_right_convex_water_convex:
                        return pygame.mask.from_surface(wall_top_right_convex_water_convex_collider)
                    else:         
                        return pygame.mask.from_surface(level_tile_collider)
                else:         
                    return pygame.mask.from_surface(level_tile_collider)

    #Wall image getters
    def get_bottom_lower_wall_hidden_section_image(self):
        ### Middle
        if self.vicinity_matrix[1][0] in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
            if self.vicinity_matrix[2][1] is not WATER:
                return random.choice(wall_bottom_lower_hidden)
            else:
                if self.vicinity_matrix[2][0] in FLOOR_LIKE:
                    return wall_bottom_lower_left_water_border_hidden
                elif self.vicinity_matrix[2][2] in FLOOR_LIKE:
                    return wall_bottom_lower_right_water_border_hidden
                else:
                    return random.choice(wall_bottom_lower_water_hidden)
        
        ### Corners
        #Normal
        elif self.vicinity_matrix[1][0] in FLOOR_LIKE:
            return wall_corner_bottom_lower_left_hidden
        elif self.vicinity_matrix[1][2] in FLOOR_LIKE:
            return wall_corner_bottom_lower_right_hidden
        
        #Water
        #Lower left corner
        elif self.vicinity_matrix[1][0] is WATER and self.vicinity_matrix[2][1] is WATER:
            if self.vicinity_matrix[0][0] is WATER and self.vicinity_matrix[2][2] is WATER:
                if self.vicinity_matrix[2][0] is WATER or self.vicinity_matrix[2][0] is WALL:
                    return wall_corner_bottom_lower_left_water_concave_hidden
                elif self.vicinity_matrix[2][0] in FLOOR_LIKE:
                    return wall_corner_bottom_lower_left_floor_convex_hidden
            
            elif self.vicinity_matrix[0][0] is WATER and self.vicinity_matrix[2][2] in FLOOR_LIKE:
                return wall_corner_bottom_lower_left_water_right_border_hidden
            elif (self.vicinity_matrix[2][2] is WATER or self.vicinity_matrix[2][2] in WALL_LIKE) and self.vicinity_matrix[0][0] in FLOOR_LIKE:
                return wall_corner_bottom_lower_left_water_top_border_hidden

            elif self.vicinity_matrix[0][0] in FLOOR_LIKE and self.vicinity_matrix[2][2] in FLOOR_LIKE:
                return wall_corner_bottom_lower_left_water_convex_hidden
        elif self.vicinity_matrix[2][0] in FLOOR_LIKE and self.vicinity_matrix[1][2] is WALL:
            if self.vicinity_matrix[1][0] is WATER:
                return wall_corner_bottom_lower_left_water_bottom_border_hidden
            elif self.vicinity_matrix[2][1] is WATER:
                return wall_corner_bottom_lower_left_water_left_border_hidden

        #Lower right corner
        elif self.vicinity_matrix[1][2] is WATER and self.vicinity_matrix[2][1] is WATER:
            if self.vicinity_matrix[0][2] is WATER and self.vicinity_matrix[2][0] is WATER:
                if self.vicinity_matrix[2][2] is WATER or self.vicinity_matrix[2][2] is WALL:
                    return wall_corner_bottom_lower_right_water_concave_hidden
                elif self.vicinity_matrix[2][2] in FLOOR_LIKE:
                    return wall_corner_bottom_lower_right_floor_convex_hidden
            
            elif self.vicinity_matrix[0][2] is WATER and self.vicinity_matrix[2][0] in FLOOR_LIKE:
                return wall_corner_bottom_lower_right_water_left_border_hidden
            elif (self.vicinity_matrix[2][0] is WATER or self.vicinity_matrix[2][0] in WALL_LIKE) and self.vicinity_matrix[0][2] in FLOOR_LIKE:
                return wall_corner_bottom_lower_right_water_top_border_hidden

            elif self.vicinity_matrix[0][2] in FLOOR_LIKE and self.vicinity_matrix[2][0] in FLOOR_LIKE:
                return wall_corner_bottom_lower_right_water_convex_hidden
        elif self.vicinity_matrix[2][2] in FLOOR_LIKE and self.vicinity_matrix[1][0] is WALL:
            if self.vicinity_matrix[1][2] is WATER:
                return wall_corner_bottom_lower_right_water_bottom_border_hidden
            elif self.vicinity_matrix[2][1] is WATER:
                return wall_corner_bottom_lower_right_water_left_border_hidden

    def get_side_wall_hidden_section_image(self):
        if self.vicinity_matrix[1][0] in FLOOR_LIKE:
            return random.choice(wall_left)
        elif self.vicinity_matrix[1][2] in FLOOR_LIKE:
            return random.choice(wall_right)
        elif self.vicinity_matrix[1][0] is WATER:
            if self.vicinity_matrix[0][0] in FLOOR_LIKE:
                return wall_left_water_border_top
            elif self.vicinity_matrix[2][0] in FLOOR_LIKE:
                return wall_left_water_border_bottom
            else:
                return random.choice(wall_left_water)
        elif self.vicinity_matrix[1][2] is WATER:
            if self.vicinity_matrix[0][2] in FLOOR_LIKE:
                return wall_right_water_border_top
            elif self.vicinity_matrix[2][2] in FLOOR_LIKE:
                return wall_right_water_border_bottom
            else:
                return random.choice(wall_right_water)
        else:
            return blank

    def get_top_wall_hidden_section_image(self):
        #Top left wall convex
        if self.vicinity_matrix[1][0] not in WALL_LIKE:
            if self.vicinity_matrix[1][0] in FLOOR_LIKE and self.vicinity_matrix[0][1] in FLOOR_LIKE:
                self.is_convex = True
                return wall_top_left_convex_floor
            elif self.vicinity_matrix[1][0] is WATER and self.vicinity_matrix[0][1] is WATER:
                if self.vicinity_matrix[0][0] is FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_left_convex_water_floor_convex
                elif self.vicinity_matrix[2][0] in IMPASSABLE_TILES and self.vicinity_matrix[0][2] in IMPASSABLE_TILES:
                    self.is_convex = True
                    return wall_top_left_convex_water_concave
                elif self.vicinity_matrix[2][0] in FLOOR_LIKE and self.vicinity_matrix[0][2] in FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_left_convex_water_convex
                elif self.vicinity_matrix[2][0] in FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_left_convex_water_bottom_border
                elif self.vicinity_matrix[0][2] in FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_left_convex_water_right_border
            elif self.vicinity_matrix[0][1] in FLOOR_LIKE and self.vicinity_matrix[1][0] is WATER:
                self.is_convex = True
                return wall_top_left_convex_water_top_border
            elif self.vicinity_matrix[1][0] in FLOOR_LIKE and self.vicinity_matrix[0][1] is WATER:
                self.is_convex = True
                return wall_top_left_convex_water_left_border
        
        #Top right wall convex
        if self.vicinity_matrix[1][2] not in WALL_LIKE:
            if self.vicinity_matrix[1][2] in FLOOR_LIKE and self.vicinity_matrix[0][1] in FLOOR_LIKE:
                self.is_convex = True
                return wall_top_right_convex_floor
            elif self.vicinity_matrix[1][2] is WATER and self.vicinity_matrix[0][1] is WATER:
                if self.vicinity_matrix[0][2] is FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_right_convex_water_floor_convex
                elif self.vicinity_matrix[2][2] in IMPASSABLE_TILES and self.vicinity_matrix[0][0] in IMPASSABLE_TILES:
                    self.is_convex = True
                    return wall_top_right_convex_water_concave
                elif self.vicinity_matrix[2][2] in FLOOR_LIKE and self.vicinity_matrix[0][0] in FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_right_convex_water_convex
                elif self.vicinity_matrix[2][2] in FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_right_convex_water_bottom_border
                elif self.vicinity_matrix[0][0] in FLOOR_LIKE:
                    self.is_convex = True
                    return wall_top_right_convex_water_left_border
            elif self.vicinity_matrix[0][1] in FLOOR_LIKE and self.vicinity_matrix[1][2] is WATER:
                self.is_convex = True
                return wall_top_right_convex_water_top_border
            elif self.vicinity_matrix[1][2] in FLOOR_LIKE and self.vicinity_matrix[0][1] is WATER:
                self.is_convex = True
                return wall_top_right_convex_water_right_border

        #Top middle wall
        if self.vicinity_matrix[1][0] in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
            if self.vicinity_matrix[0][1] in FLOOR_LIKE:
                return random.choice(wall_top_floor)
            elif self.vicinity_matrix[0][1] is WATER:
                if self.vicinity_matrix[0][0] in IMPASSABLE_TILES and self.vicinity_matrix[0][2] in IMPASSABLE_TILES:
                    return random.choice(wall_top_water)
                elif self.vicinity_matrix[0][0] in FLOOR_LIKE:
                    return random.choice(wall_top_water_left_border)
                elif self.vicinity_matrix[0][2] in FLOOR_LIKE:
                    return random.choice(wall_top_water_right_border)

    def get_side_wall_hidden_concave_image(self):
        if self.vicinity_matrix[2][0] not in WALL_LIKE and self.vicinity_matrix[1][0] in WALL_LIKE:
            return wall_top_right_concave_hidden
        elif self.vicinity_matrix[2][2] not in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
            return wall_top_left_concave_hidden
        elif self.vicinity_matrix[0][0] not in WALL_LIKE:
            if self.vicinity_matrix[0][0] in FLOOR_LIKE:
                return wall_bottom_right_concave_floor_hidden
            elif self.vicinity_matrix[0][0] is WATER:
                return wall_bottom_right_concave_water_hidden
        elif self.vicinity_matrix[0][2] not in WALL_LIKE:
            if self.vicinity_matrix[0][2] in FLOOR_LIKE:
                return wall_bottom_left_concave_floor_hidden
            elif self.vicinity_matrix[0][2] is WATER:
                return wall_bottom_left_concave_water_hidden

    def get_side_wall_primary_image(self):
        if self.vicinity_matrix[2][0] not in WALL_LIKE:
            if self.vicinity_matrix[0][1] in WALL_LIKE: 
                return random.choice(wall_left)
            else:
                return wall_left_primary_01
        
        elif self.vicinity_matrix[2][2] not in WALL_LIKE:
            if self.vicinity_matrix[0][1] in WALL_LIKE:
                return random.choice(wall_right)
            else:
                return wall_right_primary_01

        elif self.tile_index[1] == 0:
            grid_two_squares_south_right = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]+1]
            if grid_two_squares_south_right not in WALL_LIKE:
                if self.vicinity_matrix[0][1] in WALL_LIKE:
                    return random.choice(wall_right)
                else:
                    return wall_right_primary_01
        
        elif self.tile_index[1] == len(level_painter.level_layout[0])-1:
            grid_two_squares_south_left = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]-1]
            if grid_two_squares_south_left not in WALL_LIKE:
                if self.vicinity_matrix[0][1] in WALL_LIKE:
                    return random.choice(wall_left)
                else:
                    return wall_left_primary_01
        else:
            grid_two_squares_south_left = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]-1]
            grid_two_squares_south_right = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]+1]
            if grid_two_squares_south_left not in WALL_LIKE:
                if self.vicinity_matrix[0][1] in WALL_LIKE:
                    return random.choice(wall_left)
                else:
                    return wall_left_primary_01
            
            elif grid_two_squares_south_right not in WALL_LIKE:
                if self.vicinity_matrix[0][1] in WALL_LIKE:
                    return random.choice(wall_right)
                else:
                    return wall_right_primary_01

    def get_side_wall_concave_primary_image(self):
        if self.tile_index[1] == 0:
            grid_three_squares_south_right = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]+1]
            if grid_three_squares_south_right not in WALL_LIKE:
                    return wall_top_left_concave_hidden
        
        elif self.tile_index[1] == len(level_painter.level_layout[0])-1:
            grid_three_squares_south_left = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]-1]
            if grid_three_squares_south_left not in WALL_LIKE:
                return wall_top_right_concave_hidden
        else:
            grid_three_squares_south_left = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]-1]
            grid_three_squares_south_right = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]+1]
            if grid_three_squares_south_left not in WALL_LIKE:
                return wall_top_right_concave_hidden
            elif grid_three_squares_south_right not in WALL_LIKE:
                return wall_top_left_concave_hidden

    def get_level_entrance_hidden_image(self):
        if self.vicinity_matrix[1][0] is not ENTRANCE:
            if self.vicinity_matrix[0][1] is not ENTRANCE:
                return level_entrance_images_hidden[0][0]
            else:
                return level_entrance_images_hidden[1][0]
        elif self.vicinity_matrix[1][0] is ENTRANCE and self.vicinity_matrix[1][2] is ENTRANCE:
            if self.vicinity_matrix[0][1] is not ENTRANCE:
                return level_entrance_images_hidden[0][1]
            else:
                return level_entrance_images_hidden[1][1]
        elif self.vicinity_matrix[1][2] is not ENTRANCE:
            if self.vicinity_matrix[0][1] is not ENTRANCE:
                return level_entrance_images_hidden[0][2]
            else:
                return level_entrance_images_hidden[1][2]

    def get_level_exit_hidden_image(self):
        if self.vicinity_matrix[1][0] is not EXIT:
            if self.vicinity_matrix[0][1] is not EXIT:
                return level_exit_images_hidden[0][0]
            else:
                return level_exit_images_hidden[1][0]
        elif self.vicinity_matrix[1][0] is EXIT and self.vicinity_matrix[1][2] is EXIT:
            if self.vicinity_matrix[0][1] is not EXIT:
                return level_exit_images_hidden[0][1]
            else:
                return level_exit_images_hidden[1][1]
        elif self.vicinity_matrix[1][2] is not EXIT:
            if self.vicinity_matrix[0][1] is not EXIT:
                return level_exit_images_hidden[0][2]
            else:
                return level_exit_images_hidden[1][2]     

    def get_level_entrance_primary_image(self):
        if self.vicinity_matrix[1][0] is not ENTRANCE:
            if self.vicinity_matrix[0][1] is not ENTRANCE:
                return level_entrance_images_overlay[0][0]
            else:
                return level_entrance_images_overlay[1][0]
        elif self.vicinity_matrix[1][0] is ENTRANCE and self.vicinity_matrix[1][2] is ENTRANCE:
            if self.vicinity_matrix[0][1] is not ENTRANCE:
                return level_entrance_images_overlay[0][1]
            else:
                return level_entrance_images_overlay[1][1]
        elif self.vicinity_matrix[1][2] is not ENTRANCE:
            if self.vicinity_matrix[0][1] is not ENTRANCE:
                return level_entrance_images_overlay[0][2]
            else:
                return level_entrance_images_overlay[1][2]

    def get_level_exit_primary_image(self):
        if self.vicinity_matrix[1][0] is not EXIT:
            if self.vicinity_matrix[0][1] is not EXIT:
                return level_exit_images_overlay[0][0]
            else:
                return level_exit_images_overlay[1][0]
        elif self.vicinity_matrix[1][0] is EXIT and self.vicinity_matrix[1][2] is EXIT:
            if self.vicinity_matrix[0][1] is not EXIT:
                return level_exit_images_overlay[0][1]
            else:
                return level_exit_images_overlay[1][1]
        elif self.vicinity_matrix[1][2] is not EXIT:
            if self.vicinity_matrix[0][1] is not EXIT:
                return level_exit_images_overlay[0][2]
            else:
                return level_exit_images_overlay[1][2]    

    #Other
    def get_cluster_x_y(self):
        if self.TYPE is WATER:
            if self.image_unscaled in blue_water_border_convex_images[0] or self.image_unscaled in blue_water_border_convex_images[1]:
                for i in range(2):
                    for j in range(2):
                        if blue_water_border_convex_images[i][j] == self.image_unscaled:
                            return i,j
            
            elif self.image_unscaled in blue_water_border_concave_images[0] or self.image_unscaled in blue_water_border_concave_images[1]:
                for i in range(2):
                    for j in range(2):
                        if blue_water_border_concave_images[i][j] == self.image_unscaled:
                            return i,j
        
        elif self.TYPE is CORNER_CRACK:
            if self.image_unscaled in corner_crack_images[0] or self.image_unscaled in corner_crack_images[1]:
                for i in range(2):
                    for j in range(2):
                        if corner_crack_images[i][j] == self.image_unscaled:
                            return i,j

    def get_passable(self):
        if self.TYPE in IMPASSABLE_TILES:
            return False
        return True

    ##################
    ### CONDITIONS ###
    ##################
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
        if self.vicinity_matrix[0][1] in WALL_LIKE:
            return False
        return True

    def water_under_wall_middle(self):
        if entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_bottom_lower_water_hidden:
            return True
        return False

    def water_under_wall_left(self):
        if entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_corner_bottom_lower_left_gushing_water_hidden:
            return True
        return False
    
    def water_under_wall_right(self):
        if entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_corner_bottom_lower_right_gushing_water_hidden:
            return True
        return False

    def left_water_border(self):
        if self.vicinity_matrix[1][0] in FLOOR_LIKE:
            if (self.vicinity_matrix[0][1] is WATER or entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_bottom_lower_left_water_borders_hidden) and (self.vicinity_matrix[2][1] is WATER or self.vicinity_matrix[2][1] is WALL):
                return True
        return False

    def right_water_border(self):
        if self.vicinity_matrix[1][2] in FLOOR_LIKE:
            if (self.vicinity_matrix[0][1] is WATER or entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_bottom_lower_right_water_borders_hidden) and (self.vicinity_matrix[2][1] is WATER or self.vicinity_matrix[2][1] is WALL):
                return True
        return False
    
    def top_water_border(self):
        if self.vicinity_matrix[0][1] in FLOOR_LIKE or entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_bottom_lower_water_hidden or entity_manager.level_sprites_matrix[self.tile_index[0]-1][self.tile_index[1]].image_unscaled in wall_corner_bottom_hidden:
            if (self.vicinity_matrix[1][0] is WATER or self.vicinity_matrix[1][0] is WALL) and (self.vicinity_matrix[1][2] is WATER or self.vicinity_matrix[1][2] is WALL):
                return True
        return False
    
    def bottom_water_border(self):
        if self.vicinity_matrix[2][1] in FLOOR_LIKE:
            if (self.vicinity_matrix[1][0] is WATER or self.vicinity_matrix[1][0] is WALL) and (self.vicinity_matrix[1][2] is WATER or self.vicinity_matrix[1][2] is WALL):
                return True
        return False

    def water_top_left_convex(self):
        if self.vicinity_matrix[1][0] in FLOOR_LIKE and self.vicinity_matrix[0][1] in FLOOR_LIKE:
            return True

    def water_top_right_convex(self):
        if self.vicinity_matrix[0][1] in FLOOR_LIKE and self.vicinity_matrix[1][2] in FLOOR_LIKE:
            return True
    
    def water_bottom_right_convex(self):
        if self.vicinity_matrix[1][2] in FLOOR_LIKE and self.vicinity_matrix[2][1] in FLOOR_LIKE:
            return True

    def water_bottom_left_convex(self):
        if self.vicinity_matrix[1][0] in FLOOR_LIKE and self.vicinity_matrix[2][1] in FLOOR_LIKE :
            return True

    def water_top_left_concave(self):
        if self.vicinity_matrix[0][0] in FLOOR_LIKE :
            if self.vicinity_matrix[1][0] in IMPASSABLE_TILES and self.vicinity_matrix[0][1] in IMPASSABLE_TILES:
                return True

    def water_top_right_concave(self):
        if self.vicinity_matrix[0][2] in FLOOR_LIKE :
            if self.vicinity_matrix[0][1] in IMPASSABLE_TILES and self.vicinity_matrix[1][2] in IMPASSABLE_TILES:
                return True
    
    def water_bottom_right_concave(self):
        if self.vicinity_matrix[2][2] in FLOOR_LIKE :
            if self.vicinity_matrix[1][2] in IMPASSABLE_TILES and self.vicinity_matrix[2][1] in IMPASSABLE_TILES:
                return True

    def water_bottom_left_concave(self):
        if self.vicinity_matrix[2][0] in FLOOR_LIKE :
            if self.vicinity_matrix[1][0] in IMPASSABLE_TILES and self.vicinity_matrix[2][1] in IMPASSABLE_TILES:
                return True

    ### Walls
    def bottom_lower_wall_section(self):
        if self.vicinity_matrix[2][1] not in WALL_LIKE:
            return True
        return False

    def bottom_middle_wall_section(self):
        if self.tile_index[0]+2 < len(level_painter.level_layout):
            grid_two_squares_south = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]]
            if self.vicinity_matrix[2][1] in WALL_LIKE and grid_two_squares_south not in WALL_LIKE:
                return True
        return False

    def bottom_upper_wall_section(self):
        if self.tile_index[0]+2 < len(level_painter.level_layout) and self.tile_index[0]+3 < len(level_painter.level_layout):
            grid_two_squares_south = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]]
            grid_three_squares_south = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]]
            if self.vicinity_matrix[2][1] in WALL_LIKE and grid_two_squares_south in WALL_LIKE and grid_three_squares_south not in WALL_LIKE:
                return True
        return False

    def bottom_upper_left_corner_section(self):
        if 0 < self.tile_index[1]-1:
            grid_two_squares_south_left = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]-1]
            if grid_two_squares_south_left not in WALL_LIKE:
                return True

    def bottom_upper_right_corner_section(self):
        if self.tile_index[1]+1 < (len(level_painter.level_layout[0])-1):
            grid_two_squares_south_right = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]+1]
            if grid_two_squares_south_right not in WALL_LIKE:
                return True

    def top_wall_section(self):
        if self.vicinity_matrix[0][1] in FLOOR_LIKE or self.vicinity_matrix[0][1] is WATER:
            return True
        return False

    def side_wall_hidden_section(self):
        if self.vicinity_matrix[0][1] in WALL_LIKE and self.vicinity_matrix[2][1] in WALL_LIKE:
            return True
        return False

    def side_wall_primary_section(self):
        if self.tile_index[0]+2 < len(level_painter.level_layout) and self.tile_index[0]+3 < len(level_painter.level_layout):
            grid_two_squares_south = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]]
            grid_three_squares_south = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]]
            
            if self.vicinity_matrix[2][1] in WALL_LIKE and grid_two_squares_south in WALL_LIKE and grid_three_squares_south in WALL_LIKE:
                if self.vicinity_matrix[1][0] in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
                    if (self.vicinity_matrix[2][0] not in WALL_LIKE or self.vicinity_matrix[2][2] not in WALL_LIKE):
                        return True
                    
                    elif self.tile_index[1] == 0:
                        grid_two_squares_south_right = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]+1]
                        if grid_two_squares_south_right not in WALL_LIKE:
                                return True
                    
                    elif self.tile_index[1] == len(level_painter.level_layout[0])-1:
                        grid_two_squares_south_left = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]-1]
                        if grid_two_squares_south_left not in WALL_LIKE:
                            return True
                    else:
                        grid_two_squares_south_left = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]-1]
                        grid_two_squares_south_right = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]+1]
                        if grid_two_squares_south_left not in WALL_LIKE or grid_two_squares_south_right not in WALL_LIKE:
                            return True
            return False

    def wall_section_concave_hidden(self):
        if self.vicinity_matrix[2][0] not in WALL_LIKE and self.vicinity_matrix[1][0] in WALL_LIKE:
            return True
        elif self.vicinity_matrix[2][2] not in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
            return True
        elif self.vicinity_matrix[0][1] in WALL_LIKE and self.vicinity_matrix[2][1] in WALL_LIKE and self.vicinity_matrix[1][0] in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE and self.vicinity_matrix[2][0] in WALL_LIKE and self.vicinity_matrix[2][2] in WALL_LIKE:
            if (self.vicinity_matrix[0][0] not in WALL_LIKE and self.vicinity_matrix[0][2] in WALL_LIKE) or (self.vicinity_matrix[0][2] not in WALL_LIKE and self.vicinity_matrix[0][0] in WALL_LIKE):
                return True
        return False

    def side_wall_concave_section(self):
        if self.tile_index[0]+2 < len(level_painter.level_layout) and self.tile_index[0]+3 < len(level_painter.level_layout):
            grid_two_squares_south = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]]
            grid_three_squares_south = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]]
            
            if self.vicinity_matrix[0][1] in WALL_LIKE and self.vicinity_matrix[2][1] in WALL_LIKE and grid_two_squares_south in WALL_LIKE and grid_three_squares_south in WALL_LIKE:
                if self.vicinity_matrix[1][0] in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
                    if self.tile_index[1] == 0:
                        grid_three_squares_south_right = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]+1]
                        if grid_three_squares_south_right not in WALL_LIKE:
                                return True
                    
                    elif self.tile_index[1] == len(level_painter.level_layout[0])-1:
                        grid_three_squares_south_left = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]-1]
                        if grid_three_squares_south_left not in WALL_LIKE:
                            return True
                    else:
                        grid_three_squares_south_left = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]-1]
                        grid_three_squares_south_right = level_painter.level_layout[self.tile_index[0]+3][self.tile_index[1]+1]
                        if grid_three_squares_south_left not in WALL_LIKE or grid_three_squares_south_right not in WALL_LIKE:
                            return True