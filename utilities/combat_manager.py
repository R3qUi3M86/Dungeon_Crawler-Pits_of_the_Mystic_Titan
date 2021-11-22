from sounds import sound_player
from entities.characters import unique_player_object
from utilities import entity_manager
from utilities import collision_manager
from utilities.constants import *

def attack_monster_with_melee_attack(damage = 0):
    enemy_has_been_hit = False
    hit_something = False

    hit_monsters = []
    
    for entity_sprite_group in entity_manager.entity_sprite_groups:
        if entity_sprite_group.sprite != unique_player_object.HERO:
            enemy_has_been_hit = False
            
            for melee_sector in unique_player_object.HERO.entity_melee_sector_sprites:
                if melee_sector.rect.colliderect(entity_sprite_group.sprite.entity_collider_omni.rect):
                    if melee_sector.sector == unique_player_object.HERO.facing_direction and pygame.sprite.collide_mask(melee_sector, entity_sprite_group.sprite.entity_collider_omni) != None:
                        enemy_has_been_hit = True
                        break
            
            if enemy_has_been_hit:
                hit_something = True
                hit_monsters.append(entity_sprite_group.sprite)

    if hit_something:
        play_melee_attack_sound(PLAYER, HIT)
        for monster in hit_monsters:
            monster.take_damage(damage)
    else:
        play_melee_attack_sound(PLAYER, MISS)
        
def attack_player_with_melee_attack(monster, damage = 0):
    hit = False

    for melee_sector in monster.entity_melee_sector_sprites:
        if melee_sector.rect.colliderect(unique_player_object.HERO.entity_collider_omni.rect) and pygame.sprite.collide_mask(melee_sector,unique_player_object.HERO.entity_collider_omni):
            if melee_sector.sector == monster.facing_direction:
                hit = True
                break
    
    if hit:
        play_melee_attack_sound(monster.NAME, HIT)
        unique_player_object.HERO.take_damage(damage)
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