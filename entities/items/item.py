import pygame
from images.items.item_images import *
from entities.shadow import Shadow
from entities.colliders.collider import Collider
from utilities.constants import *
from utilities import util
from utilities import level_painter
from utilities import entity_manager
from sounds import sound_player

STATIC_IMAGE_DICT = {SWORD:sword, ETTIN_MACE:sword, EMERALD_CROSSBOW:emerald_crossbow}
WEAPON_DAMAGE_DICT = {SWORD:2,ETTIN_MACE:1,EMERALD_CROSSBOW:2}
WEAPON_ATTACK_SPEED_DICT = {SWORD:1,ETTIN_MACE:1,EMERALD_CROSSBOW:0.8}

class Item(pygame.sprite.Sprite):
    def __init__(self, tile_index, name):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = 0
        self.NAME = name
        self.TYPE = ITEM

        ###Position variables###
        self.tile_index = tile_index
        self.position = level_painter.get_tile_position(tile_index)
        self.map_position = round(self.position[0]+entity_manager.hero.map_position[0]-player_position[0],2), round(self.position[1]+entity_manager.hero.map_position[1]-player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION

        ###Object ID###
        self.id = util.generate_entity_id()
        
        ###Animations###
        #Static image assets
        self.item_static_image = STATIC_IMAGE_DICT[name]

        ###Owned sprites###
        #Colliders
        self.entity_small_square_collider  = Collider(self.position, self.id, SQUARE, size=SIZE_SMALL)

        #Shadow
        self.shadow = Shadow(self.position, self.map_position, self.id, SIZE_TINY, self.tile_index)

        #Sprite lists
        self.entity_auxilary_sprites = [self.entity_small_square_collider, self.shadow]

        ###Initial sprite definition###
        self.image = self.get_image()
        self.rect = self.image.get_rect(midbottom = (self.image_position))

        #####General variables#####
        ###Status flags###
        self.is_picked = False
        self.is_weapon = self.get_is_weapon()
        self.is_ammo = self.get_is_ammo()
        self.is_pickable = self.get_pickable()

        ###Item properties###
        #General
        self.damage = WEAPON_DAMAGE_DICT[name]
        self.size = self.get_item_size()

        self.ammo_type = self.get_ammo_type()
        self.ammo = self.get_ammo()
        self.attack_type = self.get_attack_type()
        self.attack_speed = self.get_attack_speed()

    #Updates
    def update(self):
        if self.is_picked:
            entity_manager.remove_item_from_the_map_and_give_to_player(self)
            sound_player.play_item_picked_sound(self)

    def update_position(self, vector=None):
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.update_owned_sprites_position()

    def update_owned_sprites_position(self):
        for auxilary_sprite in self.entity_auxilary_sprites:
                auxilary_sprite.update_position(self.position)

    #Getters
    def get_pickable(self):
        if self.is_weapon:
            return True
        elif self.is_ammo:
            return True
        return False

    def get_image(self):
        if self.NAME in WEAPONS:
            return self.item_static_image

    def get_is_weapon(self):
        if self.NAME in WEAPONS:
            return True
        return False

    def get_is_ammo(self):
        if self.NAME in AMMOTYPES:
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

    def get_attack_speed(self):
        if self.is_weapon:
            return WEAPON_ATTACK_SPEED_DICT[self.NAME]
