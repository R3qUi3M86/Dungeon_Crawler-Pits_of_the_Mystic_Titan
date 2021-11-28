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

    if entity_manager.hero.is_living:
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
        entity_manager.hero.speed_vector = round((entity_manager.hero.speed_scalar[X]/30)*entity_manager.hero.speed,2), round((entity_manager.hero.speed_scalar[Y]/30)*entity_manager.hero.speed*0.55,2)
    
    else:
        entity_manager.hero.speed_scalar = 0,0
        entity_manager.hero.speed_vector = 0,0
    
def get_player_mouse_input():
    mouse_pos = pygame.mouse.get_pos()
    entity_manager.hero.facing_direction = util.get_facing_direction(player_position,mouse_pos)
    
    if pygame.mouse.get_pressed()[0]:
        if entity_manager.hero.is_living == True:
            entity_manager.hero.is_in_pain = False
            entity_manager.hero.is_attacking = True

def order_sprites():
    sorted_entity_matrix = []
    hero_matrix_index = entity_manager.get_far_proximity_entity_and_shadow_matrix_index(entity_manager.hero.tile_index)

    for i, row in enumerate(entity_manager.far_proximity_entity_sprite_group_matrix):
        sorted_entities_row = []
        
        for j, cell in enumerate(row):
            for entity in cell:
                sorted_entities_row.append(entity)
            if (i,j) == hero_matrix_index:
                sorted_entities_row.append(entity_manager.hero_sprite_group)
                
        
        for _ in range(len(sorted_entities_row)-1):
            for j in range(len(sorted_entities_row)-1):
                if sorted_entities_row[j].sprite.map_position[Y] > sorted_entities_row[j+1].sprite.map_position[Y]:
                    sorted_entities_row[j], sorted_entities_row[j+1] = sorted_entities_row[j+1], sorted_entities_row[j]
        sorted_entity_matrix.append(sorted_entities_row)

    return sorted_entity_matrix

def draw_sprites():
    screen.blit(level_painter.level_surface,(level_painter.get_level_surface_translation_vector()))
    
    #Draw ordered entities
    for shadow in entity_manager.far_proximity_shadow_sprite_group_list:
        shadow.draw(screen)

    sorted_entity_matrix = order_sprites()
    for row in sorted_entity_matrix:
        for entity in row:
            entity.draw(screen)

entity_manager.initialize_level_sprites_matrix()
level_painter.paint_level()
entity_manager.initialize_player()
entity_manager.initialize_all_entities_and_shadows_sprite_group_matrix()
entity_manager.fill_map_with_monsters(20)
entity_manager.generate_items()
entity_manager.update_far_proximity_matrices_and_lists()
entity_manager.finish_init()

#Main game loop
while True:

    #Inputs
    get_player_wsad_input()
    get_player_mouse_input()

    #Updates
    cursor.cursor.update()
    entity_manager.update_all_objects_position_in_far_proximity()
    entity_manager.update_all_objects_in_far_proximity()
    collision_manager.detect_all_collisions()

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Drawing
    draw_sprites()
    #debug_text(f"{entity_manager.hero.map_position}")
    #debug_text(f"{entity_manager.hero.tile_index}",x = 10, y = 30)
    #debug_text(f"109 pos: {entity_manager.hero.direct_proximity_collision_tiles[1].map_position}",x = 10, y = 30)
    debug_text(f"{entity_manager.hero.tile_index}", x=10, y=30)
    debug_text(f"hero map pos: {entity_manager.hero.map_position}",x = 10, y = 45)
    # debug_text(f"mon 0 pos: {entity_manager.get_entity_sprite_by_id(0).position}",x = 10, y = 60)
    # debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(0).map_position}",x = 10, y = 75)
    # debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(0).tile_index}",x = 10, y = 90)
    # debug_text(f"mon 0 tile_index: {entity_manager.get_entity_sprite_by_id(0).tile_index}",x = 10, y = 75)
    # debug_text(f"mon 1 map_pos: {entity_manager.get_entity_sprite_by_id(1).tile_index}",x = 10, y = 90)
    cursor.cursor.draw(screen)
    
    #util.increment_print_matrix_timer(entity_manager.far_proximity_level_sprite_matrix, "S")
    #util.increment_print_matrix_timer(entity_manager.level_sprites_matrix, "S", True)
    #util.increment_print_matrix_timer(entity_manager.far_proximity_entity_and_shadow_sprite_group_matrix, "S")

    #Other
    pygame.display.update()
    clock.tick(60)