import numpy as np
import math
from copy import deepcopy
from utilities.constants import *
from utilities import entity_manager
from utilities import level_painter
from entities.level.level import ENTRANCE, WALL, WATER
from settings import *

center_x = 0
center_y = 0

ne_quadrant = False
nw_quadrant = False
sw_quadrant = False
se_quadrant = False

quartants_list = [ne_quadrant,nw_quadrant,sw_quadrant,se_quadrant]

def set_center_coordinate(x, y):
    global center_x, center_y

    center_x = x
    center_y = y

def determine_quadrant(x,y):
    global quartants_list
    
    quartants_list = [False,False,False,False]

    if x >= 0 and y >= 0:
        quartants_list[0] = True
    
    elif x <= 0 and y >= 0:
        quartants_list[1] = True
    
    elif x <= 0 and y <= 0:
        quartants_list[2] = True

    else:
        quartants_list[3] = True

def get_total_angle(current_entity_pos,other_entity_pos):
    set_center_coordinate(current_entity_pos[0],current_entity_pos[1])

    rel_x = other_entity_pos[0] - center_x
    rel_y = center_y - other_entity_pos[1]

    r = math.sqrt((rel_x*rel_x) + (rel_y*rel_y))
    if r != 0:
        angle_deg = np.absolute((np.arcsin(rel_y/r)/(np.pi/2))*90)
    else:
        angle_deg = 0

    determine_quadrant(rel_x,rel_y)

    if quartants_list[0]:
        return angle_deg
    elif quartants_list[1]:
        return 180-angle_deg
    elif quartants_list[2]:
        return angle_deg + 180
    elif quartants_list[3]:
        return 360-angle_deg

def get_facing_direction(current_entity_pos,other_entity_pos):
    angle = get_total_angle(current_entity_pos,other_entity_pos)
    if angle >= 346.5 or angle < 13.5:
        return SECTOR_E
    elif angle >= 13.5 and angle < 55:
        return SECTOR_NE
    elif angle >= 55 and angle < 125:
        return SECTOR_N
    elif angle >= 125 and angle < 166.5:
        return SECTOR_NW
    elif angle >= 166.5 and angle < 193.5:
        return SECTOR_W
    elif angle >= 193.5 and angle < 235:
        return SECTOR_SW
    elif angle >= 235 and angle < 305:
        return SECTOR_S
    elif angle >= 305 and angle < 346.5:
        return SECTOR_SE

def get_travel_speed(angle, speed):
    x_factor = math.cos(math.radians(angle))
    y_factor = 0.55*math.sin(math.radians(angle))

    x_factored_speed = x_factor*speed
    y_factored_speed = y_factor*speed

    total_factored_speed = math.sqrt((x_factored_speed*x_factored_speed) + (y_factored_speed*y_factored_speed))

    x_factor_travel = math.cos(math.radians(angle))
    y_factor_travel = math.sin(math.radians(angle))

    travel_speed = x_factor_travel*total_factored_speed, -y_factor_travel*total_factored_speed

    return travel_speed

def generate_entity_id():
    if len(entity_manager.entities_id) == 0:
        entity_manager.entities_id.append(0)
        return entity_manager.entities_id[0]
    else:
        entity_manager.entities_id.append(len(entity_manager.entities_id))
        return entity_manager.entities_id[len(entity_manager.entities_id)-1]

def get_vicinity_matrix_indices_for_index(index_x_y, size=(3,3)):
    vicinity_matrix = []
    
    tile_index = index_x_y
    if tile_index[0] <= 0:
        tile_index = 1, tile_index[1]
    elif tile_index[0] >= len(level_painter.level_layout)-1:
        tile_index = len(level_painter.level_layout)-2, tile_index[1]

    if tile_index[1] <= 0:
        tile_index = tile_index[0], 1
    elif tile_index[1] >= len(level_painter.level_layout[0])-1:
        tile_index = tile_index[0], len(level_painter.level_layout[0])-2

    for i in range(size[0]):
        vicinity_matrix_row = []
        for j in range(size[1]):
            vicinity_matrix_row.append((tile_index[0]+i-size[0]//2,tile_index[1]+j-size[1]//2))
        
        vicinity_matrix.append(deepcopy(vicinity_matrix_row))

    return vicinity_matrix

def get_absolute_distance(entity1_map_pos, entity2_map_pos):
    x_abs_distance = abs(entity1_map_pos[0] - entity2_map_pos[0])
    y_abs_distance = abs(entity1_map_pos[1] - entity2_map_pos[1])

    distance = math.sqrt((x_abs_distance*x_abs_distance)+(y_abs_distance*y_abs_distance))

    return distance

def elipses_intersect(entity1_map_pos,entity2_map_pos,entity1_a_b,entity2_a_b):
    x_abs_distance = abs(entity1_map_pos[0] - entity2_map_pos[0])
    y_abs_distance = abs(entity1_map_pos[1] - entity2_map_pos[1])
    
    if x_abs_distance > (entity1_a_b[0]+entity2_a_b[0]) or y_abs_distance > (entity1_a_b[1]+entity2_a_b[1]):
        return False
    
    else:
        angle = get_total_angle(entity1_map_pos,entity2_map_pos)
        entity1_x_abs_reach = abs(entity1_a_b[0]*math.cos(math.radians(angle)))
        entity1_y_abs_reach = abs(entity1_a_b[1]*math.sin(math.radians(angle)))
        entity2_x_abs_reach = abs(entity2_a_b[0]*math.cos(math.radians(angle)))
        entity2_y_abs_reach = abs(entity2_a_b[1]*math.sin(math.radians(angle)))
        total_x_reach = entity1_x_abs_reach + entity2_x_abs_reach
        total_y_reach = entity1_y_abs_reach + entity2_y_abs_reach

        distance = math.sqrt((x_abs_distance*x_abs_distance)+(y_abs_distance*y_abs_distance))
        reach = math.sqrt((total_x_reach*total_x_reach)+(total_y_reach*total_y_reach))

        if distance < reach:
            return True
    
    return False

def get_tile_offset(prevous_tile_index, tile_index):
    offset_x = tile_index[X] - prevous_tile_index[X]
    offset_y = tile_index[Y] - prevous_tile_index[Y]

    return offset_x,offset_y

def get_tile_index(map_pos):
    return int(map_pos[1]-screen_height//2)//level_painter.TILE_SIZE[Y] , int(map_pos[0]-screen_width//2)//level_painter.TILE_SIZE[X]

def monster_has_line_of_sight(monster_map_pos, particle_speed = 10, max_travel_x = screen_width//2, max_travel_y = screen_height//2):
    hero_map_pos = entity_manager.hero.map_position
    angle = get_total_angle(monster_map_pos,hero_map_pos)
    particle_map_pos = monster_map_pos
    current_tile_index = get_tile_index(monster_map_pos)
    previous_tile_index = current_tile_index
    traveled_distance_x = 0
    traveled_distance_y = 0

    x_speed = particle_speed*math.cos(math.radians(angle))
    y_speed = -particle_speed*math.sin(math.radians(angle))

    while abs(traveled_distance_x) < max_travel_x and abs(traveled_distance_y) < max_travel_y:
        particle_map_pos = particle_map_pos[0] + x_speed, particle_map_pos[1] + y_speed
        current_tile_index = get_tile_index(particle_map_pos)
        traveled_distance_x = int(traveled_distance_x + x_speed)
        traveled_distance_y = int(traveled_distance_y + y_speed)
        
        if current_tile_index != previous_tile_index:
            previous_tile_index = current_tile_index
            
            if particle_collided_with_wall(current_tile_index):
                return False

        if particle_collided_with_player(hero_map_pos, particle_map_pos, particle_speed):
            return True
    
    return False

#Conditions
def particle_collided_with_player(hero_map_pos, particle_map_pos, particle_speed):
    if hero_map_pos[0]-particle_speed//2 <= particle_map_pos[0] <= hero_map_pos[0]+particle_speed//2 and hero_map_pos[1]-particle_speed//2 <= particle_map_pos[1] <= hero_map_pos[1]+particle_speed//2:
        return True
    return False

def particle_collided_with_wall(current_tile_index):
    if entity_manager.level_sprites_matrix[current_tile_index[0]][current_tile_index[1]].TYPE == WALL:
        return True
    return False

#Misc
print_limit = 20
tick = 0

def increment_print_matrix_timer(matrix, mode="S", add_monsters=False, add_items=False):
    global tick
    tick += 1
    if tick == print_limit:
        tick = 0
        print_matrix(matrix, mode, add_monsters, add_items)
        
def print_matrix(matrix, mode="S", add_monsters=False, add_items=False):
    if mode == "S":
        for row, matrix_row in enumerate(matrix):
            row_string = ""
            for col, cell in enumerate(matrix_row):
                
                if matrix == entity_manager.far_proximity_level_sprite_matrix:
                    if cell.TYPE in IMPASSABLE_TILES and cell.TYPE is not WATER:
                        row_string = row_string+"X"
                    elif cell.TYPE == WATER:
                        row_string = row_string+"~"
                    else:
                        row_string = row_string+"."

                elif matrix == entity_manager.far_proximity_entity_and_shadow_sprite_group_matrix or matrix == entity_manager.far_proximity_entity_sprite_group_matrix:
                    if cell:
                        for object in cell:
                            if object.sprite.TYPE == PLAYER:
                                row_string = row_string+"P"
                            elif object.sprite.TYPE == MONSTER:
                                row_string = row_string+"M"
                            elif object.sprite.TYPE == ITEM:
                                row_string = row_string+"i"
                            else:
                                row_string = row_string+"."
                            break
                    else:
                        row_string = row_string+"."
                
                elif matrix == entity_manager.level_sprites_matrix:
                    if cell.TYPE in IMPASSABLE_TILES and cell.TYPE is not WATER:
                        row_string = row_string+"X"
                    elif cell.TYPE == WATER:
                        row_string = row_string+"~"
                    else:
                        if add_monsters == True:
                            if row == entity_manager.hero.tile_index[0] and col == entity_manager.hero.tile_index[1]:
                                row_string = row_string+"P"
                            else:
                                entities = entity_manager.all_entity_and_shadow_sprite_group_matrix[row][col]
                                found_monster = False
                                corpse = False
                                for entity in entities:
                                    if entity.sprite.TYPE == MONSTER:
                                        found_monster = True
                                        if entity.sprite.is_corpse:
                                            corpse = True
                                        break
                                if found_monster:
                                    if not corpse:
                                        row_string = row_string+"M"
                                    else:
                                        row_string = row_string+"x"
                                        corpse = False
                                else: 
                                    row_string = row_string+"."

            print(row_string)

    else:
        for row in matrix:
            row_string = ""
            for col in row:
                row_string = row_string + str(col)
            
            print(row_string)

    print("")
    # print(entity_manager.far_proximity_level_collider_sprites_list)