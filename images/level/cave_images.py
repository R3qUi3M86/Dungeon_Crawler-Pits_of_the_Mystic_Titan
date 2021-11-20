import pygame

###########################################
###### Level entrance and exit images #####
###########################################
###Common###
level_entrance_and_exit_top_left = pygame.image.load("images/level/cave/entrance_and_exit/top_left.png").convert_alpha()
level_entrance_and_exit_top_mid = pygame.image.load("images/level/cave/entrance_and_exit/top_mid.png").convert_alpha()
level_entrance_and_exit_top_right = pygame.image.load("images/level/cave/entrance_and_exit/top_right.png").convert_alpha()

###Entrance###
level_entrance_mid_left = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_mid_left.png").convert_alpha()
level_entrance_mid_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_mid_mid.png").convert_alpha()
level_entrance_mid_right = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_mid_right.png").convert_alpha()
level_entrance_bottom_left = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_bottom_left.png").convert_alpha()
level_entrance_bottom_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_bottom_mid.png").convert_alpha()
level_entrance_bottom_right = pygame.image.load("images/level/cave/entrance_and_exit/level_entrance_bottom_right.png").convert_alpha()
level_entrance_images = [[level_entrance_and_exit_top_left,level_entrance_and_exit_top_mid,level_entrance_and_exit_top_right],
                         [level_entrance_mid_left,level_entrance_mid_mid,level_entrance_mid_right],
                         [level_entrance_bottom_left,level_entrance_bottom_mid,level_entrance_bottom_right]]

###Exit###
level_exit_mid_left = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_mid_left.png").convert_alpha()
level_exit_mid_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_mid_mid.png").convert_alpha()
level_exit_mid_right = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_mid_right.png").convert_alpha()
level_exit_bottom_left = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_bottom_left.png").convert_alpha()
level_exit_bottom_mid = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_bottom_mid.png").convert_alpha()
level_exit_bottom_right = pygame.image.load("images/level/cave/entrance_and_exit/level_exit_bottom_right.png").convert_alpha()
level_exit_images = [[level_entrance_and_exit_top_left,level_entrance_and_exit_top_mid,level_entrance_and_exit_top_right],
                     [level_exit_mid_left,level_exit_mid_mid,level_exit_mid_right],
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

######################
##### Pit images #####
######################
pit_01 = pygame.image.load("images/level/cave/floors/pits/floor_pit_01.png").convert_alpha()
pit_02 = pygame.image.load("images/level/cave/floors/pits/floor_pit_02.png").convert_alpha()
pit_03 = pygame.image.load("images/level/cave/floors/pits/floor_pit_03.png").convert_alpha()
pit_tile_images = [pit_01,pit_02,pit_03]

##############################
###### Blue water images #####
##############################
###Lake###
blue_water_01 = pygame.image.load("images/level/cave/blue_water/blue_water_01.png").convert_alpha()
blue_water_02 = pygame.image.load("images/level/cave/blue_water/blue_water_02.png").convert_alpha()
blue_water_03 = pygame.image.load("images/level/cave/blue_water/blue_water_03.png").convert_alpha()
blue_water_04 = pygame.image.load("images/level/cave/blue_water/blue_water_04.png").convert_alpha()

###Coastal###
#Straight
blue_water_border_bottom_01 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_01.png").convert_alpha()
blue_water_border_bottom_02 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_02.png").convert_alpha()
blue_water_border_bottom_03 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_03.png").convert_alpha()
blue_water_border_bottom_04 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_bottom_04.png").convert_alpha()
blue_water_border_bottom_images = [blue_water_border_bottom_01,blue_water_border_bottom_02,blue_water_border_bottom_03,blue_water_border_bottom_04]

blue_water_border_top_01 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_01.png").convert_alpha()
blue_water_border_top_02 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_02.png").convert_alpha()
blue_water_border_top_03 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_03.png").convert_alpha()
blue_water_border_top_04 = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_top_04.png").convert_alpha()
blue_water_border_top_images = [blue_water_border_top_01,blue_water_border_top_02,blue_water_border_top_03,blue_water_border_top_04]

blue_water_border_left = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_left.png").convert_alpha()
blue_water_border_right = pygame.image.load("images/level/cave/blue_water/coastal/blue_water_border_right.png").convert_alpha()

#Convex
blue_water_border_top_left_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_top_left_convex.png").convert_alpha()
blue_water_border_top_right_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_top_right_convex.png").convert_alpha()
blue_water_border_bottom_left_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_bottom_left_convex.png").convert_alpha()
blue_water_border_bottom_right_convex = pygame.image.load("images/level/cave/blue_water/coastal/convex/blue_water_border_bottom_right_convex.png").convert_alpha()
blue_water_border_convex_images = [[blue_water_border_top_left_convex,blue_water_border_top_right_convex],
                                   [blue_water_border_bottom_left_convex,blue_water_border_bottom_right_convex]]

#Concave
blue_water_border_top_left_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_top_left_concave.png").convert_alpha()
blue_water_border_top_right_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_top_right_concave.png").convert_alpha()
blue_water_border_bottom_left_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_bottom_left_concave.png").convert_alpha()
blue_water_border_bottom_right_concave = pygame.image.load("images/level/cave/blue_water/coastal/concave/blue_water_border_bottom_right_concave.png").convert_alpha()
blue_water_border_concave_images = [[blue_water_border_top_left_concave,blue_water_border_top_right_concave],
                                   [blue_water_border_bottom_left_concave,blue_water_border_bottom_right_concave]]

#######################
##### Wall images #####
#######################
### Only floor in vicinity ###
#Basic
blank = pygame.image.load("images/level/cave/walls/blank.png").convert_alpha()



