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
WALL_HIDER1 = "wall hider1"
WALL_HIDER2 = "wall hider2"
WALL_HIDER3 = "wall hider3"

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

#Cutscenes
BOSS_ENTRY = "boss entry cutscene"
CUTSCENE_PLACE_INDEX = 18,17
CUTSCENE_TILE_INDICES = [(19,9),(19,10),(20,10),(20,11),(21,11),(21,12),(21,13),(22,14),(22,15),(22,16),(22,17),(22,18),(22,19),(22,20),(21,21),(21,22),(21,23),(20,23),(20,24),(20,24),(19,24),(19,25)]

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
EMERALD_CROSSBOW = "The Emerald Crossbow"
NECROLIGHT = "The Necrolight"

#Monster weapons
ETTIN_MACE = "ettin mace"
BISHOP_MAGIC_MISSILE = "bishop magic misile"
SPIKE_BALL_SPELL = "spike ball spell"
RED_ORB_SPELL = "red orb spell"
WHIRLWIND_SPELL = "whirlwind spell"

#Weapon lists
WEAPONS = [SWORD, EMERALD_CROSSBOW, NECROLIGHT, ETTIN_MACE, BISHOP_MAGIC_MISSILE, SPIKE_BALL_SPELL, RED_ORB_SPELL, WHIRLWIND_SPELL]
HERO_WEAPONS = [SWORD, EMERALD_CROSSBOW, NECROLIGHT]
RANGED_WEAPONS = [EMERALD_CROSSBOW, NECROLIGHT, BISHOP_MAGIC_MISSILE, SPIKE_BALL_SPELL, RED_ORB_SPELL, WHIRLWIND_SPELL]
MELEE_WEAPONS = [SWORD, ETTIN_MACE]

###Ammo###
EMERALD_CROSSBOW_BOLTS = "emerald crossbow bolts"
EMERALD_CROSSBOW_QUIVER = "emerald crossbow quiver"
NECRO_SMALL_AMMO = "necrolight small rune"
NECRO_LARGE_AMMO = "necrolight large rune"

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
STALAG_S = "stalagmite small"
STALAG_L = "stalagmite large"
LICH_EYE = "The Iron Lich Eye"
RUBY_PEDESTAL_EMPTY = "ruby pedestal empty"
RUBY_PEDESTAL_FULL = "ruby pedestal full"
CORPSE1 = "corpse1"
CORPSE2 = "corpse2"
BANNER = "banner"

DECORATIONS = [WALL_TORCH, VASE, SCULPTURE1, FLAME_PEDESTAL1, STALAG_S, STALAG_L, LICH_EYE, RUBY_PEDESTAL_EMPTY, RUBY_PEDESTAL_FULL, CORPSE1, CORPSE2, BANNER]

##### Projectiles #####
CROSSBOW_BOLT = "crossbow bolt"
MAGIC_MISSILE = "magic missile"
NECRO_BALL = "necro ball"
SPIKE_BALL = "spike ball"
SPIKE_SHARD = "spike shard"
WHIRLWIND = "whirlwind"
RED_ORB = "red orb"

PROJECTILE_DICT = {EMERALD_CROSSBOW:CROSSBOW_BOLT,
                   NECROLIGHT:NECRO_BALL, 
                   BISHOP_MAGIC_MISSILE:MAGIC_MISSILE, 
                   SPIKE_BALL_SPELL:SPIKE_BALL,
                   SPIKE_BALL:SPIKE_SHARD, 
                   WHIRLWIND_SPELL:WHIRLWIND, 
                   RED_ORB_SPELL:RED_ORB}

#######################
##### Level Tiles #####
#######################
###Tile types###
ENTRANCE = "E" 
EXIT = "N"
WALL = "X"
WATER = "~"
LAVA = "L"
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
LIQUIDS = [WATER,LAVA]
IMPASSABLE_TILES = [ENTRANCE,EXIT,WALL,WATER,LAVA,FLOOR_PIT]
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
SUMMON_MONSTER = "Summon Monster"


