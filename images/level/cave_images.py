import pygame

'''
legend:
E level_entrance
Q level_exit
X wall
~ water
  floor
. floor_debree_01
, floor_debree_02
; floor_debree_03
: floor_debree_04
- floor_debree_05
_ floor_debree_06
O floor_pit_01
Q floor_pit_02
0 floor_pit_03
+ cross_crack
* web_crack
` corner_crack
'''

character_walk_east1       = pygame.image.load("images/characters/ettin/east_01.png").convert_alpha()