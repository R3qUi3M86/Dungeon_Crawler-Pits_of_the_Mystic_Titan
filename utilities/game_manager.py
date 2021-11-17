import random
from entities.characters import player
from utilities.constants import *
from utilities import entity_manager
from utilities.constants import SECTOR_N

acceleration_vector = 0,0
speed_vector = 0,0

def player_movement_collision():
    for movement_collision_sprite in entity_manager.movement_and_melee_collision_sprites:
        mask_collision_coordinates = pygame.sprite.collide_mask(player.PLAYER_SHADOW_SPRITE, movement_collision_sprite)
        if mask_collision_coordinates != None:
            adjust_player_movement_vector(mask_collision_coordinates)

def monster_collision(current_monster_movement_collision_sprite):
    for monster_movement_collision_sprite in entity_manager.movement_and_melee_collision_sprites:
        if current_monster_movement_collision_sprite.id == monster_movement_collision_sprite.id:
            pass
        else:
            mask_collision_coordinates = pygame.sprite.collide_mask(current_monster_movement_collision_sprite, monster_movement_collision_sprite)
            if mask_collision_coordinates != None:
                monster = entity_manager.get_monster_sprite(current_monster_movement_collision_sprite.id)
                adjust_monster_movement_vector(mask_collision_coordinates, monster, current_monster_movement_collision_sprite)

def adjust_player_movement_vector(mask_collision_coordinates):
    global speed_vector
    global acceleration_vector

    if mask_collision_coordinates[0] >= 23 and speed_vector[0] >= 0:
        acceleration_vector = 0, acceleration_vector[1]
        speed_vector = 0, speed_vector[1]
    if mask_collision_coordinates[0] <= 13 and speed_vector[0] <= 0:
        acceleration_vector = 0, acceleration_vector[1]
        speed_vector = 0, speed_vector[1]
    if mask_collision_coordinates[1] <= 10 and speed_vector[1] <= 0:
        acceleration_vector = acceleration_vector[0], 0
        speed_vector = speed_vector[0], 0
    if mask_collision_coordinates[1] > 10 and speed_vector[1] >= 0:
        acceleration_vector = acceleration_vector[0], 0
        speed_vector = speed_vector[0], 0

def adjust_monster_movement_vector(mask_collision_coordinates, monster, current_monster_movement_collision_sprite):
    east_collision_coordinate_X = 0
    west_collision_coordinate_X = 0
    north_collision_coordinate_Y = 0
    south_collision_coordinate_Y = 0

    if current_monster_movement_collision_sprite.shadow_size == SIZE_MEDIUM:
        east_collision_coordinate_X = 31
        west_collision_coordinate_X = 30
        north_collision_coordinate_Y = 12
        south_collision_coordinate_Y = 18
    elif current_monster_movement_collision_sprite.shadow_size == SIZE_SMALL or current_monster_movement_collision_sprite.shadow_size == SIZE_MEDIUM_SMALL:
        east_collision_coordinate_X = 23
        west_collision_coordinate_X = 13
        north_collision_coordinate_Y = 10
        south_collision_coordinate_Y = 10

    if mask_collision_coordinates[0] >= east_collision_coordinate_X and monster.walk_speed_vector[0] >= 0:
        monster.monster_ai.avoid_obstacle(SECTOR_E)
    elif mask_collision_coordinates[0] <= west_collision_coordinate_X and monster.walk_speed_vector[0] <= 0:
        monster.monster_ai.avoid_obstacle(SECTOR_W)
    elif mask_collision_coordinates[1] <= north_collision_coordinate_Y and monster.walk_speed_vector[1] <= 0:
        monster.monster_ai.avoid_obstacle(SECTOR_N)
    elif mask_collision_coordinates[1] > south_collision_coordinate_Y and monster.walk_speed_vector[1] >= 0:
        monster.monster_ai.avoid_obstacle(SECTOR_S)
