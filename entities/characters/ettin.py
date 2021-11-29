import pygame
import random
from settings import *
from sounds import sound_player
from utilities import util
from utilities import combat_manager
from utilities import entity_manager
from utilities import level_painter
from utilities import monster_ai
from utilities.constants import *
from utilities.level_painter import TILE_SIZE
from images.characters.ettin_images import *
from entities.shadow import Shadow
from entities.colliders.collider import Collider

class Ettin(pygame.sprite.Sprite):
    def __init__(self,tile_index, facing_direction=SECTOR_S):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = 12
        self.NAME = ETTIN
        self.TYPE = MONSTER

        ###Position variables###
        self.tile_index = tile_index
        self.prevous_tile_index = tile_index
        self.current_tile_position = (tile_index[Y]+1)*TILE_SIZE[Y]-TILE_SIZE[Y]//2+screen_width//2, (tile_index[X]+1)*TILE_SIZE[X]-TILE_SIZE[X]//2+screen_height//2
        self.previous_tile_position = self.current_tile_position
        self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
        self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)
        self.direct_proximity_monsters = []
        self.position = level_painter.get_tile_position(tile_index)
        self.map_position = (tile_index[Y]+1)*TILE_SIZE[Y]-TILE_SIZE[Y]//2+screen_width//2, (tile_index[X]+1)*TILE_SIZE[X]-TILE_SIZE[X]//2+screen_height//2
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION
        
        ###Object ID###
        self.id = util.generate_entity_id()

        ###Animations###
        #Walk assets
        self.character_walk = character_walk
        self.character_walk_index = [6,0]
        
        #Attack assets
        self.character_attack = character_attack
        self.character_attack_index = [6,0]

        #Death assets
        self.character_death = character_death
        self.character_death_index = 0

        #Overkill assets
        self.character_overkill = character_overkill
        self.character_overkill_index = 0

        #Pain assets
        self.character_pain = character_pain
        self.character_pain_index = 0
        self.character_pain_timer = 0

        ###Owned sprites###
        #Colliders
        self.entity_collider_nw    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_NW)
        self.entity_collider_ne    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_NE)
        self.entity_collider_sw    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_SW)
        self.entity_collider_se    = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_SE)
        self.entity_collider_omni  = Collider(player_position, self.id, ENTITY_OMNI)

        #Shadow
        self.shadow = Shadow(self.position, self.map_position, self.id, SIZE_MEDIUM, self.tile_index)
        
        #Sprite lists
        self.entity_collider_sprites     = [self.entity_collider_omni,self.entity_collider_nw,self.entity_collider_ne,self.entity_collider_sw,self.entity_collider_se]
        self.entity_auxilary_sprites     = [[self.shadow],self.entity_collider_sprites]

        ###Initial sprite definition###
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.monster_ai = monster_ai.Ai(self, level_painter.pathfinding_matrix, tile_index)

        #####General variables#####
        ###Status flags###
        self.is_preparing_attack = False
        self.is_attacking = False
        self.is_living = True
        self.is_dying = False
        self.is_overkilled = False
        self.is_in_pain = False
        self.is_dead = False
        self.is_corpse = False
        self.has_los = False
        self.can_collide = False
        self.active = False
        
        ###Character properties###
        #General
        self.health = 10
        self.maxhealth = 10

        #Combat
        self.damage = 0
        self.x_melee_range = 50
        self.y_melee_range = 27
        self.melee_range = self.x_melee_range, self.y_melee_range
        self.x_size = 20
        self.y_size = 11
        self.size = self.x_size, self.y_size
        self.attack_interruption_chance = 50
        self.attack_can_be_interrupted = True
        self.can_shoot = False
        self.projectile_type = None

        #Abilities
        self.abilities = []

        #Movement
        self.facing_direction = facing_direction
        self.speed = 1.4,1
        self.speed_vector = 0,0

    #Update functions
    def update(self):
        if not self.leaving_far_proximity_matrix_margin():
            self.activate()

            if not self.is_dead:
                self.position = round((self.position[0] + self.speed_vector[0]),2),round((self.position[1] + self.speed_vector[1]),2)
                self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION
                self.update_owned_sprites_position()

                self.map_position = round(self.position[0]+entity_manager.hero.map_position[0]-player_position[0],2), round(self.position[1]+entity_manager.hero.map_position[1]-player_position[1],2)
                self.tile_index = util.get_tile_index(self.map_position)
            
                if self.tile_index != self.prevous_tile_index:
                    self.previous_tile_position = (self.prevous_tile_index[Y]+1)*TILE_SIZE[Y]-TILE_SIZE[Y]//2+screen_width//2, (self.prevous_tile_index[X]+1)*TILE_SIZE[X]-TILE_SIZE[X]//2+screen_height//2
                    self.current_tile_position = (self.tile_index[Y]+1)*TILE_SIZE[Y]-TILE_SIZE[Y]//2+screen_width//2, (self.tile_index[X]+1)*TILE_SIZE[X]-TILE_SIZE[X]//2+screen_height//2
                    self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
                    self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)
                    entity_manager.update_all_nearby_monsters_and_self_direct_proximity_monsters_lists(self.direct_proximity_index_matrix)
                    entity_manager.move_entity_in_all_matrices(self.id, MONSTER, self.prevous_tile_index, self.tile_index)
                    self.prevous_tile_index = self.tile_index
                
                self.update_decisions()

            elif not self.is_corpse:
                self.is_corpse = True
                entity_manager.fix_all_dead_objects_to_pixel_accuracy()
                entity_manager.fix_player_position_to_pixel_accuracy()
            
            self.update_animation()
            self.rect = self.image.get_rect(midbottom = (self.image_position))

        else:
            self.deactivate()

    def update_position(self, vector=None):
        if not self.leaving_far_proximity_matrix_margin():
            if vector:
                self.position = round((self.position[0]-vector[0]),2),round((self.position[1] - vector[1]),2)
            else:
                self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
            self.map_position = round(self.position[0]+entity_manager.hero.map_position[0]-player_position[0],2), round(self.position[1]+entity_manager.hero.map_position[1]-player_position[1],2)
            self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
            self.rect = self.image.get_rect(midbottom = (self.image_position))
            self.update_owned_sprites_position()
    
    def update_decisions(self):
        if self.is_living:

            if entity_manager.hero.is_living and self.monster_ai.is_idle:
                if not self.monster_ai.is_waking_up:
                    self.monster_ai.increment_los_emmision_timer()
                    self.monster_ai.increment_direction_change_decision_timer()
                else:
                    self.monster_ai.increment_waking_up_timer()
            
            elif not entity_manager.hero.is_living:
                self.speed_vector = 0,0
                self.monster_ai.increment_direction_change_decision_timer()
                self.monster_ai.reset_obstacle_avoidance_flags()
                self.monster_ai.end_pathfinding()

            elif self.monster_ai.monster_can_melee_attack_player():
                self.initialize_attack_sequence()
            
            else:
                self.start_walking()
        
        elif not self.is_dead:
            self.speed_vector = 0,0
            self.interrupt_attack()
            self.is_in_pain = False
            self.monster_ai.reset_obstacle_avoidance_flags()
            self.monster_ai.end_pathfinding()

            if self.is_overkilled:
                self.is_dying = False

    def update_animation(self): 
        self.set_character_animation_direction_indices()
        
        if self.is_living:
            self.character_walk_forward_animation()

        if self.is_in_pain and not self.is_attacking:
            self.character_pain_animation()
        
        elif self.is_attacking:
            self.character_attack_animation()
        
        elif self.is_dying:
            self.character_death_animation()

        elif self.is_overkilled:
            self.character_overkill_animation()
    
    def update_owned_sprites_position(self):
        for auxilary_sprites_row in self.entity_auxilary_sprites:
            for auxilary_sprite in auxilary_sprites_row:
                auxilary_sprite.position = self.position
                auxilary_sprite.tile_index = self.tile_index
                auxilary_sprite.update_position(self.position)
    
    #Animations
    def character_pain_animation(self):
        self.character_pain_timer += 0.05
        if int(self.character_pain_timer) >= 1:
            self.is_in_pain = False
            self.character_pain_timer = 0
        self.image = character_pain[self.character_pain_index]

    def character_death_animation(self):
        self.character_death_index += 0.1
        if int(self.character_death_index) == 7:
            self.character_death_index = 6
            self.is_dying = False
            self.is_dead = True
        self.image = self.character_death[int(self.character_death_index)]

    def character_overkill_animation(self):
        self.character_overkill_index += 0.1
        if int(self.character_overkill_index) == 10:
            self.character_overkill_index = 9
            self.is_overkilled = False
            self.is_dead = True
        self.image = self.character_overkill[int(self.character_overkill_index)]       

    def character_walk_forward_animation(self):
        if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
            self.character_walk_index[1] += 0.1
            if int(self.character_walk_index[1]) == 4:
                self.character_walk_index[1] = 0
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        self.character_attack_index[1] += 0.1
        if int(self.character_attack_index[1]) == 3:
            self.interrupt_attack()
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
        else:
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]    
            if round(self.character_attack_index[1],2) == 2.00:
                combat_manager.attack_player_with_melee_attack(self, self.damage)

    def set_character_animation_direction_indices(self):
        for sector in SECTORS:
            if sector == self.facing_direction:
                self.character_walk_index[0] = sector
                self.character_attack_index[0] = sector
                self.character_pain_index = sector           

    #Walking functions
    def start_walking(self):
        if not self.monster_ai.is_following_path and not self.monster_ai.is_path_finding:
            self.monster_ai.increment_direction_change_decision_timer()
            self.monster_ai.increment_pathfinding_prepare_timer()
            self.set_speed_vector()
        
        else:
            self.use_pathfinding_logic()

    def use_pathfinding_logic(self):
        if self.monster_ai.is_path_finding and not self.monster_ai.is_following_path:
            self.monster_ai.pathfinder.monster_tile_index = self.tile_index
            self.monster_ai.pathfinder.create_path()
            self.monster_ai.next_tile_pos_x = level_painter.get_tile_sprite_by_index((self.monster_ai.pathfinder.path[0][1],self.monster_ai.pathfinder.path[0][0])).map_position[0]
            self.monster_ai.next_tile_pos_y = level_painter.get_tile_sprite_by_index((self.monster_ai.pathfinder.path[0][1],self.monster_ai.pathfinder.path[0][0])).map_position[1]
            self.monster_ai.is_path_finding = False
            self.monster_ai.is_following_path = True
        
        elif self.monster_ai.is_following_path and len(self.monster_ai.pathfinder.path) != 0:
            self.monster_ai.change_to_next_point_direction()

    def set_speed_vector(self):
        if self.is_living and not self.is_preparing_attack and not self.is_attacking:
            if self.facing_direction == SECTOR_E:
                self.speed_vector = 1.4,0
            elif self.facing_direction == SECTOR_NE:
                self.speed_vector = 0.99,-0.58
            elif self.facing_direction == SECTOR_N:
                self.speed_vector = 0,-0.77
            elif self.facing_direction == SECTOR_NW:
                self.speed_vector = -0.99,-0.58
            elif self.facing_direction == SECTOR_W:
                self.speed_vector = -1.4,0
            elif self.facing_direction == SECTOR_SW:
                self.speed_vector = -0.99,0.58
            elif self.facing_direction == SECTOR_S:
                self.speed_vector = 0,0.77
            elif self.facing_direction == SECTOR_SE:
                self.speed_vector = 0.99,0.58
            
    #Combat functions
    def initialize_attack_sequence(self):
        self.speed_vector = 0,0
                
        if not self.is_preparing_attack and not self.is_attacking:
            self.is_preparing_attack = True
            self.facing_direction = util.get_facing_direction(self.position,player_position)
            self.monster_ai.reset_obstacle_avoidance_flags()
            self.monster_ai.end_pathfinding()

        elif self.is_preparing_attack:
            self.monster_ai.increment_attack_decision_timer()
        
        elif self.is_attacking and self.is_in_pain and self.attack_can_be_interrupted and self.attack_interupted():
                self.interrupt_attack()

    def take_damage(self, damage):
        self.health -= damage
        
        if self.monster_ai.is_idle:
            self.monster_ai.is_waking_up = True
        
        if self.health > 0:
            self.is_in_pain = True
            if random.choice(range(4)) == 0:
                sound_player.ettin_pain_sound.play()
        else:
            sound_player.ettin_pain_sound.stop()
            sound_player.ettin_death_sound.play()
            self.is_living = False
            self.is_in_pain = False
            self.is_dying = True
            
            if -(self.maxhealth//2) >= self.health:
                sound_player.ettin_death_sound.stop()
                sound_player.ettin_overkill_sound.play()
                self.is_living = False
                self.is_in_pain = False
                self.is_dying = False
                self.is_overkilled = True

    def interrupt_attack(self):
        self.is_attacking = False
        self.character_attack_index[1] = 0

    def attack_interupted(self):
        if random.choice(range(1,101)) <= self.attack_interruption_chance:
            return True
        self.attack_can_be_interrupted = False
        return False
    
    def emit_los_particle_and_wake_up_if_player_is_seen(self):
        if util.monster_has_line_of_sight(self.map_position):
            hero_sector = util.get_facing_direction(self.position,player_position)
            
            if self.monster_ai.is_idle:
                if self.facing_direction+1 == 8 and hero_sector in [7,0,1]:
                    self.monster_ai.direction_change_decision_timer_limit = 60
                    self.monster_ai.is_waking_up = True
                
                elif self.facing_direction+2 == 8 and hero_sector in [6,7,0]:
                    self.monster_ai.direction_change_decision_timer_limit = 60
                    self.monster_ai.is_waking_up = True
                
                elif hero_sector in [self.facing_direction-1,self.facing_direction,self.facing_direction+1]:
                    self.monster_ai.direction_change_decision_timer_limit = 60
                    self.monster_ai.is_waking_up = True

    #Misc
    def activate(self):
        self.active = True
        self.can_collide = True

    def deactivate(self):
        self.speed_vector = 0,0
        self.can_collide = False
        self.active = False

        if not self.monster_ai.is_idle:
            self.monster_ai.end_pathfinding()
            self.monster_ai.reset_obstacle_avoidance_flags()

    #Conditions
    def leaving_far_proximity_matrix_margin(self):
        hero_tile_index = entity_manager.hero.tile_index
        tile_row_offset = screen_height//2//TILE_SIZE[Y]+far_matrix_offset_y//3
        tile_col_offset = screen_width//2//TILE_SIZE[X]+far_matrix_offset_x//3
        if abs(self.tile_index[0]-hero_tile_index[0]) > tile_row_offset or abs(self.tile_index[1]-hero_tile_index[1]) > tile_col_offset:
            return True
        return False