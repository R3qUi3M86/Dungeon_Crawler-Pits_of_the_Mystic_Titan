import pygame
from settings import *

#Main light
central_light1 = pygame.image.load("images/ui/light_source1.png").convert_alpha()
central_light2 = pygame.image.load("images/ui/light_source2.png").convert_alpha()
central_light3 = pygame.image.load("images/ui/light_source3.png").convert_alpha()
central_light4 = pygame.image.load("images/ui/light_source4.png").convert_alpha()
central_light5 = pygame.image.load("images/ui/light_source5.png").convert_alpha()
central_light6 = pygame.image.load("images/ui/light_source6.png").convert_alpha()
central_light7 = pygame.image.load("images/ui/light_source7.png").convert_alpha()

#Wall hider
wall_hider_mask = pygame.image.load("images/ui/wall_hider_mask.png").convert_alpha()
wall_hider_mask2 = pygame.image.load("images/ui/wall_hider_mask2.png").convert_alpha()

#Health bar
health_bar_empty = pygame.image.load("images/ui/health_bar/empty_bar.png").convert_alpha()
health_bar_health = pygame.image.load("images/ui/health_bar/health.png").convert_alpha()
health_bar_health_mask = pygame.image.load("images/ui/health_bar/health_mask.png").convert_alpha()
inner_shadow = pygame.image.load("images/ui/health_bar/inner_shadow.png").convert_alpha()

#Ammo counter
ammo_counter_overlay = pygame.image.load("images/ui/ammo_counter/ammo_counter.png").convert_alpha()
ammo_counter_overlay2 = pygame.image.load("images/ui/ammo_counter/ammo_counter2.png").convert_alpha()
sword_inv = pygame.image.load("images/ui/ammo_counter/sword.png").convert_alpha()
crossbow_inv = pygame.image.load("images/ui/ammo_counter/crossbow.png").convert_alpha()
inventory_weapons = [sword_inv, crossbow_inv]
infinity_sign = pygame.image.load("images/ui/ammo_counter/infinity.png").convert_alpha()

#Consumables counter
consumable_counter_overlay = pygame.image.load("images/ui/consumables/consumable_gui.png").convert_alpha()
consumable_use_01 = pygame.image.load("images/ui/consumables/consumable_use_01.png").convert_alpha()
consumable_use_02 = pygame.image.load("images/ui/consumables/consumable_use_02.png").convert_alpha()
consumable_use_03 = pygame.image.load("images/ui/consumables/consumable_use_03.png").convert_alpha()
consumable_use_04 = pygame.image.load("images/ui/consumables/consumable_use_04.png").convert_alpha()
health_potion_inv = pygame.image.load("images/ui/consumables/healh_potion.png").convert_alpha()
consumable_use = [consumable_use_01,consumable_use_02,consumable_use_03,consumable_use_04]
inventory_consumables = [health_potion_inv]

