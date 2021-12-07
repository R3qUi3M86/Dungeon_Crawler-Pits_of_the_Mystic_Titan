import pygame
from utilities.constants import *

########################
### Weapons and ammo ###
########################
### Sword
sword = pygame.image.load("images/ui/ammo_counter/sword.png").convert_alpha()

### Emerald crossbow
emerald_crossbow = pygame.image.load("images/items/weapons_and_ammo/emerald_crossbow/crossbow.png").convert_alpha()
crossbow_quiver_01 = pygame.image.load("images/items/weapons_and_ammo/emerald_crossbow/crossbow_quiver_01.png").convert_alpha()
crossbow_quiver_02 = pygame.image.load("images/items/weapons_and_ammo/emerald_crossbow/crossbow_quiver_02.png").convert_alpha()
crossbow_quiver_03 = pygame.image.load("images/items/weapons_and_ammo/emerald_crossbow/crossbow_quiver_03.png").convert_alpha()
crossbow_bolts = pygame.image.load("images/items/weapons_and_ammo/emerald_crossbow/crossbow_bolts.png").convert_alpha()

crossbow_quiver = [crossbow_quiver_01,crossbow_quiver_02,crossbow_quiver_03]

###################
### Consumables ###
###################
### Quartz flask
quartz_flask_01 = pygame.image.load("images/items/consumables/quartz_flask/quartz_flask_01.png").convert_alpha()
quartz_flask_02 = pygame.image.load("images/items/consumables/quartz_flask/quartz_flask_02.png").convert_alpha()
quartz_flask_03 = pygame.image.load("images/items/consumables/quartz_flask/quartz_flask_03.png").convert_alpha()

quartz_flask = [quartz_flask_01,quartz_flask_02,quartz_flask_03]

###################
### Decorations ###
###################
### Torch
torch_01 = pygame.image.load("images/items/decor/torch/torch_01.png").convert_alpha()
torch_02 = pygame.image.load("images/items/decor/torch/torch_02.png").convert_alpha()
torch_03 = pygame.image.load("images/items/decor/torch/torch_03.png").convert_alpha()
torch_04 = pygame.image.load("images/items/decor/torch/torch_04.png").convert_alpha()
torch_05 = pygame.image.load("images/items/decor/torch/torch_05.png").convert_alpha()
torch_06 = pygame.image.load("images/items/decor/torch/torch_06.png").convert_alpha()
torch_07 = pygame.image.load("images/items/decor/torch/torch_07.png").convert_alpha()
torch_08 = pygame.image.load("images/items/decor/torch/torch_08.png").convert_alpha()
torch_light_source = pygame.image.load("images/items/decor/torch/light_source.png").convert_alpha()

wall_torch_images = [torch_01, torch_02, torch_03, torch_04, torch_05, torch_06, torch_07, torch_08]

                     #Weapons
STATIC_IMAGE_DICT = {SWORD:sword, EMERALD_CROSSBOW:emerald_crossbow,
                     ETTIN_MACE:sword, BISHOP_MAGIC_MISSILE:sword, 
                     #Ammo
                     EMERALD_CROSSBOW_QUIVER:crossbow_quiver_01, EMERALD_CROSSBOW_BOLTS:crossbow_bolts, 
                     #Consumables
                     QUARTZ_FLASK:quartz_flask_01,
                     #Decor
                     WALL_TORCH:torch_01}

ANIMATED_ITEMS = [EMERALD_CROSSBOW_QUIVER, QUARTZ_FLASK, WALL_TORCH]
ANIMATED_ITEM_IMAGES = {WALL_TORCH:wall_torch_images, EMERALD_CROSSBOW_QUIVER:crossbow_quiver, QUARTZ_FLASK:quartz_flask}