from math import sqrt
from utilities.constants import *
from utilities import entity_manager
from utilities import util
from utilities import level_painter

moving_to_next_level = False
wall_hider_timer = 0
wall_hider_timer_limit = 15

#Master function
def detect_all_collisions():
    global wall_hider_timer
    
    player_vs_monster_movement_collision()
    character_vs_level_collision(entity_manager.hero)
    
    if entity_manager.hero.speed_vector != 0:
        if wall_hider_timer == wall_hider_timer_limit:
            wall_hider_vs_obscuring_walls_collision()
            wall_hider_timer = 0
        else:
            wall_hider_timer += 1

    for character in entity_manager.far_proximity_character_sprites_list:
        monster_vs_monster_collision(character)
        character_vs_level_collision(character)

    for projectile in entity_manager.far_proximity_projectile_sprites_list:   
        projectile_vs_entity_collision(projectile)
        projectile_vs_level_collision(projectile)

    for item in entity_manager.far_proximity_item_sprites_list:
        player_vs_item_collision(item)
        if item.is_falling_apart:
            item_vs_level_collision(item)

        character_vs_impassable_item_collison(item)

#Collision types
def player_vs_monster_movement_collision():
    hero = entity_manager.hero
    
    for monster in entity_manager.hero.direct_proximity_monsters:
        if not monster.is_corpse and not monster.is_overkilled and monster.can_collide_with_player and util.elipses_intersect(hero.map_position, monster.map_position, hero.size, monster.size):
            collision_matrix = get_collision_matrix(entity_manager.hero, monster)
                       
            if any_sector_collider_collides(collision_matrix):
                bump_entity_back(entity_manager.hero, monster, collision_matrix)
                #slow_down_player()
                if monster.monster_ai.is_idle:
                    monster.monster_ai.is_waking_up = True
                
def character_vs_level_collision(character):
    global moving_to_next_level

    for level_collision_sprite in character.direct_proximity_collision_tiles:        
        if character.can_collide and not (level_collision_sprite.TYPE is WATER and FLYING in character.abilities) and character.entity_collider_omni.rect.colliderect(level_collision_sprite.rect):
            if character is entity_manager.hero and level_collision_sprite.is_exit_tile:
                moving_to_next_level = True
            
            collision_matrix = get_collision_matrix(character,level_collision_sprite)

            if any_sector_collider_collides(collision_matrix):
                correct_character_position_by_vector(character,level_collision_sprite, collision_matrix)
                 
                if character.TYPE == MONSTER and character.monster_ai.is_path_finding == False and character.monster_ai.path_finding_is_ready:
                    character.monster_ai.initialize_monster_path_finding()
                
                elif character.TYPE == MONSTER and character.monster_ai.is_following_path:
                    collision_matrix = get_collision_matrix(character, level_collision_sprite)
                    adjust_monster_movement_vector(character, collision_matrix)

def wall_hider_vs_obscuring_walls_collision():
    for secondary_wall_sprite in entity_manager.far_proximity_secondary_wall_sprites_list:
        if entity_manager.hero.wall_hider_collider.rect.colliderect(secondary_wall_sprite):
            
            if hero_is_above_wall_grid(secondary_wall_sprite.tile_index):
                secondary_wall_sprite.is_hiding_player = True
            else:
                secondary_wall_sprite.is_hiding_player = False
        else:
            secondary_wall_sprite.is_hiding_player = False

def monster_vs_monster_collision(monster):
    for character in monster.direct_proximity_monsters:
        
        if character.can_collide and character != monster and not character.is_corpse and not character.is_overkilled:            
            if util.elipses_intersect(monster.map_position, character.map_position, monster.size, character.size):
                collision_matrix = get_collision_matrix(monster, character)

                if any_sector_collider_collides(collision_matrix):
                    adjust_monster_movement_vector(monster, collision_matrix)

def projectile_vs_level_collision(projectile_sprite):
    for wall_like_tile in projectile_sprite.direct_proximity_wall_like_tiles:
        if wall_like_tile.rect.colliderect(projectile_sprite.projectile_collider.rect):
            if pygame.sprite.collide_mask(projectile_sprite.projectile_collider,wall_like_tile) and not projectile_sprite.is_disintegrating:
                projectile_sprite.has_impacted = True

def projectile_vs_entity_collision(projectile_sprite):
    for character in projectile_sprite.direct_proximity_characters:
        if not character.is_summoned and character.entity_collider_omni.rect.colliderect(projectile_sprite.projectile_collider.rect):
            if util.elipses_intersect(character.map_position, projectile_sprite.map_position, character.size, projectile_sprite.size) and not projectile_sprite.is_disintegrating and not projectile_sprite.has_impacted and not character.is_dead and not character.is_overkilled:
                projectile_sprite.has_impacted = True
                character.take_damage(projectile_sprite.damage)

    for item in projectile_sprite.direct_proximity_coolidable_items:
        if util.elipses_intersect(item.map_position, projectile_sprite.map_position, item.size, projectile_sprite.size) and not projectile_sprite.is_disintegrating and not projectile_sprite.has_impacted:
            projectile_sprite.has_impacted = True
            if item.is_destructible and not item.NAME is VASE:
                item.destroy_item()

def player_vs_item_collision(item_sprite):
    hero = entity_manager.hero

    if item_sprite.can_collide and util.elipses_intersect(hero.map_position, item_sprite.map_position, hero.size, item_sprite.size):
        if item_sprite.is_pickable:
            item_sprite.is_picked = True
        elif item_sprite.is_destructible and not item_sprite.is_falling_apart and not item_sprite.is_destroyed and pygame.sprite.collide_mask(hero.entity_collider_omni, item_sprite.entity_tiny_omni_collider):
            collision_matrix = get_collision_matrix(entity_manager.hero, item_sprite)
            bump_entity_back(hero, item_sprite, collision_matrix)
            item_sprite.destroy_item()
        elif pygame.sprite.collide_mask(hero.entity_collider_omni, item_sprite.entity_collider_omni):
            collision_matrix = get_collision_matrix(entity_manager.hero, item_sprite)
            bump_entity_back(hero, item_sprite, collision_matrix)

def character_vs_impassable_item_collison(item_sprite):
    if item_sprite.can_collide and not item_sprite.is_destructible and not item_sprite.is_pickable:
        for monster in entity_manager.far_proximity_character_sprites_list:
            if util.elipses_intersect(monster.map_position, item_sprite.map_position, monster.size, item_sprite.size):
                collision_matrix = get_collision_matrix(monster, item_sprite)
                if any_sector_collider_collides(collision_matrix):
                    if monster.monster_ai.is_path_finding == False and monster.monster_ai.path_finding_is_ready:
                        monster.monster_ai.initialize_monster_path_finding()
                    else:
                        adjust_monster_movement_vector(monster, collision_matrix)
        


def item_vs_level_collision(item_sprite):
    for collision_tile in item_sprite.direct_proximity_collision_tiles:
        if item_sprite.entity_small_square_collider.rect.colliderect(collision_tile.rect):
            item_sprite.speed = 0,0

#Movement vector adjustment
def slow_down_player(factor=3):
    entity_manager.hero.speed_scalar = round(entity_manager.hero.speed_scalar[0]/3,2), round(entity_manager.hero.speed_scalar[1]/factor,2)
    entity_manager.hero.speed_vector = round(entity_manager.hero.speed_vector[0]/3,2), round(entity_manager.hero.speed_scalar[1]/factor,2)

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
    colliding_tile_index = colliding_entity_sprite.tile_index
    east_tile_index = colliding_tile_index[0],colliding_tile_index[1]+1
    west_tile_index = colliding_tile_index[0],colliding_tile_index[1]-1
    south_tile_index = colliding_tile_index[0]+1,colliding_tile_index[1]
    north_tile_index = colliding_tile_index[0]-1,colliding_tile_index[1]
  
    if colliding_tile_index[0] == 0:
        level_collision_sprite_north = entity_manager.level_sprites_matrix[0][0]
    else:
        level_collision_sprite_north = entity_manager.level_sprites_matrix[north_tile_index[0]][north_tile_index[1]]        
        
    if colliding_tile_index[0] == len(level_painter.level_layout)-1:
        level_collision_sprite_south = entity_manager.level_sprites_matrix[0][0]
    else:
        level_collision_sprite_south = entity_manager.level_sprites_matrix[south_tile_index[0]][south_tile_index[1]]

    if colliding_tile_index[1] == len(level_painter.level_layout[0])-1:
        level_collision_sprite_east = entity_manager.level_sprites_matrix[0][0]
    else:
        level_collision_sprite_east = entity_manager.level_sprites_matrix[east_tile_index[0]][east_tile_index[1]]

    if colliding_tile_index[1] == 0:
        level_collision_sprite_west = entity_manager.level_sprites_matrix[0][0]
    else:
        level_collision_sprite_west = entity_manager.level_sprites_matrix[west_tile_index[0]][west_tile_index[1]]

    current_collision_matrix = collision_matrix
    

    original_speed_scalar = 0,0
    if current_entity_sprite == entity_manager.hero:
        original_speed_scalar = entity_manager.hero.speed_scalar
    
    speed_vector = current_entity_sprite.speed_vector
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
                    correction_vector = 0,1
                else:
                    correction_vector = -1,0
            elif south_east_collision:
                if level_collision_sprite_north != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = -1,0
            elif north_west_collision:
                correction_vector = 1,1
            elif south_west_collision:
                correction_vector = 1,-1

        elif character_moving_west(current_entity_sprite):
            if north_west_collision:
                if level_collision_sprite_south != None:
                    correction_vector = 0,1
                else:
                    correction_vector = 1,0
            elif south_west_collision:
                if level_collision_sprite_north != None:
                    correction_vector = 0,-1
                else:
                    correction_vector = 1,0
            elif north_east_collision:
                correction_vector = -1,1
            elif south_east_collision:
                correction_vector = -1,-1

        elif character_moving_north(current_entity_sprite):
            if north_west_collision:
                if level_collision_sprite_east != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,1
            elif north_east_collision:
                if level_collision_sprite_west != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,1
            elif south_west_collision:
                correction_vector = 1,-1
            elif south_east_collision:
                correction_vector = -1,-1

        elif character_moving_south(current_entity_sprite):
            if south_west_collision:
                if level_collision_sprite_east != None:
                    correction_vector = 1,0
                else:
                    correction_vector = 0,-1
            elif south_east_collision:
                if level_collision_sprite_west != None:
                    correction_vector = -1,0
                else:
                    correction_vector = 0,-1
            elif north_west_collision:
                correction_vector = 1,1
            elif north_east_collision:
                correction_vector = -1,1

        elif character_moving_north_east(current_entity_sprite):
            if north_east_collision:
                if level_collision_sprite_south == None and level_collision_sprite_west == None:
                    correction_vector = -speed_vector[0], -speed_vector[1]
                elif level_collision_sprite_south != None:
                    correction_vector = -1, 0
                elif level_collision_sprite_west != None:
                    correction_vector = 0, 1
            elif north_west_collision:
                correction_vector = 0, 1
            elif south_east_collision:
                correction_vector = -1,0
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
            entity_manager.update_far_proximity_non_player_entities_position(entity_manager.far_proximity_entity_sprites_list, correction_vector)
            entity_manager.update_far_proximity_level_colliders_position()
            entity_manager.update_far_proximity_primary_walls_position()
            entity_manager.update_far_proximity_secondary_walls_position()
        else:
            current_entity_sprite.update_position((-2*correction_vector[0],-2*correction_vector[1]))
            if entity_manager.level_sprites_matrix[colliding_tile_index[0]][colliding_tile_index[1]].is_convex == False:
                current_entity_sprite.facing_direction = util.get_facing_direction(current_entity_sprite.map_position,current_entity_sprite.current_tile_position)
            else:
                current_entity_sprite.facing_direction = util.get_facing_direction(current_entity_sprite.map_position,current_entity_sprite.previous_tile_position)
            current_entity_sprite.set_speed_vector()

        correction_vector = 0,0
        current_collision_matrix = get_collision_matrix(current_entity_sprite,colliding_entity_sprite)
        
def bump_entity_back(player_sprite, entity_sprite, collision_matrix):
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
            bounce_vector = get_bounce_vector_for_static_player(player_sprite, entity_sprite)
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
        bounce_vector = get_bounce_vector_for_static_player(player_sprite, entity_sprite)

    if entity_sprite.TYPE is not ITEM:
        entity_sprite.update_position((-bounce_vector[0],-bounce_vector[1]))
        adjust_player_speed_scalar(entity_manager.hero.speed_scalar,(-bounce_vector[0],-bounce_vector[1]),15)
    else:
        if entity_sprite.is_destructible:
            hero_x_speed = entity_manager.hero.speed_vector[0]
            hero_y_speed = entity_manager.hero.speed_vector[1]
            hero_abs_speed = sqrt(hero_x_speed*hero_x_speed+hero_y_speed*hero_y_speed)
            entity_sprite.speed = (-hero_abs_speed*bounce_vector[0],-hero_abs_speed*bounce_vector[1])
        else:
            adjust_player_speed_scalar(entity_manager.hero.speed_scalar,(-bounce_vector[0],-bounce_vector[1]),8)

def get_bounce_vector_for_static_player(player_sprite, entity_sprite):
    bounce_direction_sector = util.get_facing_direction(player_sprite.map_position, entity_sprite.map_position)
    
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
    if colliding_entity_sprite.TYPE in IMPASSABLE_TILES and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_ne, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_ne, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    elif colliding_entity_sprite.TYPE == ITEM:
        if colliding_entity_sprite.is_destructible and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_ne, colliding_entity_sprite.entity_tiny_omni_collider) != None:
            return True
        elif pygame.sprite.collide_mask(current_entity_sprite.entity_collider_ne, colliding_entity_sprite.entity_collider_omni) != None:
            return True
    return False

def get_nw_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE in IMPASSABLE_TILES and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_nw, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_nw, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    elif colliding_entity_sprite.TYPE == ITEM:
        if colliding_entity_sprite.is_destructible and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_nw, colliding_entity_sprite.entity_tiny_omni_collider) != None:
            return True
        elif pygame.sprite.collide_mask(current_entity_sprite.entity_collider_nw, colliding_entity_sprite.entity_collider_omni) != None:
            return True
    return False

def get_se_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE in IMPASSABLE_TILES and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_se, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_se, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    elif colliding_entity_sprite.TYPE == ITEM:
        if colliding_entity_sprite.is_destructible and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_se, colliding_entity_sprite.entity_tiny_omni_collider) != None:
            return True
        elif pygame.sprite.collide_mask(current_entity_sprite.entity_collider_se, colliding_entity_sprite.entity_collider_omni) != None:
            return True
    return False

def get_sw_collider_collision(current_entity_sprite,colliding_entity_sprite):
    if colliding_entity_sprite.TYPE in IMPASSABLE_TILES and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_sw, colliding_entity_sprite) != None:
        return True
    elif (colliding_entity_sprite.TYPE == MONSTER or colliding_entity_sprite.TYPE == PLAYER) and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_sw, colliding_entity_sprite.entity_collider_omni) != None:
        return True
    elif colliding_entity_sprite.TYPE == ITEM:
        if colliding_entity_sprite.is_destructible and pygame.sprite.collide_mask(current_entity_sprite.entity_collider_sw, colliding_entity_sprite.entity_tiny_omni_collider) != None:
            return True
        elif pygame.sprite.collide_mask(current_entity_sprite.entity_collider_sw, colliding_entity_sprite.entity_collider_omni) != None:
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

def hero_is_above_wall_grid(tile_index):
    hero = entity_manager.hero
    wall_grid_index = None

    if level_painter.level_layout[tile_index[0]+1][tile_index[1]] in WALL_LIKE:
        wall_grid_index = tile_index[0]+1, tile_index[1]
    elif level_painter.level_layout[tile_index[0]+2][tile_index[1]] in WALL_LIKE:
        wall_grid_index = tile_index[0]+2, tile_index[1]
    elif level_painter.level_layout[tile_index[0]][tile_index[1]] in WALL_LIKE:
        wall_grid_index = tile_index

    if tile_index[0]+2 >= hero.tile_index[0] <= wall_grid_index[0]:
        return True
