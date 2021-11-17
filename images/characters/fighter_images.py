import pygame

character_walk_east1       = pygame.image.load("images/characters/fighter/east_01.png").convert_alpha()
character_walk_east2       = pygame.image.load("images/characters/fighter/east_02.png").convert_alpha()
character_walk_east3       = pygame.image.load("images/characters/fighter/east_03.png").convert_alpha()
character_walk_east4       = pygame.image.load("images/characters/fighter/east_04.png").convert_alpha()
character_walk_north_east1 = pygame.image.load("images/characters/fighter/north_east_01.png").convert_alpha()
character_walk_north_east2 = pygame.image.load("images/characters/fighter/north_east_02.png").convert_alpha()
character_walk_north_east3 = pygame.image.load("images/characters/fighter/north_east_03.png").convert_alpha()
character_walk_north_east4 = pygame.image.load("images/characters/fighter/north_east_04.png").convert_alpha()
character_walk_north1      = pygame.image.load("images/characters/fighter/north_01.png").convert_alpha()
character_walk_north2      = pygame.image.load("images/characters/fighter/north_02.png").convert_alpha()
character_walk_north3      = pygame.image.load("images/characters/fighter/north_03.png").convert_alpha()
character_walk_north4      = pygame.image.load("images/characters/fighter/north_04.png").convert_alpha()
character_walk_north_west1 = pygame.image.load("images/characters/fighter/north_west_01.png").convert_alpha()
character_walk_north_west2 = pygame.image.load("images/characters/fighter/north_west_02.png").convert_alpha()
character_walk_north_west3 = pygame.image.load("images/characters/fighter/north_west_03.png").convert_alpha()
character_walk_north_west4 = pygame.image.load("images/characters/fighter/north_west_04.png").convert_alpha()
character_walk_west1       = pygame.image.load("images/characters/fighter/west_01.png").convert_alpha()
character_walk_west2       = pygame.image.load("images/characters/fighter/west_02.png").convert_alpha()
character_walk_west3       = pygame.image.load("images/characters/fighter/west_03.png").convert_alpha()
character_walk_west4       = pygame.image.load("images/characters/fighter/west_04.png").convert_alpha()
character_walk_south_west1 = pygame.image.load("images/characters/fighter/south_west_01.png").convert_alpha()
character_walk_south_west2 = pygame.image.load("images/characters/fighter/south_west_02.png").convert_alpha()
character_walk_south_west3 = pygame.image.load("images/characters/fighter/south_west_03.png").convert_alpha()
character_walk_south_west4 = pygame.image.load("images/characters/fighter/south_west_04.png").convert_alpha()
character_walk_south1      = pygame.image.load("images/characters/fighter/south_01.png").convert_alpha()
character_walk_south2      = pygame.image.load("images/characters/fighter/south_02.png").convert_alpha()
character_walk_south3      = pygame.image.load("images/characters/fighter/south_03.png").convert_alpha()
character_walk_south4      = pygame.image.load("images/characters/fighter/south_04.png").convert_alpha()
character_walk_south_east1 = pygame.image.load("images/characters/fighter/south_east_01.png").convert_alpha()
character_walk_south_east2 = pygame.image.load("images/characters/fighter/south_east_02.png").convert_alpha()
character_walk_south_east3 = pygame.image.load("images/characters/fighter/south_east_03.png").convert_alpha()
character_walk_south_east4 = pygame.image.load("images/characters/fighter/south_east_04.png").convert_alpha()

character_attack_east1       = pygame.image.load("images/characters/fighter/east_attack_01.png").convert_alpha()
character_attack_east2       = pygame.image.load("images/characters/fighter/east_attack_02.png").convert_alpha()
character_attack_north_east1 = pygame.image.load("images/characters/fighter/north_east_attack_01.png").convert_alpha()
character_attack_north_east2 = pygame.image.load("images/characters/fighter/north_east_attack_02.png").convert_alpha()
character_attack_north1      = pygame.image.load("images/characters/fighter/north_attack_01.png").convert_alpha()
character_attack_north2      = pygame.image.load("images/characters/fighter/north_attack_02.png").convert_alpha()
character_attack_north_west1 = pygame.image.load("images/characters/fighter/north_west_attack_01.png").convert_alpha()
character_attack_north_west2 = pygame.image.load("images/characters/fighter/north_west_attack_02.png").convert_alpha()
character_attack_west1       = pygame.image.load("images/characters/fighter/west_attack_01.png").convert_alpha()
character_attack_west2       = pygame.image.load("images/characters/fighter/west_attack_02.png").convert_alpha()
character_attack_south_west1 = pygame.image.load("images/characters/fighter/south_west_attack_01.png").convert_alpha()
character_attack_south_west2 = pygame.image.load("images/characters/fighter/south_west_attack_02.png").convert_alpha()
character_attack_south1      = pygame.image.load("images/characters/fighter/south_attack_01.png").convert_alpha()
character_attack_south2      = pygame.image.load("images/characters/fighter/south_attack_02.png").convert_alpha()
character_attack_south_east1 = pygame.image.load("images/characters/fighter/south_east_attack_01.png").convert_alpha()
character_attack_south_east2 = pygame.image.load("images/characters/fighter/south_east_attack_02.png").convert_alpha()

character_walk =[[character_walk_east1,character_walk_east2,character_walk_east3,character_walk_east4],
                [character_walk_north_east1,character_walk_north_east2,character_walk_north_east3,character_walk_north_east4],
                [character_walk_north1,character_walk_north2,character_walk_north3,character_walk_north4],
                [character_walk_north_west1,character_walk_north_west2,character_walk_north_west3,character_walk_north_west4],
                [character_walk_west1,character_walk_west2,character_walk_west3,character_walk_west4],
                [character_walk_south_west1,character_walk_south_west2,character_walk_south_west3,character_walk_south_west4],
                [character_walk_south1,character_walk_south2,character_walk_south3,character_walk_south4],
                [character_walk_south_east1,character_walk_south_east2,character_walk_south_east3,character_walk_south_east4]]

character_attack = [[character_attack_east1,character_attack_east2],
                [character_attack_north_east1,character_attack_north_east2],
                [character_attack_north1,character_attack_north2],
                [character_attack_north_west1,character_attack_north_west2],
                [character_attack_west1,character_attack_west2],
                [character_attack_south_west1,character_attack_south_west2],
                [character_attack_south1,character_attack_south2],
                [character_attack_south_east1,character_attack_south_east2]]

