import pygame
import math
from utilities.constants import *
from entities.characters.ettin import Ettin
from entities.characters.player import Hero

entities_id = []

#Standard entities
hero = Hero(player_position)
entity_sprite_groups = []
shadow_sprite_groups = []
level_sprite_groups = []
projectile_sprite_groups = []

#Collision entities
level_collision_sprite_groups = [] #For collision search optimization
melee_sector_sprite_groups = []
entity_collision_sprite_groups = []

#Hero entity initialization
def initialize_player_object():
    entity_sprite_groups.append(pygame.sprite.GroupSingle(hero))
    shadow_sprite_groups.append(pygame.sprite.GroupSingle(hero.shadow))
    melee_sector_sprite_groups.append(pygame.sprite.Group(hero.entity_melee_sector_sprites))
    entity_collision_sprite_groups.append(pygame.sprite.Group(hero.entity_collider_sprites))  

#Get sprites
def get_level_collision_sprite_by_index(index):
    for level_collision_sprite_group in level_collision_sprite_groups:
        if level_collision_sprite_group.sprite.get_index() == index:
            return level_collision_sprite_group.sprite

def get_entity_sprite_by_id(entity_id):
    for entity in entity_sprite_groups:
        if entity.sprite.id == entity_id:
            return entity.sprite

#Updates
def update_all_entities():
    global entity_sprite_groups
    global level_sprite_groups
    global projectile_sprite_groups

    for entity_sprite_group in entity_sprite_groups:
        entity_sprite_group.sprite.update()
    
    for level_sprite_group in level_sprite_groups:
        level_sprite_group.sprite.update()

    for projectile_sprite_group in projectile_sprite_groups:
        sprites = projectile_sprite_group.sprites()
        for projectile_sprite in sprites:
            projectile_sprite.update()

def update_all_non_player_entities_position_by_vector(vector):
    update_non_player_group_single_entities_position(vector,entity_sprite_groups)
    if round(hero.speed_scalar[0],2) != 0.0 or round(hero.speed_scalar[1],2) != 0.0:
        update_non_player_group_single_entities_position(vector,level_collision_sprite_groups)
    update_non_player_group_single_entities_position(vector,projectile_sprite_groups)

def update_hero_position():
    hero.update_position(hero.speed_vector)

def update_non_player_group_single_entities_position(vector,entities):
    for entity in entities:
        if entity.sprite != hero:
            entity.sprite.update_position(vector)

def update_non_player_group_entities_position(vector,entities):
    for _ in entities:
        entity_sprites = entities.sprites()
        for entity_sprite in entity_sprites:
            entity_sprite.update_position(vector)

#Monster generation
def generate_monsters():
    generate_monster(ETTIN,(4,2))
    # generate_monster(ETTIN, (5,6))
    # generate_monster(ETTIN, (4,1))
    # generate_monster(ETTIN, (7,3))
    # generate_monster(ETTIN, (7,8))
    # generate_monster(ETTIN, (6,7))
    # generate_monster(ETTIN,(11,22))
    # generate_monster(ETTIN, (11,23))
    # generate_monster(ETTIN, (11,24))
    # generate_monster(ETTIN, (10,22))
    # generate_monster(ETTIN, (10,23))
    # generate_monster(ETTIN, (10,24))
    # generate_monster(ETTIN, (10,25))
    # generate_monster(ETTIN, (3,25))
    # generate_monster(ETTIN, (3,26))
    # generate_monster(ETTIN, (3,24))
    # generate_monster(ETTIN, (3,23))
    # generate_monster(ETTIN, (4,25))
    # generate_monster(ETTIN, (4,26))
    # generate_monster(ETTIN, (4,24))
    # generate_monster(ETTIN, (4,23))
    # generate_monster(ETTIN, (4,25))
    # generate_monster(ETTIN, (4,26))
    # generate_monster(ETTIN, (2,24))
    # generate_monster(ETTIN, (2,23))
    # generate_monster(ETTIN, (2,25))
    # generate_monster(ETTIN, (2,26))
    # generate_monster(ETTIN, (2,27))
    # generate_monster(ETTIN, (4,22))
    pass

def generate_monster(monster_type, tile_index):
    if monster_type == ETTIN:
        create_ettin_monster(tile_index)

def create_ettin_monster(position):
    monster = Ettin(position)
    append_sprite_groups_lists(monster)

#Object auxilary entities generation
def append_sprite_groups_lists(object_entity):
    global entity_sprite_groups
    global shadow_sprite_groups
    global entity_collision_sprite_groups
    global melee_sector_sprite_groups

    entity_sprite_groups.append(pygame.sprite.GroupSingle(object_entity))
    shadow_sprite_groups.append(pygame.sprite.GroupSingle(object_entity.shadow))
    entity_collision_sprite_groups.append(pygame.sprite.Group(object_entity.entity_collider_sprites))
    
    if object_entity.TYPE == MONSTER:
        melee_sector_sprite_groups.append(pygame.sprite.Group(object_entity.entity_melee_sector_sprites))

#Misc
def kill_entity_colliders_and_melee_entities(id):
    global entity_collision_sprite_groups
    global melee_sector_sprite_groups

    for entity_collision_sprite_group in entity_collision_sprite_groups:
        if entity_collision_sprite_group.sprites()[0].id == id:
            entity_collision_sprite_groups.remove(entity_collision_sprite_group)
    
    for melee_sector_sprite_group in melee_sector_sprite_groups:
        if melee_sector_sprite_group.sprites()[0].id == id:
            melee_sector_sprite_groups.remove(melee_sector_sprite_group)

def fix_all_dead_objects_to_pixel_accuracy():
    for entity_sprite_group in entity_sprite_groups:
        if entity_sprite_group.sprite.is_living == False:
            entity_sprite_group.sprite.position = math.ceil(entity_sprite_group.sprite.position[0]), math.ceil(entity_sprite_group.sprite.position[1])

def fix_all_tiles_to_pixel_accuracy():
    for level_sprite_group in level_sprite_groups:
        level_sprite_group.sprite.position = math.ceil(level_sprite_group.sprite.position[0]), math.ceil(level_sprite_group.sprite.position[1])

def fix_player_position_to_pixel_accuracy():
    hero.position = math.floor(hero.position[0]), math.floor(hero.position[1])
    hero.map_position = math.floor(hero.map_position[0]), math.floor(hero.map_position[1])