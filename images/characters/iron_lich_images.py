import pygame
from utilities.constants import *

iron_lich_walk_east = pygame.image.load("images/characters/iron_lich/east_01.png").convert_alpha()
iron_lich_walk_north_east = pygame.image.load("images/characters/iron_lich/north_east_01.png").convert_alpha()
iron_lich_walk_north = pygame.image.load("images/characters/iron_lich/north_01.png").convert_alpha()
iron_lich_walk_north_west = pygame.image.load("images/characters/iron_lich/north_west_01.png").convert_alpha()
iron_lich_walk_west = pygame.image.load("images/characters/iron_lich/west_01.png").convert_alpha()
iron_lich_walk_south_west = pygame.image.load("images/characters/iron_lich/south_west_01.png").convert_alpha()
iron_lich_walk_south = pygame.image.load("images/characters/iron_lich/south_01.png").convert_alpha()
iron_lich_walk_south_east = pygame.image.load("images/characters/iron_lich/south_east_01.png").convert_alpha()

iron_lich_attack_east = pygame.image.load("images/characters/iron_lich/east_attack_01.png").convert_alpha()
iron_lich_attack_north_east = pygame.image.load("images/characters/iron_lich/north_east_attack_01.png").convert_alpha()
iron_lich_attack_north = pygame.image.load("images/characters/iron_lich/north_attack_01.png").convert_alpha()
iron_lich_attack_north_west = pygame.image.load("images/characters/iron_lich/north_west_attack_01.png").convert_alpha()
iron_lich_attack_west = pygame.image.load("images/characters/iron_lich/west_attack_01.png").convert_alpha()
iron_lich_attack_south_west = pygame.image.load("images/characters/iron_lich/south_west_attack_01.png").convert_alpha()
iron_lich_attack_south = pygame.image.load("images/characters/iron_lich/south_attack_01.png").convert_alpha()
iron_lich_attack_south_east = pygame.image.load("images/characters/iron_lich/south_east_attack_01.png").convert_alpha()

iron_lich_death1 = pygame.image.load("images/characters/iron_lich/death_01.png").convert_alpha()
iron_lich_death2 = pygame.image.load("images/characters/iron_lich/death_02.png").convert_alpha()
iron_lich_death3 = pygame.image.load("images/characters/iron_lich/death_03.png").convert_alpha()
iron_lich_death4 = pygame.image.load("images/characters/iron_lich/death_04.png").convert_alpha()
iron_lich_death5 = pygame.image.load("images/characters/iron_lich/death_05.png").convert_alpha()
iron_lich_death6 = pygame.image.load("images/characters/iron_lich/death_06.png").convert_alpha()
iron_lich_death7 = pygame.image.load("images/characters/iron_lich/death_07.png").convert_alpha()

iron_lich_walk = [[iron_lich_walk_east, iron_lich_walk_east],
                  [iron_lich_walk_north_east, iron_lich_walk_north_east],
                  [iron_lich_walk_north, iron_lich_walk_north],
                  [iron_lich_walk_north_west, iron_lich_walk_north_west],
                  [iron_lich_walk_west, iron_lich_walk_west],
                  [iron_lich_walk_south_west, iron_lich_walk_south_west],
                  [iron_lich_walk_south, iron_lich_walk_south],
                  [iron_lich_walk_south_east, iron_lich_walk_south_east]]

iron_lich_attack = [[iron_lich_attack_east, iron_lich_attack_east, iron_lich_attack_east],
                    [iron_lich_attack_north_east, iron_lich_attack_north_east, iron_lich_attack_north_east],
                    [iron_lich_attack_north, iron_lich_attack_north, iron_lich_attack_north],
                    [iron_lich_attack_north_west, iron_lich_attack_north_west, iron_lich_attack_north_west],
                    [iron_lich_attack_west, iron_lich_attack_west, iron_lich_attack_west],
                    [iron_lich_attack_south_west, iron_lich_attack_south_west, iron_lich_attack_south_west],
                    [iron_lich_attack_south, iron_lich_attack_south, iron_lich_attack_south],
                    [iron_lich_attack_south_east, iron_lich_attack_south_east, iron_lich_attack_south_east]]

iron_lich_death = [iron_lich_death1, iron_lich_death2, iron_lich_death3, iron_lich_death4, iron_lich_death5, iron_lich_death6, iron_lich_death7]

iron_lich_overkill = [iron_lich_death7, iron_lich_death7]

iron_lich_pain = [iron_lich_walk_east, iron_lich_walk_north_east, iron_lich_walk_north, iron_lich_walk_north_west, iron_lich_walk_west, iron_lich_walk_south_west, iron_lich_walk_south, iron_lich_walk_south_east]