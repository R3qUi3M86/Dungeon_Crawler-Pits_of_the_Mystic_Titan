import pygame
import random
from settings import *
from sounds import sound_player
from utilities import combat_manager
from utilities import util
from utilities.text_printer import *
from utilities.constants import *
from utilities import entity_manager
from images.characters.fighter_images import *
from entities.shadow import Shadow
from entities.colliders.collider import Collider
from entities.items.item import Item

IMAGE_DISPLAY_CORRECTION = 8

class Hero(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = IMAGE_DISPLAY_CORRECTION
        self.NAME = PLAYER
        self.TYPE = PLAYER

        ###Position variables###
        self.tile_index = 0,0
        self.prevous_tile_index = self.tile_index
        self.direct_proximity_index_matrix = []
        self.direct_proximity_collision_tiles = []
        self.direct_proximity_monsters = []
        self.position = position
        self.map_position = 0,0
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION

        ###Object ID###
        self.id = PLAYER_ID

        ###Animations
        #Walk assets
        self.character_walk = character_walk
        self.character_walk_index = [6,0]
        
        #Attack assets
        self.character_attack = character_attack
        self.character_attack_index = [6,0]
        
        #Death assets
        self.character_death = character_death
        self.character_death_index = 0

        #Overkill assets
        self.character_overkill = character_overkill
        self.character_overkill_index = 0

        #Pain assets
        self.character_pain = character_pain
        self.character_pain_index = 0
        self.character_pain_timer = 0
        
        ###Owned sprites###
        #Colliders
        self.entity_collider_nw    = Collider(player_position, self.id, ENTITY_SECTOR, SECTOR_NW)
        self.entity_collider_ne    = Collider(player_position, self.id, ENTITY_SECTOR, SECTOR_NE)
        self.entity_collider_sw    = Collider(player_position, self.id, ENTITY_SECTOR, SECTOR_SW)
        self.entity_collider_se    = Collider(player_position, self.id, ENTITY_SECTOR, SECTOR_SE)
        self.entity_collider_omni  = Collider(player_position, self.id, ENTITY_OMNI)
        self.wall_hider_collider = Collider(WALL_HIDER_POSITION, self.id, WALL_HIDER)

        #Shadow
        self.shadow = Shadow(player_position, self.map_position, PLAYER_ID, SIZE_SMALL)

        #Sprite lists
        self.entity_collider_sprites     = [self.entity_collider_omni,self.entity_collider_nw,self.entity_collider_ne,self.entity_collider_sw,self.entity_collider_se]
        self.entity_auxilary_sprites     = [[self.shadow],self.entity_collider_sprites]

        ###Initial sprite definition###
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.image_position))

        ###General variables###
        #Status flags
        self.is_monster = False
        self.is_attacking = False
        self.is_living = True
        self.is_dying = False
        self.is_overkilled = False
        self.is_in_pain = False
        self.is_dead = False
        self.is_corpse = False
        self.can_collide = True

        ###Character properties###
        #General
        self.maxhealth = 20
        self.health = self.maxhealth

        #Combat
        self.melee_damage_modifier = 2
        self.ranged_damage_modifier = 1
        self.x_melee_range = 58
        self.y_melee_range = 32
        self.melee_range = self.x_melee_range, self.y_melee_range
        self.x_size = 20
        self.y_size = 11
        self.size = self.x_size, self.y_size
        self.attack_can_be_interrupted = False
        self.selected_weapon = WEAPONS[0]
        
        #Abilities and items list
        self.abilities = []
        self.items = []
        self.consumables = []
        self.weapons = {SWORD:None, EMERALD_CROSSBOW:None}
        self.ammo = {SWORD:0, EMERALD_CROSSBOW:30}
        
        #Movement
        self.speed = 3
        self.speed_scalar = 0,0
        self.speed_vector = 0,0
        self.facing_direction = SECTOR_S

    #Update functions
    def update(self):
        self.increment_all_items_cooldown()
        self.update_animation()
        self.rect = self.image.get_rect(midbottom = (self.image_position))

    def update_position(self,vector):
        self.map_position = round(self.map_position[0] + vector[0],2),round(self.map_position[1] + vector[1],2)
        self.tile_index = util.get_tile_index(self.map_position)
        
        if self.tile_index != self.prevous_tile_index:
            self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
            self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)
            self.direct_proximity_monsters = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, MONSTER)
            entity_manager.update_far_proximity_matrices_and_lists(util.get_tile_offset(self.prevous_tile_index, self.tile_index))
            #entity_manager.move_entity_in_all_matrices(self.id, self.TYPE, self.prevous_tile_index, self.tile_index)
            self.prevous_tile_index = self.tile_index

    def update_animation(self):
        if not self.is_dead:
            self.set_character_animation_direction_indices()
            
            if self.is_living:
                self.walking_animation()
                self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

                if self.is_attacking == True:
                    if self.weapons[self.selected_weapon].is_ready_to_use and (self.ammo[self.selected_weapon] > 0 or self.ammo[self.selected_weapon] == -1):
                        if self.selected_weapon in MELEE_WEAPONS:             
                            self.character_melee_attack_animation()
                        elif self.selected_weapon in RANGED_WEAPONS:
                            self.character_ranged_attack_animation()
                    else:
                        self.is_attacking = False

                elif self.is_in_pain == True:
                    self.character_pain_animation()
            
            elif self.is_dying == True:
                self.character_death_animation()

            elif self.is_overkilled == True:
                self.character_overkill_animation()

    #Getters
    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.NAME is item_name:
                return item

    def get_weapon_by_name(self, item_name):
        for item in self.items:
            if item.NAME is item_name:
                return item

    #Animations
    def walking_animation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and self.facing_southwards():
            self.character_walk_forward_animation()
        elif keys[pygame.K_w] and self.facing_northwards():
            self.character_walk_forward_animation()
        elif keys[pygame.K_a] and self.facing_westwards():
            self.character_walk_forward_animation()
        elif keys[pygame.K_d] and self.facing_eastwards():
            self.character_walk_forward_animation()
        elif keys[pygame.K_s] and self.facing_northwards():
            self.character_walk_backward_animation()
        elif keys[pygame.K_w] and self.facing_southwards():
            self.character_walk_backward_animation()
        elif keys[pygame.K_a] and self.facing_eastwards():
            self.character_walk_backward_animation()
        elif keys[pygame.K_d] and self.facing_westwards():
            self.character_walk_backward_animation()

    def character_pain_animation(self):
        if self.is_attacking or self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
            self.is_in_pain = False
            self.character_pain_timer = 0
        else:
            self.character_pain_timer += 0.05
            self.image = character_pain[self.character_pain_index]
            if int(self.character_pain_timer) >= 1:
                self.is_in_pain = False
                self.character_pain_timer = 0

    def character_death_animation(self):
        if self.is_overkilled == False:
            self.character_death_index += 0.1
            if int(self.character_death_index) == 7:
                self.character_death_index = 6
                self.is_dying = False
                self.is_dead = True
            self.image = self.character_death[int(self.character_death_index)]

    def character_overkill_animation(self):
        self.character_overkill_index += 0.1
        if int(self.character_overkill_index) == 10:
            self.character_overkill_index = 9
            self.is_overkilled = False
            self.is_dead = True
        self.image = self.character_overkill[int(self.character_overkill_index)]       

    def character_walk_forward_animation(self):
        if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
            self.character_walk_index[1] += 0.1
            if int(self.character_walk_index[1]) == 4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_walk_backward_animation(self):
        if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
            self.character_walk_index[1] -= 0.1
            if int(self.character_walk_index[1]) == -4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_melee_attack_animation(self):
        weapon = self.weapons[self.selected_weapon]
        self.character_attack_index[1] += 0.05*weapon.attack_speed
        
        if round(self.character_attack_index[1],2) == 1.00:
            combat_manager.attack_monster_with_melee_attack(weapon, self.melee_damage_modifier)
        
        if int(self.character_attack_index[1]) == 2:
            self.is_attacking = False
            self.character_attack_index[1] = 0
            self.weapons[self.selected_weapon].is_ready_to_use = False
            if self.ammo[weapon.NAME] != -1:
                self.ammo[weapon.NAME] -= 1
        
        if self.character_attack_index[1] != 0 or pygame.mouse.get_pressed()[0]:
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]

    def character_ranged_attack_animation(self):
        weapon = self.weapons[self.selected_weapon]

        if round(self.character_attack_index[1],3) == 1:
            self.character_attack_index[1] = 1
            if weapon.chainfire_cooldown >= weapon.chainfire_cooldown_limit:
                combat_manager.attack_monsters_with_ranged_weapon(weapon, self.ranged_damage_modifier)
                weapon.chainfire_cooldown = 0
                weapon.chainfire -= 1
            else:
                weapon.increment_chainfire_cooldown()

        if weapon.chainfire == 0:
            self.character_attack_index[1] += 0.025*weapon.attack_speed
            if int(self.character_attack_index[1]) == 2:
                self.is_attacking = False
                self.character_attack_index[1] = 1
                self.weapons[self.selected_weapon].is_ready_to_use = False
                if self.ammo[weapon.NAME] != -1:
                    self.ammo[weapon.NAME] -= 1

        self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]

    def set_character_animation_direction_indices(self):
        for sector in SECTORS:
            if sector == self.facing_direction:
                self.character_walk_index[0] = sector
                self.character_attack_index[0] = sector
                self.character_pain_index = sector

    #Combat functions
    def take_damage(self, damage):
        self.health -= damage

        if self.health > 0:
            self.is_in_pain = True
            sound_player.player_pain_sound.stop()
            sound_player.player_pain_sound.play()

        else:
            sound_player.player_pain_sound.stop()
            if not self.is_dying:
                sound_player.player_death_sound.play()
            self.is_living = False
            self.is_dying = True

            if -(self.maxhealth//2) >= self.health:
                sound_player.player_death_sound.stop()
                if not self.is_overkilled:
                    random.choice(sound_player.player_overkill_sounds).play()
                self.is_living = False
                self.is_dying = False
                self.is_overkilled = True

    def increment_all_items_cooldown(self):
        for weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            if weapon and not weapon.is_ready_to_use:
                weapon.increment_item_cooldown_timer()

        for consumable in self.consumables:
            if not consumable.is_ready_to_use:
                consumable.increment_item_cooldown_timer()


    #Conditions
    def facing_southwards(self):
        if self.facing_direction == SECTOR_S or self.facing_direction == SECTOR_SE or self.facing_direction == SECTOR_SW or self.facing_direction == SECTOR_E or self.facing_direction == SECTOR_W:
            return True
        return False
    
    def facing_eastwards(self):
        if self.facing_direction == SECTOR_E or self.facing_direction == SECTOR_SE or self.facing_direction == SECTOR_NE or self.facing_direction == SECTOR_N or self.facing_direction == SECTOR_S:
            return True
        return False
    
    def facing_northwards(self):
        if self.facing_direction == SECTOR_N or self.facing_direction == SECTOR_NE or self.facing_direction == SECTOR_NW or self.facing_direction == SECTOR_E or self.facing_direction == SECTOR_W:
            return True
        return False

    def facing_westwards(self):
        if self.facing_direction == SECTOR_W or self.facing_direction == SECTOR_SW or self.facing_direction == SECTOR_NW or self.facing_direction == SECTOR_N or self.facing_direction == SECTOR_S:
            return True
        return False
