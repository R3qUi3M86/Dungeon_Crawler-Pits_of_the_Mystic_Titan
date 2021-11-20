import pygame
import random
from settings import *
from entities import shadow
from entities import melee_range
from utilities import util
from utilities import combat_manager
from utilities import movement_manager
from utilities import entity_manager
from utilities import level_painter
from utilities.text_printer import *
from entities.characters import unique_player_objects
from utilities.constants import *
from utilities import monster_ai
from sounds import sound_player
from images.characters.ettin_images import *

class Ettin(pygame.sprite.Sprite):
    def __init__(self,tile_position):
        super().__init__()
        #Walk assets
        self.character_walk = character_walk
        self.character_walk_index = [6,0]
        
        #Attack assets
        self.character_attack = character_attack
        self.character_attack_index = [6,0]

        #Death assets
        self.character_death = character_death
        self.character_death_index = 0

        #Pain assets
        self.character_pain_timer = 0

        #Position variables
        self.tile_position = tile_position
        self.position = level_painter.get_tile_position(tile_position)
        self.map_position = round(self.position[0]-player_position[0]+movement_manager.player_position_on_map[0],2), round(self.position[1]-player_position[1]+movement_manager.player_position_on_map[1],2)
        self.sprite_display_correction = 12
        self.sprite_position = self.position[0], self.position[1] + self.sprite_display_correction
        
        #Object ID
        self.id = util.generate_entity_id()

        #Owned sprites
        self.character_collision_shadow = shadow.Shadow(self.position, self.id, SIZE_SMALL, False)
        self.character_collision_mask_nw = shadow.Shadow(self.position, self.id, SIZE_SMALL, False, SECTOR_NW)
        self.character_collision_mask_ne = shadow.Shadow(self.position, self.id, SIZE_SMALL, False, SECTOR_NE)
        self.character_collision_mask_sw = shadow.Shadow(self.position, self.id, SIZE_SMALL, False, SECTOR_SW)
        self.character_collision_mask_se = shadow.Shadow(self.position, self.id, SIZE_SMALL, False, SECTOR_SE)
        self.melee_collision_shadow = shadow.Shadow(self.position, self.id, SIZE_MEDIUM, False)
        self.shadow                  = shadow.Shadow(self.position, self.id, SIZE_MEDIUM, True)
        self.character_melee_e_sector  = melee_range.Melee(self.position, SECTOR_E)
        self.character_melee_ne_sector = melee_range.Melee(self.position, SECTOR_NE)
        self.character_melee_n_sector  = melee_range.Melee(self.position, SECTOR_N)
        self.character_melee_nw_sector = melee_range.Melee(self.position, SECTOR_NW)
        self.character_melee_w_sector  = melee_range.Melee(self.position, SECTOR_W)
        self.character_melee_sw_sector = melee_range.Melee(self.position, SECTOR_SW)
        self.character_melee_s_sector  = melee_range.Melee(self.position, SECTOR_S)
        self.character_melee_se_sector = melee_range.Melee(self.position, SECTOR_SE)
        self.character_collision_mask_sprites = [self.character_collision_mask_nw,self.character_collision_mask_ne,self.character_collision_mask_sw,self.character_collision_mask_se]
        self.character_melee_sprites = [self.character_melee_e_sector,self.character_melee_ne_sector,self.character_melee_n_sector,self.character_melee_nw_sector,self.character_melee_w_sector,self.character_melee_sw_sector,self.character_melee_s_sector,self.character_melee_se_sector]
        self.character_auxilary_sprites = [self.character_collision_shadow,self.melee_collision_shadow,self.shadow]
        
        #Owned sprite groups
        self.movement_collision_shadow_sprite_group = pygame.sprite.GroupSingle(self.character_collision_shadow)
        self.melee_collision_shadow_sprite_group = pygame.sprite.GroupSingle(self.melee_collision_shadow)
        self.shadow_group = pygame.sprite.GroupSingle(self.shadow)
        self.melee_sector_sprite_group = pygame.sprite.Group(self.character_melee_sprites)

        #Initial image definition
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

        #Character properties        
        self.name = ETTIN
        self.attack = False
        self.attack_interruption_chance = 50
        self.attack_can_be_interrupted = True
        self.facing_direction = SECTOR_S
        self.speed_vector = 0,0
        self.monster_ai = monster_ai.Ai(self)
        self.living = True
        self.dying = False
        self.in_pain = False
        self.health = 10

    #Update functions
    def update(self):
        if self.living == True:
            if self.monster_ai.monster_can_melee_attack_player() == False and self.attack == False:
                self.monster_ai.increment_direction_change_decision_timer()
            else:
                self.facing_direction = self.monster_ai.player_direction_sector

            if self.attack == False and self.in_pain == False:
                self.set_facing_direction()

            if self.monster_ai.monster_can_melee_attack_player():
                self.monster_ai.increment_attack_decision_timer()

            if self.attack == False and self.in_pain == False and unique_player_objects.HERO.living == True:
                self.set_speed_vector()
                if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
                    self.character_walk_forward_animation()
            
            elif self.attack == True and self.in_pain == True:
                self.speed_vector = 0,0
                if self.attack_can_be_interrupted and self.attack_interupted():
                    self.interrupt_attack()

            if self.in_pain == True and self.attack == False:
                self.speed_vector = 0,0
                self.character_pain_animation()

            elif self.attack == True:
                self.speed_vector = 0,0
                self.character_attack_animation()
        
        elif self.dying == True:
            self.interrupt_attack()
            self.in_pain = False
            self.speed_vector = 0,0
            self.character_death_animation()

        if  unique_player_objects.HERO.living == False:
            self.speed_vector = 0,0
      
        self.position = round((self.position[0] + self.speed_vector[0]),2),round((self.position[1] + self.speed_vector[1]),2)
        self.map_position = round(self.position[0]-player_position[0]+movement_manager.player_position_on_map[0],2), round(self.position[1]-player_position[1]+movement_manager.player_position_on_map[1],2)
        self.tile_position = int(self.map_position[1])//48 , int(self.map_position[0])//48
        self.sprite_position = self.position[0], self.position[1] + self.sprite_display_correction
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.update_owned_sprites_position()

    def update_position(self, vector):
        self.position = round((self.position[0]-vector[0]),2),round((self.position[1] - vector[1]),2)
        self.sprite_position = self.position[0], self.position[1] + self.sprite_display_correction
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.update_owned_sprites_position()
    
    def set_facing_direction(self):
        self.set_character_animation_direction_indices()
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
    
    def update_owned_sprites_position(self):
        for auxilary_sprite in self.character_auxilary_sprites:
            auxilary_sprite.position = self.position
            auxilary_sprite.update()
        
        for melee_sprite  in self.character_melee_sprites:
            melee_sprite.position = self.position
            melee_sprite.update()

        for character_collision_mask_sprite in self.character_collision_mask_sprites:
            character_collision_mask_sprite.position = self.position
            character_collision_mask_sprite.update()

    #Animations
    def character_pain_animation(self):
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
            self.in_pain = False
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
            self.character_pain_timer = 0

    def character_death_animation(self):
        self.character_death_index += 0.1
        if int(self.character_death_index) == 7:
            self.character_death_index = 6
            self.dying == False
        self.image = self.character_death[int(self.character_death_index)]

    def character_walk_forward_animation(self):
        self.character_walk_index[1] += 0.1
        if int(self.character_walk_index[1]) == 4:
            self.character_walk_index[1] = 0
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        if self.attack:
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]
            self.rect = self.image.get_rect(midbottom = (self.sprite_position))

            self.character_attack_index[1] += 0.1
            if round(self.character_attack_index[1],2) == 2.00:
                combat_manager.attack_player_with_melee_attack(self)
            if int(self.character_attack_index[1]) == 3:
                self.interrupt_attack()
                self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
                self.rect = self.image.get_rect(midbottom = (self.sprite_position))

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

    #Walk speed vector setting
    def set_speed_vector(self):
        if self.monster_ai.monster_can_melee_attack_player():
            if self.monster_ai.avoiding_obstacle == True:
                self.monster_ai.finish_avoiding_obstacle()
            self.speed_vector = 0,0
        else:
            movement_manager.monster_vs_monster_collision(entity_manager.get_collision_sprite_by_id(self.id))
            if self.facing_direction == SECTOR_E:
                self.speed_vector = 1.4,0
            elif self.facing_direction == SECTOR_NE:
                self.speed_vector = 0.99,-0.58
            elif self.facing_direction == SECTOR_N:
                self.speed_vector = 0,-0.77
            elif self.facing_direction == SECTOR_NW:
                self.speed_vector = -0.99,-0.58
            elif self.facing_direction == SECTOR_W:
                self.speed_vector = -1.4,0
            elif self.facing_direction == SECTOR_SW:
                self.speed_vector = -0.99,0.58
            elif self.facing_direction == SECTOR_S:
                self.speed_vector = 0,0.77
            elif self.facing_direction == SECTOR_SE:
                self.speed_vector = 0.99,0.58
            
    #Combat functions
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            sound_player.ettin_death_sound.play()
            self.living = False
            self.dying = True
            self.speed_vector = 0,0
            entity_manager.kill_character_auxilary_entities(self.id)
            entity_manager.fix_all_dead_bodies_to_pixel_accuracy()
            entity_manager.fix_all_tiles_to_pixel_accuracy()
            entity_manager.fix_player_position_to_pixel_accuracy()
        else:
            self.in_pain = True
            if random.choice(range(4)) == 0:
                sound_player.ettin_pain_sound.play()

    def interrupt_attack(self):
        self.attack = False
        self.character_attack_index[1] = 0

    def attack_interupted(self):
        if random.choice(range(1,101)) <= self.attack_interruption_chance:
            return True
        self.attack_can_be_interrupted = False
        return False