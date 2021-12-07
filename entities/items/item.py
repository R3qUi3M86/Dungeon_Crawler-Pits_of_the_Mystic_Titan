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
CONSUMABLE_COOLDOWN_DICT = {QUARTZ_FLASK:5}

class Item(pygame.sprite.Sprite):
    def __init__(self, tile_index, name):
        super().__init__()
        ###Constants###
        self.NAME = name
        self.TYPE = ITEM
        self.IMAGE_DISPLAY_CORRECTION = self.get_img_display_correction()

        ###Position variables###
        self.tile_index = tile_index
        self.prevous_tile_index = tile_index
        self.position = self.get_position()
        self.map_position = round(self.position[0]+entity_manager.hero.map_position[0]-player_position[0],2), round(self.position[1]+entity_manager.hero.map_position[1]-player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION
        self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
        self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)

        ###Object ID###
        self.id = util.generate_entity_id()
        
        ###Animations###
        self.item_static_image = STATIC_IMAGE_DICT[name]
        self.item_animation_images = self.get_item_animation_images()
        self.item_destruction_images = self.get_item_destruction_images()
        self.animation_index = 0
        self.destruction_index = 0

        ###Owned sprites###
        #Colliders
        self.entity_small_square_collider  = Collider(self.position, self.id, SQUARE, size=SIZE_SMALL)
        self.entity_tiny_omni_collider = Collider(self.position, self.id, ENTITY_OMNI, size=SIZE_TINY)

        #Shadow
        self.shadow = Shadow(self.position, self.map_position, self.id, SIZE_TINY, self.tile_index)

        #Sprite lists
        self.entity_auxilary_sprites = [self.entity_small_square_collider, self.shadow, self.entity_tiny_omni_collider]

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
        self.is_currency = self.get_is_currency()
        self.is_consumable = self.get_is_consumable()
        self.is_pickable = self.get_is_pickable()
        self.is_destructible = self.get_is_destructible()
        self.is_falling_apart = False
        self.is_destroyed = False
        self.can_collide = self.get_can_collide()

        ###Item properties###
        #General
        self.damage = self.get_weapon_damage()
        self.chainfire = self.get_chainfire()
        self.chainfire_cooldown_limit = self.get_chainfire_cooldown()
        self.chainfire_cooldown = self.chainfire_cooldown_limit
        self.size = self.get_item_size()
        self.speed = 0,0

        self.ammo_type = self.get_ammo_type()
        self.ammo = self.get_ammo()
        self.attack_type = self.get_attack_type()
        self.attack_speed = self.get_attack_speed()
        self.range = self.get_weapon_range()
        self.is_ready_to_use = True
        self.use_cooldown = 0
        self.use_cooldown_limit = self.get_use_cooldown_limit()
        self.quantity = self.get_quantity()

    #Updates
    def update(self):
        if self.is_picked:
            entity_manager.remove_item_from_the_map_and_give_to_player(self)
            sound_player.play_item_picked_sound(self)
        
        if self.is_animated:
            self.increment_animation_timer()

        if self.is_falling_apart:
            self.update_position(self.speed)
            self.bleed_off_speed()
            self.increment_destruction_animation_timer()

    def update_position(self, vector=None):
        if vector:
            self.position = round((self.position[0]-vector[0]),2),round((self.position[1] - vector[1]),2)
            self.map_position = round(self.position[0] + entity_manager.hero.map_position[0] - player_position[0],2), round(self.position[1]+entity_manager.hero.map_position[1]-player_position[1],2)
            self.tile_index = util.get_tile_index(self.map_position)
        else:
            self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.update_owned_sprites_position()
        if self.tile_index != self.prevous_tile_index:
            self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
            self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)
            entity_manager.move_entity_in_all_matrices(self.id, ITEM, self.prevous_tile_index, self.tile_index)
            self.prevous_tile_index = self.tile_index

    def update_owned_sprites_position(self):
        for auxilary_sprite in self.entity_auxilary_sprites:
                auxilary_sprite.update_position(self.position)

    #Getters
    def get_img_display_correction(self):
        if self.NAME is GOLD_COINS:
            return 8
        elif self.NAME is VASE:
            return 3
        else:
            return 0

    def get_position(self):
        if self.NAME is WALL_TORCH:
            return level_painter.get_tile_position(self.tile_index)[0]+24, level_painter.get_tile_position(self.tile_index)[1]
        else:
            return level_painter.get_tile_position(self.tile_index)[0]+24, level_painter.get_tile_position(self.tile_index)[1]+24

    def get_is_pickable(self):
        if self.is_weapon:
            return True
        elif self.is_ammo:
            return True
        elif self.is_consumable:
            return True
        elif self.is_currency:
            return True
        return False       

    def get_is_destructible(self):
        if self.NAME in DESTRUCTIBLE_ITEMS:
            return True
        return False

    def get_item_animation_images(self):
        if self.NAME in ANIMATED_ITEMS:
            return ANIMATED_ITEM_IMAGES[self.NAME]

    def get_item_destruction_images(self):
        if self.NAME in DESTRUCTIBLE_ITEMS:
            return DESTRUCTIBLE_ITEM_IMAGES[self.NAME]

    def get_is_animated(self):
        if self.NAME in ANIMATED_ITEMS:
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

    def get_is_currency(self):
        if self.NAME in CURRENCIES:
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
        if self.NAME is VASE:
            return 18, 10

    def get_can_collide(self):
        if self.is_pickable:
            return True
        elif self.NAME is VASE:
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

    def get_quantity(self):
        if self.is_consumable:
            return 1
        elif self.is_currency:
            return random.choice(range(1,26))

    #Item destruction
    def destroy_item(self):
        sound_player.play_vase_break_sound()
        self.is_falling_apart = True

    def bleed_off_speed(self):
        x_speed = self.speed[0]
        y_speed = self.speed[1]
        if x_speed > 0:
            x_speed -= 0.05
            if x_speed < 0:
                x_speed = 0
        else:
            x_speed += 0.05
            if x_speed > 0:
                x_speed = 0
        
        if y_speed > 0:
            y_speed -= 0.05
            if y_speed < 0:
                y_speed = 0
        else:
            y_speed += 0.05
            if y_speed > 0:
                y_speed = 0
        
        self.speed = x_speed, y_speed

    #Timers
    def increment_animation_timer(self):
        self.animation_index += 0.1
        if int(self.animation_index) >= len(self.item_animation_images):
            self.animation_index = 0
        
        if self.NAME is WALL_TORCH:
            if int(self.animation_index) >= 1:
                self.animation_index = 0
                self.image = self.item_animation_images[random.choice(range(len(self.item_animation_images)))]
        
        elif self.NAME is GOLD_COINS:
            if int(self.animation_index) >= 5:
                spark_decision = random.choice(range(3))
                spark_choice = None
                if spark_decision > 1:
                    spark_choice = random.choice(range(1,7))
                    self.animation_index = 4.3
                else:
                    spark_choice = 0
                    self.animation_index = 0
                self.image = self.item_animation_images[spark_choice]
        else:
            self.image = self.item_animation_images[int(self.animation_index)]

    def increment_destruction_animation_timer(self):
        self.animation_index += 0.2
        if int(self.animation_index) >= len(self.item_destruction_images):
            self.animation_index = len(self.item_destruction_images)-1
            self.is_destroyed = True
            self.is_falling_apart = False
            item = Item(self.tile_index,GOLD_COINS)
            item.position = self.position[0], self.position[1]+1
            item.map_position = self.map_position[0], self.map_position[1]+1
            item.update_position()
            entity_manager.put_item_in_matrices_and_lists(item)
            entity_manager.fix_all_dead_objects_to_pixel_accuracy()
        self.image = self.item_destruction_images[int(self.animation_index)]

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