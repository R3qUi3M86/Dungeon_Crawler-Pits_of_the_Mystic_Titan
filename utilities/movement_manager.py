from entities.characters import unique_player_objects
from utilities.constants import *
from utilities import entity_manager
from utilities.constants import SECTOR_N

acceleration_vector = 0,0
speed_vector = 0,0
player_speed = 15.4
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
                    collision_correction_vector = get_all_entities_position_correction_vector(movement_collision_sprite_group.sprite)
                    entity_manager.update_all_non_player_entities_position(collision_correction_vector)
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

def get_all_entities_position_correction_vector(movement_collision_sprite):
    if speed_vector[0] > 0 and speed_vector[1] == 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_E)
    elif speed_vector[0] < 0 and speed_vector[1] == 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_W)
    elif speed_vector[0] == 0 and speed_vector[1] < 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_N)
    elif speed_vector[0] == 0 and speed_vector[1] > 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_S)
    elif speed_vector[0] > 0 and speed_vector[1] < 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_NE)
    elif speed_vector[0] > 0 and speed_vector[1] > 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_SE)
    elif speed_vector[0] < 0 and speed_vector[1] > 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_NW)
    elif speed_vector[0] < 0 and speed_vector[1] < 0:
        collision_correction_vector = create_correction_vector(movement_collision_sprite, SECTOR_SW)
    elif speed_vector[0] == 0 and speed_vector[1] == 0:
        collision_correction_vector = 0,0
    return collision_correction_vector

def adjust_player_movement_vector(mask_collision_coordinates):
    global speed_vector
    global acceleration_vector

    if mask_collision_coordinates[0] >= 23 and speed_vector[0] > 0:
        acceleration_vector = 0, acceleration_vector[1]
        speed_vector = 0, speed_vector[1]
    if mask_collision_coordinates[0] < 23 and speed_vector[0] < 0:
        acceleration_vector = 0, acceleration_vector[1]
        speed_vector = 0, speed_vector[1]
    if mask_collision_coordinates[1] <= 10 and speed_vector[1] < 0:
        acceleration_vector = acceleration_vector[0], 0
        speed_vector = speed_vector[0], 0
    if mask_collision_coordinates[1] > 10 and speed_vector[1] > 0:
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

def create_correction_vector(movement_collision_sprite, colliding_entity_sector):
    if colliding_entity_sector == SECTOR_E:
        offset = -20,0
    elif colliding_entity_sector == SECTOR_W:
        offset = 20,0
    elif colliding_entity_sector == SECTOR_N:
        offset = 0,20
    elif colliding_entity_sector == SECTOR_S:
        offset = 0,-20
    elif colliding_entity_sector == SECTOR_NE:
        offset = -15,15
    elif colliding_entity_sector == SECTOR_NW:
        offset = 15,15
    elif colliding_entity_sector == SECTOR_SE:
        offset = -15,-15
    elif colliding_entity_sector == SECTOR_SW:
        offset = 15,-15
    #print(unique_player_objects.PLAYER_SHADOW_SPRITE.mask.overlap_mask(movement_collision_sprite.mask, offset))
    return offset