from sounds import sound_player
from entities.projectiles.projectile import Projectile
from utilities import entity_manager
from utilities.constants import *
from utilities import util

melee_hit_angle_margin = 30

def attack_monster_with_melee_attack(weapon, damage_modifer):
    damage = weapon.damage + damage_modifer
    hit_monsters = []
    
    for character_sprite in entity_manager.far_proximity_character_sprites_list:
        hero = entity_manager.hero
        
        if not (character_sprite.is_dead or character_sprite.is_overkilled):
            enemy_angle = util.get_total_angle(hero.map_position, character_sprite.map_position)
            mouse_angle = util.get_total_angle(player_position, pygame.mouse.get_pos())   
            left_margin_angle = enemy_angle + melee_hit_angle_margin
            right_margin_angle = enemy_angle - melee_hit_angle_margin

            if mouse_angle > 360 - melee_hit_angle_margin and enemy_angle < melee_hit_angle_margin:
                left_margin_angle += 360
                right_margin_angle += 360
            elif mouse_angle < melee_hit_angle_margin and enemy_angle > 360 - melee_hit_angle_margin:
                left_margin_angle -= 360
                right_margin_angle -= 360

            if left_margin_angle > mouse_angle > right_margin_angle and util.elipses_intersect(hero.map_position,character_sprite.map_position,hero.melee_range,character_sprite.size):
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
    launch_projectile(entity_manager.hero.tile_index, player_position, entity_manager.hero.map_position, angle, weapon, PLAYER, damage_modifer)
    sound_player.play_ranged_attack_sound(weapon.NAME)

def attack_player_with_melee_attack(monster, weapon, damage_modifier):
    hero = entity_manager.hero
    if monster.facing_direction == util.get_facing_direction(monster.map_position,hero.map_position) and util.elipses_intersect(monster.map_position,hero.map_position,monster.melee_range,hero.size):
        sound_player.play_melee_attack_sound(monster.NAME, HIT)
        hero.take_damage(weapon.damage + damage_modifier)
    else:
        sound_player.play_melee_attack_sound(monster.NAME, MISS)

def attack_player_with_ranged_attack(self, weapon, damage_modifier):
    pass

def launch_projectile(launching_tile_index, entity_pos, launching_map_pos, angle, weapon, launching_entity_type, damage_modifer):
    projectile_name = PROJECTILE_DICT[weapon.NAME]
    damage = weapon.damage + damage_modifer
    new_projectile = Projectile(launching_tile_index, entity_pos, launching_map_pos, damage, angle, projectile_name, launching_entity_type)
    entity_manager.put_projectile_in_matrices_and_lists(new_projectile)