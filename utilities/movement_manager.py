from entities.characters import unique_player_objects
from utilities.constants import *
from utilities import entity_manager
from utilities import level_painter
from utilities.constants import SECTOR_N
from utilities.text_printer import debug_text

acceleration_vector = 0,0
speed_vector = 0,0
player_speed = 3
player_position_on_map = 0,0
player_tile_index = 0,0
pathfinding_matrix = []

def player_vs_monster_movement_collision():
    for monster_movement_collision_sprite_group in entity_manager.monster_movement_collision_sprite_groups:
        if unique_player_objects.PLAYER_SHADOW_SPRITE.rect.colliderect(monster_movement_collision_sprite_group.sprite.rect):
            mask_collision_coordinates = pygame.sprite.collide_mask(unique_player_objects.PLAYER_SHADOW_SPRITE, monster_movement_collision_sprite_group.sprite)
            if mask_collision_coordinates != None:
                bump_monster_back(unique_player_objects.HERO, entity_manager.get_monster_sprite(monster_movement_collision_sprite_group.sprite.id))
                adjust_player_movement_vector(mask_collision_coordinates)
                
def character_vs_level_movement_collision(entity):
    for level_collision_sprite_group in entity_manager.level_collision_sprite_groups:
            if entity.sprite.shadow.rect.colliderect(level_collision_sprite_group.sprite.rect) and any_sector_mask_collides(entity.sprite,level_collision_sprite_group.sprite):
                correct_character_position_by_vector(entity.sprite,level_collision_sprite_group.sprite)
                if entity.sprite.is_monster:
                    entity.sprite.monster_ai.is_avoiding_obstacle = False
                    entity.sprite.monster_ai.is_path_finding = True

def monster_vs_monster_collision(current_monster_movement_collision_sprite):
    for monster_movement_collision_sprite_group in entity_manager.monster_movement_collision_sprite_groups:
        movement_collision_sprite = monster_movement_collision_sprite_group.sprite
        if monster_movement_collision_sprite_group == unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP or current_monster_movement_collision_sprite == movement_collision_sprite:
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

def correct_character_position_by_vector(current_entity_sprite,colliding_entity_sprite):
    colliding_tile_index = colliding_entity_sprite.get_index()
    east_tile_index = colliding_tile_index[0],colliding_tile_index[1]+1
    west_tile_index = colliding_tile_index[0],colliding_tile_index[1]-1
    south_tile_index = colliding_tile_index[0]+1,colliding_tile_index[1]
    north_tile_index = colliding_tile_index[0]-1,colliding_tile_index[1]
    current_entity_speed_vector = None

    if current_entity_sprite == unique_player_objects.HERO:
        current_entity_speed_vector = speed_vector
    else:
        current_entity_speed_vector = current_entity_sprite.speed_vector

    correction_vector = 0,0
    while any_sector_mask_collides(current_entity_sprite,colliding_entity_sprite):
        if east_mask_collides(current_entity_sprite,colliding_entity_sprite):
            correction_vector = -1,0
        elif west_mask_collides(current_entity_sprite,colliding_entity_sprite):
            correction_vector = 1,0
        elif north_mask_collides(current_entity_sprite,colliding_entity_sprite):
            correction_vector = 0,1
        elif south_mask_collides(current_entity_sprite,colliding_entity_sprite):
            correction_vector = 0,-1

        if character_moving_east(current_entity_sprite):
            if north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,1
            elif south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,-1

        elif character_moving_west(current_entity_sprite):
            if north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,1
            elif south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,-1

        elif character_moving_north(current_entity_sprite):
            if north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,1
                else:
                    correction_vector = 1,0
            elif north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,1
                else:
                    correction_vector = -1,0

        elif character_moving_south(current_entity_sprite):
            if south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = 1,0
            elif south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = -1,0

        elif character_moving_north_east(current_entity_sprite):
            if north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(west_tile_index) == None:
                    correction_vector = -current_entity_speed_vector[0], -current_entity_speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = -1, 0
                elif entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0, 1
            elif north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = 0, 1
            elif south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = -1, 0

        elif character_moving_north_west(current_entity_sprite):
            if north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(east_tile_index) == None:
                    correction_vector = -current_entity_speed_vector[0], -current_entity_speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = 1, 0
                elif entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0, 1
            elif north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = 0, 1
            elif south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = 1, 0

        elif character_moving_south_east(current_entity_sprite):
            if south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(north_tile_index) == None:
                    correction_vector = -current_entity_speed_vector[0], -current_entity_speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,-1
                elif entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = -1,0
            elif north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = -1, 0
            elif south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = 0, -1

        elif character_moving_south_west(current_entity_sprite):
            if south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(north_tile_index) == None:
                    correction_vector = -current_entity_speed_vector[0], -current_entity_speed_vector[1]
                elif entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,-1
                elif entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = 1,0
            elif north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = 1, 0
            elif south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                correction_vector = 0, -1

        elif character_not_moving(current_entity_sprite):
            if north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(west_tile_index) == None:
                    correction_vector = 1, 1
                elif entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = -1, 0
                elif entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0, 1
            elif north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(south_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(east_tile_index) == None:
                    correction_vector = -1, 1
                elif entity_manager.get_level_collision_sprite_by_index(south_tile_index) != None:
                    correction_vector = 1, 0
                elif entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0, 1
            elif south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(west_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(north_tile_index) == None:
                    correction_vector = -1, -1
                elif entity_manager.get_level_collision_sprite_by_index(west_tile_index) != None:
                    correction_vector = 0,-1
                elif entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = -1,0
            elif south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
                if entity_manager.get_level_collision_sprite_by_index(east_tile_index) == None and entity_manager.get_level_collision_sprite_by_index(north_tile_index) == None:
                    correction_vector = 1, -1
                elif entity_manager.get_level_collision_sprite_by_index(east_tile_index) != None:
                    correction_vector = 0,-1
                elif entity_manager.get_level_collision_sprite_by_index(north_tile_index) != None:
                    correction_vector = 1,0

        if current_entity_sprite == unique_player_objects.HERO:
            entity_manager.update_all_non_player_entities_position_by_vector(correction_vector)
        else:
            current_entity_sprite.update_position((-correction_vector[0],-correction_vector[1]))

def bump_monster_back(player_sprite, monster_sprite):
    bounce_vector = 0,0

    if all_sector_mask_collide(player_sprite, monster_sprite.character_collision_shadow):
        if character_moving_east(player_sprite):
            bounce_vector = -1,0
        elif character_moving_west(player_sprite):
            bounce_vector = 1,0
        elif character_moving_north(player_sprite):
            bounce_vector = 0,1
        elif character_moving_south(player_sprite):
            bounce_vector = 0,-1
        elif character_moving_north_east(player_sprite):
            bounce_vector = -1,0.58
        elif character_moving_north_west(player_sprite):
            bounce_vector = 1,0.58
        elif character_moving_south_east(player_sprite):
            bounce_vector = -1,-0.58
        elif character_moving_south_west(player_sprite):
            bounce_vector = 1,-0.58
    elif east_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = 1,0
    elif west_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = -1,0
    elif north_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = 0,-1
    elif south_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = 0,1
    elif north_east_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = 1,-1
    elif north_west_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = -1,-1
    elif south_east_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = 1,1
    elif south_west_mask_collides(player_sprite, monster_sprite.character_collision_shadow):
        bounce_vector = -1,1

    debug_text(f"{bounce_vector}",'Black',10,50)
    monster_sprite.update_position((-bounce_vector[0],-bounce_vector[1]))

def character_moving_east(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] > 0 and speed_vector[1] == 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] > 0 and current_entity_sprite.speed_vector[1] == 0:
            return True
    return False

def character_moving_west(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] < 0 and speed_vector[1] == 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] < 0 and current_entity_sprite.speed_vector[1] == 0:
            return True
    return False

def character_moving_south(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[1] > 0 and speed_vector[0] == 0:
            return True
    else:
        if current_entity_sprite.speed_vector[1] > 0 and current_entity_sprite.speed_vector[0] == 0:
            return True
    return False

def character_moving_north(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[1] < 0 and speed_vector[0] == 0:
            return True
    else:
        if current_entity_sprite.speed_vector[1] < 0 and current_entity_sprite.speed_vector[0] == 0:
            return True
    return False

def character_moving_north_east(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] > 0 and speed_vector[1] < 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] > 0 and current_entity_sprite.speed_vector[1] < 0:
            return True
    return False

def character_moving_south_east(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] > 0 and speed_vector[1] > 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] > 0 and current_entity_sprite.speed_vector[1] > 0:
            return True
    return False

def character_moving_north_west(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] < 0 and speed_vector[1] < 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] < 0 and current_entity_sprite.speed_vector[1] < 0:
            return True
    return False

def character_moving_south_west(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] < 0 and speed_vector[1] > 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] < 0 and current_entity_sprite.speed_vector[1] > 0:
            return True
    return False

def character_not_moving(current_entity_sprite):
    if current_entity_sprite == unique_player_objects.HERO:
        if speed_vector[0] == 0 and speed_vector[1] == 0:
            return True
    else:
        if current_entity_sprite.speed_vector[0] == 0 and current_entity_sprite.speed_vector[1] == 0:
            return True
    return False

def east_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) != None:
        return True
    return False

def west_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) != None:
        return True
    return False

def north_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) != None:
        return True
    return False

def south_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) != None:
        return True
    return False

def north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) == None  and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) == None:
        return True
    return False

def north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) == None  and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) == None:
        return True
    return False

def south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) == None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) == None:
        return True
    return False

def south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) == None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) == None:
        return True
    return False

def any_sector_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) != None or pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) != None or pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) != None or pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) != None:
        return True
    return False

def all_sector_mask_collide(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_nw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_sw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.character_collision_mask_se, colliding_entity_sprite) != None:
        return True
    return False