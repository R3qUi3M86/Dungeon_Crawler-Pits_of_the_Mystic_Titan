import pygame
import random
from settings import *
from utilities import util
from utilities import movement_manager
from utilities import combat_manager
from utilities.constants import *
from sounds import sound_player
from images.characters.fighter_images import *

class Hero(pygame.sprite.Sprite):
    def __init__(self,position):
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

        #Overkill assets
        self.character_overkill = character_overkill
        self.character_overkill_index = 0

        #Pain assets
        self.character_pain_timer = 0

        #Position variables
        self.position = position
        self.sprite_display_correction = 8
        self.sprite_position = self.position[0], self.position[1] + self.sprite_display_correction
        
        #Object ID
        self.id = -1

        #Initial image definition
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

        #Character properties
        self.attack = False
        self.facing_direction = SECTOR_S
        self.living = True
        self.dying = False
        self.overkill = False
        self.in_pain = False
        self.maxhealth = 20
        self.health = 20

    #Update functions
    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.set_facing_direction()
        
        if self.living == False:
            movement_manager.speed_vector = 0,0
        else:
            self.player_input()

        if self.in_pain == True:
            self.character_pain_animation()
        
        elif self.dying == True and self.overkill == False:
            self.character_death_animation()

        elif self.overkill == True:
            self.character_overkill_animation()

    def update_position(self,vector):
        pass

    def set_facing_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        self.facing_direction = util.get_facing_direction(player_position,mouse_pos)
        self.set_character_animation_direction_indices()
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
    
    #Input functions
    def player_input(self):
        keys = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0] == False:
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
        
        if pygame.mouse.get_pressed()[0] or self.attack == True:
            self.attack = True
            self.character_attack_animation()
    
    #Animations
    def character_pain_animation(self):
        if self.attack or movement_manager.speed_vector[0] != 0 or movement_manager.speed_vector[1] != 0:
            self.in_pain = False
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
                self.in_pain = False
                self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
                self.character_pain_timer = 0

    def character_death_animation(self):
        self.character_death_index += 0.1
        if int(self.character_death_index) == 7:
            self.character_death_index = 6
            self.dying == False
        self.image = self.character_death[int(self.character_death_index)]

    def character_overkill_animation(self):
        self.character_overkill_index += 0.1
        if int(self.character_overkill_index) == 10:
            self.character_overkill_index = 9
            self.dying == False
            self.overkill == False
        self.image = self.character_overkill[int(self.character_overkill_index)]       

    def character_walk_forward_animation(self):
        if movement_manager.speed_vector[0] != 0 or movement_manager.speed_vector[1] != 0:
            self.character_walk_index[1] += 0.1
            if int(self.character_walk_index[1]) == 4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_walk_backward_animation(self):
        if movement_manager.speed_vector[0] != 0 or movement_manager.speed_vector[1] != 0:
            self.character_walk_index[1] -= 0.1
            if int(self.character_walk_index[1]) == -4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        if self.attack:
            movement_manager.speed_vector = 0,0
            movement_manager.acceleration_vector = 0,0
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]
            self.rect = self.image.get_rect(midbottom = (self.sprite_position))

            self.character_attack_index[1] += 0.05
            if round(self.character_attack_index[1],2) == 1.00:
                combat_manager.attack_monster_with_melee_attack()
            if int(self.character_attack_index[1]) == 2:
                self.attack = False
                self.character_attack_index[1] = 0
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

    #Combat functions
    def take_damage(self, damage):
        self.health -= damage
        print(self.health)

        if self.health > 0:
            self.in_pain = True
            sound_player.player_pain_sound.play()

        else:
            if self.living == True:
                sound_player.player_pain_sound.stop()
                sound_player.player_death_sound.play()
                self.living = False
                self.in_pain = False
                self.dying = True

            if self.overkill == False and -(self.maxhealth//2) >= self.health:
                sound_player.player_death_sound.stop()
                random.choice(sound_player.player_overkill_sounds).play()
                self.living = False
                self.in_pain = False
                self.dying = True
                self.overkill = True

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
