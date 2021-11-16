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
    if keys[pygame.K_s] and game_manager.acceleration_vector[Y] < 30:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],game_manager.acceleration_vector[Y]+1

    if not keys[pygame.K_s] and game_manager.acceleration_vector[Y] > 0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],0
    
    if keys[pygame.K_w] and game_manager.acceleration_vector[Y] > -30:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],game_manager.acceleration_vector[Y]-1

    if not keys[pygame.K_w] and game_manager.acceleration_vector[Y] < 0:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X],0

    if keys[pygame.K_a] and game_manager.acceleration_vector[X] > -30:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X]-1,game_manager.acceleration_vector[1]

    if not keys[pygame.K_a] and game_manager.acceleration_vector[X] < 0:
        game_manager.acceleration_vector = 0,game_manager.acceleration_vector[Y]
    
    if keys[pygame.K_d] and game_manager.acceleration_vector[X] < 30:
        game_manager.acceleration_vector = game_manager.acceleration_vector[X]+1,game_manager.acceleration_vector[Y]

    if not keys[pygame.K_d] and game_manager.acceleration_vector[X] > 0:
        game_manager.acceleration_vector = 0,game_manager.acceleration_vector[Y]

    if game_manager.acceleration_vector[0] > 10 and game_manager.acceleration_vector[1] > 10:
        game_manager.acceleration_vector = 11,11
    elif game_manager.acceleration_vector[0] > 10 and game_manager.acceleration_vector[1] < -10:
        game_manager.acceleration_vector = 11,-11
    elif game_manager.acceleration_vector[0] < -10 and game_manager.acceleration_vector[1] > 10:
        game_manager.acceleration_vector = -11,11
    elif game_manager.acceleration_vector[0] < -10 and game_manager.acceleration_vector[1] < -10:
        game_manager.acceleration_vector = -11,-11



    if game_manager.acceleration_vector[Y] > 20:
        game_manager.speed_vector = game_manager.speed_vector[X], 3
    elif 20 >= game_manager.acceleration_vector[Y] > 10:
        game_manager.speed_vector = game_manager.speed_vector[X], 2
    elif 10 >= game_manager.acceleration_vector[Y] > 0:
        game_manager.speed_vector = game_manager.speed_vector[X], 1
    elif game_manager.acceleration_vector[Y] == 0:
        game_manager.speed_vector = game_manager.speed_vector[X], 0
    elif -10 <= game_manager.acceleration_vector[Y] < 0:
        game_manager.speed_vector = game_manager.speed_vector[X], -1
    elif -20 <= game_manager.acceleration_vector[Y] < -10:
        game_manager.speed_vector = game_manager.speed_vector[X], -2
    elif game_manager.acceleration_vector[Y] < -20:
        game_manager.speed_vector = game_manager.speed_vector[X], -3

    if game_manager.acceleration_vector[X] > 20:
        game_manager.speed_vector = 3, game_manager.speed_vector[Y]
    elif 20 >= game_manager.acceleration_vector[X] > 10:
        game_manager.speed_vector = 2, game_manager.speed_vector[Y]
    elif 10 >= game_manager.acceleration_vector[X] > 0:
        game_manager.speed_vector = 1, game_manager.speed_vector[Y]
    elif game_manager.acceleration_vector[X] == 0:
        game_manager.speed_vector = 0, game_manager.speed_vector[Y]
    elif -10 <= game_manager.acceleration_vector[X] < 0:
        game_manager.speed_vector = -1, game_manager.speed_vector[Y]
    elif -20 <= game_manager.acceleration_vector[X] < -10:
        game_manager.speed_vector = -2, game_manager.speed_vector[Y]
    elif game_manager.acceleration_vector[X] < -20:
        game_manager.speed_vector = -3, game_manager.speed_vector[Y]

def order_sprites():
    for _ in range(len(entity_manager.all_entities)-1):
        for j in range(len(entity_manager.all_entities)-1):
            if entity_manager.all_entities[j].sprites()[0].sprite_position[Y] > entity_manager.all_entities[j+1].sprites()[0].sprite_position[Y]:
                    entity_manager.all_entities[j], entity_manager.all_entities[j+1] = entity_manager.all_entities[j+1], entity_manager.all_entities[j]

def collision_detection():
    game_manager.player_movement_collision()
    #other collisions

while True:
    SCREEN.fill([25, 23, 22])
    order_sprites()

    keys = pygame.key.get_pressed()
    get_player_wsad_input(keys)
    collision_detection()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for entity in entity_manager.all_entities:
        entity.draw(SCREEN)
    
    cursor.cursor.draw(SCREEN)
    cursor.cursor.update()
    
    #screen.blit(level.test_surface_scaled,(-800,0))
    entity_manager.update_all_entities(entity_manager.all_entities)
    entity_manager.update_non_player_entities_position(entity_manager.non_player_entities)

    pygame.display.update()
    clock.tick(60)