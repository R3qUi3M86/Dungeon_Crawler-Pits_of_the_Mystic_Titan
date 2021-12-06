import pygame
import random
from images.items.item_images import *
from entities.shadow import Shadow
from entities.colliders.collider import Collider
from utilities.constants import *
from utilities import util
from utilities import level_painter
from utilities import entity_manager
from sounds import sound_player

WEAPON_DAMAGE_DICT = {SWORD:2, ETTIN_MACE:1, BISHOP_MAGIC_MISSILE:1, EMERALD_CROSSBOW:2}
WEAPON_RANGE_DICT = {EMERALD_CROSSBOW:30, BISHOP_MAGIC_MISSILE:20}
WEAPON_CHAINFIRE_DICT = {SWORD:1, ETTIN_MACE:1, BISHOP_MAGIC_MISSILE:5, EMERALD_CROSSBOW:1}
WEAPON_CHAINFIRE_COOLDOWN_LIMIT_DICT = {SWORD:0, ETTIN_MACE:0, BISHOP_MAGIC_MISSILE:0.15, EMERALD_CROSSBOW:0}
WEAPON_ATTACK_SPEED_DICT = {SWORD:1, ETTIN_MACE:1, BISHOP_MAGIC_MISSILE:0.8, EMERALD_CROSSBOW:3}
WEAPON_ATTACK_COOLDOWN_DICT = {SWORD:0, ETTIN_MACE:0, BISHOP_MAGIC_MISSILE:3.5, EMERALD_CROSSBOW:1.2}
CONSUMABLE_COOLDOWN_DICT = {CRYSTAL_VIAL:5}

class Item(pygame.sprite.Sprite):
    def __init__(self, tile_index, name):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = 0
        self.NAME = name
        self.TYPE = ITEM

        ###Position variables###
        self.tile_index = tile_index
        self.position = self.get_position()
        self.map_position = round(self.position[0]+entity_manager.hero.map_position[0]-player_position[0],2), round(self.position[1]+entity_manager.hero.map_position[1]-player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION

        ###Object ID###
        self.id = util.generate_entity_id()
        
        ###Animations###
        self.item_static_image = STATIC_IMAGE_DICT[name]
        self.item_animation_images = self.get_item_animation_images()
        self.animation_index = 0

        ###Owned sprites###
        #Colliders
        self.entity_small_square_collider  = Collider(self.position, self.id, SQUARE, size=SIZE_SMALL)

        #Shadow
        self.shadow = Shadow(self.position, self.map_position, self.id, SIZE_TINY, self.tile_index)

        #Sprite lists
        self.entity_auxilary_sprites = [self.entity_small_square_collider, self.shadow]

        ###Initial sprite definition###
        self.image = self.item_static_image
        self.rect = self.image.get_rect(midbottom = (self.image_position))

        #####General variables#####
        ###Status flags###
        self.is_picked = False
        self.is_animated = self.get_is_animated()
        self.is_decor = self.get_is_decor()
        self.is_weapon = self.get_is_weapon()
        self.is_ammo = self.get_is_ammo()
        self.is_consumable = self.get_is_consumable()
        self.is_pickable = self.get_pickable()
        self.can_collide = self.get_can_collide()

        ###Item properties###
        #General
        self.damage = self.get_weapon_damage()
        self.chainfire = self.get_chainfire()
        self.chainfire_cooldown_limit = self.get_chainfire_cooldown()
        self.chainfire_cooldown = self.chainfire_cooldown_limit
        self.size = self.get_item_size()

        self.ammo_type = self.get_ammo_type()
        self.ammo = self.get_ammo()
        self.attack_type = self.get_attack_type()
        self.attack_speed = self.get_attack_speed()
        self.range = self.get_weapon_range()
        self.is_ready_to_use = True
        self.use_cooldown = 0
        self.use_cooldown_limit = self.get_use_cooldown_limit()
        self.consumable_quantity = 1

    #Updates
    def update(self):
        if self.is_picked:
            entity_manager.remove_item_from_the_map_and_give_to_player(self)
            sound_player.play_item_picked_sound(self)
        
        if self.is_animated:
            self.increment_animation_timer()

    def update_position(self, vector=None):
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.update_owned_sprites_position()

    def update_owned_sprites_position(self):
        for auxilary_sprite in self.entity_auxilary_sprites:
                auxilary_sprite.update_position(self.position)

    #Getters
    def get_position(self):
        if self.NAME is WALL_TORCH:
            return level_painter.get_tile_position(self.tile_index)[0]+24, level_painter.get_tile_position(self.tile_index)[1]
        else:
            return level_painter.get_tile_position(self.tile_index)[0]+24, level_painter.get_tile_position(self.tile_index)[1]+24

    def get_pickable(self):
        if self.is_weapon:
            return True
        elif self.is_ammo:
            return True
        return False       

    def get_item_animation_images(self):
        if self.NAME in DECORATIONS:
            if self.NAME is WALL_TORCH:
                return wall_torch_images
        elif self.NAME in AMMOTYPES:
            if self.NAME is EMERALD_CROSSBOW_QUIVER:
                return crossbow_quiver

    def get_is_animated(self):
        if self.NAME is WALL_TORCH:
            return True
        elif self.NAME is EMERALD_CROSSBOW_QUIVER:
            return True
        return False

    def get_is_weapon(self):
        if self.NAME in WEAPONS:
            return True
        return False

    def get_is_decor(self):
        if self.NAME in DECORATIONS:
            return True
        return False

    def get_is_ammo(self):
        if self.NAME in AMMOTYPES:
            return True
        return False

    def get_is_consumable(self):
        if self.NAME in CONSUMABLES:
            return True
        return False

    def get_ammo(self):
        if self.is_weapon:
            if self.NAME is not SWORD:
                return 3
            else:
                return -1

        elif self.is_ammo:
            if self.NAME is EMERALD_CROSSBOW_BOLTS:
                return 5
            elif self.NAME is EMERALD_CROSSBOW_QUIVER:
                return 10
        else:
            return 0

    def get_ammo_type(self):
        if self.is_ammo:
            if self.NAME in CROSSBOW_AMMO:
                return EMERALD_CROSSBOW
    
    def get_attack_type(self):
        if self.is_weapon:
            if self.NAME in RANGED_WEAPONS:
                return RANGED
            else:
                return MELEE

    def get_item_size(self):
        if self.is_pickable or self.is_weapon:
            return 15, 8

    def get_can_collide(self):
        if self.is_pickable:
            return True
        elif self.NAME is WALL_TORCH:
            return False
        return False

    def get_attack_speed(self):
        if self.is_weapon:
            return WEAPON_ATTACK_SPEED_DICT[self.NAME]

    def get_weapon_damage(self):
        if self.is_weapon:
            return WEAPON_DAMAGE_DICT[self.NAME]

    def get_weapon_range(self):
        if self.is_weapon and self.attack_type is RANGED:
            return WEAPON_RANGE_DICT[self.NAME]

    def get_chainfire(self):
        if self.is_weapon:
            return WEAPON_CHAINFIRE_DICT[self.NAME]

    def get_chainfire_cooldown(self):
        if self.is_weapon:
            return WEAPON_CHAINFIRE_COOLDOWN_LIMIT_DICT[self.NAME]

    def get_use_cooldown_limit(self):
        if self.is_weapon:
            return WEAPON_ATTACK_COOLDOWN_DICT[self.NAME]

        elif self.is_consumable:
            return CONSUMABLE_COOLDOWN_DICT[self.NAME]

    #Timers
    def increment_animation_timer(self):
        self.animation_index += 0.1
        if int(self.animation_index) >= len(self.item_animation_images):
            self.animation_index = 0
        
        if self.NAME is WALL_TORCH:
            if int(self.animation_index) >= 1:
                self.animation_index = 0
                self.image = self.item_animation_images[random.choice(range(len(self.item_animation_images)))]
        else:
            self.image = self.item_animation_images[int(self.animation_index)]

    def increment_item_cooldown_timer(self):
        if not self.is_ready_to_use:
            if self.is_weapon:
                if self.attack_type is MELEE:
                    self.use_cooldown += 0.05
                elif self.attack_type is RANGED:
                    self.use_cooldown += 0.025
            
            elif self.is_consumable:
                self.use_cooldown += 0.01667
        
        if self.use_cooldown >= self.use_cooldown_limit:
            self.is_ready_to_use = True
            self.use_cooldown = 0
            if self.is_weapon:
                self.chainfire_cooldown = self.chainfire_cooldown_limit
                self.chainfire = WEAPON_CHAINFIRE_DICT[self.NAME]

    def increment_chainfire_cooldown(self):
        self.chainfire_cooldown += 0.0167