import pygame
from utilities.constants import *
from utilities import entity_manager
from utilities import movement_manager
from sys import exit
from entities import cursor

pygame.init()
clock = pygame.time.Clock()

entity_manager.generate_monsters()

def get_player_wsad_input(keys):
    if keys[pygame.K_s] and movement_manager.acceleration_vector[Y] < 30.0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X],movement_manager.acceleration_vector[Y]+1

    if not keys[pygame.K_s] and movement_manager.acceleration_vector[Y] > 0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X],0
    
    if keys[pygame.K_w] and movement_manager.acceleration_vector[Y] > -30.0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X],movement_manager.acceleration_vector[Y]-1

    if not keys[pygame.K_w] and movement_manager.acceleration_vector[Y] < 0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X],0

    if keys[pygame.K_a] and movement_manager.acceleration_vector[X] > -30.0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X]-1,movement_manager.acceleration_vector[1]

    if not keys[pygame.K_a] and movement_manager.acceleration_vector[X] < 0:
        movement_manager.acceleration_vector = 0,movement_manager.acceleration_vector[Y]
    
    if keys[pygame.K_d] and movement_manager.acceleration_vector[X] < 30.0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X]+1,movement_manager.acceleration_vector[Y]

    if not keys[pygame.K_d] and movement_manager.acceleration_vector[X] > 0:
        movement_manager.acceleration_vector = 0,movement_manager.acceleration_vector[Y]

    if movement_manager.acceleration_vector[X] > 21.2 and movement_manager.acceleration_vector[Y] > 22.54:
        movement_manager.acceleration_vector = 21.2,22.54
    elif movement_manager.acceleration_vector[X] > 21.2 and movement_manager.acceleration_vector[Y] < -22.54:
        movement_manager.acceleration_vector = 21.2,-22.54
    elif movement_manager.acceleration_vector[X] < -21.2 and movement_manager.acceleration_vector[Y] > 22.54:
        movement_manager.acceleration_vector = -21.2,22.54
    elif movement_manager.acceleration_vector[X] < -21.2 and movement_manager.acceleration_vector[Y] < -22.54:
        movement_manager.acceleration_vector = -21.2,-22.54

    if movement_manager.acceleration_vector[X] > 30.0:
        movement_manager.acceleration_vector = 30.0, movement_manager.acceleration_vector[Y]
    elif movement_manager.acceleration_vector[X] < -30.0:
        movement_manager.acceleration_vector = -30.0, movement_manager.acceleration_vector[Y]
    if movement_manager.acceleration_vector[Y] > 30.0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X], 30.0
    elif movement_manager.acceleration_vector[Y] < -30.0:
        movement_manager.acceleration_vector = movement_manager.acceleration_vector[X], -30.0

    movement_manager.speed_vector = round(((movement_manager.acceleration_vector[X]/30)*movement_manager.player_speed),2), round(((movement_manager.acceleration_vector[Y]/30)*movement_manager.player_speed*0.55),2)

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
    
    for _ in range(len(entity_manager.character_sprite_groups)-1):
        for j in range(len(entity_manager.character_sprite_groups)-1):
            if entity_manager.character_sprite_groups[j].sprite.sprite_position[Y] > entity_manager.character_sprite_groups[j+1].sprite.sprite_position[Y]:
                    entity_manager.character_sprite_groups[j], entity_manager.character_sprite_groups[j+1] = entity_manager.character_sprite_groups[j+1], entity_manager.character_sprite_groups[j]

def collision_detection():
    movement_manager.player_movement_collision()
    #possible other collisions

def draw_sprites():
    for melee_sectors in entity_manager.melee_sector_sprite_groups:
        melee_sectors.draw(SCREEN)
    for shadow in entity_manager.shadow_sprite_groups:
        shadow.draw(SCREEN)
    for character in entity_manager.character_sprite_groups:
        character.draw(SCREEN)

#Main game loop
while True:
    SCREEN.fill([25, 23, 22])
    order_sprites()

    #Inputs
    keys = pygame.key.get_pressed()
    get_player_wsad_input(keys)

    #Updates
    entity_manager.update_all_entities()
    entity_manager.update_all_non_player_entities_position(movement_manager.speed_vector)
    collision_detection()

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Drawing
    draw_sprites()
    
    cursor.cursor.draw(SCREEN)
    cursor.cursor.update()
    #screen.blit(level.test_surface_scaled,(-800,0))
    
    #Other
    pygame.display.update()
    clock.tick(60)