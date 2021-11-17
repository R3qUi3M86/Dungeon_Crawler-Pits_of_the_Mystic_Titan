from copy import deepcopy
from entities.characters import player
from utilities import entity_manager
from sounds import sound_player
from utilities.constants import *
from utilities.constant_objects import *

enemy_has_been_hit = False
hit_something = False

def attack_monster_with_melee_attack():
    global enemy_has_been_hit
    global hit_something

    hit_entity_list = []
    for entity in entity_manager.movement_and_melee_collision_sprites:
        if player.hero.facing_direction == SECTOR_E and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_E, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_NE and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_NE, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_N and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_N, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_NW and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_NW, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_W and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_W, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_SW and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_SW, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_S and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_S, entity) != None:
            enemy_has_been_hit = True
        elif player.hero.facing_direction == SECTOR_SE and pygame.sprite.collide_mask(player.PLAYER_MELEE_SPRITE_SE, entity) != None:
            enemy_has_been_hit = True
        
        if enemy_has_been_hit == True:
            hit_something = True
            hit_entity_list.append(entity)
        enemy_has_been_hit = False

    play_melee_attack_sound()
    hit_something = False
    for entity in hit_entity_list:
        deal_damage_to_monster(entity)

def attack_player_with_melee_attack():
    sound_player.monster_melee_miss_sound.play()

def deal_damage_to_monster(entity):
    id = entity.id
    for monster in entity_manager.monster_sprites:
        if id == monster.id:
            monster.take_damage(4)

def play_melee_attack_sound():
    if hit_something:
        sound_player.hero_melee_hit_sound.play()
    else:
        sound_player.hero_melee_miss_sound.play()