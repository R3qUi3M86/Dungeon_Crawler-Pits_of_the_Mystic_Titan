from utilities.constants import *
from entities.characters import unique_player_object
from utilities import entity_manager

pathfinding_matrix = []

#Collision types
def player_vs_monster_movement_collision():
    for entity_sprite_group in entity_manager.entity_sprite_groups:
        if entity_sprite_group.sprite != unique_player_object.HERO and unique_player_object.HERO.entity_collision_mask.rect.colliderect(entity_sprite_group.sprite.entity_collision_mask.rect):
            mask_collision_coordinates = pygame.sprite.collide_mask(unique_player_object.HERO.entity_collision_mask, entity_sprite_group.sprite.entity_collision_mask.sprite)
            if mask_collision_coordinates != None:
                bump_monster_back(unique_player_object.HERO, entity_sprite_group.sprite)
                adjust_player_movement_vector(mask_collision_coordinates)
                
def character_vs_level_movement_collision(character):
    for level_collision_sprite_group in entity_manager.level_collision_sprite_groups:
        if character.sprite.entity_collision_mask.rect.colliderect(level_collision_sprite_group.sprite.rect) and any_sector_mask_collides(character.sprite,level_collision_sprite_group.sprite):
            correct_character_position_by_vector(character.sprite,level_collision_sprite_group.sprite)
            if character.sprite.is_monster:
                if character.sprite.monster_ai.is_path_finding == False and character.sprite.monster_ai.is_following_path == False:
                    character.sprite.monster_ai.reset_obstacle_avoidance_flags()
                    character.sprite.monster_ai.is_path_finding = True

def monster_vs_monster_collision(character):
    for entity_sprite_group in entity_manager.entity_sprite_groups:
        if character.sprite != unique_player_object.HERO and character != entity_sprite_group:
            character_collider = character.sprite.collision_mask
            entity_collider = entity_sprite_group.sprite.collision_mask
            if character_collider.rect.colliderect(entity_collider):
                if pygame.sprite.collide_mask(character_collider, entity_collider) != None:
                    adjust_monster_movement_vector(character.sprite, entity_sprite_group.sprite)

def projectile_collision(projectile):
    #Projectile collision logic
    pass

def item_collision(item):
    #Item collision logic
    pass

#Movement vector adjustment
def adjust_player_movement_vector(mask_collision_coordinates):
    if mask_collision_coordinates[0] >= 20 and unique_player_object.HERO.speed_vector[0] > 0:
        unique_player_object.HERO.speed_scalar = round(unique_player_object.HERO.speed_scalar[0]/3,2), unique_player_object.HERO.speed_scalar[1]
        unique_player_object.HERO.speed_vector = round(unique_player_object.HERO.speed_vector[0]/3,2), unique_player_object.HERO.speed_vector[1]
    if mask_collision_coordinates[0] < 20 and unique_player_object.HERO.speed_vector[0] < 0:
        unique_player_object.HERO.speed_scalar = round(unique_player_object.HERO.speed_scalar[0]/3,2), unique_player_object.HERO.speed_scalar[1]
        unique_player_object.HERO.speed_vector = round(unique_player_object.HERO.speed_vector[0]/3,2), unique_player_object.HERO.speed_vector[1]
    if mask_collision_coordinates[1] <= 11 and unique_player_object.HERO.speed_vector[1] < 0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[0], round(unique_player_object.HERO.speed_scalar[1]/3,2)
        unique_player_object.HERO.speed_vector = unique_player_object.HERO.speed_vector[0], round(unique_player_object.HERO.speed_vector[1]/3,2)
    if mask_collision_coordinates[1] > 11 and unique_player_object.HERO.speed_vector[1] > 0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[0], round(unique_player_object.HERO.speed_scalar[1]/3,2)
        unique_player_object.HERO.speed_vector = unique_player_object.HERO.speed_vector[0], round(unique_player_object.HERO.speed_vector[1]/3,2)

def adjust_monster_movement_vector(monster, current_monster_movement_collision_sprite):
    if east_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_E)
    elif west_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_W)
    elif north_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_N)
    elif south_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_S)
    elif north_east_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_NE)
    elif north_west_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_NW)
    elif south_east_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_SE)
    elif south_west_mask_collides(monster,current_monster_movement_collision_sprite):
        monster.monster_ai.avoid_obstacle(SECTOR_SW)

#Character bounce-back
def correct_character_position_by_vector(current_entity_sprite,colliding_entity_sprite):
    colliding_tile_index = colliding_entity_sprite.get_index()
    east_tile_index = colliding_tile_index[0],colliding_tile_index[1]+1
    west_tile_index = colliding_tile_index[0],colliding_tile_index[1]-1
    south_tile_index = colliding_tile_index[0]+1,colliding_tile_index[1]
    north_tile_index = colliding_tile_index[0]-1,colliding_tile_index[1]
    
    speed_vector = current_entity_sprite.speed_vector

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
                    correction_vector = -speed_vector[0], -speed_vector[1]
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
                    correction_vector = -speed_vector[0], -speed_vector[1]
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
                    correction_vector = -speed_vector[0], -speed_vector[1]
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
                    correction_vector = -speed_vector[0], -speed_vector[1]
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

        if current_entity_sprite == unique_player_object.HERO and (correction_vector[0] != 0 or correction_vector[1] != 0):
            unique_player_object.HERO.update_position(correction_vector)
            entity_manager.update_all_non_player_entities_position_by_vector(correction_vector)
        elif correction_vector[0] != 0 or correction_vector[1] != 0:
            current_entity_sprite.update_map_position_by_vector(correction_vector)
            current_entity_sprite.update_position((-correction_vector[0],-correction_vector[1]))

def bump_monster_back(player_sprite, monster_sprite):
    bounce_vector = 0,0

    if all_sector_mask_collide(player_sprite, monster_sprite.entity_collision_mask):
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
    elif east_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = 1,0
    elif west_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = -1,0
    elif north_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = 0,-1
    elif south_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = 0,1
    elif north_east_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = 1,-1
    elif north_west_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = -1,-1
    elif south_east_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = 1,1
    elif south_west_mask_collides(player_sprite, monster_sprite.entity_collision_mask):
        bounce_vector = -1,1

    monster_sprite.update_position((-bounce_vector[0],-bounce_vector[1]))
    monster_sprite.update_map_position_by_vector(bounce_vector)

#Conditions
def character_moving_east(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] > 0 and current_entity_sprite.speed_vector[1] == 0:
        return True
    return False

def character_moving_west(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] < 0 and current_entity_sprite.speed_vector[1] == 0:
        return True
    return False

def character_moving_south(current_entity_sprite):
    if current_entity_sprite.speed_vector[1] > 0 and current_entity_sprite.speed_vector[0] == 0:
        return True
    return False

def character_moving_north(current_entity_sprite):
    if current_entity_sprite.speed_vector[1] < 0 and current_entity_sprite.speed_vector[0] == 0:
        return True
    return False

def character_moving_north_east(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] > 0 and current_entity_sprite.speed_vector[1] < 0:
        return True
    return False

def character_moving_south_east(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] > 0 and current_entity_sprite.speed_vector[1] > 0:
        return True
    return False

def character_moving_north_west(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] < 0 and current_entity_sprite.speed_vector[1] < 0:
        return True
    return False

def character_moving_south_west(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] < 0 and current_entity_sprite.speed_vector[1] > 0:
        return True
    return False

def character_not_moving(current_entity_sprite):
    if current_entity_sprite.speed_vector[0] == 0 and current_entity_sprite.speed_vector[1] == 0:
        return True
    return False

def east_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) != None:
        return True
    return False

def west_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) != None:
        return True
    return False

def north_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) != None:
        return True
    return False

def south_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) != None:
        return True
    return False

def north_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) == None  and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) == None:
        return True
    return False

def north_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) == None  and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) == None:
        return True
    return False

def south_east_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) == None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) == None:
        return True
    return False

def south_west_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) == None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) == None:
        return True
    return False

def any_sector_mask_collides(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) != None or pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) != None or pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) != None or pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) != None:
        return True
    return False

def all_sector_mask_collide(current_entity_sprite,colliding_entity_sprite):
    if pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_nw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_ne, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_sw, colliding_entity_sprite) != None and pygame.sprite.collide_mask(current_entity_sprite.entity_collision_mask_se, colliding_entity_sprite) != None:
        return True
    return False