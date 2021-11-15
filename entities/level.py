import pygame
from settings import *

level_map = [
"XXEEEXXXXXXXXXXXXXXXXX",
"XXEEEXXXXXXX XXXX  XXX",
"XXEEEXXXXX  ; XX  XXXX",
"XXEEEXXXXXXXX XX  XX X",
"X        XXXX.    XX X",
"X  ,    :XXXX   ``   X",
"XXQ       0     ``XXXX",
"XX   .     -    + XXXX",
"XX    ~~    XX    XXXX",
"X  _  ~~  O XX    *  X",
"X    XXX  . XX  ~~,  X",
"X   XXXX       ~~~   X",
"XX  XXXX~~~~~ ~~~~~XXX",
"XX  XXXX~~~~~ ~~~~~XXX",
"XXXXXXX~~*        ~XXX",
"XXXXXX    ~~~      XXX", 
"XQQQXX  `XXX~~~~ ~~~XX",
"XQQQXX  `XXX~~~~ ~~~~X",
"XQQQX.   XXXX~~  ~~ ~X",
"X        XXXX~~~    ~X",
"XXXXXXXXXXXXX~~~~ ~~~X",
"XXXXXXXXXXXXX~~~~~~~~X"     
]

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


test_surface = pygame.image.load("images/map/cave/test.png").convert()

test_surface_scaled = pygame.transform.scale(test_surface, (2400,1800))