import random
import numpy as np
from utilities import util
from utilities import entity_manager
from utilities.constants import *
from sounds import sound_player

USABLE_ABILITIES_DICT = {FLYING:False, TELEPORT_BLUR: True}


class Ability():
    def __init__(self, owner, name):
        ABILITIES_COOLDOWN_DICT = {FLYING:0, TELEPORT_BLUR: 4 + random.choice(np.arange(0,1,0.05))}

        self.monster = owner
        self.NAME = name
        self.TYPE = ABILITY

        self.use_speed = 0.5
        self.use_speed_timer = 0

        self.cooldown = ABILITIES_COOLDOWN_DICT[self.NAME]
        self.cooldown_timer = 0

        self.is_usable = USABLE_ABILITIES_DICT[self.NAME]
        self.is_ready_to_use = True
        self.is_being_used = False

    #Updates
    def update(self):
        if self.is_usable:
            if self.is_being_used:
                if self.is_ready_to_use:
                    self.apply_ability_effects()
                    self.is_ready_to_use = False
                self.increment_use_speed_timer()
            
            elif not self.is_ready_to_use:
                self.increment_cooldown_timer()
        
    #Abilities effects
    def apply_ability_effects(self):
        if self.NAME is TELEPORT_BLUR:
            self.use_teleport_blur_ability()

    def use_teleport_blur_ability(self):
        self.monster.can_collide_with_player = False
        
        random_angle = 0
        
        distance_to_player = util.get_absolute_distance(self.monster.map_position, entity_manager.hero.map_position)
        angle_to_player = util.get_total_angle(self.monster.map_position, entity_manager.hero.map_position)
        if 300 >= distance_to_player >= 48: 
            random_angle = random.choice(range(90,271)) + angle_to_player
        elif 300 < distance_to_player or distance_to_player < 48:
            random_angle = random.choice(range(-45,46)) + angle_to_player
        
        movement_speed = 7
        travel_speed = util.get_travel_speed(random_angle, movement_speed)
        self.monster.speed_vector = travel_speed
        
        sound_player.play_ability_use_sound(self.NAME)

    #Timers
    def increment_use_speed_timer(self):
        if self.use_speed_timer >= self.use_speed:
            self.is_being_used = False
            self.monster.monster_ai.is_using_ability = False
            self.use_speed_timer = 0
            if self.NAME is TELEPORT_BLUR:
                self.monster.can_collide_with_player = True
        self.use_speed_timer += 0.0167

    def increment_cooldown_timer(self):
        if self.cooldown_timer >= self.cooldown:
            self.is_ready_to_use = True
            self.cooldown_timer = 0
        self.cooldown_timer += 0.0167