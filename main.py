import pygame
from utilities.constants import *
from utilities import entity_manager
from utilities import game_manager
from sys import exit
from entities import cursor

pygame.init()
clock = pygame.time.Clock()

entity_manager.generate_monsters()

def get_player_wsad_input(keys):
    if keys[pygame.K_s] and game_manager.acceleration_vector[Y] < 30.0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],game_manager.acceleration_vector[Y]+1

    if not keys[pygame.K_s] and game_manager.acceleration_vector[Y] > 0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],0
    
    if keys[pygame.K_w] and game_manager.acceleration_vector[Y] > -30.0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],game_manager.acceleration_vector[Y]-1

    if not keys[pygame.K_w] and game_manager.acceleration_vector[Y] < 0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],0

    if keys[pygame.K_a] and game_manager.acceleration_vector[X] > -30.0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X]-1,game_manager.acceleration_vector[1]

    if not keys[pygame.K_a] and game_manager.acceleration_vector[X] < 0:
        game_manager.acceleration_vector = 0,game_manager.acceleration_vector[Y]
    
    if keys[pygame.K_d] and game_manager.acceleration_vector[X] < 30.0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X]+1,game_manager.acceleration_vector[Y]

    if not keys[pygame.K_d] and game_manager.acceleration_vector[X] > 0:
        game_manager.acceleration_vector = 0,game_manager.acceleration_vector[Y]

    if game_manager.acceleration_vector[X] > 21.2 and game_manager.acceleration_vector[Y] > 22.54:
        game_manager.acceleration_vector = 21.2,22.54
    elif game_manager.acceleration_vector[X] > 21.2 and game_manager.acceleration_vector[Y] < -22.54:
        game_manager.acceleration_vector = 21.2,-22.54
    elif game_manager.acceleration_vector[X] < -21.2 and game_manager.acceleration_vector[Y] > 22.54:
        game_manager.acceleration_vector = -21.2,22.54
    elif game_manager.acceleration_vector[X] < -21.2 and game_manager.acceleration_vector[Y] < -22.54:
        game_manager.acceleration_vector = -21.2,-22.54

    if game_manager.acceleration_vector[X] > 30.0:
        game_manager.acceleration_vector = 30.0, game_manager.acceleration_vector[Y]
    elif game_manager.acceleration_vector[X] < -30.0:
        game_manager.acceleration_vector = -30.0, game_manager.acceleration_vector[Y]
    if game_manager.acceleration_vector[Y] > 30.0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X], 30.0
    elif game_manager.acceleration_vector[Y] < -30.0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X], -30.0

    game_manager.speed_vector = (game_manager.acceleration_vector[X]/30)*game_manager.player_speed, (game_manager.acceleration_vector[Y]/30)*game_manager.player_speed*0.55

def order_sprites():
    for _ in range(len(entity_manager.all_entities)-1):
        for j in range(len(entity_manager.all_entities)-1):
            if entity_manager.all_entities[j].sprites()[0].position[Y] > entity_manager.all_entities[j+1].sprites()[0].position[Y]:
                    entity_manager.all_entities[j], entity_manager.all_entities[j+1] = entity_manager.all_entities[j+1], entity_manager.all_entities[j]

def collision_detection():
    game_manager.player_movement_collision()
    #possible other collisions

#Main game loop
while True:
    SCREEN.fill([25, 23, 22])
    order_sprites()

    #Inputs
    keys = pygame.key.get_pressed()
    get_player_wsad_input(keys)
    collision_detection()

    #Updates
    entity_manager.update_non_player_entities_position(entity_manager.monster_sprites)
    entity_manager.update_all_entities(entity_manager.all_entities)

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Drawing
    for entity in entity_manager.all_entities:
        entity.draw(SCREEN)
    
    cursor.cursor.draw(SCREEN)
    cursor.cursor.update()
    #screen.blit(level.test_surface_scaled,(-800,0))
    
    #Other
    pygame.display.update()
    clock.tick(60)