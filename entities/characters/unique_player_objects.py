import pygame
from entities import melee_range
from entities import shadow
from entities.characters import player
from utilities.constants import *

HERO = player.Hero(player_position)

PLAYER_MELEE_SPRITE_E  = melee_range.Melee(player_position, SECTOR_E)
PLAYER_MELEE_SPRITE_NE = melee_range.Melee(player_position, SECTOR_NE)
PLAYER_MELEE_SPRITE_N  = melee_range.Melee(player_position, SECTOR_N)
PLAYER_MELEE_SPRITE_NW = melee_range.Melee(player_position, SECTOR_NW)
PLAYER_MELEE_SPRITE_W  = melee_range.Melee(player_position, SECTOR_W)
PLAYER_MELEE_SPRITE_SW = melee_range.Melee(player_position, SECTOR_SW)
PLAYER_MELEE_SPRITE_S  = melee_range.Melee(player_position, SECTOR_S)
PLAYER_MELEE_SPRITE_SE = melee_range.Melee(player_position, SECTOR_SE)
PLAYER_SHADOW_SPRITE   = HERO.shadow

PLAYER_MELEE_SPRITES = [PLAYER_MELEE_SPRITE_E,PLAYER_MELEE_SPRITE_NE,PLAYER_MELEE_SPRITE_N,PLAYER_MELEE_SPRITE_NW,PLAYER_MELEE_SPRITE_W,PLAYER_MELEE_SPRITE_SW,PLAYER_MELEE_SPRITE_S,PLAYER_MELEE_SPRITE_SE]

HERO_SPRITE_GROUP = pygame.sprite.GroupSingle(HERO)
HERO_MELEE_SECTOR_SPRITE_GROUP = pygame.sprite.Group(PLAYER_MELEE_SPRITES)
PLAYER_SHADOW_SPRITE_GROUP = pygame.sprite.GroupSingle(PLAYER_SHADOW_SPRITE)