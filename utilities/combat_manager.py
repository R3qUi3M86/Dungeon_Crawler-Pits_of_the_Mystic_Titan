from sounds import sound_player
from utilities import entity_manager
from utilities.constants import *
from utilities import util

def attack_monster_with_melee_attack(damage):
    hit_monsters = []
    
    for character_sprite in entity_manager.far_proximity_character_sprites_list:
        hero = entity_manager.hero
        
        if character_sprite != hero and not (character_sprite.is_dead or character_sprite.is_overkilled) and hero.facing_direction == util.get_facing_direction(hero.map_position, character_sprite.map_position) and util.elipses_intersect(hero.map_position,character_sprite.map_position,hero.melee_range,character_sprite.size):
            hit_monsters.append(character_sprite)

    if hit_monsters:
        play_melee_attack_sound(PLAYER, HIT)
        
        for monster in hit_monsters:
            monster.take_damage(damage)
    else:
        play_melee_attack_sound(PLAYER, MISS)
        
def attack_player_with_melee_attack(monster, damage):
    hero = entity_manager.hero
    
    if monster.facing_direction == util.get_facing_direction(monster.map_position,hero.map_position) and util.elipses_intersect(monster.map_position,hero.map_position,monster.melee_range,hero.size):
        play_melee_attack_sound(monster.NAME, HIT)
        hero.take_damage(damage)
    else:
        play_melee_attack_sound(monster.NAME, MISS)

def play_melee_attack_sound(attacking_entity, hit):
    if hit:
        if attacking_entity == PLAYER:
            sound_player.hero_melee_hit_sound.play()
        elif attacking_entity == ETTIN:
            sound_player.monster_melee_hit_sound.play()
    else:
        if attacking_entity == PLAYER:
            sound_player.hero_melee_miss_sound.play()
        elif attacking_entity == ETTIN:
            sound_player.monster_melee_miss_sound.play()