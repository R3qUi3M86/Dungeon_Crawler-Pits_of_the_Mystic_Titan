import pygame
from copy import deepcopy
from settings import *
from entities.level.level import *
from entities.level.tile import Tile
from utilities import entity_manager
from utilities import movement_manager

TILE_SIZE = 48,48
player_starting_tile_index = None
level = level_01_map

def set_player_tile_index():
    global player_starting_tile_index

    for row_index,level_layout_row in enumerate(level):
        for col_index,cell in enumerate(level_layout_row):
            if cell_is_starting_position(row_index,col_index,cell):
                player_starting_tile_index = row_index,col_index
                movement_manager.player_tile_index = player_starting_tile_index

def set_player_position_on_map():
    movement_manager.player_position_on_map = TILE_SIZE[0]//2+(48*player_starting_tile_index[0]),TILE_SIZE[1]//2+(48*player_starting_tile_index[1])

def create_all_level_tiles():
    set_player_tile_index()
    set_player_position_on_map()
    for row_index,level_layout_row in enumerate(level):
        for col_index,cell in enumerate(level_layout_row):
            type = cell
            level_tile_index = row_index,col_index
            position = get_tile_position(level_tile_index)
            vicinity_matrix = get_vicinity_matrix_for_tile(level_tile_index)
            create_level_tile(type,position,TILE_SIZE,vicinity_matrix)

def create_level_tile(type,position,size,vicinity_matrix):
    new_tile_sprite = Tile(type,position,size,vicinity_matrix)
    entity_manager.level_sprite_groups.append(pygame.sprite.GroupSingle(new_tile_sprite))
    if new_tile_sprite.passable == False:
        entity_manager.level_collision_sprite_groups.append(pygame.sprite.GroupSingle(new_tile_sprite))

def cell_is_starting_position(row_index,col_index,cell):
    if level[row_index-1][col_index-1] == ENTRANCE and level[row_index-1][col_index] == ENTRANCE and level[row_index-1][col_index+1] == ENTRANCE and cell == FLOOR:
        return True
    return False

def get_tile_position(level_tile_index):
    index_distance_x = level_tile_index[1] - player_starting_tile_index[1]
    index_distance_y = level_tile_index[0] - player_starting_tile_index[0]

    distance_x = TILE_SIZE[0]*index_distance_x
    distance_y = TILE_SIZE[1]*index_distance_y

    position_x = player_position[0] + distance_x
    position_y = player_position[1] + distance_y

    return position_x,position_y

def get_vicinity_matrix_for_tile(level_tile_index):
    vicinity_matrix = []
    for i in range(3):
        vicinity_matrix_row = []
        
        for j in range(3):
            if 0 <= level_tile_index[0]+i-1 < len(level) and 0 <= level_tile_index[1]+j-1 < len(level[0]):
                cell = level[level_tile_index[0]+i-1][level_tile_index[1]+j-1]
                vicinity_matrix_row.append(cell)
            else:
                cell = WALL
        
        vicinity_matrix.append(deepcopy(vicinity_matrix_row))
        vicinity_matrix_row.clear()

    return vicinity_matrix