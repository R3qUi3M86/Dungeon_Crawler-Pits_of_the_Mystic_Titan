import pygame

###################
###### Entity #####
###################
###Characters
entity_collider_small = pygame.image.load("images/misc/colliders/entity_collider_omni_small.png").convert_alpha()
entity_collider_medium = pygame.image.load("images/misc/colliders/entity_collider_medium.png").convert_alpha()
entity_collider_sector_nw = pygame.image.load("images/misc/colliders/entity_collider_small_nw.png").convert_alpha()
entity_collider_sector_ne = pygame.image.load("images/misc/colliders/entity_collider_small_ne.png").convert_alpha()
entity_collider_sector_sw = pygame.image.load("images/misc/colliders/entity_collider_small_sw.png").convert_alpha()
entity_collider_sector_se = pygame.image.load("images/misc/colliders/entity_collider_small_se.png").convert_alpha()

###Projectiles
projectile_collider = pygame.image.load("images/misc/colliders/projectile_collider.png").convert_alpha()

###Misc
wall_hider_coolider = pygame.image.load("images/misc/colliders/wall_hider_coolider.png").convert_alpha()
small_square_collider = pygame.image.load("images/misc/colliders/small_square.png").convert_alpha()
medium_square_collider = pygame.image.load("images/misc/colliders/medium_square.png").convert_alpha()

#################
##### Level #####
#################
level_tile_collider = pygame.image.load("images/misc/colliders/level_tile_collider.png").convert_alpha()

### Floor pit collider
floor_pit_collider = pygame.image.load("images/level/cave/floors/pits/colliders/floor_pit_collider.png").convert_alpha()

### Water colliders
blue_water_border_bottom_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_bottom_collider.png").convert_alpha()
blue_water_border_top_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_top_collider.png").convert_alpha()
blue_water_border_left_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_left_collider.png").convert_alpha()
blue_water_border_right_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_right_collider.png").convert_alpha()

blue_water_border_top_left_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_top_left_convex_collider.png").convert_alpha()
blue_water_border_top_right_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_top_right_convex_collider.png").convert_alpha()
blue_water_border_bottom_left_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_bottom_left_convex_collider.png").convert_alpha()
blue_water_border_bottom_right_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_bottom_right_convex_collider.png").convert_alpha()

blue_water_border_convex_colliders = [[blue_water_border_top_left_convex_collider,blue_water_border_top_right_convex_collider],
                                      [blue_water_border_bottom_left_convex_collider,blue_water_border_bottom_right_convex_collider]]

### Wall colliders
#Bottom ending
wall_bottom_mid_floor_collider = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/wall_bottom_mid_floor_collider.png").convert_alpha()
wall_corner_bottom_left_floor_collider = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/wall_corner_bottom_left_floor_collider.png").convert_alpha()
wall_corner_bottom_right_floor_collider = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/wall_corner_bottom_right_floor_collider.png").convert_alpha()
wall_corner_bottom_left_water_left_border_collider = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/wall_corner_bottom_left_water_left_border_collider.png").convert_alpha()
wall_corner_bottom_right_water_right_border_collider = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/wall_corner_bottom_right_water_right_border_collider.png").convert_alpha()
small_collider_top_left = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/small_collider_top_left.png").convert_alpha()
small_collider_top_right = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/small_collider_top_right.png").convert_alpha()
small_collider_bottom_left = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/small_collider_bottom_left.png").convert_alpha()
small_collider_bottom_right = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/small_collider_bottom_right.png").convert_alpha()
small_dual_collider_ne_sw = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/small_dual_collider_ne_sw.png").convert_alpha()
small_dual_collider_nw_se = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/colliders/small_dual_collider_nw_se.png").convert_alpha()

#Side wall
wall_left_collider = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/colliders/wall_left_collider.png").convert_alpha()
wall_right_collider = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/colliders/wall_right_collider.png").convert_alpha()

#Top wall
wall_top_floor_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_floor_collider.png").convert_alpha()
wall_top_left_convex_floor_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_left_convex_floor_collider.png").convert_alpha()
wall_top_right_convex_floor_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_right_convex_floor_collider.png").convert_alpha()
wall_top_left_convex_water_left_border_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_left_convex_water_left_border_collider.png").convert_alpha()
wall_top_right_convex_water_right_border_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_right_convex_water_right_border_collider.png").convert_alpha()
wall_top_small_left_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_small_left_collider.png").convert_alpha()
wall_top_small_right_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_small_right_collider.png").convert_alpha()
wall_top_left_convex_water_convex_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_left_convex_water_convex_collider.png").convert_alpha()
wall_top_right_convex_water_convex_collider = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/colliders/wall_top_right_convex_water_convex_collider.png").convert_alpha()