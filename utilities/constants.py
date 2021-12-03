from settings import *

PLAYER_ID = -1

X = 0
Y = 1

PLAYER = "player"
MONSTER = "monster"
ENTITY = "entity"
SHADOW = "shadow"
ITEM = "item"
PROJECTILE = "projectile"
TILE = "tile"
COLLISION_TILE = "collison_tile"

#Tile types
ENTRANCE = "E" 
EXIT = "N"
WALL = "X"
WATER = "~"
FLOOR = " "
FLOOR_PIT = "O"
SIMPLE_CRACK = "*"
CORNER_CRACK = "`"

#Tile painting mode
VISIBLE = "visible"
HIDDEN = "hidden"
PRIMARY_OVERLAY = "primary_overlay"
SECONDARY_OVERLAY = "secondary_overlay"

IMPASSABLE_TILES = [ENTRANCE,EXIT,WALL,WATER,FLOOR_PIT]
PASSABLE_TILES = [FLOOR,SIMPLE_CRACK,CORNER_CRACK]
WALL_LIKE = [ENTRANCE,EXIT,WALL]
FLOOR_LIKE = [FLOOR, FLOOR_PIT, SIMPLE_CRACK, CORNER_CRACK]

#Monsters
ETTIN = "ettin"

MONSTER_IMAGE_DISPLAY_CORRECTION = {ETTIN:12}

###Items###
#Weapons
SWORD = "sword"
ETTIN_MACE = "ettin mace"
EMERALD_CROSSBOW = "Emerald Crossbow"

RANGED = "ranged"
MELEE = "melee"
WEAPONS = [SWORD,ETTIN_MACE,EMERALD_CROSSBOW]
HERO_WEAPONS = [SWORD,EMERALD_CROSSBOW]
RANGED_WEAPONS = [EMERALD_CROSSBOW]
MELEE_WEAPONS = [SWORD,ETTIN_MACE]

#Ammo
EMERALD_CROSSBOW_BOLTS = "emerald crossbow bolts"
EMERALD_CROSSBOW_QUIVER = "emerald crossbow quiver"

AMMOTYPES = [EMERALD_CROSSBOW_BOLTS,EMERALD_CROSSBOW_QUIVER]
CROSSBOW_AMMO = [EMERALD_CROSSBOW_BOLTS,EMERALD_CROSSBOW_QUIVER]

###Projectiles
CROSSBOW_BOLT = "crossbow bolt"

PROJECTILE_DICT = {EMERALD_CROSSBOW:CROSSBOW_BOLT}

#Hit types
HIT = True
MISS = False

#Sizes
SIZE_TINY = "tiny"
SIZE_SMALL = 'small'
SIZE_MEDIUM = "medium"

#Far proximity types
FAR_ENTITY_MATRIX = "far entity matrix"
FAR_SHADOW_MATRIX = "far shadow matrix"
FAR_LEVEL_MATRIX = "far level matrix"

FAR_ENTITY_LIST = "far entity list"
FAR_TILE_LIST = "far level wall or water list"

#Collider types
MELEE_SECTOR = "melee sector"
ENTITY_OMNI = "movement omni"
ENTITY_SECTOR = "movement sector"
SQUARE = "square"
WALL_HIDER = "wall hider"

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

#Direction name
HORIZONTAL = "horizontal"
VERTICAL = "vertical"

#Wall hider
WALL_HIDER_POSITION = player_position[0], player_position[1] - 48