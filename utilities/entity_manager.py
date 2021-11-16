import pygame
from utilities.constants import *
from utilities import game_manager
from entities import melee_range
from entities import shadow
from entities.characters import ettin
from entities.characters import player

entities_id = []
monster_sprites = []
level_sprites = []
movement_collision_sprites = []
non_player_entities = []
all_entities = [player.character]

def generate_monster(monster_type, position):
    if monster_type == ETTIN:
        create_ettin_monster(position)

def update_entity_position(entity, translation_vector):
    for sprite in entity:
        sprite.update_position(translation_vector)

def update_non_player_entities_position(entities):
    for entity in entities:
        update_entity_position(entity, game_manager.speed_vector)

def get_monster_sprite(monster_id):
    for monster in monster_sprites:
        if monster.monster_id == monster_id:
            return monster

def create_ettin_monster_sprite(monster_sprite_position):
    return ettin.Ettin(monster_sprite_position)

def create_monster_character(monster_sprite, monster_shadow):
    character = pygame.sprite.Group()
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_e_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_ne_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_n_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_nw_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_w_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_sw_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_s_sector_position))
    character.add(melee_range.Melee(monster_sprite.sprite_position, monster_sprite.monster_melee_se_sector_position))
    character.add(monster_shadow)
    character.add(monster_sprite)
    return character

def create_ettin_monster(position):
    monster_sprite = create_ettin_monster_sprite(position)
    add_auxilary_objects(monster_sprite)

def add_auxilary_objects(monster_sprite):
    monster_shadow = create_monster_shadow(monster_sprite)
    monster_character = create_monster_character(monster_sprite, monster_shadow)
    append_sprites_and_entities_lists(monster_sprite,monster_shadow,monster_character)

def append_sprites_and_entities_lists(monster_sprite,monster_shadow,monster_character):
    global monster_sprites
    global movement_collision_sprites
    global non_player_entities
    global all_entities

    movement_collision_sprites.append(monster_shadow)
    monster_sprites.append(monster_sprite)
    non_player_entities.append(monster_character)
    all_entities.append(monster_character)

def create_monster_shadow(monster_sprite):
    return shadow.Shadow(monster_sprite.sprite_position, monster_sprite.id, SIZE_MEDIUM)

def update_all_entities(all_entities):
    for entity in all_entities:
        entity.update()

def generate_monsters():
    generate_monster(ETTIN, (200,200))
    generate_monster(ETTIN, (400,200))