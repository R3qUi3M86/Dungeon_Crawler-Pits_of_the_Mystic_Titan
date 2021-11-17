import random
from utilities.constants import *
from utilities import util
from utilities import entity_manager
from entities.characters import player

class Ai():
    def __init__(self,owner):
        self.owning_monster = owner
        self.moving_direction = SECTOR_S
        self.player_direction_sector = SECTOR_S
        self.melee_colliding_sprite = None
        #self.player_direction_angle = self.get_player_direction_angle(self.owning_monster.sprite_position)
        self.direction_change_decision_timer = 0.0
        self.direction_change_decision_timer_limit = 6

    def get_player_direction_angle(self,monster_position):
        util.get_total_angle(monster_position,PLAYER_POSITION)
    
    def randomize_direction_change_decision_timer_limit(self):
        self.direction_change_decision_timer_limit += random.choice(range(12))

    def increment_direction_change_decision_timer(self):
        self.direction_change_decision_timer += 0.1
        if int(self.direction_change_decision_timer) == self.direction_change_decision_timer_limit:
            self.direction_change()
            self.direction_change_decision_timer = 0.0
            self.direction_change_decision_timer_limit = 6
            self.randomize_direction_change_decision_timer_limit()

    def direction_change(self):
        decision = random.choice([0,1,2,3])
        if decision == 0:
            self.owning_monster.facing_direction = random.choice(SECTORS)
        else:
            self.owning_monster.facing_direction = util.get_facing_direction(self.owning_monster.sprite_position,PLAYER_POSITION)
    
    def monster_can_melee_attack_player(self):
        self.player_direction_sector = util.get_facing_direction(self.owning_monster.sprite_position,PLAYER_POSITION)
        for melee_sprite in self.owning_monster.monster_melee_sprites:
            if melee_sprite.rect.colliderect(player.PLAYER_SHADOW_SPRITE):
                self.melee_colliding_sprite = melee_sprite
                return True
        return False


