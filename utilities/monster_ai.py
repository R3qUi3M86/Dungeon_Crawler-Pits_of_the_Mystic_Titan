import random
from utilities import util
from utilities import pathfinder
from utilities.constants import *
from entities.characters import unique_player_object

class Ai():
    def __init__(self,owner, pathfinding_matrix, tile_index):
        self.monster = owner
        self.moving_direction = SECTOR_S
        self.player_direction_sector = SECTOR_S

        self.direction_change_decision_timer = 0.0
        self.direction_change_decision_timer_limit = 6

        self.attack_decision_timer = 0.0
        self.attack_decision_timer_limit = 3
        
        self.pathfinder = pathfinder.Pathfinder(pathfinding_matrix, tile_index)
        self.pathfinding_collision_rect = pygame.Rect((self.monster.position[0] - 2, self.monster.position[1] -2),(4,4))
        self.is_path_finding = False
        self.is_following_path = False
        self.is_avoiding_obstacle = False
        self.obstacle_sector = None
        self.avoidance_direction_sector = None
        self.is_doing_diagonal_avoidance = False
        self.is_on_final_approach = False
    
    #Movement directional change timer
    def increment_direction_change_decision_timer(self):
        self.direction_change_decision_timer += 0.1
        if int(self.direction_change_decision_timer) == self.direction_change_decision_timer_limit:
            self.direction_change()
            self.direction_change_decision_timer = 0.0
            if self.is_avoiding_obstacle == False:
                self.direction_change_decision_timer_limit = 6
                self.randomize_direction_change_decision_timer_limit() 

    def randomize_direction_change_decision_timer_limit(self):
        self.direction_change_decision_timer_limit += random.choice(range(12))

    #Obstacle avoidance logic
    def set_avoidance_direction_sector(self, monster_position,horizontal_vertial):
        player_direction_angle = self.get_player_direction_angle(monster_position)
        if horizontal_vertial == VERTICAL:
            if 180 > int(player_direction_angle) >= 0:
                self.avoidance_direction_sector = SECTOR_N
            else:
                self.avoidance_direction_sector = SECTOR_S
        elif horizontal_vertial == HORIZONTAL:
            if 90 > int(player_direction_angle) or 270 <= player_direction_angle:
                self.avoidance_direction_sector = SECTOR_E
            else:
                self.avoidance_direction_sector = SECTOR_W

    def avoid_obstacle(self,sector):
        self.finish_avoiding_obstacle()
        self.direction_change_decision_timer_limit = 1
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

    def direction_change(self):
        if self.is_avoiding_obstacle == False and self.is_path_finding == False and self.is_following_path == False:
            decision = random.choice(range(7))
            if decision == 0:
                self.monster.facing_direction = random.choice(SECTORS)
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
            self.finish_avoiding_obstacle()

    def change_to_parallel_direction(self):
            if self.obstacle_sector == SECTOR_N or self.obstacle_sector == SECTOR_S:
                self.set_avoidance_direction_sector(self.monster.position, HORIZONTAL)
            else:
                self.set_avoidance_direction_sector(self.monster.position, VERTICAL)
            self.monster.facing_direction = self.avoidance_direction_sector
            self.direction_change_decision_timer_limit = 6

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
    
    def change_to_next_point_direction(self):
        # if self.pathfinder.points and self.monster.pathfinding_collision_rect.collidepoint(self.pathfinder.points[0]):
        #     del self.pathfinder.points[0]
        self.monster.facing_direction = util.get_facing_direction(self.monster.map_position,self.pathfinder.points[0])

    def finish_avoiding_obstacle(self):
        self.is_avoiding_obstacle = False
        self.obstacle_sector = None
        self.avoidance_direction_sector = None
        self.is_doing_diagonal_avoidance = False
        self.is_on_final_approach = False

    def finish_pathfinding(self):
        self.pathfinder.update(pathfinding = False)
        self.is_path_finding = False
        self.is_following_path = False

    #Combat decisions
    def monster_can_melee_attack_player(self):
        if unique_player_object.HERO.is_living == True:
            self.player_direction_sector = util.get_facing_direction(self.monster.position,player_position)
            for melee_sprite in self.monster.character_melee_sprites:
                if melee_sprite.rect.colliderect(unique_player_object.HERO.entity_collision_mask):
                    if pygame.sprite.collide_mask(melee_sprite, unique_player_object.HERO.entity_collision_mask):
                        return True
        return False

    #Combat decisions timer
    def increment_attack_decision_timer(self):
        self.attack_decision_timer += 0.05
        if int(self.attack_decision_timer) == self.attack_decision_timer_limit:
            self.monster.is_attacking = True
            self.monster.attack_can_be_interrupted = True
            self.attack_decision_timer = 0.0
    
    #Misc
    def get_player_direction_angle(self,monster_position):
        return util.get_total_angle(monster_position,player_position)



