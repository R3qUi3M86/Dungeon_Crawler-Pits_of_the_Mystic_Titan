from entities.characters import unique_player_objects
from utilities.constants import *
from utilities import entity_manager
from utilities.constants import SECTOR_N

acceleration_vector = 0,0
speed_vector = 0,0
player_speed = 3
player_position_on_map = 0,0
player_tile_index = 0,0

def player_vs_monster_movement_collision():
    for movement_collision_sprite_group in entity_manager.player_and_monster_movement_collision_sprite_groups:
        if movement_collision_sprite_group == unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP:
            pass
        else:
            if unique_player_objects.PLAYER_SHADOW_SPRITE.rect.colliderect(movement_collision_sprite_group.sprite.rect):
                mask_collision_coordinates = pygame.sprite.collide_mask(unique_player_objects.PLAYER_SHADOW_SPRITE, movement_collision_sprite_group.sprite)
                if mask_collision_coordinates != None:
                    #collision_correction_vector = get_correction_vector(mask_collision_coordinates)
                    #entity_manager.update_all_non_player_entities_position_by_vector(collision_correction_vector)
                    #adjust_player_movement_vector(mask_collision_coordinates)
                    pass

def character_vs_level_movement_collision(entity):
    for movement_collision_sprite_group in entity_manager.level_collision_sprite_groups:
        if movement_collision_sprite_group == entity:
            pass
        else:
            if entity.sprite.rect.colliderect(movement_collision_sprite_group.sprite.rect):
                mask_collision_coordinates = pygame.sprite.collide_mask(entity.sprite, movement_collision_sprite_group.sprite)
                if mask_collision_coordinates != None:
                    correct_character_position_by_vector(movement_collision_sprite_group.sprite)

def monster_vs_monster_collision(current_monster_movement_collision_sprite):
    for movement_collision_sprite_group in entity_manager.player_and_monster_movement_collision_sprite_groups:
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

def correct_character_position_by_vector(colliding_entity):
    correction_vector = 0,0

    colliding_tile_index = colliding_entity.get_index()
    east_tile_index = colliding_tile_index[0],colliding_tile_index[1]+1
    west_tile_index = colliding_tile_index[0],colliding_tile_index[1]-1
    south_tile_index = colliding_tile_index[0]+1,colliding_tile_index[1]
    north_tile_index = colliding_tile_index[0]-1,colliding_tile_index[1]

    while any_sector_mask_collides(colliding_entity):
        if east_mask_collides(colliding_entity):
            correction_vector = -1,0
        elif west_mask_collides(colliding_entity):
            correction_vector = 1,0
        elif north_mask_collides(colliding_entity):
            correction_vector = 0,1
        elif south_mask_collides(colliding_entity):
            correction_vector = 0,-1

        if player_moving_east():
            if north_east_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,1
            elif south_east_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,-1

        elif player_moving_west():
            if north_west_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,1
            elif south_west_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,-1

        elif player_moving_north():
            if north_west_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,1
                else:
                    correction_vector = 1,0
            elif north_east_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,1
                else:
                    correction_vector = -1,0

        elif player_moving_south():
            if south_west_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = 1,0
            elif south_east_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = -1,0

        elif player_moving_north_east():
            if north_east_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(west_tile_index) == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = -1, 0
                elif entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0, 1
            elif north_west_mask_collides(colliding_entity):
                correction_vector = 0, 1
            elif south_east_mask_collides(colliding_entity):
                correction_vector = -1, 0

        elif player_moving_north_west():
            if north_west_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(east_tile_index) == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = 1, 0
                elif entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0, 1
            elif north_east_mask_collides(colliding_entity):
                correction_vector = 0, 1
            elif south_west_mask_collides(colliding_entity):
                correction_vector = 1, 0

        elif player_moving_south_east():
            if south_east_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(north_tile_index) == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,-1
                elif entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = -1,0
            elif north_east_mask_collides(colliding_entity):
                correction_vector = -1, 0
            elif south_west_mask_collides(colliding_entity):
                correction_vector = 0, -1

        elif player_moving_south_west():
            if south_west_mask_collides(colliding_entity):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(north_tile_index) == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,-1
                elif entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = 1,0
            elif north_west_mask_collides(colliding_entity):
                correction_vector = 1, 0
            elif south_east_mask_collides(colliding_entity):
                correction_vector = 0, -1

        entity_manager.update_all_non_player_entities_position_by_vector(correction_vector)

def player_moving_east():
    if speed_vector[0] > 0 and speed_vector[1] == 0:
        return True
    return False

def player_moving_west():
    if speed_vector[0] < 0 and speed_vector[1] == 0:
        return True
    return False

def player_moving_south():
    if speed_vector[1] > 0 and speed_vector[0] == 0:
        return True
    return False

def player_moving_north():
    if speed_vector[1] < 0 and speed_vector[0] == 0:
        return True
    return False

def player_moving_north_east():
    if speed_vector[0] > 0 and speed_vector[1] < 0:
        return True
    return False

def player_moving_south_east():
    if speed_vector[0] > 0 and speed_vector[1] > 0:
        return True
    return False

def player_moving_north_west():
    if speed_vector[0] < 0 and speed_vector[1] < 0:
        return True
    return False

def player_moving_south_west():
    if speed_vector[0] < 0 and speed_vector[1] > 0:
        return True
    return False

def east_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NE, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SE, colliding_entity) != None:
        return True
    return False

def west_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NW, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SW, colliding_entity) != None:
        return True
    return False

def north_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NE, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NW, colliding_entity) != None:
        return True
    return False

def south_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SE, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SW, colliding_entity) != None:
        return True
    return False

def north_east_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NE, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NW, colliding_entity) == None  and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SE, colliding_entity) == None:
        return True
    return False

def north_west_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NW, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NE, colliding_entity) == None  and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SW, colliding_entity) == None:
        return True
    return False

def south_east_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SE, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NE, colliding_entity) == None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SW, colliding_entity) == None:
        return True
    return False

def south_west_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SW, colliding_entity) != None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NW, colliding_entity) == None and pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SE, colliding_entity) == None:
        return True
    return False

def any_sector_mask_collides(colliding_entity):
    if pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NW, colliding_entity) != None or pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_NE, colliding_entity) != None or pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SW, colliding_entity) != None or pygame.sprite.collide_mask(unique_player_objects.PLAYER_COLISION_MASK_SE, colliding_entity) != None:
        return True
    return False