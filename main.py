import pygame
from sounds.sound_player import *
from utilities.text_printer import *
from utilities.constants import *
from utilities import entity_manager
from utilities import collision_manager
from utilities import level_painter
from utilities import util
from entities.characters import unique_player_object
from sys import exit
from entities import cursor

pygame.init()
clock = pygame.time.Clock()
set_volume_for_all_sounds(VOLUME)

def initialize_player_object():
    unique_player_object.initialize_player()
    entity_manager.entity_sprite_groups.append(pygame.sprite.GroupSingle(unique_player_object.HERO))
    entity_manager.shadow_sprite_groups.append(pygame.sprite.GroupSingle(unique_player_object.HERO.shadow))
    entity_manager.melee_sector_sprite_groups.append(pygame.sprite.Group(unique_player_object.HERO.entity_melee_sector_sprites))
    entity_manager.entity_collision_sprite_groups.append(pygame.sprite.Group(unique_player_object.HERO.entity_collider_sprites))    

def get_player_wsad_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] and unique_player_object.HERO.speed_scalar[Y] < 30.0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X],unique_player_object.HERO.speed_scalar[Y]+1

    if (not keys[pygame.K_s] or unique_player_object.HERO.is_attacking) and unique_player_object.HERO.speed_scalar[Y] > 0:
        if unique_player_object.HERO.speed_scalar[Y] < 3:
            unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X],0
        else:
            unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X],unique_player_object.HERO.speed_scalar[Y]-3
    
    if keys[pygame.K_w] and unique_player_object.HERO.speed_scalar[Y] > -30.0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X],unique_player_object.HERO.speed_scalar[Y]-1

    if (not keys[pygame.K_w] or unique_player_object.HERO.is_attacking) and unique_player_object.HERO.speed_scalar[Y] < 0:
        if unique_player_object.HERO.speed_scalar[Y] > -3:
            unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X],0
        else:
            unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X],unique_player_object.HERO.speed_scalar[Y]+3

    if keys[pygame.K_a] and unique_player_object.HERO.speed_scalar[X] > -30.0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X]-1,unique_player_object.HERO.speed_scalar[1]

    if (not keys[pygame.K_a] or unique_player_object.HERO.is_attacking) and unique_player_object.HERO.speed_scalar[X] < 0:
        if unique_player_object.HERO.speed_scalar[X] > -3:
            unique_player_object.HERO.speed_scalar = 0,unique_player_object.HERO.speed_scalar[Y]
        else:
            unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X]+3,unique_player_object.HERO.speed_scalar[Y]
    
    if keys[pygame.K_d] and unique_player_object.HERO.speed_scalar[X] < 30.0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X]+1,unique_player_object.HERO.speed_scalar[Y]

    if (not keys[pygame.K_d] or unique_player_object.HERO.is_attacking) and unique_player_object.HERO.speed_scalar[X] > 0:
        if unique_player_object.HERO.speed_scalar[X] < 3:
            unique_player_object.HERO.speed_scalar = 0,unique_player_object.HERO.speed_scalar[Y]
        else:
            unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X]-3,unique_player_object.HERO.speed_scalar[Y]

    if unique_player_object.HERO.speed_scalar[X] > 21.2 and unique_player_object.HERO.speed_scalar[Y] > 22.54:
        unique_player_object.HERO.speed_scalar = 21.2,22.54
    elif unique_player_object.HERO.speed_scalar[X] > 21.2 and unique_player_object.HERO.speed_scalar[Y] < -22.54:
        unique_player_object.HERO.speed_scalar = 21.2,-22.54
    elif unique_player_object.HERO.speed_scalar[X] < -21.2 and unique_player_object.HERO.speed_scalar[Y] > 22.54:
        unique_player_object.HERO.speed_scalar = -21.2,22.54
    elif unique_player_object.HERO.speed_scalar[X] < -21.2 and unique_player_object.HERO.speed_scalar[Y] < -22.54:
        unique_player_object.HERO.speed_scalar = -21.2,-22.54

    if unique_player_object.HERO.speed_scalar[X] > 30.0:
        unique_player_object.HERO.speed_scalar = 30.0, unique_player_object.HERO.speed_scalar[Y]
    elif unique_player_object.HERO.speed_scalar[X] < -30.0:
        unique_player_object.HERO.speed_scalar = -30.0, unique_player_object.HERO.speed_scalar[Y]
    if unique_player_object.HERO.speed_scalar[Y] > 30.0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X], 30.0
    elif unique_player_object.HERO.speed_scalar[Y] < -30.0:
        unique_player_object.HERO.speed_scalar = unique_player_object.HERO.speed_scalar[X], -30.0

    unique_player_object.HERO.speed_scalar = round(unique_player_object.HERO.speed_scalar[0],2),round(unique_player_object.HERO.speed_scalar[1],2)
    unique_player_object.HERO.speed_vector = round(((unique_player_object.HERO.speed_scalar[X]/30)*unique_player_object.HERO.speed),2), round(((unique_player_object.HERO.speed_scalar[Y]/30)*unique_player_object.HERO.speed*0.55),2)

def get_player_mouse_input():
    mouse_pos = pygame.mouse.get_pos()
    unique_player_object.HERO.facing_direction = util.get_facing_direction(player_position,mouse_pos)
    
    if pygame.mouse.get_pressed()[0]:
        if unique_player_object.HERO.is_living == True:
            unique_player_object.HERO.is_in_pain = False
            unique_player_object.HERO.is_attacking = True

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

def collision_detection():
    collision_manager.player_vs_monster_movement_collision()

    for entity_sprite_group in entity_manager.entity_sprite_groups:
        collision_manager.character_vs_level_movement_collision(entity_sprite_group)
        collision_manager.monster_vs_monster_collision(entity_sprite_group)
        collision_manager.projectile_collision(entity_sprite_group)
        collision_manager.item_collision(entity_sprite_group)

def draw_sprites():
    for tile in entity_manager.level_sprite_groups:
        tile.draw(screen)
    # for melee_sector_sprite_group in entity_manager.melee_sector_sprite_groups:
    #     melee_sector_sprite_group.draw(screen)
    for entity_collision_sprite_group in entity_manager.entity_collision_sprite_groups:
        entity_collision_sprite_group.draw(screen)
    for shadow in entity_manager.shadow_sprite_groups:
        shadow.draw(screen)
    for entity in entity_manager.entity_sprite_groups:
        entity.draw(screen)

def draw_pathfinding_path_for_monster(monster_index):
    monster_sprite = entity_manager.get_entity_sprite_by_id(monster_index)
    if monster_sprite != None:
        monster_sprite.monster_ai.pathfinder.draw_path()

initialize_player_object()
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
    unique_player_object.HERO.update_position(unique_player_object.HERO.speed_vector)
    entity_manager.update_all_non_player_entities_position_by_vector(unique_player_object.HERO.speed_vector)
    collision_detection()

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Drawing
    draw_sprites()
    draw_pathfinding_path_for_monster(0)
    points = [(entity_manager.level_sprite_groups[0].sprite.position[0], entity_manager.level_sprite_groups[0].sprite.position[1]),(entity_manager.level_sprite_groups[50].sprite.position[0], entity_manager.level_sprite_groups[50].sprite.position[1])]
    pygame.draw.lines(screen,'#aa0000',False,points,5)
    debug_text(f"{unique_player_object.HERO.map_position}")
    debug_text(f"{unique_player_object.HERO.tile_index}",x = 10, y = 30)
    debug_text(f"mon index: {entity_manager.get_entity_sprite_by_id(0).tile_index}",x = 10, y = 50)
    debug_text(f"mon map_pos: {entity_manager.get_entity_sprite_by_id(0).map_position}",x = 10, y = 70)
    debug_text(f"mon pos: {entity_manager.get_entity_sprite_by_id(0).map_position}",x = 10, y = 90)
    
    cursor.cursor.draw(screen)
    cursor.cursor.update()
    
    #Other
    pygame.display.update()
    clock.tick(60)