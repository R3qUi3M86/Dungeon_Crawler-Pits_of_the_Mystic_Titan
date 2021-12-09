from settings import *

###################
##### General #####
###################
PLAYER_ID = -1

X = 0
Y = 1

NEW_GAME = "new game"
CONTINUE_GAME = "continue game"

#Object type
ENTITY = "entity"
SHADOW = "shadow"
TILE = "tile"

#Hit types
HIT = True
MISS = False

#Sizes
SIZE_TINY = "tiny"
SIZE_SMALL = "small"
SIZE_MEDIUM = "medium"
SIZE_LARGE = "large"

#Glow types
GREEN_GLOW = "green glow"
RED_GLOW = "red glow"
BLUE_GLOW = "blue glow"

#Collider types
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

####################
##### Entities #####
####################
PLAYER = "player"
MONSTER = "monster"
ITEM = "item"
PROJECTILE = "projectile"

##### Monsters #####
ETTIN = "ettin"
DARK_BISHOP = "dark bishop"
IRON_LICH = "iron lich"

##### Items #####
###Currency###
GOLD_COINS = "gold coin"

CURRENCIES = [GOLD_COINS]

###Weapons###
RANGED = "ranged"
MELEE = "melee"

#Player weapons
SWORD = "Sword"
EMERALD_CROSSBOW = "Emerald Crossbow"
NECROLIGHT = "Necrolight"

#Monster weapons
ETTIN_MACE = "ettin mace"
BISHOP_MAGIC_MISSILE = "bishop magic misile"

#Weapon lists
WEAPONS = [SWORD, ETTIN_MACE, EMERALD_CROSSBOW, BISHOP_MAGIC_MISSILE, NECROLIGHT]
HERO_WEAPONS = [SWORD, EMERALD_CROSSBOW, NECROLIGHT]
RANGED_WEAPONS = [EMERALD_CROSSBOW, BISHOP_MAGIC_MISSILE, NECROLIGHT]
MELEE_WEAPONS = [SWORD, ETTIN_MACE]

###Ammo###
EMERALD_CROSSBOW_BOLTS = "emerald crossbow bolts"
EMERALD_CROSSBOW_QUIVER = "emerald crossbow quiver"
NECRO_SMALL_AMMO = "necro small ammo"
NECRO_LARGE_AMMO = "necro small ammo"

AMMOTYPES = [EMERALD_CROSSBOW_BOLTS,EMERALD_CROSSBOW_QUIVER, NECRO_SMALL_AMMO, NECRO_LARGE_AMMO]
CROSSBOW_AMMO = [EMERALD_CROSSBOW_BOLTS,EMERALD_CROSSBOW_QUIVER]
NECROLIGHT_AMMO = [NECRO_SMALL_AMMO, NECRO_LARGE_AMMO]

###Consumable###
QUARTZ_FLASK = "quartz flask"

CONSUMABLES = [QUARTZ_FLASK]

###Decorations###
WALL_TORCH = "wall torch"
VASE = "vase"
SCULPTURE1 = "sculpture 1"
FLAME_PEDESTAL1 = "flame pedestal 1"

DECORATIONS = [WALL_TORCH, VASE, SCULPTURE1, FLAME_PEDESTAL1]

##### Projectiles #####
CROSSBOW_BOLT = "crossbow bolt"
MAGIC_MISSILE = "magic missile"


PROJECTILE_DICT = {EMERALD_CROSSBOW:CROSSBOW_BOLT, BISHOP_MAGIC_MISSILE:MAGIC_MISSILE}

#######################
##### Level Tiles #####
#######################
###Tile types###
ENTRANCE = "E" 
EXIT = "N"
WALL = "X"
WATER = "~"
FLOOR = " "
FLOOR_PIT = "O"
SIMPLE_CRACK = "*"
CORNER_CRACK = "`"

###Tile painting mode###
VISIBLE = "visible"
HIDDEN = "hidden"
PRIMARY_OVERLAY = "primary_overlay"
SECONDARY_OVERLAY = "secondary_overlay"

COLLISION_TILE = "collison_tile"
IMPASSABLE_TILES = [ENTRANCE,EXIT,WALL,WATER,FLOOR_PIT]
PASSABLE_TILES = [FLOOR,SIMPLE_CRACK,CORNER_CRACK]
WALL_LIKE = [ENTRANCE,EXIT,WALL]
FLOOR_LIKE = [FLOOR, FLOOR_PIT, SIMPLE_CRACK, CORNER_CRACK]

#####################
##### Abilities #####
#####################
###Ability names###
ABILITY = "ability"

FLYING = "Flying"
TELEPORT_BLUR = "Teleport Blur"


