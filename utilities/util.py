import numpy as np
import math
from copy import deepcopy
from utilities.constants import *
from utilities import entity_manager
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

def generate_entity_id():
    if len(entity_manager.entities_id) == 0:
        entity_manager.entities_id.append(0)
        return entity_manager.entities_id[0]
    else:
        entity_manager.entities_id.append(len(entity_manager.entities_id))
        return entity_manager.entities_id[len(entity_manager.entities_id)-1]

def get_vicinity_matrix_indices_for_index(index_x_y, size=(3,3)):
    vicinity_matrix = []
    for i in range(size[0]):
        vicinity_matrix_row = []
        for j in range(size[1]):
            vicinity_matrix_row.append((index_x_y[0]+i-size[0]//2,index_x_y[1]+j-size[1]//2))
        
        vicinity_matrix.append(deepcopy(vicinity_matrix_row))

    return vicinity_matrix
# def draw_pathfinding_path_for_monster(monster_index):
#     monster_sprite = entity_manager.get_entity_sprite_by_id(monster_index)
#     if monster_sprite != None:
#         monster_sprite.monster_ai.pathfinder.draw_path()