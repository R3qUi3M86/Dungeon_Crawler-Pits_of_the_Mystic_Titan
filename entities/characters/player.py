import pygame
import random
from settings import *
from sounds import sound_player
from utilities import combat_manager
from utilities import util
from utilities.level_painter import TILE_SIZE
from utilities.text_printer import *
from utilities.constants import *
from utilities import entity_manager
from images.characters.fighter_images import *
from entities.shadow import Shadow
from entities.colliders.collider import Collider

class Hero(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = 8
        self.NAME = PLAYER
        self.TYPE = PLAYER

        ###Position variables###
        self.tile_index = 0,0
        self.prevous_tile_index = self.tile_index
        self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
        self.direct_proximity_collision_tiles = []
        self.far_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index,(screen_height//48+5,screen_width//screen_width+4))
        self.far_proximity_collision_tiles = []
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
        self.entity_collider_nw    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_NW)
        self.entity_collider_ne    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_NE)
        self.entity_collider_sw    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_SW)
        self.entity_collider_se    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_SE)
        self.entity_collider_omni  = Collider(player_position, self.id, ENTITY_OMNI)
        self.small_square         = Collider(self.position, self.id, SQUARE)

        #Melee sectors
        self.melee_collider_e  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_E)
        self.melee_collider_ne = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_NE)
        self.melee_collider_n  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_N)
        self.melee_collider_nw = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_NW)
        self.melee_collider_w  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_W)
        self.melee_collider_sw = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_SW)
        self.melee_collider_s  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_S)
        self.melee_collider_se = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_SE)

        #Shadow
        self.shadow = Shadow(player_position, PLAYER_ID, SIZE_SMALL)

        #Sprite lists
        self.entity_collider_sprites     = [self.entity_collider_omni,self.entity_collider_nw,self.entity_collider_ne,self.entity_collider_sw,self.entity_collider_se,self.small_square]
        self.entity_melee_sector_sprites = [self.melee_collider_e,self.melee_collider_ne,self.melee_collider_n,self.melee_collider_nw,self.melee_collider_w,self.melee_collider_sw,self.melee_collider_s,self.melee_collider_se]
        self.entity_auxilary_sprites     = [[self.shadow],self.entity_melee_sector_sprites,self.entity_collider_sprites]

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

        #Character properties
        self.health = 20
        self.maxhealth = 20
        self.damage = 4
        self.x_range = 58
        self.y_range = 32
        self.x_size = 20
        self.y_size = 11
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
        self.update_animation()
        self.rect = self.image.get_rect(midbottom = (self.image_position))

    def update_position(self,vector):
        self.map_position = round(self.map_position[0] + vector[0],2),round(self.map_position[1] + vector[1],2)
        self.tile_index = int((self.map_position[1]-screen_height//2) // TILE_SIZE[X]), int((self.map_position[0]-screen_width//2)// TILE_SIZE[Y])
        
        if self.tile_index != self.prevous_tile_index:
            self.prevous_tile_index = self.tile_index
            self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
            self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_collision_tiles_list(self.direct_proximity_index_matrix)

            self.far_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index,(screen_height//48+5,screen_width//screen_width+4))

    def update_animation(self):
        if not self.is_dead:
            self.set_character_animation_direction_indices()
            
            if self.is_living:
                self.walking_animation()
                self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

                if self.is_attacking == True:             
                    self.character_attack_animation()

                elif self.is_in_pain == True:
                    self.character_pain_animation()
            
            elif self.is_dying == True:
                self.character_death_animation()

            elif self.is_overkilled == True:
                self.character_overkill_animation()

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

    def character_attack_animation(self):
        self.character_attack_index[1] += 0.05
        if round(self.character_attack_index[1],2) == 1.00:
            combat_manager.attack_monster_with_melee_attack(self.damage)
        if int(self.character_attack_index[1]) == 2:
            self.is_attacking = False
            self.character_attack_index[1] = 0
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
            sound_player.player_death_sound.play()
            self.is_living = False
            self.is_dying = True

            if -(self.maxhealth//2) >= self.health:
                sound_player.player_death_sound.stop()
                random.choice(sound_player.player_overkill_sounds).play()
                self.is_living = False
                self.is_dying = False
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
