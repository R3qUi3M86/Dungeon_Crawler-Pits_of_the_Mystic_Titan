from sounds import sound_player
from utilities import entity_manager
from utilities.constants import *
from utilities import util

def attack_monster_with_melee_attack(weapon, damage_modifer):
    damage = weapon.damage + damage_modifer
    hit_monsters = []
    
    for character_sprite in entity_manager.far_proximity_character_sprites_list:
        hero = entity_manager.hero
        
        if character_sprite != hero and not (character_sprite.is_dead or character_sprite.is_overkilled) and hero.facing_direction == util.get_facing_direction(hero.map_position, character_sprite.map_position) and util.elipses_intersect(hero.map_position,character_sprite.map_position,hero.melee_range,character_sprite.size):
            hit_monsters.append(character_sprite)

    if hit_monsters:
        sound_player.play_melee_attack_sound(PLAYER, HIT)
        
        for monster in hit_monsters:
            monster.take_damage(damage)
    else:
        sound_player.play_melee_attack_sound(PLAYER, MISS)

    entity_manager.wake_up_any_sleeping_monsters_in_far_proximity_matrix()

def attack_monsters_with_ranged_weapon(weapon, damage_modifer):
    cursor_location = pygame.mouse.get_pos()
    angle = util.get_total_angle(player_position, cursor_location)
    launch_projectile(entity_manager.hero.map_position, angle, weapon, PLAYER, damage_modifer)

def attack_player_with_melee_attack(monster, damage):
    hero = entity_manager.hero
    
    if monster.facing_direction == util.get_facing_direction(monster.map_position,hero.map_position) and util.elipses_intersect(monster.map_position,hero.map_position,monster.melee_range,hero.size):
        sound_player.play_melee_attack_sound(monster.NAME, HIT)
        hero.take_damage(damage)
    else:
        sound_player.play_melee_attack_sound(monster.NAME, MISS)

def launch_projectile(launching_map_pos, angle, weapon, launching_entity_type, damage_modifer):
    pass