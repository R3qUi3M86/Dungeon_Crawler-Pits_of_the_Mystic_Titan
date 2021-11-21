import pygame
import random
from settings import *
from sounds import sound_player
from entities import shadow
from entities import melee_range
from utilities import util
from utilities import combat_manager
from utilities import collision_manager
from utilities import entity_manager
from utilities.level_painter import TILE_SIZE
from utilities.text_printer import *
from utilities.constants import *
from images.characters.fighter_images import *

class Hero(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        ###Constants###
        self.SPRITE_DISPLAY_CORRECTION = 8
        self.NAME = PLAYER
        self.TYPE = PLAYER

        ###Position variables###
        self.tile_index = 0,0
        self.position = position
        self.map_position = 0,0
        self.sprite_position = self.position[0], self.position[1] + self.SPRITE_DISPLAY_CORRECTION

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
        self.character_pain_timer = 0
        
        ###Owned sprites###
        #Colliders
        self.entity_collision_mask_nw = shadow.Shadow(player_position, PLAYER_ID, SIZE_SMALL, True, SECTOR_NW)
        self.entity_collision_mask_ne = shadow.Shadow(player_position, PLAYER_ID, SIZE_SMALL, True, SECTOR_NE)
        self.entity_collision_mask_sw = shadow.Shadow(player_position, PLAYER_ID, SIZE_SMALL, True, SECTOR_SW)
        self.entity_collision_mask_se = shadow.Shadow(player_position, PLAYER_ID, SIZE_SMALL, True, SECTOR_SE)
        self.entity_collision_mask    = shadow.Shadow(player_position, PLAYER_ID, SIZE_SMALL, True)

        #Melee sectors
        self.entity_melee_e_sector  = melee_range.Melee(player_position, SECTOR_E)
        self.entity_melee_ne_sector = melee_range.Melee(player_position, SECTOR_NE)
        self.entity_melee_n_sector  = melee_range.Melee(player_position, SECTOR_N)
        self.entity_melee_nw_sector = melee_range.Melee(player_position, SECTOR_NW)
        self.entity_melee_w_sector  = melee_range.Melee(player_position, SECTOR_W)
        self.entity_melee_sw_sector = melee_range.Melee(player_position, SECTOR_SW)
        self.entity_melee_s_sector  = melee_range.Melee(player_position, SECTOR_S)
        self.entity_melee_se_sector = melee_range.Melee(player_position, SECTOR_SE)

        #Shadow
        self.shadow = shadow.Shadow(player_position, PLAYER_ID, SIZE_SMALL)

        #Sprite lists
        self.entity_collision_mask_sprites = [self.entity_collision_mask_nw,self.entity_collision_mask_ne,self.entity_collision_mask_sw,self.entity_collision_mask_se]
        self.entity_melee_sector_sprites   = [self.entity_melee_e_sector,self.entity_melee_ne_sector,self.entity_melee_n_sector,self.entity_melee_nw_sector,self.entity_melee_w_sector,self.entity_melee_sw_sector,self.entity_melee_s_sector,self.entity_melee_se_sector]
        self.entity_auxilary_sprites       = [[self.shadow],self.entity_collision_mask_sprites,self.entity_melee_sector_sprites]


        ###Initial sprite definition###
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

        ###General variables###
        #Status flags
        self.is_monster = False
        self.is_attacking = False
        self.is_living = True
        self.is_dying = False
        self.is_overkilled = False
        self.is_in_pain = False

        #Character properties
        self.health = 20
        self.maxhealth = 20
        self.attack_can_be_interrupted = False
        self.can_shoot = False
        self.projectile_type = None
        self.abilities = []
        self.facing_direction = SECTOR_S
        self.speed = 3
        self.speed_scalar = 0,0
        self.speed_vector = 0,0

    #Update functions
    def update(self):
        
        if self.is_living == False:
            self.speed_vector = 0,0
        else:
            self.set_character_animation_direction_indices()
            self.image = character_walk[int(self.character_walk_index[0])][int(self.character_walk_index[1])]
            self.walking_animation()

        if self.is_attacking == True:
            self.character_attack_animation()

        if self.is_in_pain == True:
            self.character_pain_animation()
        
        if self.is_dying == True:
            self.character_death_animation()

        if self.is_overkilled == True:
            self.character_overkill_animation()

    def update_position(self,vector):
        self.map_position = round(self.map_position[0] + vector[0],2),round(self.map_position[1] + vector[1],2)
        self.tile_index = int(self.map_position[1] // TILE_SIZE[X]), int(self.map_position[0]// TILE_SIZE[Y])

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
        else:
            self.character_pain_timer += 0.05
            if self.facing_direction == SECTOR_E:
                self.image = character_pain_east
            elif self.facing_direction == SECTOR_NE:
                self.image = character_pain_north_east
            elif self.facing_direction == SECTOR_N:
                self.image = character_pain_north
            elif self.facing_direction == SECTOR_NW:
                self.image = character_pain_north_west
            elif self.facing_direction == SECTOR_W:
                self.image = character_pain_west
            elif self.facing_direction == SECTOR_SW:
                self.image = character_pain_south_west
            elif self.facing_direction == SECTOR_S:
                self.image = character_pain_south
            elif self.facing_direction == SECTOR_SE:
                self.image = character_pain_south_east
            if int(self.character_pain_timer) >= 1:
                self.is_in_pain = False
                self.character_pain_timer = 0

    def character_death_animation(self):
        if self.is_overkilled == False:
            self.character_death_index += 0.1
            if int(self.character_death_index) == 7:
                self.character_death_index = 6
                self.is_dying == False
            self.image = self.character_death[int(self.character_death_index)]

    def character_overkill_animation(self):
        self.character_overkill_index += 0.1
        if int(self.character_overkill_index) == 10:
            self.character_overkill_index = 9
            self.is_overkilled == False
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

    def character_attack_animation(self):
        if self.is_attacking:
            self.character_attack_index[1] += 0.05
            if round(self.character_attack_index[1],2) == 1.00:
                combat_manager.attack_monster_with_melee_attack()
            if int(self.character_attack_index[1]) == 2:
                self.is_attacking = False
                self.character_attack_index[1] = 0
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]

    def set_character_animation_direction_indices(self):
        if self.facing_direction == SECTOR_E:
            self.character_walk_index[0] = 0
            self.character_attack_index[0] = 0
        elif self.facing_direction == SECTOR_NE:
            self.character_walk_index[0] = 1
            self.character_attack_index[0] = 1
        elif self.facing_direction == SECTOR_N:
            self.character_walk_index[0] = 2
            self.character_attack_index[0] = 2
        elif self.facing_direction == SECTOR_NW:
            self.character_walk_index[0] = 3
            self.character_attack_index[0] = 3
        elif self.facing_direction == SECTOR_W:
            self.character_walk_index[0] = 4
            self.character_attack_index[0] = 4
        elif self.facing_direction == SECTOR_SW:
            self.character_walk_index[0] = 5
            self.character_attack_index[0] = 5
        elif self.facing_direction == SECTOR_S:
            self.character_walk_index[0] = 6
            self.character_attack_index[0] = 6
        elif self.facing_direction == SECTOR_SE:
            self.character_walk_index[0] = 7
            self.character_attack_index[0] = 7 

    #Combat functions
    def take_damage(self, damage):
        self.health -= damage

        if self.health > 0:
            self.is_in_pain = True
            sound_player.player_pain_sound.play()

        else:
            if self.is_living == True:
                sound_player.player_pain_sound.stop()
                sound_player.player_death_sound.play()
                self.is_living = False
                self.is_in_pain = False
                self.is_dying = True

            if self.is_overkilled == False and -(self.maxhealth//2) >= self.health:
                sound_player.player_death_sound.stop()
                random.choice(sound_player.player_overkill_sounds).play()
                self.is_living = False
                self.is_in_pain = False
                self.is_dying = True
                self.is_overkilled = True

    #Misc
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
