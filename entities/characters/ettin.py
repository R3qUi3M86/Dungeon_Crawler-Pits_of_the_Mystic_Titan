import pygame
import random
from settings import *
from entities import shadow
from entities import melee_range
from utilities import util
from utilities import combat_manager
from utilities import game_manager
from utilities import entity_manager
from utilities.constants import *
from utilities import monster_ai
from sounds import sound_player

class Ettin(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        character_walk_east1       = pygame.image.load("images/characters/hexen/ettin/east_01.png").convert_alpha()
        character_walk_east2       = pygame.image.load("images/characters/hexen/ettin/east_02.png").convert_alpha()
        character_walk_east3       = pygame.image.load("images/characters/hexen/ettin/east_03.png").convert_alpha()
        character_walk_east4       = pygame.image.load("images/characters/hexen/ettin/east_04.png").convert_alpha()
        character_walk_north_east1 = pygame.image.load("images/characters/hexen/ettin/north_east_01.png").convert_alpha()
        character_walk_north_east2 = pygame.image.load("images/characters/hexen/ettin/north_east_02.png").convert_alpha()
        character_walk_north_east3 = pygame.image.load("images/characters/hexen/ettin/north_east_03.png").convert_alpha()
        character_walk_north_east4 = pygame.image.load("images/characters/hexen/ettin/north_east_04.png").convert_alpha()
        character_walk_north1      = pygame.image.load("images/characters/hexen/ettin/north_01.png").convert_alpha()
        character_walk_north2      = pygame.image.load("images/characters/hexen/ettin/north_02.png").convert_alpha()
        character_walk_north3      = pygame.image.load("images/characters/hexen/ettin/north_03.png").convert_alpha()
        character_walk_north4      = pygame.image.load("images/characters/hexen/ettin/north_04.png").convert_alpha()
        character_walk_north_west1 = pygame.image.load("images/characters/hexen/ettin/north_west_01.png").convert_alpha()
        character_walk_north_west2 = pygame.image.load("images/characters/hexen/ettin/north_west_02.png").convert_alpha()
        character_walk_north_west3 = pygame.image.load("images/characters/hexen/ettin/north_west_03.png").convert_alpha()
        character_walk_north_west4 = pygame.image.load("images/characters/hexen/ettin/north_west_04.png").convert_alpha()
        character_walk_west1       = pygame.image.load("images/characters/hexen/ettin/west_01.png").convert_alpha()
        character_walk_west2       = pygame.image.load("images/characters/hexen/ettin/west_02.png").convert_alpha()
        character_walk_west3       = pygame.image.load("images/characters/hexen/ettin/west_03.png").convert_alpha()
        character_walk_west4       = pygame.image.load("images/characters/hexen/ettin/west_04.png").convert_alpha()
        character_walk_south_west1 = pygame.image.load("images/characters/hexen/ettin/south_west_01.png").convert_alpha()
        character_walk_south_west2 = pygame.image.load("images/characters/hexen/ettin/south_west_02.png").convert_alpha()
        character_walk_south_west3 = pygame.image.load("images/characters/hexen/ettin/south_west_03.png").convert_alpha()
        character_walk_south_west4 = pygame.image.load("images/characters/hexen/ettin/south_west_04.png").convert_alpha()
        character_walk_south1      = pygame.image.load("images/characters/hexen/ettin/south_01.png").convert_alpha()
        character_walk_south2      = pygame.image.load("images/characters/hexen/ettin/south_02.png").convert_alpha()
        character_walk_south3      = pygame.image.load("images/characters/hexen/ettin/south_03.png").convert_alpha()
        character_walk_south4      = pygame.image.load("images/characters/hexen/ettin/south_04.png").convert_alpha()
        character_walk_south_east1 = pygame.image.load("images/characters/hexen/ettin/south_east_01.png").convert_alpha()
        character_walk_south_east2 = pygame.image.load("images/characters/hexen/ettin/south_east_02.png").convert_alpha()
        character_walk_south_east3 = pygame.image.load("images/characters/hexen/ettin/south_east_03.png").convert_alpha()
        character_walk_south_east4 = pygame.image.load("images/characters/hexen/ettin/south_east_04.png").convert_alpha()
        self.character_walk =   [[character_walk_east1,character_walk_east2,character_walk_east3,character_walk_east4],
                                [character_walk_north_east1,character_walk_north_east2,character_walk_north_east3,character_walk_north_east4],
                                [character_walk_north1,character_walk_north2,character_walk_north3,character_walk_north4],
                                [character_walk_north_west1,character_walk_north_west2,character_walk_north_west3,character_walk_north_west4],
                                [character_walk_west1,character_walk_west2,character_walk_west3,character_walk_west4],
                                [character_walk_south_west1,character_walk_south_west2,character_walk_south_west3,character_walk_south_west4],
                                [character_walk_south1,character_walk_south2,character_walk_south3,character_walk_south4],
                                [character_walk_south_east1,character_walk_south_east2,character_walk_south_east3,character_walk_south_east4]]
        self.character_walk_index = [6,0]
        
        character_attack_east1       = pygame.image.load("images/characters/hexen/ettin/east_attack_01.png").convert_alpha()
        character_attack_east2       = pygame.image.load("images/characters/hexen/ettin/east_attack_02.png").convert_alpha()
        character_attack_east3       = pygame.image.load("images/characters/hexen/ettin/east_attack_03.png").convert_alpha()
        character_attack_north_east1 = pygame.image.load("images/characters/hexen/ettin/north_east_attack_01.png").convert_alpha()
        character_attack_north_east2 = pygame.image.load("images/characters/hexen/ettin/north_east_attack_02.png").convert_alpha()
        character_attack_north_east3 = pygame.image.load("images/characters/hexen/ettin/north_east_attack_03.png").convert_alpha()
        character_attack_north1      = pygame.image.load("images/characters/hexen/ettin/north_attack_01.png").convert_alpha()
        character_attack_north2      = pygame.image.load("images/characters/hexen/ettin/north_attack_02.png").convert_alpha()
        character_attack_north3      = pygame.image.load("images/characters/hexen/ettin/north_attack_03.png").convert_alpha()
        character_attack_north_west1 = pygame.image.load("images/characters/hexen/ettin/north_west_attack_01.png").convert_alpha()
        character_attack_north_west2 = pygame.image.load("images/characters/hexen/ettin/north_west_attack_02.png").convert_alpha()
        character_attack_north_west3 = pygame.image.load("images/characters/hexen/ettin/north_west_attack_03.png").convert_alpha()
        character_attack_west1       = pygame.image.load("images/characters/hexen/ettin/west_attack_01.png").convert_alpha()
        character_attack_west2       = pygame.image.load("images/characters/hexen/ettin/west_attack_02.png").convert_alpha()
        character_attack_west3       = pygame.image.load("images/characters/hexen/ettin/west_attack_03.png").convert_alpha()
        character_attack_south_west1 = pygame.image.load("images/characters/hexen/ettin/south_west_attack_01.png").convert_alpha()
        character_attack_south_west2 = pygame.image.load("images/characters/hexen/ettin/south_west_attack_02.png").convert_alpha()
        character_attack_south_west3 = pygame.image.load("images/characters/hexen/ettin/south_west_attack_03.png").convert_alpha()
        character_attack_south1      = pygame.image.load("images/characters/hexen/ettin/south_attack_01.png").convert_alpha()
        character_attack_south2      = pygame.image.load("images/characters/hexen/ettin/south_attack_02.png").convert_alpha()
        character_attack_south3      = pygame.image.load("images/characters/hexen/ettin/south_attack_03.png").convert_alpha()
        character_attack_south_east1 = pygame.image.load("images/characters/hexen/ettin/south_east_attack_01.png").convert_alpha()
        character_attack_south_east2 = pygame.image.load("images/characters/hexen/ettin/south_east_attack_02.png").convert_alpha()
        character_attack_south_east3 = pygame.image.load("images/characters/hexen/ettin/south_east_attack_03.png").convert_alpha()
        self.character_attack = [[character_attack_east1,character_attack_east2,character_attack_east3],
                                [character_attack_north_east1,character_attack_north_east2,character_attack_north_east3],
                                [character_attack_north1,character_attack_north2,character_attack_north3],
                                [character_attack_north_west1,character_attack_north_west2,character_attack_north_west3],
                                [character_attack_west1,character_attack_west2,character_attack_west3],
                                [character_attack_south_west1,character_attack_south_west2,character_attack_south_west3],
                                [character_attack_south1,character_attack_south2,character_attack_south3],
                                [character_attack_south_east1,character_attack_south_east2,character_attack_south_east3]]
        self.character_attack_index = [6,0]

        character_death1 = pygame.image.load("images/characters/hexen/ettin/death_01.png").convert_alpha()
        character_death2 = pygame.image.load("images/characters/hexen/ettin/death_02.png").convert_alpha()
        character_death3 = pygame.image.load("images/characters/hexen/ettin/death_03.png").convert_alpha()
        character_death4 = pygame.image.load("images/characters/hexen/ettin/death_04.png").convert_alpha()
        character_death5 = pygame.image.load("images/characters/hexen/ettin/death_05.png").convert_alpha()
        character_death6 = pygame.image.load("images/characters/hexen/ettin/death_06.png").convert_alpha()
        character_death7 = pygame.image.load("images/characters/hexen/ettin/death_07.png").convert_alpha()
        self.character_death = [character_death1,character_death2,character_death3,character_death4,character_death5,character_death6,character_death7]
        self.character_death_index = 0

        self.character_pain_east       = pygame.image.load("images/characters/hexen/ettin/east_pain.png").convert_alpha()
        self.character_pain_north_east = pygame.image.load("images/characters/hexen/ettin/north_east_pain.png").convert_alpha()
        self.character_pain_north      = pygame.image.load("images/characters/hexen/ettin/north_pain.png").convert_alpha()
        self.character_pain_north_west = pygame.image.load("images/characters/hexen/ettin/north_west_pain.png").convert_alpha()
        self.character_pain_west       = pygame.image.load("images/characters/hexen/ettin/west_pain.png").convert_alpha()
        self.character_pain_south_west = pygame.image.load("images/characters/hexen/ettin/south_west_pain.png").convert_alpha()
        self.character_pain_south      = pygame.image.load("images/characters/hexen/ettin/south_pain.png").convert_alpha()
        self.character_pain_south_east = pygame.image.load("images/characters/hexen/ettin/south_east_pain.png").convert_alpha()
        self.character_pain_timer = 0

        self.sprite_position = position

        self.atack = False
        self.facing_direction = SECTOR_S
        self.walk_speed_vector = 0,0
        self.monster_ai = monster_ai.Ai(self)

        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.id = util.generate_entity_id()
        self.name = ETTIN

        self.living = True
        self.dying = False
        self.in_pain = False
        self.health = 10

        self.monster_shadow          = shadow.Shadow(self.sprite_position, self.id, SIZE_MEDIUM)
        self.monster_melee_e_sector  = melee_range.Melee(self.sprite_position, SECTOR_E)
        self.monster_melee_ne_sector = melee_range.Melee(self.sprite_position, SECTOR_NE)
        self.monster_melee_n_sector  = melee_range.Melee(self.sprite_position, SECTOR_N)
        self.monster_melee_nw_sector = melee_range.Melee(self.sprite_position, SECTOR_NW)
        self.monster_melee_w_sector  = melee_range.Melee(self.sprite_position, SECTOR_W)
        self.monster_melee_sw_sector = melee_range.Melee(self.sprite_position, SECTOR_SW)
        self.monster_melee_s_sector  = melee_range.Melee(self.sprite_position, SECTOR_S)
        self.monster_melee_se_sector = melee_range.Melee(self.sprite_position, SECTOR_SE)
        self.monster_melee_sprites = [self.monster_melee_e_sector,self.monster_melee_ne_sector,self.monster_melee_n_sector,self.monster_melee_nw_sector,self.monster_melee_w_sector,self.monster_melee_sw_sector,self.monster_melee_s_sector,self.monster_melee_se_sector]
        self.monster_auxilary_sprites = [self.monster_shadow,self.monster_melee_e_sector,self.monster_melee_ne_sector,self.monster_melee_n_sector,self.monster_melee_nw_sector,self.monster_melee_w_sector,self.monster_melee_sw_sector,self.monster_melee_s_sector,self.monster_melee_se_sector]

    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        if self.living == True:
            self.set_facing_direction()
            if self.in_pain == False and self.dying == False:
                self.set_walk_speed_vector()
                if self.walk_speed_vector[0] != 0 or self.walk_speed_vector[1] != 0:
                    self.character_walk_forward_animation()
            if self.in_pain == True:
                self.character_pain_animation()
        elif self.dying == True:
            self.walk_speed_vector = 0,0
            self.character_death_animation()

    def update_position(self, vector):
        if self.living == True:
            if self.monster_ai.monster_can_melee_attack_player() == False:
                self.monster_ai.increment_direction_change_decision_timer()
            else:
                self.facing_direction = self.monster_ai.player_direction_sector
        self.sprite_position = self.sprite_position[0]-vector[0]+self.walk_speed_vector[0],self.sprite_position[1] - vector[1] +self.walk_speed_vector[1]
        for auxilary_sprite in self.monster_auxilary_sprites:
            auxilary_sprite.sprite_position = self.sprite_position
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            sound_player.ettin_death_sound.play()
            self.living = False
            self.dying = True
            entity_manager.kill_monster(self.id)
        else:
            self.in_pain = True
            if random.choice(range(4)) == 0:
                sound_player.ettin_pain_sound.play()
    
    def character_pain_animation(self):
        self.character_pain_timer += 0.025
        if self.facing_direction == SECTOR_E:
            self.image = self.character_pain_east
        elif self.facing_direction == SECTOR_NE:
            self.image = self.character_pain_north_east
        elif self.facing_direction == SECTOR_N:
            self.image = self.character_pain_north
        elif self.facing_direction == SECTOR_NW:
            self.image = self.character_pain_north_west
        elif self.facing_direction == SECTOR_W:
            self.image = self.character_pain_west
        elif self.facing_direction == SECTOR_SW:
            self.image = self.character_pain_south_west
        elif self.facing_direction == SECTOR_S:
            self.image = self.character_pain_south
        elif self.facing_direction == SECTOR_SE:
            self.image = self.character_pain_south_east
        if int(self.character_pain_timer) >= 1:
            self.in_pain = False
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
            self.character_pain_timer = 0

    def character_death_animation(self):
        self.in_pain == False
        self.character_death_index += 0.1
        if int(self.character_death_index) == 7:
            self.character_death_index = 6
            self.dying == False
        self.image = self.character_death[int(self.character_death_index)]

    def set_facing_direction(self):
        self.set_character_animation_direction_indices()
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

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

    def set_walk_speed_vector(self):
        if self.monster_ai.monster_can_melee_attack_player():
            self.walk_speed_vector = 0,0
        else:
            if self.facing_direction == SECTOR_E:
                self.walk_speed_vector = 1.4,0
            elif self.facing_direction == SECTOR_NE:
                self.walk_speed_vector = 1,-1
            elif self.facing_direction == SECTOR_N:
                self.walk_speed_vector = 0,-1.4
            elif self.facing_direction == SECTOR_NW:
                self.walk_speed_vector = -1,-1
            elif self.facing_direction == SECTOR_W:
                self.walk_speed_vector = -1.4,0
            elif self.facing_direction == SECTOR_SW:
                self.walk_speed_vector = -1,1
            elif self.facing_direction == SECTOR_S:
                self.walk_speed_vector = 0,1.4
            elif self.facing_direction == SECTOR_SE:
                self.walk_speed_vector = 1,1

    def character_walk_forward_animation(self):
        self.character_walk_index[1] += 0.1
        if int(self.character_walk_index[1]) == 4:
            self.character_walk_index[1] = 0
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        if self.atack:
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]
            self.rect = self.image.get_rect(midbottom = (self.monster_sprite_position))

            self.character_attack_index[1] += 0.05
            if round(self.character_attack_index[1],2) == 2.00:
                combat_manager.attack_player_with_melee_attack()
            if int(self.character_attack_index[1]) == 3:
                self.atack = False
                self.character_attack_index[1] = 0
                self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
                self.rect = self.image.get_rect(midbottom = (self.monster_sprite_position))







