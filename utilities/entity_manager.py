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
item_sprites = []
movement_and_melee_collision_sprites = []
all_entities = [player.character]

def get_collision_sprite_by_id(id):
    for collision_sprite in movement_and_melee_collision_sprites:
        if collision_sprite.id == id:
            return collision_sprite

def generate_monster(monster_type, position):
    if monster_type == ETTIN:
        create_ettin_monster(position)

def update_non_player_entities_position(entities):
    for entity in entities:
        if player.hero.atack == True:
            game_manager.speed_vector = 0,0
        entity.update_position(game_manager.speed_vector)

def get_monster_sprite(monster_id):
    for monster in monster_sprites:
        if monster.id == monster_id:
            return monster

def create_ettin_monster_sprite(monster_sprite_position):
    return ettin.Ettin(monster_sprite_position)

def create_monster_character(monster_sprite):
    character = pygame.sprite.Group()
    character.add(monster_sprite.monster_melee_e_sector)
    character.add(monster_sprite.monster_melee_ne_sector)
    character.add(monster_sprite.monster_melee_n_sector)
    character.add(monster_sprite.monster_melee_nw_sector)
    character.add(monster_sprite.monster_melee_w_sector)
    character.add(monster_sprite.monster_melee_sw_sector)
    character.add(monster_sprite.monster_melee_s_sector)
    character.add(monster_sprite.monster_melee_se_sector)
    character.add(monster_sprite.monster_shadow)
    character.add(monster_sprite)
    return character

def kill_monster(id):
    global monster_sprites
    global movement_and_melee_collision_sprites
    for collision_sprite in movement_and_melee_collision_sprites:
        if collision_sprite.id == id:
            movement_and_melee_collision_sprites.remove(collision_sprite)

def create_ettin_monster(position):
    monster_sprite = create_ettin_monster_sprite(position)
    add_auxilary_objects(monster_sprite)

def add_auxilary_objects(monster_sprite):
    monster_shadow = monster_sprite.monster_shadow
    monster_character = create_monster_character(monster_sprite)
    append_sprites_and_entities_lists(monster_sprite,monster_shadow,monster_character)

def append_sprites_and_entities_lists(monster_sprite,monster_shadow,monster_character):
    global monster_sprites
    global movement_and_melee_collision_sprites
    global all_entities

    movement_and_melee_collision_sprites.append(monster_shadow)
    monster_sprites.append(monster_sprite)
    all_entities.append(monster_character)

def create_monster_shadow(monster_sprite):
    return shadow.Shadow(monster_sprite.sprite_position, monster_sprite.id, SIZE_MEDIUM_SMALL)

def update_all_entities(all_entities):
    for entity in all_entities:
        entity.update()

def generate_monsters():
    generate_monster(ETTIN, (200,200))
    generate_monster(ETTIN, (400,200))