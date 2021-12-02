from numpy import mat
import pygame
import math
import random
from utilities import util
from utilities.constants import *
from utilities import level_painter
from utilities.level_painter import level_layout
from utilities.level_painter import TILE_SIZE
from entities.level.level import WATER
from entities.characters.ettin import Ettin
from entities.characters.player import Hero
from entities.items.item import Item

entities_id = []

##### Entities #####
### Whole level ###
hero = Hero(player_position)
hero_sprite_group = pygame.sprite.GroupSingle(hero)
all_monsters = []

level_sprites_matrix = [[]]
primary_wall_sprites_matrix = [[]]
secondary_wall_sprites_matrix = [[]]
all_entity_and_shadow_sprite_group_matrix = [[[]]]

### Far proximity ###
#Matrices
far_proximity_index_matrix = [[]] #Only indices
far_proximity_level_sprite_matrix = [[]]
far_proximity_primary_wall_sprite_matrix = [[]]
far_proximity_secondary_wall_sprite_matrix = [[]]
far_proximity_entity_and_shadow_sprite_group_matrix = [[[]]]
far_proximity_entity_sprite_group_matrix = [[[]]] #For faster sprite sorting

#Lists
far_proximity_shadow_sprite_group_list = [pygame.sprite.GroupSingle(hero.shadow)] #For faster drawing on screen

far_proximity_entity_sprites_list = []
far_proximity_character_sprites_list = [] #For faster collision type handling
far_proximity_item_sprites_list = [] #For faster collision type handling
far_proximity_projectile_sprites_list = [] #For faster collision type handling

far_proximity_level_collider_sprites_list = [] #For faster update_position
far_proximity_primary_wall_sprites_list = [] #For faster update_position
far_proximity_secondary_wall_sprites_list = [] #For faster update_position
far_proximity_level_water_sprites_list = [] #For faster update_position - animation to be implemented

#Initialization
def initialize_player():
    hero.tile_index = level_painter.player_starting_tile
    hero.prevous_tile_index = level_painter.player_starting_tile
    hero.map_position = TILE_SIZE[X]//2+(48*hero.tile_index[1])+screen_width//2, TILE_SIZE[Y]//2+(48*hero.tile_index[0]+screen_height//2)

def initialize_level_matrices():
    initialize_level_sprites_matrix(level_sprites_matrix)
    initialize_level_sprites_matrix(primary_wall_sprites_matrix)
    initialize_level_sprites_matrix(secondary_wall_sprites_matrix)

def initialize_level_sprites_matrix(matrix):
    global level_sprites_matrix
    global primary_wall_sprites_matrix
    global secondary_wall_sprites_matrix

    new_level_matrix = []

    x = len(level_layout)
    y = len(level_layout[0])
    for _ in range(x):
        row = []
        for _ in range (y):
            row.append(0)
        new_level_matrix.append(row)

    if matrix == level_sprites_matrix:
        level_sprites_matrix = new_level_matrix
    elif matrix == primary_wall_sprites_matrix:
        primary_wall_sprites_matrix = new_level_matrix
    elif matrix == secondary_wall_sprites_matrix:
        secondary_wall_sprites_matrix = new_level_matrix

def initialize_all_entities_and_shadows_sprite_group_matrix():
    global all_entity_and_shadow_sprite_group_matrix
    
    all_entity_and_shadow_sprite_group_matrix = []
    x = len(level_layout)
    y = len(level_layout[0])
    
    for _ in range(x):
        row = []

        for _ in range (y):
            row.append([])
        all_entity_and_shadow_sprite_group_matrix.append(row)

def initialize_far_proximity_matrix_and_lists(matrix_type):
    if matrix_type == far_proximity_level_sprite_matrix:
        initialize_far_proximity_level_sprite_matrix()
        initialize_far_proximity_primary_wall_sprite_matrix()
        initialize_far_proximity_secondary_wall_sprite_matrix()
        initialize_far_proximity_level_collider_and_water_sprites_list()
        initialize_far_proximity_primary_wall_sprites_list()
        initialize_far_proximity_secondary_wall_sprites_list()
    
    elif matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
        initialize_far_proximity_entity_and_shadow_sprite_group_matrix()
        initialize_far_proximity_all_entities_and_shadows_sprite_group_lists()
        initialize_far_proximity_entity_sprite_group_matrix()

def initialize_far_proximity_level_sprite_matrix():
    global far_proximity_level_sprite_matrix
    
    matrix = []
    for row in far_proximity_index_matrix:
        new_tiles_row = []
        for cell in row:
            if 0 <= cell[0] < len(level_layout) and 0 <= cell[1] < len(level_layout[0]):
                tile_sprite = level_sprites_matrix[cell[0]][cell[1]]
                new_tiles_row.append(tile_sprite)
        if len(new_tiles_row) > 0:
            matrix.append(new_tiles_row)

    far_proximity_level_sprite_matrix = matrix 

def initialize_far_proximity_primary_wall_sprite_matrix():
    global far_proximity_primary_wall_sprite_matrix
    
    matrix = []
    for row in far_proximity_index_matrix:
        new_tiles_row = []
        for cell in row:
            if 0 <= cell[0] < len(level_layout) and 0 <= cell[1] < len(level_layout[0]):
                tile_sprite = primary_wall_sprites_matrix[cell[0]][cell[1]]
                new_tiles_row.append(tile_sprite)
        if len(new_tiles_row) > 0:
            matrix.append(new_tiles_row)

    far_proximity_primary_wall_sprite_matrix = matrix

def initialize_far_proximity_secondary_wall_sprite_matrix():
    global far_proximity_secondary_wall_sprite_matrix
    
    matrix = []
    for row in far_proximity_index_matrix:
        new_tiles_row = []
        for cell in row:
            if 0 <= cell[0] < len(level_layout) and 0 <= cell[1] < len(level_layout[0]):
                tile_sprite = secondary_wall_sprites_matrix[cell[0]][cell[1]]
                new_tiles_row.append(tile_sprite)
        if len(new_tiles_row) > 0:
            matrix.append(new_tiles_row)

    far_proximity_secondary_wall_sprite_matrix = matrix

def initialize_far_proximity_entity_and_shadow_sprite_group_matrix():
    global far_proximity_entity_and_shadow_sprite_group_matrix

    matrix = []
    for row in far_proximity_index_matrix:
        new_list = []
        for cell in row:
            if 0 <= cell[0] < len(level_layout) and 0 <= cell[1] < len(level_layout[0]):
                entity_and_shadow_sprite_groups_list = all_entity_and_shadow_sprite_group_matrix[cell[0]][cell[1]]
                new_list.append(entity_and_shadow_sprite_groups_list)

        if len(new_list) > 0:
            matrix.append(new_list)

    far_proximity_entity_and_shadow_sprite_group_matrix = matrix 

def initialize_far_proximity_entity_sprite_group_matrix():
    global far_proximity_entity_sprite_group_matrix
    
    matrix = []
    for row in far_proximity_entity_and_shadow_sprite_group_matrix:
        new_row = []

        for cell in row:
            entities = []

            for object in cell:
                if object.sprite.TYPE is not SHADOW:
                    entities.append(object)
            new_row.append(entities)
        
        matrix.append(new_row)
    
    far_proximity_entity_sprite_group_matrix = matrix

def initialize_far_proximity_level_collider_and_water_sprites_list():
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list

    for row in far_proximity_level_sprite_matrix:
        for tile in row:
            if tile.TYPE in IMPASSABLE_TILES:
                far_proximity_level_collider_sprites_list.append(tile)
                if tile.TYPE == WATER:
                    far_proximity_level_water_sprites_list.append(tile)

def initialize_far_proximity_primary_wall_sprites_list():
    global far_proximity_primary_wall_sprites_list

    for row in far_proximity_primary_wall_sprite_matrix:
        for tile in row:
            if tile != 0:
                far_proximity_primary_wall_sprites_list.append(tile)

def initialize_far_proximity_secondary_wall_sprites_list():
    global far_proximity_secondary_wall_sprites_list

    for row in far_proximity_secondary_wall_sprite_matrix:
        for tile in row:
            if tile != 0:
                far_proximity_secondary_wall_sprites_list.append(tile)

def initialize_far_proximity_all_entities_and_shadows_sprite_group_lists():
    global far_proximity_shadow_sprite_group_list

    global far_proximity_entity_sprites_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list

    for row in far_proximity_entity_and_shadow_sprite_group_matrix:
        for object_sprite_group_list in row:
            for object_sprite_group in object_sprite_group_list:
                if object_sprite_group.sprite.TYPE == SHADOW:
                    far_proximity_shadow_sprite_group_list.append(object_sprite_group)
                else:
                    far_proximity_entity_sprites_list.append(object_sprite_group.sprite)
                    if object_sprite_group.sprite.TYPE == MONSTER:
                        far_proximity_character_sprites_list.append(object_sprite_group.sprite)
                    
                    elif object_sprite_group.sprite.TYPE == ITEM:
                        far_proximity_item_sprites_list.append(object_sprite_group.sprite)

                    elif object_sprite_group.sprite.TYPE == PROJECTILE:
                        far_proximity_projectile_sprites_list.append(object_sprite_group.sprite)

def finish_init():
    hero.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(hero.tile_index)
    hero.direct_proximity_collision_tiles = get_direct_proximity_objects_list(hero.direct_proximity_index_matrix)
    hero.direct_proximity_monsters = get_direct_proximity_objects_list(hero.direct_proximity_index_matrix, MONSTER)

#Getters
def get_entity_sprite_group_by_id_from_matrix_cell(entity_id, tile_index, type=SHADOW):
    if type == SHADOW:
        for shadow in all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]:
            if shadow.sprite.TYPE is SHADOW and shadow.sprite.id == entity_id:
                return shadow
    
    elif type == MONSTER:
        for entity in all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]:
            if entity.sprite.TYPE is MONSTER and entity.sprite.id == entity_id:
                return entity
    
    elif type == PLAYER:
        for entity in all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]:
            if entity.sprite.TYPE is PLAYER and entity.sprite.id == entity_id:
                return entity

    elif type == ITEM:
        for entity in all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]:
            if entity.sprite.TYPE is ITEM and entity.sprite.id == entity_id:
                return entity
    
def get_direct_proximity_objects_list(matrix, object_type = IMPASSABLE_TILES):
    if object_type == IMPASSABLE_TILES:
        direct_proximity_impassable_tile_sprites = []
        for row in matrix:
            for tile_index in row:
                if level_sprites_matrix[tile_index[0]][tile_index[1]].passable == False:
                    direct_proximity_impassable_tile_sprites.append(level_sprites_matrix[tile_index[0]][tile_index[1]])
                
        return direct_proximity_impassable_tile_sprites
    
    elif object_type == MONSTER:
        direct_proximity_monster_sprites = []
        for row in matrix:
            for tile_index in row:
                for entity in all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]:
                    if entity.sprite.TYPE == MONSTER:
                        direct_proximity_monster_sprites.append(entity.sprite)
        
        return direct_proximity_monster_sprites

def get_entity_sprite_by_id(entity_id):
    for monster in all_monsters:
        if monster.id == entity_id:
            return monster

def get_far_proximity_entity_and_shadow_matrix_index(tile_index):
    i = 0
    for row in far_proximity_index_matrix:
        if row[0][0] >= 0:
            j = 0
            for cell in row:
                if cell[1] >= 0:
                    if cell == tile_index:
                        return i,j
                    else:
                        j += 1
            i += 1

#Objects updates
def update_all_objects_in_far_proximity():
    hero.update()

    for character_sprite in far_proximity_character_sprites_list:
        character_sprite.update()

    for shadow_sprite_group in far_proximity_shadow_sprite_group_list:
        shadow_sprite_group.sprite.update()

    for item_sprite in far_proximity_item_sprites_list:
        item_sprite.update()

    for projectile_sprite in far_proximity_projectile_sprites_list:
        projectile_sprite.update()

    for primary_wall_sprite in far_proximity_primary_wall_sprites_list:
        primary_wall_sprite.update()
    
    for secondary_wall_sprite in far_proximity_secondary_wall_sprites_list:
        secondary_wall_sprite.update()

    for water_sprite in far_proximity_level_water_sprites_list:
        water_sprite.update()

def update_all_objects_position_in_far_proximity():
    if round(hero.speed_scalar[0],2) != 0.00 or round(hero.speed_scalar[1],2) != 0.00:
        hero.update_position(hero.speed_vector)
        update_far_proximity_non_player_entities_position(far_proximity_character_sprites_list)
        update_far_proximity_non_player_entities_position(far_proximity_item_sprites_list)
        update_far_proximity_level_colliders_position()
        update_far_proximity_primary_walls_position()
        update_far_proximity_secondary_walls_position()

def update_far_proximity_non_player_entities_position(entities, vector=None):
    for entity in entities:
        if entity is not hero:
            entity.update_position(vector)

def update_far_proximity_level_colliders_position():
    for tile in far_proximity_level_collider_sprites_list:
        tile.update_position()

def update_far_proximity_primary_walls_position():
    for tile in far_proximity_primary_wall_sprites_list:
        tile.update_position()

def update_far_proximity_secondary_walls_position():
    for tile in far_proximity_secondary_wall_sprites_list:
        tile.update_position()

def update_all_nearby_monsters_and_self_direct_proximity_monsters_lists(direct_proximity_matrix):
    for row in direct_proximity_matrix:
        for tile_index in row:
            for entity in all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]:
                if entity.sprite.TYPE == MONSTER:
                    monster = entity.sprite
                    monster.direct_proximity_monsters = get_direct_proximity_objects_list(monster.direct_proximity_index_matrix, MONSTER)

##### Matrix updates #####
def update_far_proximity_matrices_and_lists(offset = None):
    update_far_proximity_index_matrix(offset)
    
    update_far_proximity_matrix_and_lists(far_proximity_entity_and_shadow_sprite_group_matrix, offset)
    update_far_proximity_matrix_and_lists(far_proximity_level_sprite_matrix, offset)
    update_far_proximity_matrix_and_lists(far_proximity_primary_wall_sprite_matrix, offset)
    update_far_proximity_matrix_and_lists(far_proximity_secondary_wall_sprite_matrix, offset)

def update_far_proximity_index_matrix(offset = None):
    global far_proximity_index_matrix

    size = screen_height // TILE_SIZE[Y] + far_matrix_offset_y, screen_width // TILE_SIZE[X] + far_matrix_offset_x

    if offset == None:
        far_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(hero.tile_index, size)
    else:
        new_entities_and_shadows_row = []
        if offset[0] == 1:
            del far_proximity_index_matrix[0]
            for index in far_proximity_index_matrix[-1]:
                new_tile_index = index[0]+1, index[1]
                new_entities_and_shadows_row.append(new_tile_index)
            far_proximity_index_matrix.append(new_entities_and_shadows_row)

        elif offset[0] == -1:
            del far_proximity_index_matrix[-1]
            for index in far_proximity_index_matrix[0]:
                new_tile_index = index[0]-1, index[1]
                new_entities_and_shadows_row.append(new_tile_index)
            far_proximity_index_matrix.insert(0, new_entities_and_shadows_row)

        if offset[1] == 1:
            for row in far_proximity_index_matrix:
                del row[0]
                new_tile_index = row[-1][0], row[-1][1]+1
                row.append(new_tile_index)

        elif offset[1] == -1:          
            for row in far_proximity_index_matrix:
                del row[-1]
                new_tile_index = row[0][0], row[0][1]-1
                row.insert(0, new_tile_index)

def update_far_proximity_matrix_and_lists(matrix_type, offset = None):
    if offset == None:
        initialize_far_proximity_matrix_and_lists(matrix_type)
    else:
        offset_far_proximity_matrix_and_update_lists(matrix_type, offset)

def offset_far_proximity_matrix_and_update_lists(matrix_type, offset):
    corrected_y_offset_matrix = None
    if offset[0] != 0 and offset[1] != 0:
        corrected_y_offset_matrix = get_diagonal_corrected_far_proximity_index_matrix(offset[1])
        if offset[0] == 1:
            remove_first_row_from_matrix_and_objects_from_lists(matrix_type)
            append_last_row_to_matrix_and_objects_to_lists(matrix_type, corrected_y_offset_matrix)

        elif offset[0] == -1:
            remove_last_row_from_matrix_and_objects_from_lists(matrix_type)
            insert_first_row_in_matrix_and_append_objects_to_lists(matrix_type, corrected_y_offset_matrix)
    else:
        if offset[0] == 1:
            remove_first_row_from_matrix_and_objects_from_lists(matrix_type)
            append_last_row_to_matrix_and_objects_to_lists(matrix_type, far_proximity_index_matrix)

        elif offset[0] == -1:
            remove_last_row_from_matrix_and_objects_from_lists(matrix_type)
            insert_first_row_in_matrix_and_append_objects_to_lists(matrix_type, far_proximity_index_matrix)

    if offset[1] == 1:
        remove_first_col_from_matrix_and_objects_from_lists(matrix_type)
        append_last_col_to_matrix_and_objects_to_lists(matrix_type)

    elif offset[1] == -1:
        remove_last_col_from_matrix_and_objects_from_lists(matrix_type)
        insert_first_col_in_matrix_and_append_objects_to_lists(matrix_type)
 
### X MATRIX OFFSET ### 
#X = +1
def remove_first_row_from_matrix_and_objects_from_lists(matrix_type):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_entity_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list
    
    #Entities and shadows (3D MATRIX)
    if far_proximity_index_matrix[0][0][0] > 0: 
        if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix: #3D MATRIX
            for cell in far_proximity_entity_and_shadow_sprite_group_matrix[0]:
                for object in cell:
                    if object.sprite.TYPE is not SHADOW:
                        far_proximity_entity_sprites_list.remove(object.sprite)
                        if object.sprite.TYPE == MONSTER:
                            far_proximity_character_sprites_list.remove(object.sprite)

                        elif object.sprite.TYPE == ITEM:
                            far_proximity_item_sprites_list.remove(object.sprite)

                        elif object.sprite.TYPE == PROJECTILE:
                            far_proximity_projectile_sprites_list.remove(object.sprite)
                    else:
                        far_proximity_shadow_sprite_group_list.remove(object)

            del far_proximity_entity_and_shadow_sprite_group_matrix[0]
            del far_proximity_entity_sprite_group_matrix[0]

        #Level sprites (2D MATRIX)
        elif matrix_type == far_proximity_level_sprite_matrix:
            for tile in far_proximity_level_sprite_matrix[0]:
                if tile.TYPE in IMPASSABLE_TILES:
                    far_proximity_level_collider_sprites_list.remove(tile)
                    if tile.TYPE is WATER:
                        far_proximity_level_water_sprites_list.remove(tile)
            del far_proximity_level_sprite_matrix[0]

        elif matrix_type == far_proximity_primary_wall_sprite_matrix:
            for tile in far_proximity_primary_wall_sprite_matrix[0]:
                if tile != 0:
                    far_proximity_primary_wall_sprites_list.remove(tile)
            del far_proximity_primary_wall_sprite_matrix[0]

        elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
            for tile in far_proximity_secondary_wall_sprite_matrix[0]:
                if tile != 0:
                    far_proximity_secondary_wall_sprites_list.remove(tile)
            del far_proximity_secondary_wall_sprite_matrix[0]

def append_last_row_to_matrix_and_objects_to_lists(matrix_type, tile_indices_matrix):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_entity_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_entity_sprites_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list
    
    if tile_indices_matrix[-1][0][0] < len(level_layout):

        #Entities and shadows (3D MATRIX)
        if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
            new_entities_and_shadows_row = []
            new_entities_row = []
            
            for tile_index in tile_indices_matrix[-1]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    objects = all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]
                    new_entities_and_shadows_row.append(objects)
                    new_entities_cell = []
                    
                    for object in objects:
                        if object.sprite.TYPE is not SHADOW:
                            far_proximity_entity_sprites_list.append(object.sprite)
                            new_entities_cell.append(object)
                            if object.sprite.TYPE is MONSTER:
                                far_proximity_character_sprites_list.append(object.sprite)

                            elif object.sprite.TYPE is ITEM:
                                far_proximity_item_sprites_list.append(object.sprite)

                            elif object.sprite.TYPE is PROJECTILE:
                                far_proximity_projectile_sprites_list.append(object.sprite)                                
                        else:
                            far_proximity_shadow_sprite_group_list.append(object)
                    new_entities_row.append(new_entities_cell)

            far_proximity_entity_and_shadow_sprite_group_matrix.append(new_entities_and_shadows_row)
            far_proximity_entity_sprite_group_matrix.append(new_entities_row)

        #Level sprites (2D MATRIX)
        elif matrix_type == far_proximity_level_sprite_matrix:
            new_level_tiles_row = []
            
            for tile_index in tile_indices_matrix[-1]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    tile = level_sprites_matrix[tile_index[0]][tile_index[1]]
                    new_level_tiles_row.append(tile)
                    if tile.TYPE in IMPASSABLE_TILES:
                        far_proximity_level_collider_sprites_list.append(tile)
                        if tile.TYPE == WATER:
                            far_proximity_level_water_sprites_list.append(tile)  
            far_proximity_level_sprite_matrix.append(new_level_tiles_row)

        elif matrix_type == far_proximity_primary_wall_sprite_matrix:
            new_level_tiles_row = []
            
            for tile_index in tile_indices_matrix[-1]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    tile = primary_wall_sprites_matrix[tile_index[0]][tile_index[1]]
                    new_level_tiles_row.append(tile)
                    if tile != 0:
                        far_proximity_primary_wall_sprites_list.append(tile)
            far_proximity_primary_wall_sprite_matrix.append(new_level_tiles_row)

        elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
            new_level_tiles_row = []
            
            for tile_index in tile_indices_matrix[-1]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    tile = secondary_wall_sprites_matrix[tile_index[0]][tile_index[1]]
                    new_level_tiles_row.append(tile)
                    if tile != 0:
                        far_proximity_secondary_wall_sprites_list.append(tile)
            far_proximity_secondary_wall_sprite_matrix.append(new_level_tiles_row)

#X = -1
def remove_last_row_from_matrix_and_objects_from_lists(matrix_type):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_entity_sprite_group_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list
    
    if far_proximity_index_matrix[-1][0][0] < len(level_layout)-1: 
        
        #Entities and shadows (3D MATRIX)
        if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
            for cell in far_proximity_entity_and_shadow_sprite_group_matrix[-1]:
                for object in cell:
                    if object.sprite.TYPE is not SHADOW:
                        far_proximity_entity_sprites_list.remove(object.sprite)
                        if object.sprite.TYPE == MONSTER:
                            far_proximity_character_sprites_list.remove(object.sprite)

                        elif object.sprite.TYPE == ITEM:
                            far_proximity_item_sprites_list.remove(object.sprite)

                        elif object.sprite.TYPE == PROJECTILE:
                            far_proximity_projectile_sprites_list.remove(object.sprite)
                    else:
                        far_proximity_shadow_sprite_group_list.remove(object)

            del far_proximity_entity_and_shadow_sprite_group_matrix[-1]
            del far_proximity_entity_sprite_group_matrix[-1]

        #Level sprites (2D MATRIX)
        elif matrix_type == far_proximity_level_sprite_matrix:
            for tile in far_proximity_level_sprite_matrix[-1]:
                if tile.TYPE in IMPASSABLE_TILES:
                    far_proximity_level_collider_sprites_list.remove(tile)
                    if tile.TYPE is WATER:
                        far_proximity_level_water_sprites_list.remove(tile)
            del far_proximity_level_sprite_matrix[-1]

        elif matrix_type == far_proximity_primary_wall_sprite_matrix:
            for tile in far_proximity_primary_wall_sprite_matrix[-1]:
                if tile != 0:
                    far_proximity_primary_wall_sprites_list.remove(tile)
            del far_proximity_primary_wall_sprite_matrix[-1]

        elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
            for tile in far_proximity_secondary_wall_sprite_matrix[-1]:
                if tile != 0:
                    far_proximity_secondary_wall_sprites_list.remove(tile)
            del far_proximity_secondary_wall_sprite_matrix[-1]

def insert_first_row_in_matrix_and_append_objects_to_lists(matrix_type, tile_indices_matrix):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_entity_sprites_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list

    if tile_indices_matrix[0][0][0] >= 0:

        #Entities and shadows (3D MATRIX)
        if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
            new_entities_and_shadows_row = []
            new_entities_row = []

            for tile_index in tile_indices_matrix[0]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    objects = all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]]
                    new_entities_and_shadows_row.append(objects)
                    new_entities_cell = []

                    for object in objects:
                        if object.sprite.TYPE is not SHADOW:
                            new_entities_cell.append(object)
                            far_proximity_entity_sprites_list.append(object.sprite)
                            if object.sprite.TYPE is MONSTER:
                                far_proximity_character_sprites_list.append(object.sprite)

                            elif object.sprite.TYPE is ITEM:
                                far_proximity_item_sprites_list.append(object.sprite)

                            elif object.sprite.TYPE is PROJECTILE:
                                far_proximity_projectile_sprites_list.append(object.sprite)                                
                        else:
                            far_proximity_shadow_sprite_group_list.append(object)
                    new_entities_row.append(new_entities_cell)

            far_proximity_entity_and_shadow_sprite_group_matrix.insert(0, new_entities_and_shadows_row)
            far_proximity_entity_sprite_group_matrix.insert(0, new_entities_row)

        #Level sprites (2D MATRIX)
        elif matrix_type == far_proximity_level_sprite_matrix:
            new_level_tiles_row = []
            
            for tile_index in tile_indices_matrix[0]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    tile = level_sprites_matrix[tile_index[0]][tile_index[1]]
                    new_level_tiles_row.append(tile)
                    if tile.TYPE in IMPASSABLE_TILES:
                        far_proximity_level_collider_sprites_list.append(tile)
                        if tile.TYPE == WATER:
                            far_proximity_level_water_sprites_list.append(tile)
            far_proximity_level_sprite_matrix.insert(0, new_level_tiles_row)

        elif matrix_type == far_proximity_primary_wall_sprite_matrix:
            new_level_tiles_row = []
            
            for tile_index in tile_indices_matrix[0]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    tile = primary_wall_sprites_matrix[tile_index[0]][tile_index[1]]
                    new_level_tiles_row.append(tile)
                    if tile != 0:
                        far_proximity_primary_wall_sprites_list.append(tile)
            far_proximity_primary_wall_sprite_matrix.insert(0, new_level_tiles_row)

        elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
            new_level_tiles_row = []
            
            for tile_index in tile_indices_matrix[0]:
                if 0 <= tile_index[1] < len(level_layout[0]):
                    tile = secondary_wall_sprites_matrix[tile_index[0]][tile_index[1]]
                    new_level_tiles_row.append(tile)
                    if tile != 0:
                        far_proximity_secondary_wall_sprites_list.append(tile)
            far_proximity_secondary_wall_sprite_matrix.insert(0, new_level_tiles_row)

### Y MATRIX OFFSET ###
#Y = +1
def remove_first_col_from_matrix_and_objects_from_lists(matrix_type):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list
    
    if far_proximity_index_matrix[0][0][1] > 0:

        #Entities and shadows (3D MATRIX)
        if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
            for i, objects_row in enumerate(far_proximity_entity_and_shadow_sprite_group_matrix):
                for object in objects_row[0]:
                    
                    if object.sprite.TYPE is not SHADOW:
                        far_proximity_entity_sprites_list.remove(object.sprite)
                        if object.sprite.TYPE is MONSTER:
                            far_proximity_character_sprites_list.remove(object.sprite)
                        elif object.sprite.TYPE is ITEM:
                            far_proximity_item_sprites_list.remove(object.sprite)
                        elif object.sprite.TYPE is PROJECTILE:
                            far_proximity_projectile_sprites_list.remove(object.sprite)
                    else:
                        far_proximity_shadow_sprite_group_list.remove(object)

                del far_proximity_entity_and_shadow_sprite_group_matrix[i][0]
                del far_proximity_entity_sprite_group_matrix[i][0]

        #Level sprites (2D MATRIX)
        elif matrix_type == far_proximity_level_sprite_matrix:
            for i, tile_row in enumerate(far_proximity_level_sprite_matrix):
                if tile_row[0].TYPE in IMPASSABLE_TILES:
                    far_proximity_level_collider_sprites_list.remove(tile_row[0])
                    if tile_row[0].TYPE == WATER:
                        far_proximity_level_water_sprites_list.remove(tile_row[0])
                del far_proximity_level_sprite_matrix[i][0]

        elif matrix_type == far_proximity_primary_wall_sprite_matrix:
            for i, tile_row in enumerate(far_proximity_primary_wall_sprite_matrix):
                if tile_row[0] != 0:
                    far_proximity_primary_wall_sprites_list.remove(tile_row[0])      
                del far_proximity_primary_wall_sprite_matrix[i][0]

        elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
            for i, tile_row in enumerate(far_proximity_secondary_wall_sprite_matrix):
                if tile_row[0] != 0:
                    far_proximity_secondary_wall_sprites_list.remove(tile_row[0])      
                del far_proximity_secondary_wall_sprite_matrix[i][0]
                
def append_last_col_to_matrix_and_objects_to_lists(matrix_type):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_entity_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_entity_sprites_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list

    i = 0
    for row_indices in far_proximity_index_matrix:
        if 0 <= row_indices[-1][0] < len(level_layout) and row_indices[-1][1] < len(level_layout[0]):
            
            #Entities and shadows (3D MATRIX)
            if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
                objects = all_entity_and_shadow_sprite_group_matrix[row_indices[-1][0]][row_indices[-1][1]]
                far_proximity_entity_and_shadow_sprite_group_matrix[i].append(objects)
                entities = []

                for object in objects:
                    if object.sprite.TYPE is not SHADOW:
                        entities.append(object)
                        far_proximity_entity_sprites_list.append(object.sprite)
                        if object.sprite.TYPE is MONSTER:
                            far_proximity_character_sprites_list.append(object.sprite)

                        elif object.sprite.TYPE is ITEM:
                            far_proximity_item_sprites_list.append(object.sprite)

                        elif object.sprite.TYPE is PROJECTILE:
                            far_proximity_projectile_sprites_list.append(object.sprite)
                    else:
                        far_proximity_shadow_sprite_group_list.append(object)
                far_proximity_entity_sprite_group_matrix[i].append(entities)

            #Level sprites (2D MATRIX)
            elif matrix_type == far_proximity_level_sprite_matrix:
                tile = level_sprites_matrix[row_indices[-1][0]][row_indices[-1][1]]
                far_proximity_level_sprite_matrix[i].append(tile)
                if tile.TYPE in IMPASSABLE_TILES:
                    far_proximity_level_collider_sprites_list.append(tile)
                    if tile.TYPE is WATER:
                        far_proximity_level_water_sprites_list.append(tile)

            elif matrix_type == far_proximity_primary_wall_sprite_matrix:
                tile = primary_wall_sprites_matrix[row_indices[-1][0]][row_indices[-1][1]]
                far_proximity_primary_wall_sprite_matrix[i].append(tile)
                if tile != 0:
                    far_proximity_primary_wall_sprites_list.append(tile)

            elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
                tile = secondary_wall_sprites_matrix[row_indices[-1][0]][row_indices[-1][1]]
                far_proximity_secondary_wall_sprite_matrix[i].append(tile)
                if tile != 0:
                    far_proximity_secondary_wall_sprites_list.append(tile)
            i += 1

#Y = -1
def remove_last_col_from_matrix_and_objects_from_lists(matrix_type):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_entity_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list

    if far_proximity_index_matrix[0][-1][1] < len(level_layout[0])-1:
        
        #Entities and shadows (3D MATRIX)
        if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
            for i, objects_row in enumerate(far_proximity_entity_and_shadow_sprite_group_matrix):
                for object in objects_row[-1]:
        
                    if object.sprite.TYPE is not SHADOW:
                        far_proximity_entity_sprites_list.remove(object.sprite)
                        if object.sprite.TYPE is MONSTER:
                            far_proximity_character_sprites_list.remove(object.sprite)
                        elif object.sprite.TYPE is ITEM:
                            far_proximity_item_sprites_list.remove(object.sprite)
                        elif object.sprite.TYPE is PROJECTILE:
                            far_proximity_projectile_sprites_list.remove(object.sprite)
                    else:
                        far_proximity_shadow_sprite_group_list.remove(object)

                del far_proximity_entity_and_shadow_sprite_group_matrix[i][-1]
                del far_proximity_entity_sprite_group_matrix[i][-1]

        #Level sprites (2D MATRIX)
        elif matrix_type == far_proximity_level_sprite_matrix:
            for i, tile_row in enumerate(far_proximity_level_sprite_matrix):
                if tile_row[-1].TYPE in IMPASSABLE_TILES:
                    far_proximity_level_collider_sprites_list.remove(tile_row[-1])
                    if tile_row[-1].TYPE is WATER:
                        far_proximity_level_water_sprites_list.remove(tile_row[-1])
                del far_proximity_level_sprite_matrix[i][-1]

        elif matrix_type == far_proximity_primary_wall_sprite_matrix:
            for i, tile_row in enumerate(far_proximity_primary_wall_sprite_matrix):
                if tile_row[-1] != 0:
                    far_proximity_primary_wall_sprites_list.remove(tile_row[-1])      
                del far_proximity_primary_wall_sprite_matrix[i][-1]

        elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
            for i, tile_row in enumerate(far_proximity_secondary_wall_sprite_matrix):
                if tile_row[-1] != 0:
                    far_proximity_secondary_wall_sprites_list.remove(tile_row[-1])      
                del far_proximity_secondary_wall_sprite_matrix[i][-1]
                    
def insert_first_col_in_matrix_and_append_objects_to_lists(matrix_type):
    global far_proximity_entity_and_shadow_sprite_group_matrix
    global far_proximity_entity_sprite_group_matrix
    global far_proximity_level_sprite_matrix
    global far_proximity_primary_wall_sprite_matrix
    global far_proximity_secondary_wall_sprite_matrix

    global far_proximity_shadow_sprite_group_list
    global far_proximity_entity_sprites_list
    global far_proximity_character_sprites_list
    global far_proximity_item_sprites_list
    global far_proximity_projectile_sprites_list
    global far_proximity_level_collider_sprites_list
    global far_proximity_level_water_sprites_list
    global far_proximity_primary_wall_sprites_list
    global far_proximity_secondary_wall_sprites_list

    i = 0
    for row_indices in far_proximity_index_matrix:
        if 0 <= row_indices[0][0] < len(level_layout) and 0 <= row_indices[0][1]:

            #Entities and shadows (3D MATRIX)
            if matrix_type == far_proximity_entity_and_shadow_sprite_group_matrix:
                objects = all_entity_and_shadow_sprite_group_matrix[row_indices[0][0]][row_indices[0][1]]
                far_proximity_entity_and_shadow_sprite_group_matrix[i].insert(0, objects)
                entities = []

                for object in objects:
                    if object.sprite.TYPE is not SHADOW:
                        entities.append(object)
                        far_proximity_entity_sprites_list.append(object.sprite)
                        if object.sprite.TYPE is MONSTER:
                            far_proximity_character_sprites_list.append(object.sprite)

                        elif object.sprite.TYPE is ITEM:
                            far_proximity_item_sprites_list.append(object.sprite)

                        elif object.sprite.TYPE is PROJECTILE:
                            far_proximity_projectile_sprites_list.append(object.sprite)
                    else:
                        far_proximity_shadow_sprite_group_list.append(object)
                far_proximity_entity_sprite_group_matrix[i].insert(0,entities)
        
            #Level sprites (2D MATRIX)
            elif matrix_type == far_proximity_level_sprite_matrix:
                tile = level_sprites_matrix[row_indices[0][0]][row_indices[0][1]]
                far_proximity_level_sprite_matrix[i].insert(0, tile)
                if tile.TYPE in IMPASSABLE_TILES:
                    far_proximity_level_collider_sprites_list.append(tile)
                    if tile.TYPE is WATER:
                        far_proximity_level_water_sprites_list.append(tile)

            elif matrix_type == far_proximity_primary_wall_sprite_matrix:
                tile = primary_wall_sprites_matrix[row_indices[0][0]][row_indices[0][1]]
                far_proximity_primary_wall_sprite_matrix[i].insert(0, tile)
                if tile != 0:
                    far_proximity_primary_wall_sprites_list.append(tile)

            elif matrix_type == far_proximity_secondary_wall_sprite_matrix:
                tile = secondary_wall_sprites_matrix[row_indices[0][0]][row_indices[0][1]]
                far_proximity_secondary_wall_sprite_matrix[i].insert(0, tile)
                if tile != 0:
                    far_proximity_secondary_wall_sprites_list.append(tile)
            i += 1

def get_diagonal_corrected_far_proximity_index_matrix(y_offset):
    matrix = []
    for row in far_proximity_index_matrix:
        new_matrix_row = []
        for cell in row:
            new_matrix_row.append(cell)
        matrix.append(new_matrix_row)

    for row in matrix:
        if y_offset == 1:
            del row[-1]
            row.insert(0, (row[0][0],row[0][1]-1))

        elif y_offset == -1:
            del row[0]
            row.append((row[-1][0],row[-1][1]+1))

    return matrix

#Entity matrix movement
def move_entity_in_all_matrices(entity_id, entity_type, old_tile_index, new_tile_index):
    entity_sprite_group = get_entity_sprite_group_by_id_from_matrix_cell(entity_id, old_tile_index, entity_type)
    shadow_sprite_group = get_entity_sprite_group_by_id_from_matrix_cell(entity_id, old_tile_index, SHADOW)

    all_entity_and_shadow_sprite_group_matrix[old_tile_index[0]][old_tile_index[1]].remove(entity_sprite_group)
    all_entity_and_shadow_sprite_group_matrix[old_tile_index[0]][old_tile_index[1]].remove(shadow_sprite_group)
    
    all_entity_and_shadow_sprite_group_matrix[new_tile_index[0]][new_tile_index[1]].append(entity_sprite_group)
    all_entity_and_shadow_sprite_group_matrix[new_tile_index[0]][new_tile_index[1]].append(shadow_sprite_group)


    if entity_is_in_far_proximity_matrix(new_tile_index):
        proximity_matrix_old_index = get_far_proximity_entity_and_shadow_matrix_index(old_tile_index)
        proximity_matrix_new_index = get_far_proximity_entity_and_shadow_matrix_index(new_tile_index)

        # util.print_matrix(far_proximity_entity_sprite_group_matrix)
        # util.print_matrix(far_proximity_entity_and_shadow_sprite_group_matrix)
        # far_proximity_entity_and_shadow_sprite_group_matrix[proximity_matrix_old_index[0]][proximity_matrix_old_index[1]].remove(entity_sprite_group)
        # far_proximity_entity_and_shadow_sprite_group_matrix[proximity_matrix_old_index[0]][proximity_matrix_old_index[1]].remove(shadow_sprite_group)
        far_proximity_entity_sprite_group_matrix[proximity_matrix_old_index[0]][proximity_matrix_old_index[1]].remove(entity_sprite_group)
        
        # far_proximity_entity_and_shadow_sprite_group_matrix[proximity_matrix_new_index[0]][proximity_matrix_new_index[1]].append(entity_sprite_group)
        # far_proximity_entity_and_shadow_sprite_group_matrix[proximity_matrix_new_index[0]][proximity_matrix_new_index[1]].append(shadow_sprite_group)
        far_proximity_entity_sprite_group_matrix[proximity_matrix_new_index[0]][proximity_matrix_new_index[1]].append(entity_sprite_group)

#Monster entities
def generate_monsters():
    generate_monster(ETTIN,(7,3))
    # generate_monster(ETTIN,(4,2))
    # generate_monster(ETTIN, (4,1))
    # generate_monster(ETTIN, (7,3))
    # generate_monster(ETTIN, (7,8))
    # generate_monster(ETTIN, (6,7))
    # generate_monster(ETTIN,(11,22))
    # generate_monster(ETTIN, (11,23))
    # generate_monster(ETTIN, (11,24))
    # generate_monster(ETTIN, (10,22))
    # generate_monster(ETTIN, (10,23))
    # generate_monster(ETTIN, (10,24))
    # generate_monster(ETTIN, (10,25))
    # generate_monster(ETTIN, (3,25))
    # generate_monster(ETTIN, (3,26))
    # generate_monster(ETTIN, (3,24))
    # generate_monster(ETTIN, (3,23))
    # generate_monster(ETTIN, (4,25))
    # generate_monster(ETTIN, (4,26))
    # generate_monster(ETTIN, (4,24))
    # generate_monster(ETTIN, (4,23))
    # generate_monster(ETTIN, (4,25))
    # generate_monster(ETTIN, (4,26))
    # generate_monster(ETTIN, (2,24))
    # generate_monster(ETTIN, (2,23))
    # generate_monster(ETTIN, (2,25))
    # generate_monster(ETTIN, (2,26))
    # generate_monster(ETTIN, (2,27))
    # generate_monster(ETTIN, (4,22))
    pass

def fill_map_with_monsters(density):
    for row in level_sprites_matrix:
        for tile in row:
            if tile.TYPE == FLOOR and tile.tile_index is not hero.tile_index:
                result = random.choice(range(1,101))
                if result <= density:
                    generate_monster(ETTIN,(tile.tile_index[0],tile.tile_index[1]))

def generate_monster(monster_type, tile_index):
    global all_entity_and_shadow_sprite_group_matrix
    global all_monsters

    if monster_type == ETTIN:
        monster = Ettin(tile_index)

    all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]].append(pygame.sprite.GroupSingle(monster))
    all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]].append(pygame.sprite.GroupSingle(monster.shadow))
    all_monsters.append(monster)

#Item entities
def generate_items():
    generate_item((8,5), EMERALD_CROSSBOW)

def generate_item(tile_index, item_name):
    global all_entity_and_shadow_sprite_group_matrix

    item = Item(tile_index, item_name)

    all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]].append(pygame.sprite.GroupSingle(item))
    all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]].append(pygame.sprite.GroupSingle(item.shadow))

def remove_item_from_the_map_and_give_to_player(item):
    tile_index = item.tile_index

    give_item_to_player(item)

    item_sprite_group = get_entity_sprite_group_by_id_from_matrix_cell(item.id, tile_index, type=ITEM)
    all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]].remove(item_sprite_group)
    far_proximity_entity_sprite_group_matrix[tile_index[0]][tile_index[1]].remove(item_sprite_group)

    shadow_sprite_group = get_entity_sprite_group_by_id_from_matrix_cell(item.id, tile_index, type=SHADOW)
    all_entity_and_shadow_sprite_group_matrix[tile_index[0]][tile_index[1]].remove(shadow_sprite_group)

    far_proximity_shadow_sprite_group_list.remove(shadow_sprite_group)
    far_proximity_entity_sprites_list.remove(item)
    far_proximity_item_sprites_list.remove(item)

def give_item_to_player(item):
    if item.is_weapon:
        hero.ammo[item.NAME] += item.ammo
        if hero.weapons[item.NAME] == False:
            hero.items.append(item)
            hero.weapons[item.NAME] = True
    
    elif item.is_ammo:
        hero.ammo[item.ammo_type] += item.ammo

#Misc
def wake_up_any_sleeping_monsters_in_far_proximity_matrix():
    for monster in far_proximity_character_sprites_list:
        if monster.monster_ai.is_idle:
            monster.monster_ai.is_waking_up = True

def fix_all_dead_objects_to_pixel_accuracy():
    for character in far_proximity_character_sprites_list:
        if character.is_living == False:
            character.map_position = math.ceil(character.map_position[0]), math.ceil(character.map_position[1])

def fix_player_position_to_pixel_accuracy():
    hero.map_position = math.floor(hero.map_position[0]), math.floor(hero.map_position[1])

def set_entity_screen_position(entity):
    position_x = player_position[0] + entity.sprite.map_position[0] - hero.map_position[0]
    position_y = player_position[1] + entity.sprite.map_position[1] - hero.map_position[1]

    entity.sprite.position = position_x,position_y

#Conditions
def entity_is_in_far_proximity_matrix(new_tile_index):
    if (far_proximity_index_matrix[0][0][0] <= new_tile_index[0] <= far_proximity_index_matrix[-1][0][0]) and (far_proximity_index_matrix[0][0][1] <= new_tile_index[1] <= far_proximity_index_matrix[0][-1][1]):
        return True
    return False