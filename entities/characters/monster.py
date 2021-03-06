import pygame
import random
from settings import *
from sounds import sound_player
from utilities import util
from utilities import combat_manager
from utilities import entity_manager
from utilities import level_painter
from utilities import monster_ai
from utilities import cutscene_manager
from utilities import t_ctrl
from utilities import collision_manager
from utilities.constants import *
from utilities.level_painter import TILE_SIZE
from images.characters.ettin_images import *
from images.characters.dark_bishop_images import *
from images.characters.iron_lich_images import *
from images.abilities.ability_images import *
from entities.characters.ability import Ability
from entities.shadow import Shadow
from entities.colliders.collider import Collider
from entities.items.item import Item
from utilities.profile import profile

MONSTER_IMAGE_DISPLAY_CORRECTION = {ETTIN:12, DARK_BISHOP:0, IRON_LICH:19}
MONSTER_SHADOW_SIZE = {ETTIN:SIZE_MEDIUM, DARK_BISHOP:SIZE_SMALL, IRON_LICH:SIZE_LARGE}
MAX_HEALTH_DICT = {ETTIN:10, DARK_BISHOP:10, IRON_LICH:1666}
BASE_DAMAGE_DICT = {ETTIN:2, DARK_BISHOP:0, IRON_LICH:0}
X_MELEE_RANGE_DICT = {ETTIN:50, DARK_BISHOP:50, IRON_LICH:50}
Y_MELEE_RANGE_DICT = {ETTIN:27, DARK_BISHOP:27, IRON_LICH:27}
X_SIZE_DICT = {ETTIN:20, DARK_BISHOP:20, IRON_LICH:30}
Y_SIZE_DICT = {ETTIN:11, DARK_BISHOP:11, IRON_LICH:17}
INTERRUPT_CHANCE_DICT = {ETTIN:50, DARK_BISHOP:70, IRON_LICH:10}
SELECTED_WEAPON_DICT = {ETTIN:ETTIN_MACE, DARK_BISHOP:BISHOP_MAGIC_MISSILE, IRON_LICH:SPIKE_BALL_SPELL}
WEAPON_NAMES_DICT = {ETTIN:[ETTIN_MACE], DARK_BISHOP:[BISHOP_MAGIC_MISSILE], IRON_LICH:[SPIKE_BALL_SPELL,WHIRLWIND_SPELL,RED_ORB_SPELL]}
ABILITIES_DICT = {ETTIN:[None], DARK_BISHOP:[FLYING, TELEPORT_BLUR], IRON_LICH:[FLYING, SUMMON_MONSTER]}
SPEED_DICT = {ETTIN:1.7, DARK_BISHOP:1.5, IRON_LICH:1.8}
REFLEX_DICT = {ETTIN:2, DARK_BISHOP:2.2, IRON_LICH:3.6}

monster_walk = {ETTIN:ettin_walk, DARK_BISHOP:dark_bishop_walk, IRON_LICH:iron_lich_walk}
monster_attack = {ETTIN:ettin_attack, DARK_BISHOP:dark_bishop_attack, IRON_LICH:iron_lich_attack}
monster_death = {ETTIN:ettin_death, DARK_BISHOP:dark_bishop_death, IRON_LICH:iron_lich_death}
monster_overkill = {ETTIN:ettin_overkill, DARK_BISHOP:dark_bishop_overkill, IRON_LICH:iron_lich_overkill}
monster_pain = {ETTIN:ettin_pain, DARK_BISHOP:dark_bishop_pain, IRON_LICH:iron_lich_pain}

class Monster(pygame.sprite.Sprite):
    def __init__(self,tile_index, name, facing_direction=SECTOR_S):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = MONSTER_IMAGE_DISPLAY_CORRECTION[name]
        self.NAME = name
        self.TYPE = MONSTER

        ###Position variables###
        self.tile_index = tile_index
        self.prevous_tile_index = tile_index
        self.current_tile_position = int(self.tile_index[1] * level_painter.TILE_SIZE[X]+screen_width//2), int(self.tile_index[0] * level_painter.TILE_SIZE[Y] + screen_height//2)
        self.previous_tile_position = self.current_tile_position
        self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
        self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)
        self.direct_proximity_monsters = []
        self.direct_proximity_items = []
        self.direct_proximity_projectiles = []
        self.map_position = int(self.tile_index[1] * level_painter.TILE_SIZE[X]+screen_width//2), int(self.tile_index[0] * level_painter.TILE_SIZE[Y] + screen_height//2)
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        
        ###Object ID###
        self.id = util.generate_entity_id()

        ###Animations###
        #Walk assets
        self.character_walk = monster_walk[name]
        self.character_walk_index = [6,0]
        
        #Attack assets
        self.character_attack = monster_attack[name]
        self.character_attack_index = [6,0]

        #Death assets
        self.character_death = monster_death[name]
        self.character_death_index = 0

        #Overkill assets
        self.character_overkill = monster_overkill[name]
        self.character_overkill_index = 0

        #Pain assets
        self.character_pain = monster_pain[name]
        self.character_pain_index = 0
        self.character_pain_timer = 0

        #Summon assets
        self.summon_flash = summon_flash
        self.summon_flash_index = 0
        self.summon_flash_timer = 0
        self.summon_flash_timer_limit = 1.5

        ###Owned sprites###
        #Colliders
        self.entity_collider_nw    = Collider(self.map_position, self.id, ENTITY_SECTOR, SECTOR_NW)
        self.entity_collider_ne    = Collider(self.map_position, self.id, ENTITY_SECTOR, SECTOR_NE)
        self.entity_collider_sw    = Collider(self.map_position, self.id, ENTITY_SECTOR, SECTOR_SW)
        self.entity_collider_se    = Collider(self.map_position, self.id, ENTITY_SECTOR, SECTOR_SE)
        self.entity_collider_omni  = Collider(self.map_position, self.id, ENTITY_OMNI)

        #Shadow
        self.shadow = Shadow(self.position, self.map_position, self.id, MONSTER_SHADOW_SIZE[name], self.tile_index)
        
        #Sprite lists
        self.entity_collider_sprites     = [self.entity_collider_omni,self.entity_collider_nw,self.entity_collider_ne,self.entity_collider_sw,self.entity_collider_se]
        self.entity_auxilary_sprites     = [[self.shadow],self.entity_collider_sprites]

        ###Initial sprite definition###
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.position))
        self.monster_ai = self.get_monster_ai()

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
        self.is_summoned = False
        self.has_los = False
        self.can_collide = False
        self.can_collide_with_player = True
        self.has_collided = False
        self.active = False
        
        ###Character properties###
        #General
        self.maxhealth = MAX_HEALTH_DICT[name]
        self.health = self.maxhealth


        #Combat
        self.reflex = REFLEX_DICT[name]
        self.base_damage = BASE_DAMAGE_DICT[name]
        self.x_melee_range = X_MELEE_RANGE_DICT[name]
        self.y_melee_range = Y_MELEE_RANGE_DICT[name]
        self.melee_range = self.x_melee_range, self.y_melee_range
        self.x_size = X_SIZE_DICT[name]
        self.y_size = Y_SIZE_DICT[name]
        self.size = self.x_size, self.y_size
        self.attack_interruption_chance = INTERRUPT_CHANCE_DICT[name]
        self.attack_can_be_interrupted = True
        self.selected_weapon = SELECTED_WEAPON_DICT[name]

        #Abilities and weapons list
        self.abilities = self.get_abilities_dict()
        self.weapons = self.get_weapons_dict()

        #Movement
        self.facing_direction = facing_direction
        self.speed = SPEED_DICT[name]
        self.speed_vector = 0,0
        self.noise_timer = 0
        self.noise_timer_limit = 3

    #Update functions
    def update(self):
        if not self.leaving_far_proximity_matrix_margin() and not cutscene_manager.playing_cutscene:
            self.activate()
            
            self.increment_all_weapons_cooldown()
            self.update_abilities()

            if not self.is_summoned:
                if not self.is_dead:
                    self.update_position_and_detect_collisions()
                    self.update_decisions()

                elif not self.is_corpse:
                    self.is_corpse = True
                    if self.NAME is DARK_BISHOP and self.is_overkilled:
                        entity_manager.remove_monster_from_the_game(self)
                    else:
                        entity_manager.fix_all_dead_objects_to_pixel_accuracy()
                        entity_manager.fix_player_position_to_pixel_accuracy()
                        if self.NAME is IRON_LICH:
                            entity_manager.drop_item(self, LICH_EYE)
            
            if not self.monster_ai.is_using_ability:
                self.update_animation()
            self.rect = self.image.get_rect(midbottom = self.position)

        else:
            self.deactivate()

    def update_position(self, vector=None):
        if vector:
            self.map_position = round(self.map_position[0]+vector[0],2), round(self.map_position[1]+vector[1],2)
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1] + self.IMAGE_DISPLAY_CORRECTION,2)
        self.rect.midbottom = self.position
        self.update_owned_sprites_position()
    
    def update_position_and_detect_collisions(self):
        traveled_distance_x = 0
        traveled_distance_y = 0
        frame_travel_x = self.speed_vector[0] * t_ctrl.dt
        frame_travel_y = self.speed_vector[1] * t_ctrl.dt
        x_travel = self.speed_vector[0]
        y_travel = self.speed_vector[1]

        if abs(x_travel) > 6 and abs(x_travel) > abs(y_travel):
            proportion = y_travel/x_travel
            if x_travel > 0:
                x_travel = 6
            else:
                x_travel = -6
            y_travel = x_travel * proportion
        
        elif abs(y_travel) > 3 and abs(y_travel) > abs(x_travel):
            proportion = x_travel/y_travel
            if y_travel > 0:
                y_travel = 3
            else:
                y_travel = -3
            x_travel = y_travel * proportion
        
        while 1:
            if abs(frame_travel_x) - abs(traveled_distance_x) <= abs(x_travel):
                x_travel = frame_travel_x - traveled_distance_x
            if abs(frame_travel_y) - abs(traveled_distance_y) <= abs(y_travel):
                y_travel = frame_travel_y - traveled_distance_y

            traveled_distance_x += x_travel
            traveled_distance_y += y_travel

            self.map_position = round(self.map_position[0]+x_travel,2), round(self.map_position[1]+y_travel,2)
            self.update_owned_sprites_position()
            self.tile_index = util.get_tile_index(self.map_position)
        
            if self.tile_index != self.prevous_tile_index:
                self.previous_tile_position = self.current_tile_position
                self.current_tile_position = int(self.tile_index[1] * level_painter.TILE_SIZE[X]+screen_width//2), int(self.tile_index[0] * level_painter.TILE_SIZE[Y] + screen_height//2)
                self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
                self.direct_proximity_collision_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix)
                self.direct_proximity_items = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, ITEM)
                self.direct_proximity_projectiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, PROJECTILE)
                entity_manager.update_all_nearby_monsters_and_self_direct_proximity_monsters_lists(self.direct_proximity_index_matrix)
                entity_manager.move_entity_in_all_matrices(self.id, MONSTER, self.prevous_tile_index, self.tile_index)
                self.prevous_tile_index = self.tile_index

            collision_manager.monster_vs_monster_collision(self)
            collision_manager.character_vs_level_collision(self)
            collision_manager.monster_vs_impassable_item_collison(self)
            for projectile in self.direct_proximity_projectiles:
                if projectile.launched_by == PLAYER:
                    collision_manager.projectile_vs_entity_collision(projectile)

            if self.leaving_far_proximity_matrix_margin() or not self.is_living or self.has_collided or (abs(traveled_distance_x) >= abs(frame_travel_x) and abs(traveled_distance_y) >= abs(frame_travel_y)):
                break

        self.has_collided = False
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1] + self.IMAGE_DISPLAY_CORRECTION,2)

    def update_decisions(self):
        if self.is_living:
            
            if not self.weapons[self.selected_weapon].is_ready_to_use and len(self.weapons) > 1:
                self.switch_weapons()

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

            elif self.weapons[self.selected_weapon].is_ready_to_use and not self.monster_ai.is_using_ability and (self.monster_ai.monster_can_melee_attack_player() or self.monster_ai.monster_can_range_attack_player()):
                self.initialize_attack_sequence()
            
            else:
                self.monster_ai.use_ability_if_able()
                self.start_walking()
                self.increment_make_noise_timer()
        
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
        
        if not self.is_summoned:
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
        
        else:
            self.character_summon_animation()
    
    def update_owned_sprites_position(self):
        for auxilary_sprites_row in self.entity_auxilary_sprites:
            for auxilary_sprite in auxilary_sprites_row:
                auxilary_sprite.tile_index = self.tile_index
                auxilary_sprite.update_position(self.map_position)
    
    def update_abilities(self):
        for ability in self.abilities:
            if self.abilities[ability] and self.abilities[ability].is_usable:
                self.abilities[ability].update()

    #Getters
    def get_monster_ai(self):
        pathfinding_matrix = None
        
        if FLYING in ABILITIES_DICT[self.NAME]:
            pathfinding_matrix = level_painter.pathfinding_flying_matrix
        else:
            pathfinding_matrix = level_painter.pathfinding_matrix
        
        return monster_ai.Ai(self, pathfinding_matrix, self.tile_index)

    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.NAME is item_name:
                return item


    def get_weapons_dict(self):
        weapon_names_list = WEAPON_NAMES_DICT[self.NAME]
        weapons_dict = {}

        for weapon_name in weapon_names_list:
            weapon = Item(self.tile_index, weapon_name)
            weapons_dict[weapon_name] = weapon

        return weapons_dict

    def get_abilities_dict(self):
        ability_names_list = ABILITIES_DICT[self.NAME]
        abilities_dict = {}

        for ability_name in ability_names_list:
            if ability_name:
                ability = Ability(self, ability_name)
                abilities_dict[ability_name] = ability

        return abilities_dict

    #Animations
    def character_pain_animation(self):
        self.character_pain_timer += 0.05 * t_ctrl.dt
        if self.character_pain_timer >= 1:
            self.is_in_pain = False
            self.character_pain_timer = 0
        if self.is_in_pain:
            self.image = self.character_pain[self.character_pain_index]

    def character_death_animation(self):
        if self.NAME is DARK_BISHOP and self.character_death_index == 0:
            entity_manager.remove_entity_shadow_from_the_game(self)

        self.character_death_index += 0.1 * t_ctrl.dt
        if self.character_death_index >= len(self.character_death)-1:
            self.character_death_index = len(self.character_death)-1
            self.is_dying = False
            self.is_dead = True
        self.image = self.character_death[int(self.character_death_index)]

    def character_overkill_animation(self):
        if self.NAME is DARK_BISHOP and self.character_overkill_index == 0:
            entity_manager.remove_entity_shadow_from_the_game(self)
        
        self.character_overkill_index += 0.1 * t_ctrl.dt
        if self.character_overkill_index >= len(self.character_overkill)-1:
            self.character_overkill_index = len(self.character_overkill)-1
            self.is_overkilled = False
            self.is_dead = True
        self.image = self.character_overkill[int(self.character_overkill_index)]       

    def character_walk_forward_animation(self):
        if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
            self.character_walk_index[1] += 0.1 * t_ctrl.dt
            if self.character_walk_index[1] >= len(self.character_walk[0]):
                self.character_walk_index[1] = 0
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        if self.character_attack_index[1] == 0:
            sound_player.play_monster_atk_prep_sound(self.NAME)
        
        weapon = self.weapons[self.selected_weapon]
        self.character_attack_index[1] += 0.02 * weapon.attack_speed * t_ctrl.dt

        if self.character_attack_index[1] >= 3:
            self.interrupt_attack()
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]     
        else:
            self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]    
            if self.character_attack_index[1] >= 2 and weapon.chainfire > 0:
                if weapon.chainfire_cooldown >= weapon.chainfire_cooldown_limit:
                    if self.weapons[self.selected_weapon].attack_type is MELEE:
                        combat_manager.attack_player_with_melee_attack(self, weapon)
                    elif self.weapons[self.selected_weapon].attack_type is RANGED:
                        combat_manager.attack_player_with_ranged_attack(self, weapon)
                    weapon.chainfire_cooldown = 0
                    weapon.chainfire -= 1
                else:
                    weapon.increment_chainfire_cooldown()
                
                self.character_attack_index[1] = 2

    def character_summon_animation(self):
        char_image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        new_char_img_surf = pygame.Surface(char_image.get_size(),pygame.SRCALPHA)
        new_char_img_surf.blit(char_image,(0,0))
        flash_rect = self.summon_flash[0].get_rect()
        flash_rect.center = char_image.get_rect().center
        new_char_img_surf.blit(self.summon_flash[int(self.summon_flash_index)],flash_rect)
        new_char_img_surf.set_alpha(int(255*self.summon_flash_timer/self.summon_flash_timer_limit))
        self.image = new_char_img_surf
        
        self.summon_flash_timer += 0.02 * t_ctrl.dt
        self.summon_flash_index = (len(self.summon_flash)-1)*self.summon_flash_timer/self.summon_flash_timer_limit
        if self.summon_flash_timer >= self.summon_flash_timer_limit:
            self.is_summoned = False

    def set_character_animation_direction_indices(self):
        for sector in SECTORS:
            if sector == self.facing_direction:
                self.character_walk_index[0] = sector
                self.character_attack_index[0] = sector
                self.character_pain_index = sector           

    #Walking functions
    def start_walking(self):
        if not self.monster_ai.is_using_ability:
            if not self.monster_ai.is_following_path and not self.monster_ai.is_path_finding:
                self.monster_ai.increment_direction_change_decision_timer()
                self.monster_ai.increment_pathfinding_prepare_timer()
                self.set_speed_vector()
            
            else:
                self.use_pathfinding_logic()

    def use_pathfinding_logic(self):
        if self.monster_ai.is_path_finding and not self.monster_ai.is_following_path:
            self.monster_ai.pathfinder.monster_tile_index = self.prevous_tile_index
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
                self.speed_vector = self.speed,0
            elif self.facing_direction == SECTOR_NE:
                self.speed_vector = 0.7*self.speed,-0.41*self.speed
            elif self.facing_direction == SECTOR_N:
                self.speed_vector = 0,-0.55*self.speed
            elif self.facing_direction == SECTOR_NW:
                self.speed_vector = -0.7*self.speed,-0.41*self.speed
            elif self.facing_direction == SECTOR_W:
                self.speed_vector = -self.speed,0
            elif self.facing_direction == SECTOR_SW:
                self.speed_vector = -0.7*self.speed,0.41*self.speed
            elif self.facing_direction == SECTOR_S:
                self.speed_vector = 0,0.55*self.speed
            elif self.facing_direction == SECTOR_SE:
                self.speed_vector = 0.7*self.speed,0.41*self.speed
            
    #Combat functions
    def initialize_attack_sequence(self):
        self.speed_vector = 0,0
                
        if not self.is_preparing_attack and not self.is_attacking:
            self.is_preparing_attack = True
            self.facing_direction = util.get_facing_direction(self.map_position,entity_manager.hero.map_position)
            self.monster_ai.reset_obstacle_avoidance_flags()
            self.monster_ai.end_pathfinding()

        elif self.is_preparing_attack:
            self.monster_ai.increment_attack_decision_timer()
        
        if self.is_attacking and self.is_in_pain and self.attack_can_be_interrupted and self.attack_interupted():
                self.interrupt_attack()

    def take_damage(self, damage):
        if not self.is_summoned:
            self.health -= damage
            
            if self.monster_ai.is_idle:
                self.monster_ai.is_waking_up = True
            
            if self.health > 0:
                self.is_in_pain = True
                if random.choice(range(4)) == 0:
                    sound_player.play_monster_pain_sound(self.NAME)
            else:
                sound_player.stop_monster_pain_sound(self.NAME)
                if not self.is_dying:
                    sound_player.play_monster_death_sound(self.NAME)
                    self.is_living = False
                    self.is_in_pain = False
                    self.is_dying = True
                
                if -(self.maxhealth//2) >= self.health:
                    sound_player.stop_monster_death_sound(self.NAME)
                    if not self.is_overkilled:
                        sound_player.play_monster_overkill_sound(self.NAME)
                    
                    self.is_living = False
                    self.is_in_pain = False
                    self.is_dying = False
                    self.is_overkilled = True

    def interrupt_attack(self):
        self.is_attacking = False
        self.character_attack_index[1] = 0
        self.weapons[self.selected_weapon].is_ready_to_use = False

    def attack_interupted(self):
        if random.choice(range(1,101)) <= self.attack_interruption_chance:
            return True
        self.is_in_pain = False
        self.attack_can_be_interrupted = False
        return False
    
    def emit_los_particle_and_wake_up_if_player_is_seen(self):
        if util.monster_has_line_of_sight(self.map_position):
            hero_sector = util.get_facing_direction(self.map_position,entity_manager.hero.map_position)
            
            if self.monster_ai.is_idle:
                if self.facing_direction+1 == 8 and hero_sector in [7,0,1]:
                    self.monster_ai.direction_change_decision_timer_limit = 50
                    self.monster_ai.is_waking_up = True
                
                elif self.facing_direction+2 == 8 and hero_sector in [6,7,0]:
                    self.monster_ai.direction_change_decision_timer_limit = 50
                    self.monster_ai.is_waking_up = True
                
                elif hero_sector in [self.facing_direction-1,self.facing_direction,self.facing_direction+1]:
                    self.monster_ai.direction_change_decision_timer_limit = 50
                    self.monster_ai.is_waking_up = True

    def increment_all_weapons_cooldown(self):
        for weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            if weapon and not weapon.is_ready_to_use:
                weapon.increment_item_cooldown_timer()

    def switch_weapons(self):
        smallest_eta_use = None
        smallest_eta_use_weap_name = None

        for weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            eta_use = weapon.use_cooldown_limit - weapon.use_cooldown
            
            if weapon.is_ready_to_use:
                smallest_eta_use = 0
                smallest_eta_use_weap_name = weapon_name

            elif smallest_eta_use == None or smallest_eta_use > eta_use:
                smallest_eta_use = eta_use
                smallest_eta_use_weap_name = weapon_name

        self.selected_weapon = smallest_eta_use_weap_name

    #Misc
    def activate(self):
        self.active = True
        self.can_collide = True

    def deactivate(self):
        self.speed_vector = 0,0
        self.can_collide = False
        self.active = False
        self.is_attacking = False
        self.is_preparing_attack = False
        self.weapons[self.selected_weapon].is_ready_to_use = False

        if not self.monster_ai.is_idle:
            self.monster_ai.end_pathfinding()
            self.monster_ai.reset_obstacle_avoidance_flags()

    def increment_make_noise_timer(self):
        if self.noise_timer == 0:
            self.noise_timer_limit += random.choice(range(6))
        self.noise_timer += 0.02 * t_ctrl.dt

        if self.noise_timer >= self.noise_timer_limit:
            self.noise_timer_limit = 5
            self.noise_timer = 0
            sound_player.play_monster_noise_sound(self.NAME)


    #Conditions
    def leaving_far_proximity_matrix_margin(self):
        hero_tile_index = entity_manager.hero.tile_index
        tile_row_offset = int(screen_height/2/TILE_SIZE[Y])+1
        tile_col_offset = int(screen_width/2/TILE_SIZE[X])+1
        if abs(self.tile_index[0]-hero_tile_index[0]) > tile_row_offset or abs(self.tile_index[1]-hero_tile_index[1]) > tile_col_offset:
            return True
        return False