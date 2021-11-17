import pygame
from copy import deepcopy
from settings import *
from entities import melee_range
from entities import shadow
from utilities import util
from utilities import game_manager
from utilities import combat_manager
from utilities.constants import *
from sounds import sound_player

class Hero(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        character_walk_east1       = pygame.image.load("images/characters/hexen/fighter/east_01.png").convert_alpha()
        character_walk_east2       = pygame.image.load("images/characters/hexen/fighter/east_02.png").convert_alpha()
        character_walk_east3       = pygame.image.load("images/characters/hexen/fighter/east_03.png").convert_alpha()
        character_walk_east4       = pygame.image.load("images/characters/hexen/fighter/east_04.png").convert_alpha()
        character_walk_north_east1 = pygame.image.load("images/characters/hexen/fighter/north_east_01.png").convert_alpha()
        character_walk_north_east2 = pygame.image.load("images/characters/hexen/fighter/north_east_02.png").convert_alpha()
        character_walk_north_east3 = pygame.image.load("images/characters/hexen/fighter/north_east_03.png").convert_alpha()
        character_walk_north_east4 = pygame.image.load("images/characters/hexen/fighter/north_east_04.png").convert_alpha()
        character_walk_north1      = pygame.image.load("images/characters/hexen/fighter/north_01.png").convert_alpha()
        character_walk_north2      = pygame.image.load("images/characters/hexen/fighter/north_02.png").convert_alpha()
        character_walk_north3      = pygame.image.load("images/characters/hexen/fighter/north_03.png").convert_alpha()
        character_walk_north4      = pygame.image.load("images/characters/hexen/fighter/north_04.png").convert_alpha()
        character_walk_north_west1 = pygame.image.load("images/characters/hexen/fighter/north_west_01.png").convert_alpha()
        character_walk_north_west2 = pygame.image.load("images/characters/hexen/fighter/north_west_02.png").convert_alpha()
        character_walk_north_west3 = pygame.image.load("images/characters/hexen/fighter/north_west_03.png").convert_alpha()
        character_walk_north_west4 = pygame.image.load("images/characters/hexen/fighter/north_west_04.png").convert_alpha()
        character_walk_west1       = pygame.image.load("images/characters/hexen/fighter/west_01.png").convert_alpha()
        character_walk_west2       = pygame.image.load("images/characters/hexen/fighter/west_02.png").convert_alpha()
        character_walk_west3       = pygame.image.load("images/characters/hexen/fighter/west_03.png").convert_alpha()
        character_walk_west4       = pygame.image.load("images/characters/hexen/fighter/west_04.png").convert_alpha()
        character_walk_south_west1 = pygame.image.load("images/characters/hexen/fighter/south_west_01.png").convert_alpha()
        character_walk_south_west2 = pygame.image.load("images/characters/hexen/fighter/south_west_02.png").convert_alpha()
        character_walk_south_west3 = pygame.image.load("images/characters/hexen/fighter/south_west_03.png").convert_alpha()
        character_walk_south_west4 = pygame.image.load("images/characters/hexen/fighter/south_west_04.png").convert_alpha()
        character_walk_south1      = pygame.image.load("images/characters/hexen/fighter/south_01.png").convert_alpha()
        character_walk_south2      = pygame.image.load("images/characters/hexen/fighter/south_02.png").convert_alpha()
        character_walk_south3      = pygame.image.load("images/characters/hexen/fighter/south_03.png").convert_alpha()
        character_walk_south4      = pygame.image.load("images/characters/hexen/fighter/south_04.png").convert_alpha()
        character_walk_south_east1 = pygame.image.load("images/characters/hexen/fighter/south_east_01.png").convert_alpha()
        character_walk_south_east2 = pygame.image.load("images/characters/hexen/fighter/south_east_02.png").convert_alpha()
        character_walk_south_east3 = pygame.image.load("images/characters/hexen/fighter/south_east_03.png").convert_alpha()
        character_walk_south_east4 = pygame.image.load("images/characters/hexen/fighter/south_east_04.png").convert_alpha()
        self.character_walk =   [[character_walk_east1,character_walk_east2,character_walk_east3,character_walk_east4],
                                [character_walk_north_east1,character_walk_north_east2,character_walk_north_east3,character_walk_north_east4],
                                [character_walk_north1,character_walk_north2,character_walk_north3,character_walk_north4],
                                [character_walk_north_west1,character_walk_north_west2,character_walk_north_west3,character_walk_north_west4],
                                [character_walk_west1,character_walk_west2,character_walk_west3,character_walk_west4],
                                [character_walk_south_west1,character_walk_south_west2,character_walk_south_west3,character_walk_south_west4],
                                [character_walk_south1,character_walk_south2,character_walk_south3,character_walk_south4],
                                [character_walk_south_east1,character_walk_south_east2,character_walk_south_east3,character_walk_south_east4]]
        self.character_walk_index = [6,0]
        
        character_attack_east1       = pygame.image.load("images/characters/hexen/fighter/east_attack_01.png").convert_alpha()
        character_attack_east2       = pygame.image.load("images/characters/hexen/fighter/east_attack_02.png").convert_alpha()
        character_attack_north_east1 = pygame.image.load("images/characters/hexen/fighter/north_east_attack_01.png").convert_alpha()
        character_attack_north_east2 = pygame.image.load("images/characters/hexen/fighter/north_east_attack_02.png").convert_alpha()
        character_attack_north1      = pygame.image.load("images/characters/hexen/fighter/north_attack_01.png").convert_alpha()
        character_attack_north2      = pygame.image.load("images/characters/hexen/fighter/north_attack_02.png").convert_alpha()
        character_attack_north_west1 = pygame.image.load("images/characters/hexen/fighter/north_west_attack_01.png").convert_alpha()
        character_attack_north_west2 = pygame.image.load("images/characters/hexen/fighter/north_west_attack_02.png").convert_alpha()
        character_attack_west1       = pygame.image.load("images/characters/hexen/fighter/west_attack_01.png").convert_alpha()
        character_attack_west2       = pygame.image.load("images/characters/hexen/fighter/west_attack_02.png").convert_alpha()
        character_attack_south_west1 = pygame.image.load("images/characters/hexen/fighter/south_west_attack_01.png").convert_alpha()
        character_attack_south_west2 = pygame.image.load("images/characters/hexen/fighter/south_west_attack_02.png").convert_alpha()
        character_attack_south1      = pygame.image.load("images/characters/hexen/fighter/south_attack_01.png").convert_alpha()
        character_attack_south2      = pygame.image.load("images/characters/hexen/fighter/south_attack_02.png").convert_alpha()
        character_attack_south_east1 = pygame.image.load("images/characters/hexen/fighter/south_east_attack_01.png").convert_alpha()
        character_attack_south_east2 = pygame.image.load("images/characters/hexen/fighter/south_east_attack_02.png").convert_alpha()
        self.character_attack = [[character_attack_east1,character_attack_east2],
                                [character_attack_north_east1,character_attack_north_east2],
                                [character_attack_north1,character_attack_north2],
                                [character_attack_north_west1,character_attack_north_west2],
                                [character_attack_west1,character_attack_west2],
                                [character_attack_south_west1,character_attack_south_west2],
                                [character_attack_south1,character_attack_south2],
                                [character_attack_south_east1,character_attack_south_east2]]
        self.character_attack_index = [6,0]
        
        self.atack = False
        self.facing_direction = SECTOR_S
        self.speed_vector = 0,0

        self.sprite_position = position

        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

    def update(self):
        self.set_facing_direction()
        self.player_input()

    def update_position(self, vector):
        pass

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

    def set_facing_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        self.facing_direction = util.get_facing_direction((PLAYER_POSITION[0],PLAYER_POSITION[1]-10),mouse_pos)
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

PLAYER_MELEE_SPRITE_E  = melee_range.Melee(PLAYER_POSITION, SECTOR_E)
PLAYER_MELEE_SPRITE_NE = melee_range.Melee(PLAYER_POSITION, SECTOR_NE)
PLAYER_MELEE_SPRITE_N  = melee_range.Melee(PLAYER_POSITION, SECTOR_N)
PLAYER_MELEE_SPRITE_NW = melee_range.Melee(PLAYER_POSITION, SECTOR_NW)
PLAYER_MELEE_SPRITE_W  = melee_range.Melee(PLAYER_POSITION, SECTOR_W)
PLAYER_MELEE_SPRITE_SW = melee_range.Melee(PLAYER_POSITION, SECTOR_SW)
PLAYER_MELEE_SPRITE_S  = melee_range.Melee(PLAYER_POSITION, SECTOR_S)
PLAYER_MELEE_SPRITE_SE = melee_range.Melee(PLAYER_POSITION, SECTOR_SE)
PLAYER_SHADOW_SPRITE   = shadow.Shadow(PLAYER_POSITION, PLAYER_SHADOW_ID, SIZE_SMALL, True)

PLAYER_MELEE_SPRITES = [PLAYER_MELEE_SPRITE_E,PLAYER_MELEE_SPRITE_NE,PLAYER_MELEE_SPRITE_N,PLAYER_MELEE_SPRITE_NW,PLAYER_MELEE_SPRITE_W,PLAYER_MELEE_SPRITE_SW,PLAYER_MELEE_SPRITE_S,PLAYER_MELEE_SPRITE_SE]

hero = Hero(PLAYER_POSITION)
character = pygame.sprite.Group()
character.add(PLAYER_MELEE_SPRITE_E)
character.add(PLAYER_MELEE_SPRITE_NE)
character.add(PLAYER_MELEE_SPRITE_N)
character.add(PLAYER_MELEE_SPRITE_NW)
character.add(PLAYER_MELEE_SPRITE_W)
character.add(PLAYER_MELEE_SPRITE_SW)
character.add(PLAYER_MELEE_SPRITE_S)
character.add(PLAYER_MELEE_SPRITE_SE)
character.add(PLAYER_SHADOW_SPRITE)
character.add(hero)







