import numpy as np
import math
from utilities import constants
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


def get_total_angle(x,y):
    rel_x = x - center_x
    rel_y = center_y - y

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

def get_facing_direction(entity_pos,facing_position):
    set_center_coordinate(entity_pos[0],entity_pos[1])
    angle = get_total_angle(facing_position[0],facing_position[1])
    if angle >= 337.5 or angle < 22.5:
        return constants.SECTOR_E
    elif angle >= 22.5 and angle < 67.5:
        return constants.SECTOR_NE
    elif angle >= 67.5 and angle < 112.5:
        return constants.SECTOR_N
    elif angle >= 112.5 and angle < 157.5:
        return constants.SECTOR_NW
    elif angle >= 157.5 and angle < 202.5:
        return constants.SECTOR_W
    elif angle >= 202.5 and angle < 247.5:
        return constants.SECTOR_SW
    elif angle >= 247.5 and angle < 292.5:
        return constants.SECTOR_S
    elif angle >= 292.5 and angle < 337.5:
        return constants.SECTOR_SE