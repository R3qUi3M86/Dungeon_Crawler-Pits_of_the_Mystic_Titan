from entities.characters import player
from utilities.constants import *
from utilities import entity_manager
from utilities.constants import SECTOR_N

acceleration_vector = 0,0
speed_vector = 0,0

def player_movement_collision():
    for movement_collision_sprite in entity_manager.movement_collision_sprites:
        mask_collision_coordinates = pygame.sprite.collide_mask(PLAYER_SHADOW_SPRITE, movement_collision_sprite)
        if mask_collision_coordinates != None:
            adjust_player_movement_vector(mask_collision_coordinates)            

def adjust_player_movement_vector(mask_collision_coordinates):
    global speed_vector
    global acceleration_vector

    if mask_collision_coordinates[0] >= 23 and speed_vector[0] >= 1:
        acceleration_vector = 0, acceleration_vector[1]
        speed_vector = 0, speed_vector[1]
    if mask_collision_coordinates[0] <= 13 and speed_vector[0] <= -1:
        acceleration_vector = 0, acceleration_vector[1]
        speed_vector = 0, speed_vector[1]
    if mask_collision_coordinates[1] <= 10 and speed_vector[1] <= -1:
        acceleration_vector = acceleration_vector[0], 0
        speed_vector = speed_vector[0], 0
    if mask_collision_coordinates[1] > 10 and speed_vector[1] >= 1:
        acceleration_vector = acceleration_vector[0], 0
        speed_vector = speed_vector[0], 0
