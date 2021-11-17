import pygame
from settings import *
from utilities import util
from utilities import game_manager
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

        #Pain assets
        self.character_pain_timer = 0

        self.sprite_position = position

        #Initial image definition
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

        self.atack = False
        self.facing_direction = SECTOR_S
        self.speed_vector = 0,0
        self.living = True
        self.dying = False
        self.in_pain = False
        self.health = 20

    #Update functions
    def update(self):
        self.set_facing_direction()
        self.player_input()

    def set_facing_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        self.facing_direction = util.get_facing_direction((PLAYER_POSITION[0],PLAYER_POSITION[1]-10),mouse_pos)
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
        
        if pygame.mouse.get_pressed()[0] or self.atack == True:
            self.atack = True
            self.character_attack_animation()
    
    #Animations
    def character_pain_animation(self):
        pass

    def character_death_animation(self):
        pass

    def character_walk_forward_animation(self):
        if game_manager.speed_vector[0] != 0 or game_manager.speed_vector[1] != 0:
            self.character_walk_index[1] += 0.1
            if int(self.character_walk_index[1]) == 4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_walk_backward_animation(self):
        if game_manager.speed_vector[0] != 0 or game_manager.speed_vector[1] != 0:
            self.character_walk_index[1] -= 0.1
            if int(self.character_walk_index[1]) == -4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        if self.atack:
            game_manager.speed_vector = 0,0
            game_manager.acceleration_vector = 0,0
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]
            self.rect = self.image.get_rect(midbottom = (self.sprite_position))

            self.character_attack_index[1] += 0.05
            if round(self.character_attack_index[1],2) == 1.00:
                combat_manager.attack_monster_with_melee_attack()
            if int(self.character_attack_index[1]) == 2:
                self.atack = False
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
        if self.health <= 0:
            sound_player.player_death_sound.play()
            self.living = False
            self.dying = True
        else:
            self.in_pain = True
            sound_player.playe.play()

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
