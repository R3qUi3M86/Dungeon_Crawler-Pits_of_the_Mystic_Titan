import pygame
from copy import deepcopy

from images.ui import ui
import math
from settings import *
from entities.level.level import *
from entities.level.tile import Tile
from images.level.cave_images import empty_tile_image
from utilities import entity_manager
from utilities.constants import *

TILE_SIZE = 48,48
level_layout = level_01_map
pathfinding_matrix = []
pathfinding_flying_matrix = []
level_surface = None
level_walls_primary_surface = None
level_walls_secondary_surface = None
player_starting_tile = None

def set_player_tile_index():
    global player_starting_tile
    
    for row_index,level_layout_row in enumerate(level_layout):
        for col_index,cell in enumerate(level_layout_row):
            if cell_is_starting_position(row_index,col_index,cell):
                player_starting_tile = row_index,col_index

def paint_level():
    global level_surface
    global level_walls_primary_surface
    global level_walls_secondary_surface

    level_surface = get_level_surface()
    level_walls_primary_surface = get_level_surface(PRIMARY_OVERLAY)
    level_walls_secondary_surface = get_level_surface(SECONDARY_OVERLAY)

    create_all_level_tiles()
    generate_pathfinding_matrix(IMPASSABLE_TILES)
    generate_pathfinding_matrix(WALL_LIKE)
    level_surface.fill([25, 23, 22])
    
    for row in entity_manager.level_sprites_matrix:
        for tile in row:
            level_surface.blit(tile.image,(tile.map_position))

    # for row in entity_manager.primary_wall_sprites_matrix:
    #     for tile in row:
    #         if tile != 0:
    #             level_surface.blit(tile.image,(tile.map_position))

    for row in entity_manager.secondary_wall_sprites_matrix:
        for tile in row:
            if tile != 0:
                level_walls_secondary_surface.blit(tile.image,(tile.map_position))

def create_all_level_tiles():
    set_player_tile_index()
    for row_index, level_layout_row in enumerate(level_layout):
        for col_index, type in enumerate(level_layout_row):
            tile_index = row_index,col_index
            position = get_tile_position(tile_index)
            vicinity_matrix = get_proximity_matrix_for_tile_index(tile_index)

            new_tile_sprite = create_level_tile(type, tile_index, position, TILE_SIZE, vicinity_matrix)
            entity_manager.level_sprites_matrix[row_index][col_index] = new_tile_sprite
            
            new_primary_wall_sprite = create_level_tile(type, tile_index, position, TILE_SIZE, vicinity_matrix, PRIMARY_OVERLAY)
            if new_primary_wall_sprite.image_unscaled is not empty_tile_image:
                entity_manager.primary_wall_sprites_matrix[row_index][col_index] = new_primary_wall_sprite
            
            new_secondary_wall_sprite = create_level_tile(type, tile_index, position, TILE_SIZE, vicinity_matrix, SECONDARY_OVERLAY)
            if new_secondary_wall_sprite.image_unscaled is not empty_tile_image:
                entity_manager.secondary_wall_sprites_matrix[row_index][col_index] = new_secondary_wall_sprite

def create_level_tile(type,tile_index,position,size,vicinity_matrix, wall_mode=HIDDEN):
    new_tile_sprite = Tile(type,tile_index,position,size,vicinity_matrix, wall_mode)
    return new_tile_sprite

def generate_pathfinding_matrix(impassable_tiles_type):
    global pathfinding_matrix
    global pathfinding_flying_matrix
    
    for level_layout_row in level_layout:
        matrix_row = []
        for cell in level_layout_row:
            if cell in impassable_tiles_type:
                matrix_row.append(0)
            else:
                matrix_row.append(1)

        if impassable_tiles_type == IMPASSABLE_TILES:
            pathfinding_matrix.append(matrix_row)
        elif impassable_tiles_type == WALL_LIKE:
            pathfinding_flying_matrix.append(matrix_row)

#Getters
def get_tile_position(tile_index):
    index_distance_y = tile_index[0] - player_starting_tile[0]
    index_distance_x = tile_index[1] - player_starting_tile[1]

    distance_x = TILE_SIZE[0]*index_distance_x
    distance_y = TILE_SIZE[1]*index_distance_y

    position_x = player_position[0] + distance_x - TILE_SIZE[X]//2
    position_y = player_position[1] + distance_y - TILE_SIZE[Y]//2

    return position_x,position_y

def get_tile_sprite_by_index(tile_index):
    return entity_manager.level_sprites_matrix[tile_index[0]][tile_index[1]]

def get_proximity_matrix_for_tile_index(index_x_y):
    vicinity_matrix = []
    for i in range(3):
        vicinity_matrix_row = []
        
        for j in range(3):
            if 0 <= index_x_y[0]+i-1 < len(level_layout) and 0 <= index_x_y[1]+j-1 < len(level_layout[0]):
                cell = level_layout[index_x_y[0]+i-1][index_x_y[1]+j-1]
            else:
                cell = WALL
            vicinity_matrix_row.append(cell)
        
        vicinity_matrix.append(deepcopy(vicinity_matrix_row))

    return vicinity_matrix

def get_level_surface(surface_type=HIDDEN):
    if surface_type is HIDDEN:
        return pygame.Surface((((len(level_layout[0])*TILE_SIZE[0])+screen_width,(len(level_layout)*TILE_SIZE[1])+screen_height)))
    else:
        return pygame.Surface((((len(level_layout[0])*TILE_SIZE[0])+screen_width,(len(level_layout)*TILE_SIZE[1])+screen_height)), pygame.SRCALPHA, 32)

def get_level_surface_translation_vector():
    return math.floor(player_position[0]-entity_manager.hero.map_position[0]-TILE_SIZE[0]//2),math.floor(player_position[1]-entity_manager.hero.map_position[1]-TILE_SIZE[1]//2)

#Conditions
def cell_is_starting_position(row_index,col_index,cell):
    if level_layout[row_index-1][col_index-1] == ENTRANCE and level_layout[row_index-1][col_index] == ENTRANCE and level_layout[row_index-1][col_index+1] == ENTRANCE and cell == FLOOR:
        return True
    return False