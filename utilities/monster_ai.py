import random
from utilities import util
from utilities import pathfinder
from utilities import level_painter
from utilities import entity_manager
from utilities.constants import *

class Ai():
    def __init__(self,owner, pathfinding_matrix, tile_index):
        self.monster = owner

        self.direction_change_decision_timer = 0
        self.direction_change_decision_timer_limit = 300
        
        self.monster_path_follow_dir_change_timer = 30
        self.monster_path_follow_dir_change_timer_limit = 30

        self.pathfinding_prepare_timer = 0
        self.pathfinding_prepare_timer_limit = 200

        self.attack_decision_timer = 0
        self.attack_decision_timer_limit = 30

        self.los_emision_timer = 0
        self.los_emision_timer_limit = 120

        self.waking_up_timer = 0
        self.waking_up_timer_limit = 30

        self.pathfinder = pathfinder.Pathfinder(pathfinding_matrix, tile_index)
        self.next_tile_pos_x = 0
        self.next_tile_pos_y = 0
        self.is_idle = True
        self.waking_up = False
        self.is_roaming = False
        self.is_path_finding = False
        self.is_following_path = False
        self.is_avoiding_obstacle = False
        self.is_doing_diagonal_avoidance = False
        self.is_on_final_approach = False
        self.path_finding_is_ready = True
        self.obstacle_sector = None
        self.avoidance_direction_sector = None
    
    #Movement directional change timer
    def increment_direction_change_decision_timer(self):
        self.direction_change_decision_timer += 1
        if self.direction_change_decision_timer == self.direction_change_decision_timer_limit:
            self.direction_change()
            self.direction_change_decision_timer = 0
            
            if self.is_roaming:
                self.direction_change_decision_timer_limit = 60
                self.randomize_direction_change_decision_timer_limit() 

    def randomize_direction_change_decision_timer_limit(self):
        self.direction_change_decision_timer_limit += random.choice(range(12))

    def increment_path_follow_dir_change_timer(self):
        if len(self.pathfinder.path) > 0:
            if int(self.monster_path_follow_dir_change_timer) == self.monster_path_follow_dir_change_timer_limit:
                self.monster_path_follow_dir_change_timer = 0
                self.monster.facing_direction = util.get_facing_direction(self.monster.map_position,(self.next_tile_pos_x,self.next_tile_pos_y))
                self.monster.set_speed_vector()
            else:
                self.monster_path_follow_dir_change_timer += 1
        else:
            self.end_pathfinding()

    def increment_pathfinding_prepare_timer(self):
        if not self.path_finding_is_ready:
            self.pathfinding_prepare_timer += 1
        if int(self.pathfinding_prepare_timer) == self.pathfinding_prepare_timer_limit:
            self.path_finding_is_ready = True
            self.pathfinding_prepare_timer = 0

    def direction_change(self):
        if self.is_idle:
            decision = random.choice(range(8))
            self.monster.facing_direction = SECTORS[decision]
        
        elif self.is_roaming:
            decision = random.choice(range(8))
            if decision == 0:
                if self.monster.facing_direction+2 == 8:
                    self.monster.facing_direction = SECTORS[0]
                elif self.monster.facing_direction+2 == 9:
                    self.monster.facing_direction = SECTORS[1]
                else:
                    self.monster.facing_direction = SECTORS[self.monster.facing_direction+random.choice([-2,2])]
            
            elif decision == 1:
                self.monster.facing_direction = SECTORS[self.monster.facing_direction-2]
            else:
                self.monster.facing_direction = util.get_facing_direction(self.monster.position,player_position)
        
        elif self.is_avoiding_obstacle == True and self.avoidance_direction_sector == None:
            self.change_to_parallel_direction()
        
        elif self.is_doing_diagonal_avoidance == False:
            self.change_to_diagonal_direction()
            self.is_doing_diagonal_avoidance = True

        elif self.is_on_final_approach == False:
            self.monster.facing_direction = util.get_facing_direction(self.monster.position,player_position)
            self.is_on_final_approach = True
        else:
            self.reset_obstacle_avoidance_flags()

    #Obstacle avoidance logic
    def avoid_obstacle(self,sector):
        self.end_pathfinding()
        self.reset_obstacle_avoidance_flags()
        self.is_roaming = False
        self.direction_change_decision_timer_limit = 60
        self.direction_change_decision_timer = 0
        self.is_avoiding_obstacle = True
        self.obstacle_sector = sector
        if sector == SECTOR_N:
            self.monster.facing_direction = SECTOR_S
        elif sector == SECTOR_S:
            self.monster.facing_direction = SECTOR_N
        elif sector == SECTOR_E:
            self.monster.facing_direction = SECTOR_W
        elif sector == SECTOR_W:
            self.monster.facing_direction = SECTOR_E
        elif sector == SECTOR_NE:
            self.monster.facing_direction = SECTOR_SW
        elif sector == SECTOR_SW:
            self.monster.facing_direction = SECTOR_NE
        elif sector == SECTOR_SE:
            self.monster.facing_direction = SECTOR_NW
        elif sector == SECTOR_NW:
            self.monster.facing_direction = SECTOR_SE

    def change_to_parallel_direction(self):
            if self.obstacle_sector == SECTOR_N or self.obstacle_sector == SECTOR_S:
                self.set_avoidance_direction_sector(self.monster.position, vertical=True)
            elif self.obstacle_sector == SECTOR_E or self.obstacle_sector == SECTOR_W:
                self.set_avoidance_direction_sector(self.monster.position, horizontal=True)
            elif self.obstacle_sector == SECTOR_NE or self.obstacle_sector == SECTOR_SW:
                self.set_avoidance_direction_sector(self.monster.position, diagonal_sw_ne=True)
            elif self.obstacle_sector == SECTOR_NW or self.obstacle_sector == SECTOR_SE:
                self.set_avoidance_direction_sector(self.monster.position, diagonal_se_nw=True)

            self.monster.facing_direction = self.avoidance_direction_sector
            self.direction_change_decision_timer_limit = 60

    def set_avoidance_direction_sector(self, monster_position,horizontal = False, vertical = False, diagonal_sw_ne = False, diagonal_se_nw = False):
        player_direction_angle = util.get_total_angle(monster_position,player_position)
        if horizontal:
            if 180 > int(player_direction_angle) >= 0:
                self.avoidance_direction_sector = SECTOR_N
            else:
                self.avoidance_direction_sector = SECTOR_S
        elif vertical:
            if 90 > int(player_direction_angle) or 270 <= player_direction_angle:
                self.avoidance_direction_sector = SECTOR_E
            else:
                self.avoidance_direction_sector = SECTOR_W
        elif diagonal_sw_ne:
            if 34.25 < int(player_direction_angle) <= 214.25:
                self.avoidance_direction_sector = SECTOR_NW
            else:
                self.avoidance_direction_sector = SECTOR_SE
        elif diagonal_se_nw:
            if 325.75 < int(player_direction_angle) or 145.75 >= player_direction_angle:
                self.avoidance_direction_sector = SECTOR_NE
            else:
                self.avoidance_direction_sector = SECTOR_SW

    def change_to_diagonal_direction(self):
            if self.obstacle_sector == SECTOR_N and self.avoidance_direction_sector == SECTOR_E:
                self.monster.facing_direction = SECTOR_NE
            elif self.obstacle_sector == SECTOR_N and self.avoidance_direction_sector == SECTOR_W:
                self.monster.facing_direction = SECTOR_NW
            elif self.obstacle_sector == SECTOR_S and self.avoidance_direction_sector == SECTOR_E:
                self.monster.facing_direction = SECTOR_SE
            elif self.obstacle_sector == SECTOR_S and self.avoidance_direction_sector == SECTOR_W:
                self.monster.facing_direction = SECTOR_SW
            elif self.obstacle_sector == SECTOR_E and self.avoidance_direction_sector == SECTOR_N:
                self.monster.facing_direction = SECTOR_NE
            elif self.obstacle_sector == SECTOR_E and self.avoidance_direction_sector == SECTOR_S:
                self.monster.facing_direction = SECTOR_SE
            elif self.obstacle_sector == SECTOR_W and self.avoidance_direction_sector == SECTOR_N:
                self.monster.facing_direction = SECTOR_NW
            elif self.obstacle_sector == SECTOR_W and self.avoidance_direction_sector == SECTOR_S:
                self.monster.facing_direction = SECTOR_SW
    
    def initialize_monster_path_finding(self):
        self.reset_obstacle_avoidance_flags()
        self.is_path_finding = True
        self.path_finding_is_ready = False
        self.monster_path_follow_dir_change_timer = self.monster_path_follow_dir_change_timer_limit

    def change_to_next_point_direction(self):
        if self.monster_reached_point_destination():
            self.pathfinder.path.remove(self.pathfinder.path[0])
            if self.pathfinder.path:
                self.next_tile_pos_x = level_painter.get_tile_sprite_by_index((self.pathfinder.path[0][1],self.pathfinder.path[0][0])).map_position[0]
                self.next_tile_pos_y = level_painter.get_tile_sprite_by_index((self.pathfinder.path[0][1],self.pathfinder.path[0][0])).map_position[1]
        self.increment_path_follow_dir_change_timer()

    def reset_obstacle_avoidance_flags(self):
        self.is_avoiding_obstacle = False
        self.obstacle_sector = None
        self.avoidance_direction_sector = None
        self.is_doing_diagonal_avoidance = False
        self.is_on_final_approach = False
        self.is_roaming = True

    def end_pathfinding(self):
        self.is_path_finding = False
        self.is_following_path = False
        self.is_roaming = True

    def monster_reached_point_destination(self):
        if self.next_tile_pos_x-20 <= self.monster.map_position[0] <= self.next_tile_pos_x+20 and self.next_tile_pos_y-20 < self.monster.map_position[1] <= self.next_tile_pos_y+20:
            return True
        return False

    #Combat decisions
    def monster_can_melee_attack_player(self):
        if entity_manager.hero.is_living == True:
            
            if self.monster.is_preparing_attack or self.monster.is_attacking:
                return True
            
            else:
                monster_map_pos = self.monster.map_position
                hero_map_pos = entity_manager.hero.map_position
                melee_range = self.monster.melee_range
                hero_size = entity_manager.hero.size
            
            if util.elipses_intersect(monster_map_pos,hero_map_pos,melee_range,hero_size):
                    return True
        return False

    #Combat decisions timer
    def increment_attack_decision_timer(self):
        self.attack_decision_timer += 1
        if self.attack_decision_timer == self.attack_decision_timer_limit:
            self.monster.is_preparing_attack = False
            self.monster.is_attacking = True
            self.monster.attack_can_be_interrupted = True
            self.attack_decision_timer = 0

    def increment_los_emmision_timer(self):
        self.los_emision_timer += 1
        if self.los_emision_timer == self.los_emision_timer_limit:
            self.monster.emit_los_particle_and_wake_up_if_player_is_seen()
            self.los_emision_timer = 0

    def increment_waking_up_timer(self):
        self.waking_up_timer += 1
        if self.waking_up_timer == self.waking_up_timer_limit:
            self.waking_up = False
            self.is_idle = False
            self.is_roaming = True