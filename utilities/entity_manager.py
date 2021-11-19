import pygame
from utilities.constants import *
from utilities import movement_manager
from entities.characters import unique_player_objects
from entities.characters import ettin

entities_id = []
character_sprite_groups = [unique_player_objects.HERO_SPRITE_GROUP]
shadow_sprite_groups = [unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP]
movement_collision_sprite_groups = [unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP]
melee_collision_sprite_groups = [unique_player_objects.PLAYER_SHADOW_SPRITE_GROUP]
item_sprite_groups = []
melee_sector_sprite_groups = [unique_player_objects.HERO_MELEE_SECTOR_SPRITE_GROUP]
level_sprite_groups = []
projectile_sprite_groups = []

def get_collision_sprite_by_id(id):
    for collision_sprite in movement_collision_sprite_groups:
        if collision_sprite.sprite.id == id:
            return collision_sprite.sprite

def generate_monster(monster_type, position):
    if monster_type == ETTIN:
        create_ettin_monster(position)

def update_non_player_group_single_entities_position(vector,entities):
    for entity in entities:
        if unique_player_objects.HERO_SPRITE_GROUP.sprite.attack == True or unique_player_objects.HERO_SPRITE_GROUP.sprite.living == False:
            movement_manager.speed_vector = 0,0
        entity.sprite.update_position(vector)

def update_non_player_group_entities_position(vector,entities):
    pass

def update_all_non_player_entities_player_position(vector):
    update_non_player_group_single_entities_position(vector,character_sprite_groups)
    update_non_player_group_single_entities_position(vector,item_sprite_groups)
    update_non_player_group_single_entities_position(vector,level_sprite_groups)
    update_non_player_group_single_entities_position(vector,projectile_sprite_groups)

def get_monster_sprite(monster_id):
    for monster in character_sprite_groups:
        if monster.sprite.id == monster_id:
            return monster.sprite

def create_ettin_monster_sprite_group(monster_sprite_position):
    ettin_monster_sprite = ettin.Ettin(monster_sprite_position)
    ettin_monster_sprite_grup = pygame.sprite.GroupSingle()
    ettin_monster_sprite_grup.add(ettin_monster_sprite)
    return ettin_monster_sprite_grup

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
    character.add(monster_sprite.monster_collision_shadow)
    character.add(monster_sprite.melee_collision_shadow)
    character.add(monster_sprite)
    return character

def kill_monster_auxilary_entities(id):
    global character_sprite_groups
    global movement_collision_sprite_groups
    for collision_sprite_group in movement_collision_sprite_groups:
        if collision_sprite_group.sprite.id == id:
            movement_collision_sprite_groups.remove(collision_sprite_group)
    for collision_sprite_group in melee_collision_sprite_groups:
        if collision_sprite_group.sprite.id == id:
            melee_collision_sprite_groups.remove(collision_sprite_group)

def create_ettin_monster(position):
    ettin_monster_sprite_grup = create_ettin_monster_sprite_group(position)
    add_auxilary_objects(ettin_monster_sprite_grup)

def add_auxilary_objects(monster_sprite_grup):
    movement_collision_shadow_sprite_group = monster_sprite_grup.sprite.movement_collision_shadow_sprite_group
    shadow_sprite_group = monster_sprite_grup.sprite.shadow_group
    melee_collision_shadow_sprite_group = monster_sprite_grup.sprite.melee_collision_shadow_sprite_group
    melee_sector_sprite_group = monster_sprite_grup.sprite.melee_sector_sprite_group
    append_sprites_and_entities_lists(monster_sprite_grup,movement_collision_shadow_sprite_group,melee_collision_shadow_sprite_group,shadow_sprite_group,melee_sector_sprite_group)

def append_sprites_and_entities_lists(monster_sprite_group,movement_collision_shadow_sprite_group,melee_collision_shadow_sprite_group,shadow_sprite_group,melee_sector_sprite_group):
    global character_sprite_groups
    global shadow_sprite_groups
    global movement_collision_sprite_groups
    global melee_collision_sprite_groups
    global melee_sector_sprite_groups

    character_sprite_groups.append(monster_sprite_group)
    shadow_sprite_groups.append(shadow_sprite_group)
    movement_collision_sprite_groups.append(movement_collision_shadow_sprite_group)
    melee_collision_sprite_groups.append(melee_collision_shadow_sprite_group)
    melee_sector_sprite_groups.append(melee_sector_sprite_group)

def update_all_entities():
    for charcter_sprite_group in character_sprite_groups:
        charcter_sprite_group.sprite.update()

    for shadow_sprite_group in shadow_sprite_groups:
        shadow_sprite_group.sprite.update()

    for movement_collision_sprite_group in movement_collision_sprite_groups:
        movement_collision_sprite_group.sprite.update()

    for melee_collision_sprite_group in melee_collision_sprite_groups:
        melee_collision_sprite_group.sprite.update()

    for item_sprite_group in item_sprite_groups:
        item_sprite_group.sprite.update()

    for melee_sector_sprite_group in melee_sector_sprite_groups:
        sprites = melee_sector_sprite_group.sprites()
        for melee_sector_sprite in sprites:
            melee_sector_sprite.update()

    for projectile_sprite_group in projectile_sprite_groups:
        sprites = projectile_sprite_group.sprites()
        for projectile_sprite in sprites:
            projectile_sprite.update()

    for level_sprite_group in level_sprite_groups:
        sprites = level_sprite_group.sprites()
        for level_sprite in sprites:
            level_sprite.update()

def generate_monsters():
    generate_monster(ETTIN, (200,200))
    generate_monster(ETTIN, (400,200))
    generate_monster(ETTIN, (600,200))
    generate_monster(ETTIN, (200,600))
    generate_monster(ETTIN, (400,600))
    generate_monster(ETTIN, (600,600))

def fix_all_dead_bodies_to_pixel_accuracy():
    for character in character_sprite_groups:
        if character.sprite.living == False:
            character.sprite.position = int(character.sprite.position[0]), int(character.sprite.position[1])