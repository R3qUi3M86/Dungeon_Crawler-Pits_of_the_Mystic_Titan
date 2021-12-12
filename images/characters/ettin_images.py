import pygame
from utilities.constants import *
    
ettin_walk_east1       = pygame.image.load("images/characters/ettin/east_01.png").convert()
ettin_walk_east2       = pygame.image.load("images/characters/ettin/east_02.png").convert()
ettin_walk_east3       = pygame.image.load("images/characters/ettin/east_03.png").convert()
ettin_walk_east4       = pygame.image.load("images/characters/ettin/east_04.png").convert()
ettin_walk_north_east1 = pygame.image.load("images/characters/ettin/north_east_01.png").convert()
ettin_walk_north_east2 = pygame.image.load("images/characters/ettin/north_east_02.png").convert()
ettin_walk_north_east3 = pygame.image.load("images/characters/ettin/north_east_03.png").convert()
ettin_walk_north_east4 = pygame.image.load("images/characters/ettin/north_east_04.png").convert()
ettin_walk_north1      = pygame.image.load("images/characters/ettin/north_01.png").convert()
ettin_walk_north2      = pygame.image.load("images/characters/ettin/north_02.png").convert()
ettin_walk_north3      = pygame.image.load("images/characters/ettin/north_03.png").convert()
ettin_walk_north4      = pygame.image.load("images/characters/ettin/north_04.png").convert()
ettin_walk_north_west1 = pygame.image.load("images/characters/ettin/north_west_01.png").convert()
ettin_walk_north_west2 = pygame.image.load("images/characters/ettin/north_west_02.png").convert()
ettin_walk_north_west3 = pygame.image.load("images/characters/ettin/north_west_03.png").convert()
ettin_walk_north_west4 = pygame.image.load("images/characters/ettin/north_west_04.png").convert()
ettin_walk_west1       = pygame.image.load("images/characters/ettin/west_01.png").convert()
ettin_walk_west2       = pygame.image.load("images/characters/ettin/west_02.png").convert()
ettin_walk_west3       = pygame.image.load("images/characters/ettin/west_03.png").convert()
ettin_walk_west4       = pygame.image.load("images/characters/ettin/west_04.png").convert()
ettin_walk_south_west1 = pygame.image.load("images/characters/ettin/south_west_01.png").convert()
ettin_walk_south_west2 = pygame.image.load("images/characters/ettin/south_west_02.png").convert()
ettin_walk_south_west3 = pygame.image.load("images/characters/ettin/south_west_03.png").convert()
ettin_walk_south_west4 = pygame.image.load("images/characters/ettin/south_west_04.png").convert()
ettin_walk_south1      = pygame.image.load("images/characters/ettin/south_01.png").convert()
ettin_walk_south2      = pygame.image.load("images/characters/ettin/south_02.png").convert()
ettin_walk_south3      = pygame.image.load("images/characters/ettin/south_03.png").convert()
ettin_walk_south4      = pygame.image.load("images/characters/ettin/south_04.png").convert()
ettin_walk_south_east1 = pygame.image.load("images/characters/ettin/south_east_01.png").convert()
ettin_walk_south_east2 = pygame.image.load("images/characters/ettin/south_east_02.png").convert()
ettin_walk_south_east3 = pygame.image.load("images/characters/ettin/south_east_03.png").convert()
ettin_walk_south_east4 = pygame.image.load("images/characters/ettin/south_east_04.png").convert()

ettin_attack_east1       = pygame.image.load("images/characters/ettin/east_attack_01.png").convert()
ettin_attack_east2       = pygame.image.load("images/characters/ettin/east_attack_02.png").convert()
ettin_attack_east3       = pygame.image.load("images/characters/ettin/east_attack_03.png").convert()
ettin_attack_north_east1 = pygame.image.load("images/characters/ettin/north_east_attack_01.png").convert()
ettin_attack_north_east2 = pygame.image.load("images/characters/ettin/north_east_attack_02.png").convert()
ettin_attack_north_east3 = pygame.image.load("images/characters/ettin/north_east_attack_03.png").convert()
ettin_attack_north1      = pygame.image.load("images/characters/ettin/north_attack_01.png").convert()
ettin_attack_north2      = pygame.image.load("images/characters/ettin/north_attack_02.png").convert()
ettin_attack_north3      = pygame.image.load("images/characters/ettin/north_attack_03.png").convert()
ettin_attack_north_west1 = pygame.image.load("images/characters/ettin/north_west_attack_01.png").convert()
ettin_attack_north_west2 = pygame.image.load("images/characters/ettin/north_west_attack_02.png").convert()
ettin_attack_north_west3 = pygame.image.load("images/characters/ettin/north_west_attack_03.png").convert()
ettin_attack_west1       = pygame.image.load("images/characters/ettin/west_attack_01.png").convert()
ettin_attack_west2       = pygame.image.load("images/characters/ettin/west_attack_02.png").convert()
ettin_attack_west3       = pygame.image.load("images/characters/ettin/west_attack_03.png").convert()
ettin_attack_south_west1 = pygame.image.load("images/characters/ettin/south_west_attack_01.png").convert()
ettin_attack_south_west2 = pygame.image.load("images/characters/ettin/south_west_attack_02.png").convert()
ettin_attack_south_west3 = pygame.image.load("images/characters/ettin/south_west_attack_03.png").convert()
ettin_attack_south1      = pygame.image.load("images/characters/ettin/south_attack_01.png").convert()
ettin_attack_south2      = pygame.image.load("images/characters/ettin/south_attack_02.png").convert()
ettin_attack_south3      = pygame.image.load("images/characters/ettin/south_attack_03.png").convert()
ettin_attack_south_east1 = pygame.image.load("images/characters/ettin/south_east_attack_01.png").convert()
ettin_attack_south_east2 = pygame.image.load("images/characters/ettin/south_east_attack_02.png").convert()
ettin_attack_south_east3 = pygame.image.load("images/characters/ettin/south_east_attack_03.png").convert()

ettin_death1 = pygame.image.load("images/characters/ettin/death_01.png").convert()
ettin_death2 = pygame.image.load("images/characters/ettin/death_02.png").convert()
ettin_death3 = pygame.image.load("images/characters/ettin/death_03.png").convert()
ettin_death4 = pygame.image.load("images/characters/ettin/death_04.png").convert()
ettin_death5 = pygame.image.load("images/characters/ettin/death_05.png").convert()
ettin_death6 = pygame.image.load("images/characters/ettin/death_06.png").convert()
ettin_death7 = pygame.image.load("images/characters/ettin/death_07.png").convert()

ettin_overkill1 = pygame.image.load("images/characters/ettin/overkill_01.png").convert()
ettin_overkill2 = pygame.image.load("images/characters/ettin/overkill_02.png").convert()
ettin_overkill3 = pygame.image.load("images/characters/ettin/overkill_03.png").convert()
ettin_overkill4 = pygame.image.load("images/characters/ettin/overkill_04.png").convert()
ettin_overkill5 = pygame.image.load("images/characters/ettin/overkill_05.png").convert()
ettin_overkill6 = pygame.image.load("images/characters/ettin/overkill_06.png").convert()
ettin_overkill7 = pygame.image.load("images/characters/ettin/overkill_07.png").convert()
ettin_overkill8 = pygame.image.load("images/characters/ettin/overkill_08.png").convert()
ettin_overkill9 = pygame.image.load("images/characters/ettin/overkill_09.png").convert()
ettin_overkill10 = pygame.image.load("images/characters/ettin/overkill_10.png").convert()


ettin_pain_east       = pygame.image.load("images/characters/ettin/east_pain.png").convert()
ettin_pain_north_east = pygame.image.load("images/characters/ettin/north_east_pain.png").convert()
ettin_pain_north      = pygame.image.load("images/characters/ettin/north_pain.png").convert()
ettin_pain_north_west = pygame.image.load("images/characters/ettin/north_west_pain.png").convert()
ettin_pain_west       = pygame.image.load("images/characters/ettin/west_pain.png").convert()
ettin_pain_south_west = pygame.image.load("images/characters/ettin/south_west_pain.png").convert()
ettin_pain_south      = pygame.image.load("images/characters/ettin/south_pain.png").convert()
ettin_pain_south_east = pygame.image.load("images/characters/ettin/south_east_pain.png").convert()

ettin_walk =[[ettin_walk_east1,ettin_walk_east2,ettin_walk_east3,ettin_walk_east4],
            [ettin_walk_north_east1,ettin_walk_north_east2,ettin_walk_north_east3,ettin_walk_north_east4],
            [ettin_walk_north1,ettin_walk_north2,ettin_walk_north3,ettin_walk_north4],
            [ettin_walk_north_west1,ettin_walk_north_west2,ettin_walk_north_west3,ettin_walk_north_west4],
            [ettin_walk_west1,ettin_walk_west2,ettin_walk_west3,ettin_walk_west4],
            [ettin_walk_south_west1,ettin_walk_south_west2,ettin_walk_south_west3,ettin_walk_south_west4],
            [ettin_walk_south1,ettin_walk_south2,ettin_walk_south3,ettin_walk_south4],
            [ettin_walk_south_east1,ettin_walk_south_east2,ettin_walk_south_east3,ettin_walk_south_east4]]

ettin_attack = [[ettin_attack_east1,ettin_attack_east2,ettin_attack_east3],
                [ettin_attack_north_east1,ettin_attack_north_east2,ettin_attack_north_east3],
                [ettin_attack_north1,ettin_attack_north2,ettin_attack_north3],
                [ettin_attack_north_west1,ettin_attack_north_west2,ettin_attack_north_west3],
                [ettin_attack_west1,ettin_attack_west2,ettin_attack_west3],
                [ettin_attack_south_west1,ettin_attack_south_west2,ettin_attack_south_west3],
                [ettin_attack_south1,ettin_attack_south2,ettin_attack_south3],
                [ettin_attack_south_east1,ettin_attack_south_east2,ettin_attack_south_east3]]

ettin_death = [ettin_death1,ettin_death2,ettin_death3,ettin_death4,ettin_death5,ettin_death6,ettin_death7]

ettin_overkill = [ettin_overkill1,ettin_overkill2,ettin_overkill3,ettin_overkill4,ettin_overkill5,ettin_overkill6,ettin_overkill7,ettin_overkill8,ettin_overkill9,ettin_overkill10]

ettin_pain = [ettin_pain_east,ettin_pain_north_east,ettin_pain_north,ettin_pain_north_west,ettin_pain_west,ettin_pain_south_east,ettin_pain_south,ettin_pain_south_east]

for row in ettin_walk:
    for img in row:
        img.set_colorkey((0,0,255))

for row in ettin_attack:
    for img in row:
        img.set_colorkey((0,0,255))

for img in ettin_death:
    img.set_colorkey((0,0,255))

for img in ettin_overkill:
    img.set_colorkey((0,0,255))

for img in ettin_pain:
    img.set_colorkey((0,0,255))