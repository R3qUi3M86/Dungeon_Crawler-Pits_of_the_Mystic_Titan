import pygame

TILE_SIZE = 48
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

PLAYER_SHADOW_ID = -1
PLAYER_POSITION = 600,400
PLAYER_SPRITE_POSITION = 600,411
PLAYER_MELEE_E_SECTOR_POSITION = 630,400
PLAYER_MELEE_NE_SECTOR_POSITION = 620,387
PLAYER_MELEE_N_SECTOR_POSITION = 600,380
PLAYER_MELEE_NW_SECTOR_POSITION = 580,387
PLAYER_MELEE_W_SECTOR_POSITION = 570,400
PLAYER_MELEE_SW_SECTOR_POSITION = 580,413
PLAYER_MELEE_S_SECTOR_POSITION = 600,420
PLAYER_MELEE_SE_SECTOR_POSITION = 620,413

X = 0
Y = 1

CHARACTER_SPRITE_INDEX = 9

PLAYER = "player"
ETTIN = "ettin"

SIZE_SMALL = 'small'
SIZE_MEDIUM_SMALL = 'medium_small'
SIZE_MEDIUM = "medium"

SECTOR_N = "North"
SECTOR_S = "South"
SECTOR_E = "East"
SECTOR_W = "West"
SECTOR_NW = "North_West"
SECTOR_NE = "North_East"
SECTOR_SW = "South_West"
SECTOR_SE = "South_East"
SECTORS = [SECTOR_N,SECTOR_S,SECTOR_E,SECTOR_W,SECTOR_NW,SECTOR_NE,SECTOR_SW,SECTOR_SE]

HORIZONTAL = "horizontal"
VERTICAL = "vertical"