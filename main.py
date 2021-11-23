import pygame
from sounds.sound_player import *
from utilities.text_printer import *
from utilities.constants import *
from utilities import entity_manager
from utilities import collision_manager
from utilities import level_painter
from utilities import util
from sys import exit
from entities import cursor

pygame.init()
clock = pygame.time.Clock()
set_volume_for_all_sounds(VOLUME)  

def get_player_wsad_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] and entity_manager.hero.speed_scalar[Y] < 30.0:
        entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]+1

    if (not keys[pygame.K_s] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[Y] > 0:
        if entity_manager.hero.speed_scalar[Y] < 3:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],0
        else:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]-3
    
    if keys[pygame.K_w] and entity_manager.hero.speed_scalar[Y] > -30.0:
        entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]-1

    if (not keys[pygame.K_w] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[Y] < 0:
        if entity_manager.hero.speed_scalar[Y] > -3:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],0
        else:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]+3

    if keys[pygame.K_a] and entity_manager.hero.speed_scalar[X] > -30.0:
        entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]-1,entity_manager.hero.speed_scalar[1]

    if (not keys[pygame.K_a] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[X] < 0:
        if entity_manager.hero.speed_scalar[X] > -3:
            entity_manager.hero.speed_scalar = 0,entity_manager.hero.speed_scalar[Y]
        else:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]+3,entity_manager.hero.speed_scalar[Y]
    
    if keys[pygame.K_d] and entity_manager.hero.speed_scalar[X] < 30.0:
        entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]+1,entity_manager.hero.speed_scalar[Y]

    if (not keys[pygame.K_d] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[X] > 0:
        if entity_manager.hero.speed_scalar[X] < 3:
            entity_manager.hero.speed_scalar = 0,entity_manager.hero.speed_scalar[Y]
        else:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]-3,entity_manager.hero.speed_scalar[Y]

    if entity_manager.hero.speed_scalar[X] > 21.2 and entity_manager.hero.speed_scalar[Y] > 22.54:
        entity_manager.hero.speed_scalar = 21.2,22.54
    elif entity_manager.hero.speed_scalar[X] > 21.2 and entity_manager.hero.speed_scalar[Y] < -22.54:
        entity_manager.hero.speed_scalar = 21.2,-22.54
    elif entity_manager.hero.speed_scalar[X] < -21.2 and entity_manager.hero.speed_scalar[Y] > 22.54:
        entity_manager.hero.speed_scalar = -21.2,22.54
    elif entity_manager.hero.speed_scalar[X] < -21.2 and entity_manager.hero.speed_scalar[Y] < -22.54:
        entity_manager.hero.speed_scalar = -21.2,-22.54

    if entity_manager.hero.speed_scalar[X] > 30.0:
        entity_manager.hero.speed_scalar = 30.0, entity_manager.hero.speed_scalar[Y]
    elif entity_manager.hero.speed_scalar[X] < -30.0:
        entity_manager.hero.speed_scalar = -30.0, entity_manager.hero.speed_scalar[Y]
    if entity_manager.hero.speed_scalar[Y] > 30.0:
        entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X], 30.0
    elif entity_manager.hero.speed_scalar[Y] < -30.0:
        entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X], -30.0

    entity_manager.hero.speed_scalar = round(entity_manager.hero.speed_scalar[0],2),round(entity_manager.hero.speed_scalar[1],2)
    entity_manager.hero.speed_vector = round(((entity_manager.hero.speed_scalar[X]/30)*entity_manager.hero.speed),2), round(((entity_manager.hero.speed_scalar[Y]/30)*entity_manager.hero.speed*0.55),2)

def get_player_mouse_input():
    mouse_pos = pygame.mouse.get_pos()
    entity_manager.hero.facing_direction = util.get_facing_direction(player_position,mouse_pos)
    
    if pygame.mouse.get_pressed()[0]:
        if entity_manager.hero.is_living == True:
            entity_manager.hero.is_in_pain = False
            entity_manager.hero.is_attacking = True

def order_sprites():
    for _ in range(len(entity_manager.melee_sector_sprite_groups)-1):
        for j in range(len(entity_manager.melee_sector_sprite_groups)-1):
            first_sprite_from_current_group = entity_manager.melee_sector_sprite_groups[j].sprites()[0]
            first_sprite_from_next_group = entity_manager.melee_sector_sprite_groups[j+1].sprites()[0]
            if first_sprite_from_current_group.position[Y] > first_sprite_from_next_group.position[Y]:
                    entity_manager.melee_sector_sprite_groups[j], entity_manager.melee_sector_sprite_groups[j+1] = entity_manager.melee_sector_sprite_groups[j+1], entity_manager.melee_sector_sprite_groups[j]

    for _ in range(len(entity_manager.shadow_sprite_groups)-1):
        for j in range(len(entity_manager.shadow_sprite_groups)-1):
            if entity_manager.shadow_sprite_groups[j].sprite.position[Y] > entity_manager.shadow_sprite_groups[j+1].sprite.position[Y]:
                    entity_manager.shadow_sprite_groups[j], entity_manager.shadow_sprite_groups[j+1] = entity_manager.shadow_sprite_groups[j+1], entity_manager.shadow_sprite_groups[j]
    
    for _ in range(len(entity_manager.entity_sprite_groups)-1):
        for j in range(len(entity_manager.entity_sprite_groups)-1):
            if entity_manager.entity_sprite_groups[j].sprite.sprite_position[Y] > entity_manager.entity_sprite_groups[j+1].sprite.sprite_position[Y]:
                    entity_manager.entity_sprite_groups[j], entity_manager.entity_sprite_groups[j+1] = entity_manager.entity_sprite_groups[j+1], entity_manager.entity_sprite_groups[j]

def draw_sprites():
    for tile in entity_manager.level_sprite_groups:
        tile.draw(screen)
    for melee_sector_sprite_group in entity_manager.melee_sector_sprite_groups:
        melee_sector_sprite_group.draw(screen)
    for entity_collision_sprite_group in entity_manager.entity_collision_sprite_groups:
        entity_collision_sprite_group.draw(screen)
    for shadow in entity_manager.shadow_sprite_groups:
        shadow.draw(screen)
    for entity in entity_manager.entity_sprite_groups:
        entity.draw(screen)

entity_manager.initialize_player_object()
level_painter.create_all_level_tiles()
entity_manager.generate_monsters()

#Main game loop
while True:
    screen.fill([25, 23, 22])
    order_sprites()

    #Inputs
    get_player_wsad_input()
    get_player_mouse_input()

    #Updates
    entity_manager.update_all_entities()
    entity_manager.update_hero_position()
    entity_manager.update_all_non_player_entities_position_by_vector(entity_manager.hero.speed_vector)
    collision_manager.detect_all_collisions()
    cursor.cursor.update()

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Drawing
    draw_sprites()
    debug_text(f"{entity_manager.hero.map_position}")
    debug_text(f"{entity_manager.hero.tile_index}",x = 10, y = 30)
    #util.draw_pathfinding_path_for_monster(0)
    # util.draw_pathfinding_path_for_monster(1)
    # util.draw_pathfinding_path_for_monster(2)
    # util.draw_pathfinding_path_for_monster(3)
    debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(0).tile_index}",x = 10, y = 50)
    debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(0).map_position}",x = 10, y = 65)
    debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(0).vicinity_index_matrix}",x = 10, y = 80)
    # debug_text(f"mon 1 map_pos: {entity_manager.get_entity_sprite_by_id(1).tile_index}",x = 10, y = 90)
    cursor.cursor.draw(screen)
    
    #Other
    pygame.display.update()
    clock.tick(60)