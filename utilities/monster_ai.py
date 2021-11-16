from utilities.constants import *
from utilities import util
from utilities import entity_manager

class Ai():
    def __init__(self,monster_position):
        self.moving_direction = SECTOR_S
        self.player_direction_angle = self.get_player_direction_angle(monster_position)

    def get_player_direction_angle(self,monster_position):
        util.get_total_angle(monster_position,PLAYER_POSITION)
