import pygame
from utilities.constants import *

################
### Currency ###
################
### Gold
gold_01 = pygame.image.load("images/items/currency/gold/gold_01.png").convert_alpha()
gold_02 = pygame.image.load("images/items/currency/gold/gold_02.png").convert_alpha()
gold_03 = pygame.image.load("images/items/currency/gold/gold_03.png").convert_alpha()
gold_04 = pygame.image.load("images/items/currency/gold/gold_04.png").convert_alpha()
gold_05 = pygame.image.load("images/items/currency/gold/gold_05.png").convert_alpha()
gold_06 = pygame.image.load("images/items/currency/gold/gold_06.png").convert_alpha()
gold_07 = pygame.image.load("images/items/currency/gold/gold_07.png").convert_alpha()

gold_coins = [gold_01,gold_02,gold_03,gold_04,gold_05,gold_06,gold_07]

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

### Necrolight
necrolight = pygame.image.load("images/items/weapons_and_ammo/necrolight/necrolight.png").convert_alpha()
necrolight_small_ammo_01 = pygame.image.load("images/items/weapons_and_ammo/necrolight/small_ammo_01.png").convert_alpha()
necrolight_small_ammo_02 = pygame.image.load("images/items/weapons_and_ammo/necrolight/small_ammo_02.png").convert_alpha()
necrolight_large_ammo_01 = pygame.image.load("images/items/weapons_and_ammo/necrolight/large_ammo_01.png").convert_alpha()
necrolight_large_ammo_02 = pygame.image.load("images/items/weapons_and_ammo/necrolight/large_ammo_02.png").convert_alpha()

necrolight_small_ammo = [necrolight_small_ammo_01,necrolight_small_ammo_02]
necrolight_large_ammo = [necrolight_large_ammo_01,necrolight_large_ammo_02]

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

### Flame Pedestal1
flame_pedestal1_01 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_01.png").convert_alpha()
flame_pedestal1_02 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_02.png").convert_alpha()
flame_pedestal1_03 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_03.png").convert_alpha()
flame_pedestal1_04 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_04.png").convert_alpha()
flame_pedestal1_05 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_05.png").convert_alpha()
flame_pedestal1_06 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_06.png").convert_alpha()
flame_pedestal1_07 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_07.png").convert_alpha()
flame_pedestal1_08 = pygame.image.load("images/items/decor/flame_pedestal1/pedestal_08.png").convert_alpha()

flame_pedestal1_images = [flame_pedestal1_01,flame_pedestal1_02,flame_pedestal1_03,flame_pedestal1_04,flame_pedestal1_05,flame_pedestal1_06,flame_pedestal1_07,flame_pedestal1_08]

### Sculpture1
sculpture1 = pygame.image.load("images/items/decor/sculpture1/sculpture_01.png").convert_alpha()

### Vase
vase_01 = pygame.image.load("images/items/decor/vase/vase_01.png").convert_alpha()
vase_02 = pygame.image.load("images/items/decor/vase/vase_02.png").convert_alpha()
vase_03 = pygame.image.load("images/items/decor/vase/vase_03.png").convert_alpha()
vase_01_destruct_01 = pygame.image.load("images/items/decor/vase/vase_01_destruct_01.png").convert_alpha()
vase_01_destruct_02 = pygame.image.load("images/items/decor/vase/vase_01_destruct_02.png").convert_alpha()
vase_01_destruct_03 = pygame.image.load("images/items/decor/vase/vase_01_destruct_03.png").convert_alpha()
vase_01_destruct_04 = pygame.image.load("images/items/decor/vase/vase_01_destruct_04.png").convert_alpha()
vase_01_destruct_05 = pygame.image.load("images/items/decor/vase/vase_01_destruct_05.png").convert_alpha()
vase_01_destruct_06 = pygame.image.load("images/items/decor/vase/vase_01_destruct_06.png").convert_alpha()
vase_01_destruct_07 = pygame.image.load("images/items/decor/vase/vase_01_destruct_07.png").convert_alpha()

vase_01_destruct = [vase_01_destruct_01,vase_01_destruct_02,vase_01_destruct_03,vase_01_destruct_04,vase_01_destruct_05,vase_01_destruct_06,vase_01_destruct_07]

                     #Weapons
STATIC_IMAGE_DICT = {SWORD:sword, EMERALD_CROSSBOW:emerald_crossbow, NECROLIGHT:necrolight,
                     ETTIN_MACE:sword, BISHOP_MAGIC_MISSILE:sword, SPIKE_BALL_SPELL:sword, WHIRLWIND_SPELL:sword, RED_ORB_SPELL:sword,
                     #Ammo
                     EMERALD_CROSSBOW_QUIVER:crossbow_quiver_01, EMERALD_CROSSBOW_BOLTS:crossbow_bolts,
                     NECRO_SMALL_AMMO:necrolight_small_ammo_01, NECRO_LARGE_AMMO:necrolight_large_ammo_01,
                     #Consumables
                     QUARTZ_FLASK:quartz_flask_01,
                     #Decor
                     WALL_TORCH:torch_01, VASE:vase_01, FLAME_PEDESTAL1:flame_pedestal1_01, SCULPTURE1:sculpture1,
                     #Currency
                     GOLD_COINS:gold_01}

ANIMATED_ITEMS = [EMERALD_CROSSBOW_QUIVER,
                  QUARTZ_FLASK, 
                  WALL_TORCH, 
                  FLAME_PEDESTAL1, 
                  GOLD_COINS, 
                  NECRO_SMALL_AMMO, 
                  NECRO_LARGE_AMMO]

ANIMATED_ITEM_IMAGES = {WALL_TORCH:wall_torch_images, 
                        FLAME_PEDESTAL1:flame_pedestal1_images, 
                        NECRO_SMALL_AMMO:necrolight_small_ammo, 
                        NECRO_LARGE_AMMO:necrolight_large_ammo, 
                        EMERALD_CROSSBOW_QUIVER:crossbow_quiver, 
                        QUARTZ_FLASK:quartz_flask, 
                        GOLD_COINS:gold_coins}

DESTRUCTIBLE_ITEMS = [VASE]
DESTRUCTIBLE_ITEM_IMAGES = {VASE:vase_01_destruct}
