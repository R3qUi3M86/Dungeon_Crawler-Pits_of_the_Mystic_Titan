import pygame
from copy import deepcopy
from settings import *
from entities.level.level import *
from entities.level.tile import Tile
from utilities import entity_manager
from utilities import collision_manager

TILE_SIZE = 48,48
level_layout = level_01_map
pathfinding_matrix = []
level_surface = pygame.Surface((((len(level_layout[0])*TILE_SIZE[0])+screen_width,(len(level_layout)*TILE_SIZE[1])+screen_height)))
#level_layout = test_map
player_starting_tile_index = 0,0

def set_player_tile_index():
    global player_starting_tile_index

    for row_index,level_layout_row in enumerate(level_layout):
        for col_index,cell in enumerate(level_layout_row):
            if cell_is_starting_position(row_index,col_index,cell):
                player_starting_tile_index = row_index,col_index
                entity_manager.hero.tile_index = player_starting_tile_index

def set_player_position_on_map():
    entity_manager.hero.map_position = TILE_SIZE[0]//2+(48*entity_manager.hero.tile_index[1])+screen_width//2,TILE_SIZE[1]//2+(48*entity_manager.hero.tile_index[0]+screen_height//2)
    level_layout

def paint_level():
    global level_surface

    create_all_level_tiles()
    generate_pathfinding_matrix()
    level_surface.fill([25, 23, 22])
    
    for tile in entity_manager.level_sprite_groups:
        level_surface.blit(tile.sprite.image,(tile.sprite.map_position))

def create_all_level_tiles():
    set_player_tile_index()
    set_player_position_on_map()

    for row_index,level_layout_row in enumerate(level_layout):
        collision_tiles_row = []
        
        for col_index,cell in enumerate(level_layout_row):
            type = cell
            tile_index = row_index,col_index
            position = get_tile_position(tile_index)
            vicinity_matrix = get_proximity_matrix_for_tile_index(tile_index)
            new_tile_sprite = create_level_tile(type,tile_index,position,TILE_SIZE,vicinity_matrix)
            
            if new_tile_sprite.passable == False:
                collision_tiles_row.append(new_tile_sprite)
            else:
                collision_tiles_row.append(None)
        
        entity_manager.level_collision_sprites_matrix.append(collision_tiles_row)

def create_level_tile(type,level_position_index,position,size,vicinity_matrix):
    new_tile_sprite = Tile(type,level_position_index,position,size,vicinity_matrix)
    entity_manager.level_sprite_groups.append(pygame.sprite.GroupSingle(new_tile_sprite))
    return new_tile_sprite

def cell_is_starting_position(row_index,col_index,cell):
    if level_layout[row_index-1][col_index-1] == ENTRANCE and level_layout[row_index-1][col_index] == ENTRANCE and level_layout[row_index-1][col_index+1] == ENTRANCE and cell == FLOOR:
        return True
    return False

def get_tile_position(tile_index):
    index_distance_y = tile_index[0] - player_starting_tile_index[0]
    index_distance_x = tile_index[1] - player_starting_tile_index[1]

    distance_x = TILE_SIZE[0]*index_distance_x
    distance_y = TILE_SIZE[1]*index_distance_y

    position_x = player_position[0] + distance_x
    position_y = player_position[1] + distance_y

    return position_x,position_y

def get_tile_sprite_by_index(tile_index):
    for tile in entity_manager.level_sprite_groups:
        if tile.sprite.tile_index == tile_index:
            return tile.sprite

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

def generate_pathfinding_matrix():
    global pathfinding_matrix
    
    for row_index,level_layout_row in enumerate(level_layout):
        matrix_row = []
        for col_index,_ in enumerate(level_layout_row):
            tile_index = row_index,col_index
            if get_tile_sprite_by_index(tile_index).passable == False:
                matrix_row.append(0)
            else:
                matrix_row.append(1)
        pathfinding_matrix.append(matrix_row)

def get_level_surface_x_y():
    return player_position[0]-entity_manager.hero.map_position[0]-TILE_SIZE[0]/2,player_position[1]-entity_manager.hero.map_position[1]-TILE_SIZE[1]/2