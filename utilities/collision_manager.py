from utilities.constants import *
from utilities import entity_manager
from utilities import util

#Master function
def detect_all_collisions():

    for entity_sprite_group in entity_manager.entity_sprite_groups:
        entity = entity_sprite_group.sprite
        
        if entity is entity_manager.hero:
            player_vs_monster_movement_collision()
            entity_vs_level_collision(entity)

        elif entity.TYPE is MONSTER:
            monster_vs_monster_collision(entity)
            entity_vs_level_collision(entity)
        
        elif entity.TYPE is PROJECTILE:    
            projectile_collision(entity)
            entity_vs_level_collision(entity)

        elif entity.TYPE is ITEM:
            item_collision(entity)
            entity_vs_level_collision(entity)

#Collision types
def player_vs_monster_movement_collision():
    for entity_sprite_group in entity_manager.entity_sprite_groups:
        entity = entity_sprite_group.sprite
        hero = entity_manager.hero

        if entity is not hero and not entity.is_corpse and not entity.is_overkilled and hero.entity_collider_omni.rect.colliderect(entity.entity_collider_omni.rect):
            collision_matrix = get_collision_matrix(entity_manager.hero,entity)
                       
            if any_sector_collider_collides(collision_matrix):
                bump_monster_back(entity_manager.hero, entity, collision_matrix)
                #slow_down_player()
                
def entity_vs_level_collision(character):
    for level_collision_sprite in character.direct_proximity_collision_tiles:
        
        if character.entity_collider_omni.rect.colliderect(level_collision_sprite.rect):
            collision_matrix = get_collision_matrix(character,level_collision_sprite)
                        
            if any_sector_collider_collides(collision_matrix):
                correct_character_position_by_vector(character,level_collision_sprite, collision_matrix)

                if character.TYPE == MONSTER and character.monster_ai.is_path_finding == False and character.monster_ai.path_finding_is_ready:
                    character.monster_ai.initialize_monster_path_finding()

def monster_vs_monster_collision(monster):
    for entity_sprite_group in entity_manager.entity_sprite_groups:
        entity = entity_sprite_group.sprite
        
        if entity != monster and entity != entity_manager.hero and not entity.is_corpse and not entity.is_overkilled:
            monster_collider = monster.entity_collider_omni
            entity_collider = entity.entity_collider_omni.rect
            
            if monster_collider.rect.colliderect(entity_collider):
                collision_matrix = get_collision_matrix(monster,entity)

                if any_sector_collider_collides(collision_matrix):
                    adjust_monster_movement_vector(monster, collision_matrix)

def projectile_collision(projectile_sprite):
    #Projectile collision logic
    pass

def item_collision(item_sprite):
    #Item collision logic
    pass

#Movement vector adjustment
def slow_down_player():
    entity_manager.hero.speed_scalar = round(entity_manager.hero.speed_scalar[0]/3,2), round(entity_manager.hero.speed_scalar[1]/3,2)
    entity_manager.hero.speed_vector = round(entity_manager.hero.speed_vector[0]/3,2), round(entity_manager.hero.speed_scalar[1]/3,2)

def adjust_monster_movement_vector(monster, collision_matrix):

    if east_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_E)
    elif west_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_W)
    elif north_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_N)
    elif south_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_S)
    elif north_east_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_NE)
    elif north_west_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_NW)
    elif south_east_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_SE)
    elif south_west_collider_collides(collision_matrix):
        monster.monster_ai.avoid_obstacle(SECTOR_SW)

def adjust_player_speed_scalar(original_speed_scalar, correction_vector,factor=30):
    speed_scalar_x = correction_vector[0]*factor
    speed_scalar_y = correction_vector[1]*factor
    entity_manager.hero.speed_scalar = original_speed_scalar[0]+speed_scalar_x, original_speed_scalar[1]+speed_scalar_y

#Character bounce-back
def correct_character_position_by_vector(current_entity_sprite,colliding_entity_sprite, collision_matrix):
    colliding_tile_index = colliding_entity_sprite.get_index()
    east_tile_index = colliding_tile_index[0],colliding_tile_index[1]+1
    west_tile_index = colliding_tile_index[0],colliding_tile_index[1]-1
    south_tile_index = colliding_tile_index[0]+1,colliding_tile_index[1]
    north_tile_index = colliding_tile_index[0]-1,colliding_tile_index[1]
    
    level_collision_sprite_south = entity_manager.get_level_collision_sprite_by_index(south_tile_index)
    level_collision_sprite_north = entity_manager.get_level_collision_sprite_by_index(north_tile_index)
    level_collision_sprite_east = entity_manager.get_level_collision_sprite_by_index(east_tile_index)
    level_collision_sprite_west = entity_manager.get_level_collision_sprite_by_index(west_tile_index)

    current_collision_matrix = collision_matrix
    
    speed_vector = current_entity_sprite.speed_vector
    original_speed_scalar = 0,0
    if current_entity_sprite == entity_manager.hero:
        original_speed_scalar = entity_manager.hero.speed_scalar
    
    speed_correction_vector = 0,0
    correction_vector = 0,0

    while True:
        east_collision = east_collider_collides(current_collision_matrix)
        north_east_collision = north_east_collider_collides(current_collision_matrix)
        north_collision = north_collider_collides(current_collision_matrix)
        north_west_collision = north_west_collider_collides(current_collision_matrix)   
        west_collision = west_collider_collides(current_collision_matrix)
        south_west_collision = south_west_collider_collides(current_collision_matrix)
        south_collision = south_collider_collides(current_collision_matrix)
        south_east_collision = south_east_collider_collides(current_collision_matrix)
      
        if east_collision:
            correction_vector = -1,0

        elif west_collision:
            correction_vector = 1,0

        elif north_collision:
            correction_vector = 0,1

        elif south_collision:
            correction_vector = 0,-1

        elif character_moving_east(current_entity_sprite):
            if north_east_collision:
                if level_collision_sprite_south != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,1
            elif south_east_collision:
                if level_collision_sprite_north != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,-1
            elif north_west_collision:
                correction_vector = 1,1
            elif south_west_collision:
                correction_vector = 1,-1

        elif character_moving_west(current_entity_sprite):
            if north_west_collision:
                if level_collision_sprite_south != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,1
            elif south_west_collision:
                if level_collision_sprite_north != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,-1
            elif north_east_collision:
                correction_vector = -1,1
            elif south_east_collision:
                correction_vector = -1,-1

        elif character_moving_north(current_entity_sprite):
            if north_west_collision:
                if level_collision_sprite_east != None:
                    correction_vector = 0,1
                else:
                    correction_vector = 1,0
            elif north_east_collision:
                if level_collision_sprite_west != None:
                    correction_vector = 0,1
                else:
                    correction_vector = -1,0
            elif south_west_collision:
                correction_vector = 1,-1
            elif south_east_collision:
                correction_vector = -1,-1

        elif character_moving_south(current_entity_sprite):
            if south_west_collision:
                if level_collision_sprite_east != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = 1,0
            elif south_east_collision:
                if level_collision_sprite_west != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = -1,0
            elif north_west_collision:
                correction_vector = 1,1
            elif north_east_collision:
                correction_vector = -1,1

        elif character_moving_north_east(current_entity_sprite):
            if north_east_collision:
                if level_collision_sprite_south == None and level_collision_sprite_west == None:
                    correction_vector = -1*speed_vector[0], -1*speed_vector[1]
                elif level_collision_sprite_south != None:
                    correction_vector = -1, 0
                elif level_collision_sprite_west != None:
                    correction_vector = 0, 1
            elif north_west_collision:
                correction_vector = 0, 1
            elif south_east_collision:
                correction_vector = -1, 0
            elif south_west_collision:
                correction_vector = 1,-1

        elif character_moving_north_west(current_entity_sprite):
            if north_west_collision:
                if level_collision_sprite_south == None and level_collision_sprite_east == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif level_collision_sprite_south != None:
                    correction_vector = 1, 0
                elif level_collision_sprite_east != None:
                    correction_vector = 0, 1
            elif north_east_collision:
                correction_vector = 0, 1
            elif south_west_collision:
                correction_vector = 1, 0
            elif south_east_collision:
                correction_vector = -1,-1

        elif character_moving_south_east(current_entity_sprite):
            if south_east_collision:
                if level_collision_sprite_west == None and level_collision_sprite_north == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif level_collision_sprite_west != None:
                    correction_vector = 0,-1
                elif level_collision_sprite_north != None:
                    correction_vector = -1,0
            elif north_east_collision:
                correction_vector = -1, 0
            elif south_west_collision:
                correction_vector = 0, -1
            elif north_west_collision:
                correction_vector = 1,1

        elif character_moving_south_west(current_entity_sprite):
            if south_west_collision:
                if level_collision_sprite_east == None and level_collision_sprite_north == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif level_collision_sprite_east != None:
                    correction_vector = 0,-1
                elif level_collision_sprite_north != None:
                    correction_vector = 1,0
            elif north_west_collision:
                correction_vector = 1, 0
            elif south_east_collision:
                correction_vector = 0, -1
            elif north_east_collision:
                correction_vector = -1,1

        elif character_not_moving(current_entity_sprite):
            if north_east_collision:
                if level_collision_sprite_south == None and level_collision_sprite_west == None:
                    correction_vector = 1, 1
                elif level_collision_sprite_south != None:
                    correction_vector = -1, 0
                elif level_collision_sprite_west != None:
                    correction_vector = 0, 1
            elif north_west_collision:
                if level_collision_sprite_south == None and level_collision_sprite_east == None:
                    correction_vector = -1, 1
                elif level_collision_sprite_south != None:
                    correction_vector = 1, 0
                elif level_collision_sprite_east != None:
                    correction_vector = 0, 1
            elif south_east_collision:
                if level_collision_sprite_west == None and level_collision_sprite_north == None:
                    correction_vector = -1, -1
                elif level_collision_sprite_west != None:
                    correction_vector = 0,-1
                elif level_collision_sprite_north != None:
                    correction_vector = -1,0
            elif south_west_collision:
                if level_collision_sprite_east == None and level_collision_sprite_north == None:
                    correction_vector = 1, -1
                elif level_collision_sprite_east != None:
                    correction_vector = 0,-1
                elif level_collision_sprite_north != None:
                    correction_vector = 1,0

        if correction_vector[0] == 0 and correction_vector[1] == 0:
            break
        
        speed_correction_vector = correction_vector

        if current_entity_sprite == entity_manager.hero:
            adjust_player_speed_scalar(original_speed_scalar,speed_correction_vector,15)
            entity_manager.hero.update_position(correction_vector)
            entity_manager.update_all_non_player_entities_position_by_vector(correction_vector)
        
        else:
            current_entity_sprite.update_position((-2*correction_vector[0],-2*correction_vector[1]))
            current_entity_sprite.facing_direction = util.get_facing_direction(current_entity_sprite.map_position,current_entity_sprite.current_tile_map_position)
            current_entity_sprite.set_speed_vector()

        correction_vector = 0,0
        current_collision_matrix = get_collision_matrix(current_entity_sprite,colliding_entity_sprite)
        
def bump_monster_back(player_sprite, monster_sprite, collision_matrix):
    bounce_vector = 0,0

    if all_sector_colliders_collide(collision_matrix):
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
        elif character_not_moving(player_sprite):
            bounce_vector = get_bounce_vector_for_static_player(player_sprite, monster_sprite)
    elif east_collider_collides(collision_matrix):
        bounce_vector = 1,0
    elif west_collider_collides(collision_matrix):
        bounce_vector = -1,0
    elif north_collider_collides(collision_matrix):
        bounce_vector = 0,-1
    elif south_collider_collides(collision_matrix):
        bounce_vector = 0,1
    elif north_east_collider_collides(collision_matrix):
        bounce_vector = 1,-1
    elif north_west_collider_collides(collision_matrix):
        bounce_vector = -1,-1
    elif south_east_collider_collides(collision_matrix):
        bounce_vector = 1,1
    elif south_west_collider_collides(collision_matrix):
        bounce_vector = -1,1
    elif any_sector_collider_collides(collision_matrix):
        bounce_vector = get_bounce_vector_for_static_player(player_sprite, monster_sprite)

    monster_sprite.update_position((-bounce_vector[0],-bounce_vector[1]))
    adjust_player_speed_scalar(entity_manager.hero.speed_scalar,(-bounce_vector[0],-bounce_vector[1]),15)

def get_bounce_vector_for_static_player(player_sprite, monster_sprite):
    bounce_direction_sector = util.get_facing_direction(player_sprite.map_position, monster_sprite.map_position)
    
    if bounce_direction_sector == SECTOR_E:
        bounce_vector = 1,0
    elif bounce_direction_sector == SECTOR_NE:
        bounce_vector = 1,-1
    elif bounce_direction_sector == SECTOR_N:
        bounce_vector = 0,-1
    elif bounce_direction_sector == SECTOR_NW:
        bounce_vector = -1,-1
    elif bounce_direction_sector == SECTOR_W:
        bounce_vector = -1,0
    elif bounce_direction_sector == SECTOR_SW:
        bounce_vector = -1,1
    elif bounce_direction_sector == SECTOR_S:
        bounce_vector = 0,1
    elif bounce_direction_sector == SECTOR_SE:
        bounce_vector = 1,1
    
    return bounce_vector

#Collision getters
def get_ne_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE == TILE and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_ne, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_ne, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    return False

def get_nw_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE == TILE and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_nw, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_nw, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    return False

def get_se_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE == TILE and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_se, colliding_entity_sprite) != None:
        return True
        
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_se, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    return False

def get_sw_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE == TILE and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_sw, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_sw, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    return False

def get_collision_matrix(current_entity_sprite,colliding_entity_sprite):
    ne_collision = get_ne_collider_collision(current_entity_sprite,colliding_entity_sprite)
    nw_collision = get_nw_collider_collision(current_entity_sprite,colliding_entity_sprite)
    se_collision = get_se_collider_collision(current_entity_sprite,colliding_entity_sprite)
    sw_collision = get_sw_collider_collision(current_entity_sprite,colliding_entity_sprite)
    return [[nw_collision,ne_collision],[sw_collision,se_collision]]

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

def east_collider_collides(collision_matrix):
    if not collision_matrix[0][0] and collision_matrix[0][1] and not collision_matrix[1][0] and collision_matrix[1][1]:
        return True
    return False

def west_collider_collides(collision_matrix):
    if collision_matrix[0][0] and not collision_matrix[0][1] and collision_matrix[1][0] and not collision_matrix[1][1]:
        return True
    return False

def north_collider_collides(collision_matrix):
    if collision_matrix[0][0] and collision_matrix[0][1] and not collision_matrix[1][0] and not collision_matrix[1][1]:
        return True
    return False

def south_collider_collides(collision_matrix):
    if not collision_matrix[0][0] and not collision_matrix[0][1] and collision_matrix[1][0] and collision_matrix[1][1]:
        return True
    return False

def north_east_collider_collides(collision_matrix):
    if not collision_matrix[0][0] and collision_matrix[0][1] and not collision_matrix[1][0] and not collision_matrix[1][1]:
        return True
    return False

def north_west_collider_collides(collision_matrix):
    if collision_matrix[0][0] and not collision_matrix[0][1] and not collision_matrix[1][0] and not collision_matrix[1][1]:
        return True
    return False

def south_east_collider_collides(collision_matrix):
    if not collision_matrix[0][0] and not collision_matrix[0][1] and not collision_matrix[1][0] and collision_matrix[1][1]:
        return True
    return False

def south_west_collider_collides(collision_matrix):
    if not collision_matrix[0][0] and not collision_matrix[0][1] and collision_matrix[1][0] and not collision_matrix[1][1]:
        return True
    return False

def any_sector_collider_collides(collision_matrix):
    if collision_matrix[0][0] or collision_matrix[0][1] or collision_matrix[1][0] or collision_matrix[1][1]:
        return True
    return False

def all_sector_colliders_collide(collision_matrix):
    if collision_matrix[0][0] and collision_matrix[0][1] and collision_matrix[1][0] and collision_matrix[1][1]:
        return True
    return False
