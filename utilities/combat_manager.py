from entities.characters import unique_player_objects
from utilities import entity_manager
from sounds import sound_player
from utilities.constants import *

enemy_has_been_hit = False
hit_something = False

def attack_monster_with_melee_attack():
    global enemy_has_been_hit
    global hit_something

    hit_entity_list = []
    for entity in entity_manager.melee_collision_sprite_groups:
        if entity != unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP:
            for PLAYER_MELEE_SPRITE in unique_player_objects.PLAYER_MELEE_SPRITES:
                if PLAYER_MELEE_SPRITE.sector == unique_player_objects.HERO.facing_direction and pygame.sprite.collide_mask(PLAYER_MELEE_SPRITE, entity.sprite) != None:
                    enemy_has_been_hit = True
                    break
            
            if enemy_has_been_hit == True:
                hit_something = True
                hit_entity_list.append(entity)
            enemy_has_been_hit = False

    play_melee_attack_sound(PLAYER)
    hit_something = False
    for entity in hit_entity_list:
        deal_damage_to_monster(entity, damage=4)

def attack_player_with_melee_attack(current_attacking_monster):
    global hit_something
    for melee_sprite in current_attacking_monster.monster_melee_sprites:
        if melee_sprite.sector == current_attacking_monster.facing_direction and pygame.sprite.collide_mask(melee_sprite, unique_player_objects.PLAYER_SHADOW_SPRITE) != None:
            hit_something = True
            break
    
    play_melee_attack_sound(current_attacking_monster.name)
    if hit_something == True:
        deal_damage_to_player(damage=2)
    hit_something = False

def deal_damage_to_monster(entity, damage):
    id = entity.sprite.id
    for monster in entity_manager.charcter_sprite_groups:
        if id == monster.sprite.id:
            monster.sprite.take_damage(damage)

def deal_damage_to_player(damage):
    unique_player_objects.HERO.take_damage(damage)

def play_melee_attack_sound(attacking_entity):
    if hit_something:
        if attacking_entity == PLAYER:
            sound_player.hero_melee_hit_sound.play()
        elif attacking_entity == ETTIN:
            sound_player.monster_melee_hit_sound.play()
    else:
        if attacking_entity == PLAYER:
            sound_player.hero_melee_miss_sound.play()
        elif attacking_entity == ETTIN:
            sound_player.monster_melee_miss_sound.play()