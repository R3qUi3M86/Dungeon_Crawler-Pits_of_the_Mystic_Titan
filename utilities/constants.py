from settings import *

PLAYER_ID = -1

X = 0
Y = 1

PLAYER = "player"
MONSTER = "monster"
ENTITY = "entity"
PROJECTILE = "projectile"
COLLISION_TILE = "collison_tile"
ITEM = "item"
TILE = "tile"
ETTIN = "ettin"

DIRECT = "direct"
FAR = "far"

HIT = True
MISS = False

SIZE_SMALL = 'small'
SIZE_MEDIUM = "medium"

#Colliders
MELEE_SECTOR = "melee sector"
ENTITY_OMNI = "movement omni"
ENTITY_SECTOR = "movement sector"
SQUARE = "square"

#Sector names
SECTOR_E = 0
SECTOR_NE = 1
SECTOR_N = 2
SECTOR_NW = 3
SECTOR_W = 4
SECTOR_SW = 5
SECTOR_S = 6
SECTOR_SE = 7
SECTORS = [SECTOR_E,SECTOR_NE,SECTOR_N,SECTOR_NW,SECTOR_W,SECTOR_SW,SECTOR_S,SECTOR_SE]

HORIZONTAL = "horizontal"
VERTICAL = "vertical"