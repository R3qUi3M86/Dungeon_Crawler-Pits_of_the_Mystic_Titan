import pygame

empty_tile_image = pygame.image.load("images/level/cave/floors/empty_tile_mask.png").convert_alpha()

###########################################
###### Level entrance and exit images #####
###########################################
###Entrance###
#Under overlay
level_entrance_top_left_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_entrance_top_left_hidden.png").convert_alpha()
level_entrance_top_mid_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_entrance_top_mid_hidden.png").convert_alpha()
level_entrance_top_right_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_entrance_top_right_hidden.png").convert_alpha()
level_entrance_bottom_left_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_entrance_bottom_left_hidden.png").convert_alpha()
level_entrance_bottom_mid_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_entrance_bottom_mid_hidden.png").convert_alpha()
level_entrance_bottom_right_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_entrance_bottom_right_hidden.png").convert_alpha()
level_entrance_images_hidden = [[level_entrance_top_left_hidden,level_entrance_top_mid_hidden,level_entrance_top_right_hidden],
                                [level_entrance_bottom_left_hidden,level_entrance_bottom_mid_hidden,level_entrance_bottom_right_hidden]]

#Overlay
level_entrance_top_left_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_entrance_top_left_overlay.png").convert_alpha()
level_entrance_top_mid_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_entrance_top_mid_overlay.png").convert_alpha()
level_entrance_top_right_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_entrance_top_right_overlay.png").convert_alpha()
level_entrance_bottom_left_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_entrance_bottom_left_overlay.png").convert_alpha()
level_entrance_bottom_mid_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_entrance_bottom_mid_overlay.png").convert_alpha()
level_entrance_bottom_right_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_entrance_bottom_right_overlay.png").convert_alpha()
level_entrance_images_overlay = [[level_entrance_top_left_overlay,level_entrance_top_mid_overlay,level_entrance_top_right_overlay],
                                [level_entrance_bottom_left_overlay,level_entrance_bottom_mid_overlay,level_entrance_bottom_right_overlay]]

###Exit###
#Under overlay
level_exit_top_left_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_exit_top_left_hidden.png").convert_alpha()
level_exit_top_mid_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_exit_top_mid_hidden.png").convert_alpha()
level_exit_top_right_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_exit_top_right_hidden.png").convert_alpha()
level_exit_bottom_left_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_exit_bottom_left_hidden.png").convert_alpha()
level_exit_bottom_mid_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_exit_bottom_mid_hidden.png").convert_alpha()
level_exit_bottom_right_hidden = pygame.image.load("images/level/cave/entrance_and_exit/hidden/level_exit_bottom_right_hidden.png").convert_alpha()
level_exit_images_hidden = [[level_exit_top_left_hidden,level_exit_top_mid_hidden,level_exit_top_right_hidden],
                            [level_exit_bottom_left_hidden,level_exit_bottom_mid_hidden,level_exit_bottom_right_hidden]]

#Overlay
level_exit_top_left_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_exit_top_left_overlay.png").convert_alpha()
level_exit_top_mid_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_exit_top_mid_overlay.png").convert_alpha()
level_exit_top_right_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_exit_top_right_overlay.png").convert_alpha()
level_exit_bottom_left_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_exit_bottom_left_overlay.png").convert_alpha()
level_exit_bottom_mid_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_exit_bottom_mid_overlay.png").convert_alpha()
level_exit_bottom_right_overlay = pygame.image.load("images/level/cave/entrance_and_exit/overlay/level_exit_bottom_right_overlay.png").convert_alpha()
level_exit_images_overlay = [[level_exit_top_left_overlay,level_exit_top_mid_overlay,level_exit_top_right_overlay],
                            [level_exit_bottom_left_overlay,level_exit_bottom_mid_overlay,level_exit_bottom_right_overlay]]

########################
##### Floor images #####
########################
###Basic floor###
floor_01 = pygame.image.load("images/level/cave/floors/floor_01.png").convert()
floor_02 = pygame.image.load("images/level/cave/floors/floor_02.png").convert()
floor_03 = pygame.image.load("images/level/cave/floors/floor_03.png").convert()
floor_04 = pygame.image.load("images/level/cave/floors/floor_04.png").convert()
floor_tile_images = [floor_01,floor_02,floor_03,floor_04]

###Floor next to entrance###
floor_level_entrance_left = pygame.image.load("images/level/cave/floors/floor_level_entrance_left.png").convert()
floor_level_entrance_mid = pygame.image.load("images/level/cave/floors/floor_level_entrance_mid.png").convert()
floor_level_entrance_right = pygame.image.load("images/level/cave/floors/floor_level_entrance_right.png").convert()
floor_tile_entrance_images = [floor_level_entrance_left,floor_level_entrance_mid,floor_level_entrance_right]

###Debree###
floor_debree_01 = pygame.image.load("images/level/cave/floors/debris/floor_debree_01.png").convert()
floor_debree_02 = pygame.image.load("images/level/cave/floors/debris/floor_debree_02.png").convert()
floor_debree_03 = pygame.image.load("images/level/cave/floors/debris/floor_debree_03.png").convert()
floor_debree_04 = pygame.image.load("images/level/cave/floors/debris/floor_debree_04.png").convert()
floor_debree_05 = pygame.image.load("images/level/cave/floors/debris/floor_debree_05.png").convert()
floor_debree_06 = pygame.image.load("images/level/cave/floors/debris/floor_debree_06.png").convert()
debree_tile_images = [floor_debree_01,floor_debree_02,floor_debree_03,floor_debree_04,floor_debree_05,floor_debree_06]

###Cracks###
cross_crack = pygame.image.load("images/level/cave/floors/cracks/cross_crack.png").convert()
web_crack = pygame.image.load("images/level/cave/floors/cracks/web_crack.png").convert()
top_left_crack = pygame.image.load("images/level/cave/floors/cracks/top_left_crack.png").convert()
top_right_crack = pygame.image.load("images/level/cave/floors/cracks/top_right_crack.png").convert()
bottom_left_crack = pygame.image.load("images/level/cave/floors/cracks/bottom_left_crack.png").convert()
bottom_right_crack = pygame.image.load("images/level/cave/floors/cracks/bottom_right_crack.png").convert()
simple_crack_images = [cross_crack,web_crack]
corner_crack_images = [[top_left_crack,top_right_crack],[bottom_left_crack,bottom_right_crack]]

######################
##### Pit images #####
######################
pit_01 = pygame.image.load("images/level/cave/floors/pits/floor_pit_01.png").convert()
pit_02 = pygame.image.load("images/level/cave/floors/pits/floor_pit_02.png").convert()
pit_03 = pygame.image.load("images/level/cave/floors/pits/floor_pit_03.png").convert()
pit_tile_images = [pit_01,pit_02,pit_03]

##############################
###### Blue water images #####
##############################
###Lake###
blue_water_01 = pygame.image.load("images/level/cave/blue_water/blue_water_01.png").convert()
blue_water_02 = pygame.image.load("images/level/cave/blue_water/blue_water_02.png").convert()
blue_water_03 = pygame.image.load("images/level/cave/blue_water/blue_water_03.png").convert()
blue_water_04 = pygame.image.load("images/level/cave/blue_water/blue_water_04.png").convert()
blue_water_under_wall_01 = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_01.png").convert()
blue_water_under_wall_02 = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_02.png").convert()
blue_water_under_wall_left = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_left.png").convert()
blue_water_under_wall_right = pygame.image.load("images/level/cave/blue_water/under_wall/water_under_wall_right.png").convert()
blue_water_images = [blue_water_01,blue_water_02,blue_water_03,blue_water_04]
blue_water_under_wall_images = [blue_water_under_wall_01,blue_water_under_wall_02]

###Coastal###
#Straight
blue_water_border_bottom_01 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_01.png").convert()
blue_water_border_bottom_02 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_02.png").convert()
blue_water_border_bottom_03 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_03.png").convert()
blue_water_border_bottom_04 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_04.png").convert()
blue_water_border_bottom_images = [blue_water_border_bottom_01,blue_water_border_bottom_02,blue_water_border_bottom_03]

blue_water_border_top_01 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_01.png").convert()
blue_water_border_top_02 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_02.png").convert()
blue_water_border_top_03 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_03.png").convert()
blue_water_border_top_04 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_04.png").convert()
blue_water_border_top_images = [blue_water_border_top_01,blue_water_border_top_02,blue_water_border_top_03]

blue_water_border_left = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_left.png").convert()
blue_water_border_right = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_right.png").convert()

#Convex
blue_water_border_top_left_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_top_left_convex.png").convert()
blue_water_border_top_right_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_top_right_convex.png").convert()
blue_water_border_bottom_left_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_bottom_left_convex.png").convert()
blue_water_border_bottom_right_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_bottom_right_convex.png").convert()
blue_water_border_convex_images = [[blue_water_border_top_left_convex,blue_water_border_top_right_convex],
                                   [blue_water_border_bottom_left_convex,blue_water_border_bottom_right_convex]]

#Concave
blue_water_border_top_left_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_top_left_concave.png").convert()
blue_water_border_top_right_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_top_right_concave.png").convert()
blue_water_border_bottom_left_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_bottom_left_concave.png").convert()
blue_water_border_bottom_right_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_bottom_right_concave.png").convert()
blue_water_border_concave_images = [[blue_water_border_top_left_concave,blue_water_border_top_right_concave],
                                   [blue_water_border_bottom_left_concave,blue_water_border_bottom_right_concave]]

########################
###### Lava images #####
########################
###Lava###
lava_01 = pygame.image.load("images/level/cave/lava/lava_01.png").convert()
lava_02 = pygame.image.load("images/level/cave/lava/lava_02.png").convert()
lava_03 = pygame.image.load("images/level/cave/lava/lava_03.png").convert()
lava_04 = pygame.image.load("images/level/cave/lava/lava_04.png").convert()
lava_05 = pygame.image.load("images/level/cave/lava/lava_05.png").convert()
lava_06 = pygame.image.load("images/level/cave/lava/lava_06.png").convert()
lava_07 = pygame.image.load("images/level/cave/lava/lava_07.png").convert()
lava_08 = pygame.image.load("images/level/cave/lava/lava_08.png").convert()
lava_09 = pygame.image.load("images/level/cave/lava/lava_09.png").convert()
lava_10 = pygame.image.load("images/level/cave/lava/lava_10.png").convert()
lava_11 = pygame.image.load("images/level/cave/lava/lava_11.png").convert()
lava_12 = pygame.image.load("images/level/cave/lava/lava_12.png").convert()
lava_under_wall_01 = pygame.image.load("images/level/cave/lava/lava_06.png").convert()
lava_under_wall_02 = pygame.image.load("images/level/cave/lava/lava_07.png").convert()
lava_under_wall_left = pygame.image.load("images/level/cave/lava/lava_06.png").convert()
lava_under_wall_right = pygame.image.load("images/level/cave/lava/lava_07.png").convert()
lava_images = [lava_01,lava_02,lava_03,lava_04,lava_05,lava_06,lava_07,lava_08,lava_09,lava_10,lava_11,lava_12]
lava_under_wall_images = [lava_under_wall_01,lava_under_wall_02]

###Coastal###
#Straight
lava_border_bottom_01 = pygame.image.load("images/level/cave/lava/coastal/lava_border_bottom_01.png").convert()
lava_border_bottom_02 = pygame.image.load("images/level/cave/lava/coastal/lava_border_bottom_02.png").convert()
lava_border_bottom_images = [lava_border_bottom_01, lava_border_bottom_02]

lava_border_top_01 = pygame.image.load("images/level/cave/lava/coastal/lava_border_top_01.png").convert()
lava_border_top_images = [lava_border_top_01]

lava_border_left = pygame.image.load("images/level/cave/lava/coastal/lava_border_left.png").convert()
lava_border_right = pygame.image.load("images/level/cave/lava/coastal/lava_border_right.png").convert()

#Convex
lava_border_top_left_convex = pygame.image.load("images/level/cave/lava/coastal/convex/lava_border_top_left_convex.png").convert()
lava_border_top_right_convex = pygame.image.load("images/level/cave/lava/coastal/convex/lava_border_top_right_convex.png").convert()
lava_border_bottom_left_convex = pygame.image.load("images/level/cave/lava/coastal/convex/lava_border_bottom_left_convex.png").convert()
lava_border_bottom_right_convex = pygame.image.load("images/level/cave/lava/coastal/convex/lava_border_bottom_right_convex.png").convert()
lava_border_convex_images = [[lava_border_top_left_convex,lava_border_top_right_convex],
                                   [lava_border_bottom_left_convex,lava_border_bottom_right_convex]]

#Concave
lava_border_top_left_concave = pygame.image.load("images/level/cave/lava/coastal/concave/lava_border_top_left_concave.png").convert()
lava_border_top_right_concave = pygame.image.load("images/level/cave/lava/coastal/concave/lava_border_top_right_concave.png").convert()
lava_border_bottom_left_concave = pygame.image.load("images/level/cave/lava/coastal/concave/lava_border_bottom_left_concave.png").convert()
lava_border_bottom_right_concave = pygame.image.load("images/level/cave/lava/coastal/concave/lava_border_bottom_right_concave.png").convert()
lava_border_concave_images = [[lava_border_top_left_concave,lava_border_top_right_concave],
                                   [lava_border_bottom_left_concave,lava_border_bottom_right_concave]]

#######################
##### Wall images #####
#######################
### Basic ###
blank = pygame.image.load("images/level/cave/walls/blank.png").convert()

### Bottom wall lower sections ###
#Under overlay
wall_bottom_lower_hidden_01 = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_hidden_01.png").convert_alpha()
wall_bottom_lower_hidden_02 = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_hidden_02.png").convert_alpha()
wall_bottom_lower_water_01_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_water_01_hidden.png").convert_alpha()
wall_bottom_lower_water_02_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_water_02_hidden.png").convert_alpha()
wall_bottom_lower_left_water_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_left_water_border_hidden.png").convert_alpha()
wall_bottom_lower_right_water_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_right_water_border_hidden.png").convert_alpha()
wall_bottom_lower_lava_01_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_lava_01_hidden.png").convert_alpha()
wall_bottom_lower_lava_02_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_lava_02_hidden.png").convert_alpha()
wall_bottom_lower_left_lava_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_left_lava_border_hidden.png").convert_alpha()
wall_bottom_lower_right_lava_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_bottom_lower_right_lava_border_hidden.png").convert_alpha()

wall_corner_bottom_lower_left_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_left_lower_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_water_concave_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_water_concave_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_water_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_water_convex_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_water_left_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_water_left_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_water_right_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_water_right_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_water_top_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_water_top_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_water_bottom_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_water_bottom_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_floor_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_floor_convex_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_concave_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_concave_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_convex_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_left_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_left_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_right_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_right_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_top_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_top_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_bottom_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_bottom_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_left_lava_floor_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_left_lava_floor_convex_hidden.png").convert_alpha()

wall_corner_bottom_lower_right_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_right_lower_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_water_concave_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_water_concave_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_water_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_water_convex_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_water_left_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_water_left_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_water_right_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_water_right_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_water_top_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_water_top_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_water_bottom_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_water_bottom_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_floor_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_floor_convex_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_concave_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_concave_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_convex_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_left_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_left_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_right_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_right_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_top_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_top_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_bottom_border_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_bottom_border_hidden.png").convert_alpha()
wall_corner_bottom_lower_right_lava_floor_convex_hidden = pygame.image.load("images/level/cave/walls/bottom_ending/lower/hidden/wall_corner_bottom_lower_right_lava_floor_convex_hidden.png").convert_alpha()

wall_bottom_lower_hidden = [wall_bottom_lower_hidden_01, wall_bottom_lower_hidden_02]
wall_bottom_lower_water_hidden = [wall_bottom_lower_water_01_hidden, wall_bottom_lower_water_02_hidden]
wall_bottom_lower_lava_hidden = [wall_bottom_lower_lava_01_hidden, wall_bottom_lower_lava_02_hidden]
wall_corner_bottom_hidden = [wall_corner_bottom_lower_left_hidden, wall_corner_bottom_lower_right_hidden]
wall_bottom_lower_left_water_borders_hidden = [wall_bottom_lower_left_water_border_hidden, wall_corner_bottom_lower_left_water_left_border_hidden, wall_corner_bottom_lower_right_water_left_border_hidden, wall_corner_bottom_lower_left_floor_convex_hidden]
wall_bottom_lower_left_lava_borders_hidden = [wall_bottom_lower_left_lava_border_hidden, wall_corner_bottom_lower_left_lava_left_border_hidden, wall_corner_bottom_lower_right_lava_left_border_hidden, wall_corner_bottom_lower_left_lava_floor_convex_hidden]
wall_bottom_lower_right_water_borders_hidden = [wall_bottom_lower_right_water_border_hidden, wall_corner_bottom_lower_left_water_right_border_hidden, wall_corner_bottom_lower_right_water_right_border_hidden, wall_corner_bottom_lower_right_floor_convex_hidden]
wall_bottom_lower_right_lava_borders_hidden = [wall_bottom_lower_right_lava_border_hidden, wall_corner_bottom_lower_left_lava_right_border_hidden, wall_corner_bottom_lower_right_lava_right_border_hidden, wall_corner_bottom_lower_right_lava_floor_convex_hidden]
wall_corner_bottom_lower_left_gushing_water_hidden = [wall_corner_bottom_lower_left_water_top_border_hidden, wall_corner_bottom_lower_left_water_concave_hidden]
wall_corner_bottom_lower_right_gushing_water_hidden = [wall_corner_bottom_lower_right_water_top_border_hidden, wall_corner_bottom_lower_right_water_concave_hidden]
wall_corner_bottom_lower_left_gushing_lava_hidden = [wall_corner_bottom_lower_left_lava_top_border_hidden, wall_corner_bottom_lower_left_lava_concave_hidden]
wall_corner_bottom_lower_right_gushing_lava_hidden = [wall_corner_bottom_lower_right_lava_top_border_hidden, wall_corner_bottom_lower_right_lava_concave_hidden]

#Overlay
wall_bottom_lower_overlay_01 = pygame.image.load("images/level/cave/walls/bottom_ending/lower/overlay/wall_bottom_lower_01.png").convert_alpha()
wall_bottom_lower_overlay_02 = pygame.image.load("images/level/cave/walls/bottom_ending/lower/overlay/wall_bottom_lower_02.png").convert_alpha()
wall_corner_bottom_left_lower_overlay = pygame.image.load("images/level/cave/walls/bottom_ending/lower/overlay/wall_corner_bottom_left_lower.png").convert_alpha()
wall_corner_bottom_right_lower_overlay = pygame.image.load("images/level/cave/walls/bottom_ending/lower/overlay/wall_corner_bottom_right_lower.png").convert_alpha()
wall_bottom_lower_overlay = [wall_bottom_lower_overlay_01, wall_bottom_lower_overlay_02]

### Bottom wall middle sections ###
#Overlay
wall_bottom_middle_overlay_01 = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_01.png").convert()
wall_bottom_middle_overlay_02 = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_02.png").convert()
wall_bottom_middle_left_overlay = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_left.png").convert()
wall_bottom_middle_right_overlay = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_right.png").convert()
wall_bottom_middle_primary_01 = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_primary_01.png").convert_alpha()
wall_bottom_middle_primary_02 = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_primary_02.png").convert_alpha()
wall_bottom_middle_left_primary = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_left_primary.png").convert_alpha()
wall_bottom_middle_right_primary = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_right_primary.png").convert_alpha()
wall_bottom_middle_secondary_01 = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_secondary_01.png").convert_alpha()
wall_bottom_middle_secondary_02 = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_secondary_02.png").convert_alpha()
wall_bottom_middle_left_secondary = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_left_secondary.png").convert_alpha()
wall_bottom_middle_right_secondary = pygame.image.load("images/level/cave/walls/bottom_ending/middle/overlay/wall_bottom_middle_right_secondary.png").convert_alpha()

wall_bottom_middle_left_overlay.set_colorkey((255,0,0))
wall_bottom_middle_right_overlay.set_colorkey((255,0,0))
wall_bottom_middle_overlay = [wall_bottom_middle_overlay_01, wall_bottom_middle_overlay_02]
wall_bottom_middle_primary_overlay = [wall_bottom_middle_primary_01, wall_bottom_middle_primary_02]

### Bottom wall upper sections ###
#Overlay
wall_bottom_upper_overlay_01 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_01.png").convert()
wall_bottom_upper_overlay_02 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_02.png").convert()
wall_bottom_upper_overlay_03 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_03.png").convert()
wall_bottom_upper_overlay_04 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_04.png").convert()
wall_bottom_upper_overlay_05 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_05.png").convert()
wall_bottom_left_upper_overlay = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_left_upper.png").convert()
wall_bottom_right_upper_overlay = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_right_upper.png").convert()
wall_bottom_upper_primary_01 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_primary_01.png").convert_alpha()
wall_bottom_upper_primary_02 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_primary_02.png").convert_alpha()
wall_bottom_upper_primary_03 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_primary_03.png").convert_alpha()
wall_bottom_upper_primary_04 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_primary_04.png").convert_alpha()
wall_bottom_upper_primary_05 = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_upper_primary_05.png").convert_alpha()
wall_bottom_left_upper_primary = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_left_upper_primary.png").convert_alpha()
wall_bottom_right_upper_primary = pygame.image.load("images/level/cave/walls/bottom_ending/upper/overlay/wall_bottom_right_upper_primary.png").convert_alpha()
wall_bottom_upper_overlay = [wall_bottom_upper_overlay_01, wall_bottom_upper_overlay_02, wall_bottom_upper_overlay_03, wall_bottom_upper_overlay_04, wall_bottom_upper_overlay_05]
wall_bottom_upper_primary = [wall_bottom_upper_primary_01, wall_bottom_upper_primary_02, wall_bottom_upper_primary_03, wall_bottom_upper_primary_04, wall_bottom_upper_primary_05]
wall_bottom_left_upper_overlay.set_colorkey((255,0,0))
wall_bottom_right_upper_overlay.set_colorkey((255,0,0))

### Top wall sections ###
#Under overlay
wall_top_floor_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_floor_01.png").convert()
wall_top_floor_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_floor_02.png").convert()
wall_top_water_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_water_01.png").convert()
wall_top_water_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_water_02.png").convert()
wall_top_water_left_border_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_water_left_border_01.png").convert()
wall_top_water_left_border_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_water_left_border_02.png").convert()
wall_top_water_right_border_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_water_right_border_01.png").convert()
wall_top_water_right_border_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_water_right_border_02.png").convert()
wall_top_lava_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_lava_01.png").convert()
wall_top_lava_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_lava_02.png").convert()
wall_top_lava_left_border_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_lava_left_border_01.png").convert()
wall_top_lava_left_border_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_lava_left_border_02.png").convert()
wall_top_lava_right_border_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_lava_right_border_01.png").convert()
wall_top_lava_right_border_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_lava_right_border_02.png").convert()

wall_top_left_convex_floor = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_floor.png").convert()
wall_top_left_convex_water_concave = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_concave.png").convert()
wall_top_left_convex_water_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_convex.png").convert()
wall_top_left_convex_water_floor_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_floor_convex.png").convert()
wall_top_left_convex_water_bottom_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_bottom_border.png").convert()
wall_top_left_convex_water_left_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_left_border.png").convert()
wall_top_left_convex_water_right_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_right_border.png").convert()
wall_top_left_convex_water_top_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_water_top_border.png").convert()
wall_top_left_convex_lava_concave = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_concave.png").convert()
wall_top_left_convex_lava_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_convex.png").convert()
wall_top_left_convex_lava_floor_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_floor_convex.png").convert()
wall_top_left_convex_lava_bottom_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_bottom_border.png").convert()
wall_top_left_convex_lava_left_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_left_border.png").convert()
wall_top_left_convex_lava_right_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_right_border.png").convert()
wall_top_left_convex_lava_top_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_left_convex_lava_top_border.png").convert()

wall_top_right_convex_floor = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_floor.png").convert()
wall_top_right_convex_water_concave = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_concave.png").convert()
wall_top_right_convex_water_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_convex.png").convert()
wall_top_right_convex_water_floor_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_floor_convex.png").convert()
wall_top_right_convex_water_bottom_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_bottom_border.png").convert()
wall_top_right_convex_water_left_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_left_border.png").convert()
wall_top_right_convex_water_right_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_right_border.png").convert()
wall_top_right_convex_water_top_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_water_top_border.png").convert()
wall_top_right_convex_lava_concave = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_concave.png").convert()
wall_top_right_convex_lava_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_convex.png").convert()
wall_top_right_convex_lava_floor_convex = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_floor_convex.png").convert()
wall_top_right_convex_lava_bottom_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_bottom_border.png").convert()
wall_top_right_convex_lava_left_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_left_border.png").convert()
wall_top_right_convex_lava_right_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_right_border.png").convert()
wall_top_right_convex_lava_top_border = pygame.image.load("images/level/cave/walls/top_and_side/top/hidden/wall_top_right_convex_lava_top_border.png").convert()

wall_top_floor = [wall_top_floor_01, wall_top_floor_02]
wall_top_water = [wall_top_water_01, wall_top_water_02]
wall_top_water_left_border = [wall_top_water_left_border_01, wall_top_water_left_border_02]
wall_top_water_right_border = [wall_top_water_right_border_01, wall_top_water_right_border_02]
wall_top_lava = [wall_top_lava_01, wall_top_lava_02]
wall_top_lava_left_border = [wall_top_lava_left_border_01, wall_top_lava_left_border_02]
wall_top_lava_right_border = [wall_top_lava_right_border_01, wall_top_lava_right_border_02]

#Overlay
wall_top_overlay_01 = pygame.image.load("images/level/cave/walls/top_and_side/top/overlay/wall_top_01.png").convert()
wall_top_overlay_02 = pygame.image.load("images/level/cave/walls/top_and_side/top/overlay/wall_top_01.png").convert()
wall_top_left_convex_overlay = pygame.image.load("images/level/cave/walls/top_and_side/top/overlay/wall_top_left_convex.png").convert()
wall_top_right_convex_overlay = pygame.image.load("images/level/cave/walls/top_and_side/top/overlay/wall_top_right_convex.png").convert()
wall_top_overlay_01.set_colorkey((255,0,0))
wall_top_overlay_02.set_colorkey((255,0,0))
wall_top_left_convex_overlay.set_colorkey((255,0,0))
wall_top_right_convex_overlay.set_colorkey((255,0,0))
wall_top_overlay = [wall_top_overlay_01, wall_top_overlay_02]

### Side wall sections ###
#Under overlay
wall_left_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_01.png").convert()
wall_left_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_02.png").convert()
wall_left_03 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_03.png").convert()
wall_left_04 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_04.png").convert()
wall_right_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_01.png").convert()
wall_right_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_02.png").convert()
wall_right_03 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_03.png").convert()
wall_right_04 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_04.png").convert()

wall_left_primary_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_primary_01.png").convert_alpha()
wall_right_primary_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_primary_01.png").convert_alpha()

wall_left_water_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_water_01.png").convert()
wall_left_water_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_water_02.png").convert()
wall_right_water_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_water_01.png").convert()
wall_right_water_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_water_02.png").convert()
wall_left_lava_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_lava_01.png").convert()
wall_left_lava_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_lava_02.png").convert()
wall_right_lava_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_lava_01.png").convert()
wall_right_lava_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_lava_02.png").convert()

wall_left_water_border_bottom = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_water_border_bottom.png").convert()
wall_left_water_border_top = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_water_border_top.png").convert()
wall_right_water_border_bottom = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_water_border_bottom.png").convert()
wall_right_water_border_top = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_water_border_top.png").convert()
wall_left_lava_border_bottom = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_lava_border_bottom.png").convert()
wall_left_lava_border_top = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_left_lava_border_top.png").convert()
wall_right_lava_border_bottom = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_lava_border_bottom.png").convert()
wall_right_lava_border_top = pygame.image.load("images/level/cave/walls/top_and_side/side/hidden/wall_right_lava_border_top.png").convert()

wall_left = [wall_left_01, wall_left_02, wall_left_03, wall_left_04]
wall_right = [wall_right_01, wall_right_02, wall_right_03, wall_right_04]
wall_left_water = [wall_left_water_01, wall_left_water_02]
wall_right_water = [wall_right_water_01, wall_right_water_02]
wall_left_lava = [wall_left_lava_01, wall_left_lava_02]
wall_right_lava = [wall_right_lava_01, wall_right_lava_02]

#Overlay
wall_left_overlay_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_left_01.png").convert()
wall_left_overlay_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_left_02.png").convert()
wall_left_overlay_03 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_left_03.png").convert()
wall_left_overlay_04 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_left_04.png").convert()
wall_right_overlay_01 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_right_01.png").convert()
wall_right_overlay_02 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_right_02.png").convert()
wall_right_overlay_03 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_right_03.png").convert()
wall_right_overlay_04 = pygame.image.load("images/level/cave/walls/top_and_side/side/overlay/wall_right_04.png").convert()
wall_left_overlay = [wall_left_overlay_01, wall_left_overlay_02, wall_left_overlay_03, wall_left_overlay_04]
wall_right_overlay = [wall_right_overlay_01, wall_right_overlay_02, wall_right_overlay_03, wall_right_overlay_04]

for img in wall_left_overlay:
    img.set_colorkey((255,0,0))

for img in wall_right_overlay:
    img.set_colorkey((255,0,0))

### Concave wall sections ###
#Under overlay
wall_top_left_concave_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_top_left_concave_hidden.png").convert()
wall_top_right_concave_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_top_right_concave_hidden.png").convert()
wall_bottom_left_concave_floor_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_bottom_left_concave_floor_hidden.png").convert()
wall_bottom_right_concave_floor_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_bottom_right_concave_floor_hidden.png").convert()
wall_bottom_left_concave_water_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_bottom_left_concave_water_hidden.png").convert()
wall_bottom_right_concave_water_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_bottom_right_concave_water_hidden.png").convert()
wall_bottom_left_concave_lava_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_bottom_left_concave_lava_hidden.png").convert()
wall_bottom_right_concave_lava_hidden = pygame.image.load("images/level/cave/walls/concave/hidden/wall_bottom_right_concave_lava_hidden.png").convert()

#Overlay
wall_corner_lower_right_concave_overlay = pygame.image.load("images/level/cave/walls/concave/overlay/wall_corner_lower_right_concave.png").convert()
wall_corner_lower_left_concave_overlay = pygame.image.load("images/level/cave/walls/concave/overlay/wall_corner_lower_left_concave.png").convert()
wall_corner_lower_left_concave_overlay.set_colorkey((255,0,0))
wall_corner_lower_right_concave_overlay.set_colorkey((255,0,0))
