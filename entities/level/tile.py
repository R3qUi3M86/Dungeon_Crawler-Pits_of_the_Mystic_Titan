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
                    elif self.side_wall_section():
                        return self.get_side_wall_hidden_section_image()
                    # elif self.top_wall_section():
                    #     return self.get_top_wall_hidden_section_image()
                    # elif self.concave_wall_section():
                    #     return self.get_side_wall_hidden_concave_image()
                    else:
                        return blank
                else:
                    return blank
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
                else:         
                    return pygame.mask.from_surface(level_tile_collider)

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
        elif self.vicinity_matrix[2][0] not in WALL_LIKE and self.vicinity_matrix[1][0] in WALL_LIKE:
            return wall_left_concave_hidden
        elif self.vicinity_matrix[2][2] not in WALL_LIKE and self.vicinity_matrix[1][2] in WALL_LIKE:
            return wall_right_concave_hidden
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
        pass

    def get_top_wall_hidden_section_image(self):
        pass

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

    # def bottom_middle_wall_section(self):
    #     grid_two_squares_south = level_painter.level_layout[self.tile_index[0]+2][self.tile_index[1]]
    #     if (grid_two_squares_south in PASSABLE_TILES or grid_two_squares_south is FLOOR_PIT or grid_two_squares_south is WATER) and (self.vicinity_matrix[0][1] is WALL):
    #         return True
    #     return False

    def bottom_upper_wall_section(self):
        pass

    def top_wall_section(self):
        pass

    def side_wall_section(self):
        if self.vicinity_matrix[0][1] in WALL_LIKE and self.vicinity_matrix[2][1] in WALL_LIKE:
            return True
        return False

    def wall_concave_section(self):
        pass
    

