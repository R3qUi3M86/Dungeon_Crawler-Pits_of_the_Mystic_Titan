import pygame
from copy import deepcopy
from settings import *
from utilities import util
from utilities import constants
from entities import shadow
from entities import melee_range
from sounds import sound_player

class Hero(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        hero_walk_east1       = pygame.image.load("images/characters/hexen/fighter/east_01.png").convert_alpha()
        hero_walk_east2       = pygame.image.load("images/characters/hexen/fighter/east_02.png").convert_alpha()
        hero_walk_east3       = pygame.image.load("images/characters/hexen/fighter/east_03.png").convert_alpha()
        hero_walk_east4       = pygame.image.load("images/characters/hexen/fighter/east_04.png").convert_alpha()
        hero_walk_north_east1 = pygame.image.load("images/characters/hexen/fighter/north_east_01.png").convert_alpha()
        hero_walk_north_east2 = pygame.image.load("images/characters/hexen/fighter/north_east_02.png").convert_alpha()
        hero_walk_north_east3 = pygame.image.load("images/characters/hexen/fighter/north_east_03.png").convert_alpha()
        hero_walk_north_east4 = pygame.image.load("images/characters/hexen/fighter/north_east_04.png").convert_alpha()
        hero_walk_north1      = pygame.image.load("images/characters/hexen/fighter/north_01.png").convert_alpha()
        hero_walk_north2      = pygame.image.load("images/characters/hexen/fighter/north_02.png").convert_alpha()
        hero_walk_north3      = pygame.image.load("images/characters/hexen/fighter/north_03.png").convert_alpha()
        hero_walk_north4      = pygame.image.load("images/characters/hexen/fighter/north_04.png").convert_alpha()
        hero_walk_north_west1 = pygame.image.load("images/characters/hexen/fighter/north_west_01.png").convert_alpha()
        hero_walk_north_west2 = pygame.image.load("images/characters/hexen/fighter/north_west_02.png").convert_alpha()
        hero_walk_north_west3 = pygame.image.load("images/characters/hexen/fighter/north_west_03.png").convert_alpha()
        hero_walk_north_west4 = pygame.image.load("images/characters/hexen/fighter/north_west_04.png").convert_alpha()
        hero_walk_west1       = pygame.image.load("images/characters/hexen/fighter/west_01.png").convert_alpha()
        hero_walk_west2       = pygame.image.load("images/characters/hexen/fighter/west_02.png").convert_alpha()
        hero_walk_west3       = pygame.image.load("images/characters/hexen/fighter/west_03.png").convert_alpha()
        hero_walk_west4       = pygame.image.load("images/characters/hexen/fighter/west_04.png").convert_alpha()
        hero_walk_south_west1 = pygame.image.load("images/characters/hexen/fighter/south_west_01.png").convert_alpha()
        hero_walk_south_west2 = pygame.image.load("images/characters/hexen/fighter/south_west_02.png").convert_alpha()
        hero_walk_south_west3 = pygame.image.load("images/characters/hexen/fighter/south_west_03.png").convert_alpha()
        hero_walk_south_west4 = pygame.image.load("images/characters/hexen/fighter/south_west_04.png").convert_alpha()
        hero_walk_south1      = pygame.image.load("images/characters/hexen/fighter/south_01.png").convert_alpha()
        hero_walk_south2      = pygame.image.load("images/characters/hexen/fighter/south_02.png").convert_alpha()
        hero_walk_south3      = pygame.image.load("images/characters/hexen/fighter/south_03.png").convert_alpha()
        hero_walk_south4      = pygame.image.load("images/characters/hexen/fighter/south_04.png").convert_alpha()
        hero_walk_south_east1 = pygame.image.load("images/characters/hexen/fighter/south_east_01.png").convert_alpha()
        hero_walk_south_east2 = pygame.image.load("images/characters/hexen/fighter/south_east_02.png").convert_alpha()
        hero_walk_south_east3 = pygame.image.load("images/characters/hexen/fighter/south_east_03.png").convert_alpha()
        hero_walk_south_east4 = pygame.image.load("images/characters/hexen/fighter/south_east_04.png").convert_alpha()
        self.hero_walk =   [[hero_walk_east1,hero_walk_east2,hero_walk_east3,hero_walk_east4],
                            [hero_walk_north_east1,hero_walk_north_east2,hero_walk_north_east3,hero_walk_north_east4],
                            [hero_walk_north1,hero_walk_north2,hero_walk_north3,hero_walk_north4],
                            [hero_walk_north_west1,hero_walk_north_west2,hero_walk_north_west3,hero_walk_north_west4],
                            [hero_walk_west1,hero_walk_west2,hero_walk_west3,hero_walk_west4],
                            [hero_walk_south_west1,hero_walk_south_west2,hero_walk_south_west3,hero_walk_south_west4],
                            [hero_walk_south1,hero_walk_south2,hero_walk_south3,hero_walk_south4],
                            [hero_walk_south_east1,hero_walk_south_east2,hero_walk_south_east3,hero_walk_south_east4]]
        self.hero_walk_index = [6,0]
        
        hero_attack_east1       = pygame.image.load("images/characters/hexen/fighter/east_attack_01.png").convert_alpha()
        hero_attack_east2       = pygame.image.load("images/characters/hexen/fighter/east_attack_02.png").convert_alpha()
        hero_attack_north_east1 = pygame.image.load("images/characters/hexen/fighter/north_east_attack_01.png").convert_alpha()
        hero_attack_north_east2 = pygame.image.load("images/characters/hexen/fighter/north_east_attack_02.png").convert_alpha()
        hero_attack_north1      = pygame.image.load("images/characters/hexen/fighter/north_attack_01.png").convert_alpha()
        hero_attack_north2      = pygame.image.load("images/characters/hexen/fighter/north_attack_02.png").convert_alpha()
        hero_attack_north_west1 = pygame.image.load("images/characters/hexen/fighter/north_west_attack_01.png").convert_alpha()
        hero_attack_north_west2 = pygame.image.load("images/characters/hexen/fighter/north_west_attack_02.png").convert_alpha()
        hero_attack_west1       = pygame.image.load("images/characters/hexen/fighter/west_attack_01.png").convert_alpha()
        hero_attack_west2       = pygame.image.load("images/characters/hexen/fighter/west_attack_02.png").convert_alpha()
        hero_attack_south_west1 = pygame.image.load("images/characters/hexen/fighter/south_west_attack_01.png").convert_alpha()
        hero_attack_south_west2 = pygame.image.load("images/characters/hexen/fighter/south_west_attack_02.png").convert_alpha()
        hero_attack_south1      = pygame.image.load("images/characters/hexen/fighter/south_attack_01.png").convert_alpha()
        hero_attack_south2      = pygame.image.load("images/characters/hexen/fighter/south_attack_02.png").convert_alpha()
        hero_attack_south_east1 = pygame.image.load("images/characters/hexen/fighter/south_east_attack_01.png").convert_alpha()
        hero_attack_south_east2 = pygame.image.load("images/characters/hexen/fighter/south_east_attack_02.png").convert_alpha()
        self.hero_attack = [[hero_attack_east1,hero_attack_east2],
                            [hero_attack_north_east1,hero_attack_north_east2],
                            [hero_attack_north1,hero_attack_north2],
                            [hero_attack_north_west1,hero_attack_north_west2],
                            [hero_attack_west1,hero_attack_west2],
                            [hero_attack_south_west1,hero_attack_south_west2],
                            [hero_attack_south1,hero_attack_south2],
                            [hero_attack_south_east1,hero_attack_south_east2]]
        self.hero_attack_index = [6,0]
        
        self.atack = False
        self.facing_direction = constants.SECTOR_S

        self.image = self.hero_walk[self.hero_walk_index[0]][self.hero_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (position))

    def hero_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_s] and self.facing_southwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_forward_animation()
        elif keys[pygame.K_w] and self.facing_northwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_forward_animation()
        elif keys[pygame.K_a] and self.facing_westwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_forward_animation()
        elif keys[pygame.K_d] and self.facing_eastwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_forward_animation()
        elif keys[pygame.K_s] and self.facing_northwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_backward_animation()
        elif keys[pygame.K_w] and self.facing_southwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_backward_animation()
        elif keys[pygame.K_a] and self.facing_eastwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_backward_animation()
        elif keys[pygame.K_d] and self.facing_westwards() and pygame.mouse.get_pressed()[0] == False:
            self.hero_walk_backward_animation()
        
        if pygame.mouse.get_pressed()[0] or self.atack == True:
            self.atack = True
            self.hero_attack_animation()

    def facing_southwards(self):
        if self.facing_direction == constants.SECTOR_S or self.facing_direction == constants.SECTOR_SE or self.facing_direction == constants.SECTOR_SW or self.facing_direction == constants.SECTOR_E or self.facing_direction == constants.SECTOR_W:
            return True
        return False
    
    def facing_eastwards(self):
        if self.facing_direction == constants.SECTOR_E or self.facing_direction == constants.SECTOR_SE or self.facing_direction == constants.SECTOR_NE or self.facing_direction == constants.SECTOR_N or self.facing_direction == constants.SECTOR_S:
            return True
        return False
    
    def facing_northwards(self):
        if self.facing_direction == constants.SECTOR_N or self.facing_direction == constants.SECTOR_NE or self.facing_direction == constants.SECTOR_NW or self.facing_direction == constants.SECTOR_E or self.facing_direction == constants.SECTOR_W:
            return True
        return False

    def facing_westwards(self):
        if self.facing_direction == constants.SECTOR_W or self.facing_direction == constants.SECTOR_SW or self.facing_direction == constants.SECTOR_NW or self.facing_direction == constants.SECTOR_N or self.facing_direction == constants.SECTOR_S:
            return True
        return False

    def update(self):
        self.set_facing_direction()
        self.hero_input()

    def set_facing_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        self.facing_direction = util.get_facing_direction(constants.PLAYER_POSITION,mouse_pos)
        self.set_hero_animation_direction_indices()
        self.image = self.hero_walk[self.hero_walk_index[0]][int(self.hero_walk_index[1])]

    def set_hero_animation_direction_indices(self):
        if self.facing_direction == constants.SECTOR_E:
            self.hero_walk_index[0] = 0
            self.hero_attack_index[0] = 0
        elif self.facing_direction == constants.SECTOR_NE:
            self.hero_walk_index[0] = 1
            self.hero_attack_index[0] = 1
        elif self.facing_direction == constants.SECTOR_N:
            self.hero_walk_index[0] = 2
            self.hero_attack_index[0] = 2
        elif self.facing_direction == constants.SECTOR_NW:
            self.hero_walk_index[0] = 3
            self.hero_attack_index[0] = 3
        elif self.facing_direction == constants.SECTOR_W:
            self.hero_walk_index[0] = 4
            self.hero_attack_index[0] = 4
        elif self.facing_direction == constants.SECTOR_SW:
            self.hero_walk_index[0] = 5
            self.hero_attack_index[0] = 5
        elif self.facing_direction == constants.SECTOR_S:
            self.hero_walk_index[0] = 6
            self.hero_attack_index[0] = 6
        elif self.facing_direction == constants.SECTOR_SE:
            self.hero_walk_index[0] = 7
            self.hero_attack_index[0] = 7            

    def hero_walk_forward_animation(self):
        self.hero_walk_index[1] += 0.1
        if int(self.hero_walk_index[1]) == 4:
            self.hero_walk_index[1] = 0
        self.image = self.hero_walk[self.hero_walk_index[0]][int(self.hero_walk_index[1])]
    
    def hero_walk_backward_animation(self):
        self.hero_walk_index[1] -= 0.1
        if int(self.hero_walk_index[1]) == -4:
            self.hero_walk_index[1] = 0
        self.image = self.hero_walk[self.hero_walk_index[0]][int(self.hero_walk_index[1])]

    def hero_attack_animation(self):
        if self.atack:
            self.image = self.hero_attack[self.hero_attack_index[0]][int(self.hero_attack_index[1])]
            self.rect = self.image.get_rect(midbottom = (constants.PLAYER_SPRITE_POSITION))

            self.hero_attack_index[1] += 0.05
            if round(self.hero_attack_index[1],2) == 1.00:
                sound_player.punch_sound.play()
            if int(self.hero_attack_index[1]) == 2:
                self.atack = False
                self.hero_attack_index[1] = 0
                self.image = self.hero_walk[self.hero_walk_index[0]][int(self.hero_walk_index[1])]
                self.rect = self.image.get_rect(midbottom = (constants.PLAYER_SPRITE_POSITION))
    
screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

hero = pygame.sprite.Group()
hero.add(melee_range.Melee(constants.PLAYER_MELEE_E_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_NE_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_N_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_NW_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_W_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_SW_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_S_SECTOR_POSITION))
hero.add(melee_range.Melee(constants.PLAYER_MELEE_SE_SECTOR_POSITION))
hero.add(shadow.Shadow(constants.PLAYER_POSITION))
hero.add(Hero(constants.PLAYER_SPRITE_POSITION))


#SECTOR_LIST = [SECTOR_E,SECTOR_NE,SECTOR_N,SECTOR_NW,SECTOR_W,SECTOR_SW,SECTOR_S,SECTOR_SE]







