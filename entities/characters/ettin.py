import pygame
from settings import *
from utilities import util
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
        
        self.sprite_position = position
        self.monster_melee_e_sector_position = self.sprite_position[0]+30,self.sprite_position[1]
        self.monster_melee_ne_sector_position = self.sprite_position[0]+20,self.sprite_position[1]-13
        self.monster_melee_n_sector_position = self.sprite_position[0],self.sprite_position[1]-20
        self.monster_melee_nw_sector_position = self.sprite_position[0]-20,self.sprite_position[1]-13
        self.monster_melee_w_sector_position = self.sprite_position[0]-30,self.sprite_position[1]
        self.monster_melee_sw_sector_position = self.sprite_position[0]-20,self.sprite_position[1]+13
        self.monster_melee_s_sector_position = self.sprite_position[0],self.sprite_position[1]+20
        self.monster_melee_se_sector_position = self.sprite_position[0]+20,self.sprite_position[1]+13

        self.atack = False
        self.facing_direction = SECTOR_S
        self.monster_ai = monster_ai.Ai(self.sprite_position)

        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.id = util.generate_entity_id()

    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.set_facing_direction()
        self.player_input()

    def update_position(self, vector):
        self.sprite_position = self.sprite_position[0]-vector[0],self.sprite_position[1] - vector[1]

    def player_input(self):
        # keys = pygame.key.get_pressed()
        
        # if pygame.mouse.get_pressed()[0] or self.atack == True:
        #     self.atack = True
        #     self.character_attack_animation()
        pass

    def set_facing_direction(self):
        self.facing_direction = util.get_facing_direction(self.sprite_position,PLAYER_POSITION)
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
                sound_player.monster_melee_miss_sound.play()
            if int(self.character_attack_index[1]) == 3:
                self.atack = False
                self.character_attack_index[1] = 0
                self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
                self.rect = self.image.get_rect(midbottom = (self.monster_sprite_position))







