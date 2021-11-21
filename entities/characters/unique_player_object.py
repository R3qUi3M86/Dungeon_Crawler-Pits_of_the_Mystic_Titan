from utilities.constants import player_position
from entities.characters.player import Hero

HERO = None

def initialize_player():
    global HERO
    
    HERO = Hero(player_position)