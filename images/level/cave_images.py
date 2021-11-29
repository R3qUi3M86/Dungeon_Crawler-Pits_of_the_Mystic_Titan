import pygame

empty_tile_image = pygame.image.load("images/level/cave/floors/empty_tile_mask.png").convert_alpha()

###########################################
###### Level entrance and exit images #####
###########################################
# ###Common###
# level_entrance_and_exit_top_left = pygame.image.load("images/level/cave/entrance_and_exit/top_left.png").convert_alpha()
# level_entrance_and_exit_top_mid = pygame.image.load("images/level/cave/entrance_and_exit/top_mid.png").convert_alpha()
# level_entrance_and_exit_top_right = pygame.image.load("images/level/cave/entrance_and_exit/top_right.png").convert_alpha()

###Entrance###
level_entrance_top_left = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_mid_left.png").convert_alpha()
level_entrance_top_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_mid_mid.png").convert_alpha()
level_entrance_top_right = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_mid_right.png").convert_alpha()
level_entrance_bottom_left = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_bottom_left.png").convert_alpha()
level_entrance_bottom_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_bottom_mid.png").convert_alpha()
level_entrance_bottom_right = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_bottom_right.png").convert_alpha()
level_entrance_images = [[level_entrance_top_left,level_entrance_top_mid,level_entrance_top_right],
                         [level_entrance_bottom_left,level_entrance_bottom_mid,level_entrance_bottom_right]]

###Exit###
level_exit_top_left = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_mid_left.png").convert_alpha()
level_exit_top_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_mid_mid.png").convert_alpha()
level_exit_top_right = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_mid_right.png").convert_alpha()
level_exit_bottom_left = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_bottom_left.png").convert_alpha()
level_exit_bottom_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_bottom_mid.png").convert_alpha()
level_exit_bottom_right = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_bottom_right.png").convert_alpha()
level_exit_images = [[level_exit_top_left,level_exit_top_mid,level_exit_top_right],
                     [level_exit_bottom_left,level_exit_bottom_mid,level_exit_bottom_right]]

########################
##### Floor images #####
########################
###Basic floor###
floor_01 = pygame.image.load("images/level/cave/floors/floor_01.png").convert_alpha()
floor_02 = pygame.image.load("images/level/cave/floors/floor_02.png").convert_alpha()
floor_03 = pygame.image.load("images/level/cave/floors/floor_03.png").convert_alpha()
floor_04 = pygame.image.load("images/level/cave/floors/floor_04.png").convert_alpha()
floor_tile_images = [floor_01,floor_02,floor_03,floor_04]

###Floor next to entrance###
floor_level_entrance_left = pygame.image.load("images/level/cave/floors/floor_level_entrance_left.png").convert_alpha()
floor_level_entrance_mid = pygame.image.load("images/level/cave/floors/floor_level_entrance_mid.png").convert_alpha()
floor_level_entrance_right = pygame.image.load("images/level/cave/floors/floor_level_entrance_right.png").convert_alpha()
floor_tile_entrance_images = [floor_level_entrance_left,floor_level_entrance_mid,floor_level_entrance_right]

###Debree###
floor_debree_01 = pygame.image.load("images/level/cave/floors/debris/floor_debree_01.png").convert_alpha()
floor_debree_02 = pygame.image.load("images/level/cave/floors/debris/floor_debree_02.png").convert_alpha()
floor_debree_03 = pygame.image.load("images/level/cave/floors/debris/floor_debree_03.png").convert_alpha()
floor_debree_04 = pygame.image.load("images/level/cave/floors/debris/floor_debree_04.png").convert_alpha()
floor_debree_05 = pygame.image.load("images/level/cave/floors/debris/floor_debree_05.png").convert_alpha()
floor_debree_06 = pygame.image.load("images/level/cave/floors/debris/floor_debree_06.png").convert_alpha()
debree_tile_images = [floor_debree_01,floor_debree_02,floor_debree_03,floor_debree_04,floor_debree_05,floor_debree_06]

###Cracks###
cross_crack = pygame.image.load("images/level/cave/floors/cracks/cross_crack.png").convert_alpha()
web_crack = pygame.image.load("images/level/cave/floors/cracks/web_crack.png").convert_alpha()
top_left_crack = pygame.image.load("images/level/cave/floors/cracks/top_left_crack.png").convert_alpha()
top_right_crack = pygame.image.load("images/level/cave/floors/cracks/top_right_crack.png").convert_alpha()
bottom_left_crack = pygame.image.load("images/level/cave/floors/cracks/bottom_left_crack.png").convert_alpha()
bottom_right_crack = pygame.image.load("images/level/cave/floors/cracks/bottom_right_crack.png").convert_alpha()
simple_crack_images = [cross_crack,web_crack]
corner_crack_images = [[top_left_crack,top_right_crack],[bottom_left_crack,bottom_right_crack]]

######################
##### Pit images #####
######################
pit_01 = pygame.image.load("images/level/cave/floors/pits/floor_pit_01.png").convert_alpha()
pit_02 = pygame.image.load("images/level/cave/floors/pits/floor_pit_02.png").convert_alpha()
pit_03 = pygame.image.load("images/level/cave/floors/pits/floor_pit_03.png").convert_alpha()
floor_pit_collider = pygame.image.load("images/level/cave/floors/pits/colliders/floor_pit_collider.png").convert_alpha()
pit_tile_images = [pit_01,pit_02,pit_03]

##############################
###### Blue water images #####
##############################
###Lake###
blue_water_01 = pygame.image.load("images/level/cave/blue_water/blue_water_01.png").convert_alpha()
blue_water_02 = pygame.image.load("images/level/cave/blue_water/blue_water_02.png").convert_alpha()
blue_water_03 = pygame.image.load("images/level/cave/blue_water/blue_water_03.png").convert_alpha()
blue_water_04 = pygame.image.load("images/level/cave/blue_water/blue_water_04.png").convert_alpha()
blue_water_under_wall_01 = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_01.png").convert_alpha()
blue_water_under_wall_02 = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_02.png").convert_alpha()
blue_water_under_wall_left = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_left.png").convert_alpha()
blue_water_under_wall_right = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_right.png").convert_alpha()
blue_water_images = [blue_water_01,blue_water_02,blue_water_03,blue_water_04]
blue_water_under_wall_images = [blue_water_under_wall_01,blue_water_under_wall_02]

###Coastal###
#Straight
blue_water_border_bottom_01 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_01.png").convert_alpha()
blue_water_border_bottom_02 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_02.png").convert_alpha()
blue_water_border_bottom_03 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_03.png").convert_alpha()
blue_water_border_bottom_04 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_04.png").convert_alpha()
blue_water_border_bottom_images = [blue_water_border_bottom_01,blue_water_border_bottom_02,blue_water_border_bottom_03]
blue_water_border_bottom_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_bottom_collider.png").convert_alpha()

blue_water_border_top_01 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_01.png").convert_alpha()
blue_water_border_top_02 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_02.png").convert_alpha()
blue_water_border_top_03 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_03.png").convert_alpha()
blue_water_border_top_04 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_04.png").convert_alpha()
blue_water_border_top_images = [blue_water_border_top_01,blue_water_border_top_02,blue_water_border_top_03]
blue_water_border_top_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_top_collider.png").convert_alpha()

blue_water_border_left = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_left.png").convert_alpha()
blue_water_border_right = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_right.png").convert_alpha()
blue_water_border_left_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_left_collider.png").convert_alpha()
blue_water_border_right_collider = pygame.image.load("images/level/cave/blue_water/coastal/colliders/blue_water_border_right_collider.png").convert_alpha()

#Convex
blue_water_border_top_left_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_top_left_convex.png").convert_alpha()
blue_water_border_top_right_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_top_right_convex.png").convert_alpha()
blue_water_border_bottom_left_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_bottom_left_convex.png").convert_alpha()
blue_water_border_bottom_right_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_bottom_right_convex.png").convert_alpha()
blue_water_border_top_left_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_top_left_convex_collider.png").convert_alpha()
blue_water_border_top_right_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_top_right_convex_collider.png").convert_alpha()
blue_water_border_bottom_left_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_bottom_left_convex_collider.png").convert_alpha()
blue_water_border_bottom_right_convex_collider = pygame.image.load("images/level/cave/blue_water/coastal/convex/colliders/blue_water_border_bottom_right_convex_collider.png").convert_alpha()
blue_water_border_convex_images = [[blue_water_border_top_left_convex,blue_water_border_top_right_convex],
                                   [blue_water_border_bottom_left_convex,blue_water_border_bottom_right_convex]]
blue_water_border_convex_colliders = [[blue_water_border_top_left_convex_collider,blue_water_border_top_right_convex_collider],
                                      [blue_water_border_bottom_left_convex_collider,blue_water_border_bottom_right_convex_collider]]

#Concave
blue_water_border_top_left_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_top_left_concave.png").convert_alpha()
blue_water_border_top_right_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_top_right_concave.png").convert_alpha()
blue_water_border_bottom_left_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_bottom_left_concave.png").convert_alpha()
blue_water_border_bottom_right_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_bottom_right_concave.png").convert_alpha()
blue_water_border_top_left_concave_collider = pygame.image.load("images/level/cave/blue_water/coastal/concave/colliders/blue_water_border_top_left_concave_collider.png").convert_alpha()
blue_water_border_top_right_concave_collider = pygame.image.load("images/level/cave/blue_water/coastal/concave/colliders/blue_water_border_top_right_concave_collider.png").convert_alpha()
blue_water_border_bottom_left_concave_collider = pygame.image.load("images/level/cave/blue_water/coastal/concave/colliders/blue_water_border_bottom_left_concave_collider.png").convert_alpha()
blue_water_border_bottom_right_concave_collider = pygame.image.load("images/level/cave/blue_water/coastal/concave/colliders/blue_water_border_bottom_right_concave_collider.png").convert_alpha()
blue_water_border_concave_images = [[blue_water_border_top_left_concave,blue_water_border_top_right_concave],
                                   [blue_water_border_bottom_left_concave,blue_water_border_bottom_right_concave]]
blue_water_border_concave_colliders = [[blue_water_border_top_left_concave_collider,blue_water_border_top_right_concave_collider],
                                      [blue_water_border_bottom_left_concave_collider,blue_water_border_bottom_right_concave_collider]]
#######################
##### Wall images #####
#######################
### Basic ###
blank = pygame.image.load("images/level/cave/walls/blank.png").convert_alpha()

### Only floor in vicinity ###
#Bottom wall lower sections
wall_bottom_lower_01 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/lower/wall_bottom_lower_01.png").convert_alpha()
wall_bottom_lower_02 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/lower/wall_bottom_lower_02.png").convert_alpha()
wall_corner_bottom_left_lower = pygame.image.load("images/level/cave/walls/floor/bottom_ending/lower/wall_corner_bottom_left_lower.png").convert_alpha()
wall_corner_bottom_right_lower = pygame.image.load("images/level/cave/walls/floor/bottom_ending/lower/wall_corner_bottom_right_lower.png").convert_alpha()
wall_bottom_lower = [wall_bottom_lower_01, wall_bottom_lower_02]

#Bottom wall middle sections
wall_bottom_middle_01 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/middle/wall_bottom_middle_01.png").convert_alpha()
wall_bottom_middle_02 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/middle/wall_bottom_middle_02.png").convert_alpha()
wall_bottom_middle_left = pygame.image.load("images/level/cave/walls/floor/bottom_ending/middle/wall_bottom_middle_left.png").convert_alpha()
wall_bottom_middle_right = pygame.image.load("images/level/cave/walls/floor/bottom_ending/middle/wall_bottom_middle_right.png").convert_alpha()
wall_bottom_middle = [wall_bottom_middle_01, wall_bottom_middle_02]

#Bottom wall upper sections
wall_bottom_upper_01 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_upper_01.png").convert_alpha()
wall_bottom_upper_02 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_upper_02.png").convert_alpha()
wall_bottom_upper_03 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_upper_03.png").convert_alpha()
wall_bottom_upper_04 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_upper_04.png").convert_alpha()
wall_bottom_upper_05 = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_upper_05.png").convert_alpha()
wall_bottom_left_upper = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_left_upper.png").convert_alpha()
wall_bottom_right_upper = pygame.image.load("images/level/cave/walls/floor/bottom_ending/upper/wall_bottom_right_upper.png").convert_alpha()
wall_bottom_upper = [wall_bottom_upper_01, wall_bottom_upper_02, wall_bottom_upper_03, wall_bottom_upper_04, wall_bottom_upper_05]

#Top wall sections
wall_top_01 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_top_01.png").convert_alpha()
wall_top_02 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_top_02.png").convert_alpha()
wall_top_left_convex = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_top_left_convex.png").convert_alpha()
wall_top_right_convex = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_top_right_convex.png").convert_alpha()
wall_top = [wall_top_01, wall_top_02]
wall_top_convex = [wall_top_left_convex, wall_top_right_convex]

#Side wall sections
wall_left_01 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_left_01.png").convert_alpha()
wall_left_02 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_left_02.png").convert_alpha()
wall_left_03 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_left_03.png").convert_alpha()
wall_left_04 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_left_04.png").convert_alpha()
wall_right_01 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_right_01.png").convert_alpha()
wall_right_02 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_right_02.png").convert_alpha()
wall_right_03 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_left_03.png").convert_alpha()
wall_right_04 = pygame.image.load("images/level/cave/walls/floor/top_and_sides/wall_left_04.png").convert_alpha()
wall_left = [wall_left_01, wall_left_02, wall_left_03, wall_left_04]
wall_right = [wall_right_01, wall_right_02, wall_right_03, wall_right_04]

#Concave wall sections
wall_upper_left_concave = pygame.image.load("images/level/cave/walls/floor/corners/wall_upper_left_concave.png").convert_alpha()
wall_upper_right_concave = pygame.image.load("images/level/cave/walls/floor/corners/wall_upper_right_concave.png").convert_alpha()
wall_lower_left_concave = pygame.image.load("images/level/cave/walls/floor/corners/wall_lower_left_concave.png").convert_alpha()
wall_lower_right_concave = pygame.image.load("images/level/cave/walls/floor/corners/wall_lower_right_concave.png").convert_alpha()
wall_concave = [[wall_upper_left_concave, wall_upper_right_concave],[wall_lower_left_concave, wall_lower_right_concave]]

