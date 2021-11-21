import pygame

collision_small_mask = pygame.image.load("images/misc/shadows/character_shadow_mask_small.png").convert_alpha()
collision_medium_mask = pygame.image.load("images/misc/shadows/character_shadow_mask_medium.png").convert_alpha()
collision_small_sector_nw = pygame.image.load("images/misc/player_collision_sectors/player_collision_mask_nw.png").convert_alpha()
collision_small_sector_ne = pygame.image.load("images/misc/player_collision_sectors/player_collision_mask_ne.png").convert_alpha()
collision_small_sector_sw = pygame.image.load("images/misc/player_collision_sectors/player_collision_mask_sw.png").convert_alpha()
collision_small_sector_se = pygame.image.load("images/misc/player_collision_sectors/player_collision_mask_se.png").convert_alpha()