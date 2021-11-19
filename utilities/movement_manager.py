from entities.characters import unique_player_objects
from utilities.constants import *
from utilities import entity_manager
from utilities.constants import SECTOR_N

acceleration_vector = 0,0
speed_vector = 0,0
player_speed = 3
collision_correction_vector = 0,0

def player_movement_collision():
    global collision_correction_vector
    for movement_collision_sprite_group in entity_manager.movement_collision_sprite_groups:
        if movement_collision_sprite_group == unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP:
            pass
        else:
            if unique_player_objects.PLAYER_SHADOW_SPRITE.rect.colliderect(movement_collision_sprite_group.sprite.rect):
                mask_collision_coordinates = pygame.sprite.collide_mask(unique_player_objects.PLAYER_SHADOW_SPRITE, movement_collision_sprite_group.sprite)
                if mask_collision_coordinates != None:
                    collision_correction_vector = get_correction_vector(mask_collision_coordinates)
                    entity_manager.update_all_non_player_entities_player_position(collision_correction_vector)
                    adjust_player_movement_vector(mask_collision_coordinates)

def monster_collision(current_monster_movement_collision_sprite):
    for movement_collision_sprite_group in entity_manager.movement_collision_sprite_groups:
        movement_collision_sprite = movement_collision_sprite_group.sprite
        if movement_collision_sprite_group == unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP or current_monster_movement_collision_sprite == movement_collision_sprite:
            pass
        else:
            if movement_collision_sprite.rect.colliderect(current_monster_movement_collision_sprite):
                mask_collision_coordinates = pygame.sprite.collide_mask(current_monster_movement_collision_sprite, movement_collision_sprite)
                if mask_collision_coordinates != None:
                    monster = entity_manager.get_monster_sprite(current_monster_movement_collision_sprite.id)
                    adjust_monster_movement_vector(mask_collision_coordinates, monster, current_monster_movement_collision_sprite)

def adjust_player_movement_vector(mask_collision_coordinates):
    global speed_vector
    global acceleration_vector

    if mask_collision_coordinates[0] >= 20 and speed_vector[0] > 0:
        acceleration_vector = round(acceleration_vector[0]/3,2), acceleration_vector[1]
        speed_vector = round(speed_vector[0]/3,2), speed_vector[1]
    if mask_collision_coordinates[0] < 20 and speed_vector[0] < 0:
        acceleration_vector = round(acceleration_vector[0]/3,2), acceleration_vector[1]
        speed_vector = round(speed_vector[0]/3,2), speed_vector[1]
    if mask_collision_coordinates[1] <= 11 and speed_vector[1] < 0:
        acceleration_vector = acceleration_vector[0], round(acceleration_vector[1]/3,2)
        speed_vector = speed_vector[0], round(speed_vector[1]/3,2)
    if mask_collision_coordinates[1] > 11 and speed_vector[1] > 0:
        acceleration_vector = acceleration_vector[0], round(acceleration_vector[1]/3,2)
        speed_vector = speed_vector[0], round(speed_vector[1]/3,2)

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

def get_correction_vector(mask_collision_coordinates):
    correction_vector = 0,0

    if speed_vector[0] > 0 and speed_vector[1] == 0:
        #player moving East
        if mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] <= 9:
            #NorthWest mask sector
            correction_vector = 0, 1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] <= 9:
            #NorthEast mask sector
            correction_vector = 0, 1
        elif mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] > 9:
            #SouthWest mask sector
            correction_vector = 0, -1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] > 9:
            #SouthEast mask sector
            correction_vector = 0, -1

    elif speed_vector[0] > 0 and speed_vector[1] < 0:
        #player moving NorthEast
        if mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] <= 4:
            #NorthWest mask sector
            correction_vector = 1, 1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] <= 4:
            #NorthEast mask sector
            correction_vector = -1, 1
        elif mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] > 4:
            #SouthWest mask sector
            correction_vector = 1, -1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] > 4:
            #SouthEast mask sector
            correction_vector = -1, -1

    elif speed_vector[0] == 0 and speed_vector[1] < 0:
        #player moving North
        if mask_collision_coordinates[0] <= 15 and mask_collision_coordinates[1] <= 11:
            #NorthWest mask sector
            correction_vector = 1, 0
        elif mask_collision_coordinates[0] > 15 and mask_collision_coordinates[1] <= 11:
            #NorthEast mask sector
            correction_vector = -1, 0
        elif mask_collision_coordinates[0] <= 15 and mask_collision_coordinates[1] > 11:
            #SouthWest mask sector
            correction_vector = 1, 0
        elif mask_collision_coordinates[0] > 15 and mask_collision_coordinates[1] > 11:
            #SouthEast mask sector
            correction_vector = -1, 0

    elif speed_vector[0] < 0 and speed_vector[1] < 0:
        #player moving NorthWest
        if mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] <= 4:
            #NorthWest mask sector
            correction_vector = 1, 1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] <= 4:
            #NorthEast mask sector
            correction_vector = -1, 1
        elif mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] > 4:
            #SouthWest mask sector
            correction_vector = 1, -1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] > 4:
            #SouthEast mask sector
            correction_vector = -1, -1

    elif speed_vector[0] < 0 and speed_vector[1] == 0:
        #player moving West
        if mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] <= 9:
            #NorthWest mask sector
            correction_vector = 0, 1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] <= 9:
            #NorthEast mask sector
            correction_vector = 0, 1
        elif mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] > 9:
            #SouthWest mask sector
            correction_vector = 0, -1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] > 9:
            #SouthEast mask sector
            correction_vector = 0, -1

    elif speed_vector[0] < 0 and speed_vector[1] > 0:
        #player moving SouthWest
        if mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] <= 12:
            #NorthWest mask sector
            correction_vector = 1, 1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] <= 12:
            #NorthEast mask sector
            correction_vector = -1, 1
        elif mask_collision_coordinates[0] <= 20 and mask_collision_coordinates[1] > 12:
            #SouthWest mask sector
            correction_vector = 1, -1
        elif mask_collision_coordinates[0] > 20 and mask_collision_coordinates[1] > 12:
            #SouthEast mask sector
            correction_vector = -1, -1

    elif speed_vector[0] == 0 and speed_vector[1] > 0:
        #player moving South
        if mask_collision_coordinates[0] <= 15 and mask_collision_coordinates[1] <= 11:
            #NorthWest mask sector
            correction_vector = 1, 0
        elif mask_collision_coordinates[0] > 15 and mask_collision_coordinates[1] <= 11:
            #NorthEast mask sector
            correction_vector = -1, 0
        elif mask_collision_coordinates[0] <= 15 and mask_collision_coordinates[1] > 11:
            #SouthWest mask sector
            correction_vector = 1, 0
        elif mask_collision_coordinates[0] > 15 and mask_collision_coordinates[1] > 11:
            #SouthEast mask sector
            correction_vector = -1, 0

    elif speed_vector[0] > 0 and speed_vector[1] > 0:
        #player moving SouthEast
        if mask_collision_coordinates[0] <= 30 and mask_collision_coordinates[1] <= 13:
            #NorthWest mask sector
            correction_vector = 1, 1
        elif mask_collision_coordinates[0] > 30 and mask_collision_coordinates[1] <= 13:
            #NorthEast mask sector
            correction_vector = -1, 1
        elif mask_collision_coordinates[0] <= 30 and mask_collision_coordinates[1] > 13:
            #SouthWest mask sector
            correction_vector = 1, -1
        elif mask_collision_coordinates[0] > 30 and mask_collision_coordinates[1] > 13:
            #SouthEast mask sector
            correction_vector = -1, -1
    
    return correction_vector