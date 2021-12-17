import random
import numpy as np

from pygame.constants import SRCALPHA
from utilities import util
from utilities import entity_manager
from utilities.constants import *
from sounds import sound_player

USABLE_ABILITIES_DICT = {FLYING:False, TELEPORT_BLUR: True, SUMMON_MONSTER: True}


class Ability():
    def __init__(self, owner, name):
        ABILITIES_COOLDOWN_DICT = {FLYING:0, TELEPORT_BLUR: 4 + random.choice(np.arange(0,1,0.05)), SUMMON_MONSTER: 9}

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

        #Blur visual effect variables
        self.monster_original_img_disp_corr = owner.IMAGE_DISPLAY_CORRECTION
        self.monster_original_image = pygame.Surface(self.monster.image.get_size(),SRCALPHA)
        self.monster_1_blur_image = pygame.Surface(self.monster.image.get_size(),SRCALPHA)
        self.monster_2_blur_image = pygame.Surface(self.monster.image.get_size(),SRCALPHA)
        self.monster_3_blur_image = pygame.Surface(self.monster.image.get_size(),SRCALPHA)
        self.monster_4_blur_image = pygame.Surface(self.monster.image.get_size(),SRCALPHA)
        self.monster_5_blur_image = pygame.Surface(self.monster.image.get_size(),SRCALPHA)
        self.monster_current_pos = owner.map_position
        self.monster_1_frame_back_pos = owner.map_position
        self.monster_2_frame_back_pos = owner.map_position
        self.monster_3_frame_back_pos = owner.map_position
        self.monster_4_frame_back_pos = owner.map_position
        self.monster_5_frame_back_pos = owner.map_position
        self.travel_speed = None

    #Updates
    def update(self):
        if self.is_usable:
            if self.is_being_used:
                if self.is_ready_to_use:
                    self.apply_ability_effects()
                    self.is_ready_to_use = False
                if self.NAME is TELEPORT_BLUR:
                    self.apply_blur_visual_effect()

                self.increment_use_speed_timer()
            
            elif not self.is_ready_to_use:
                self.increment_cooldown_timer()
        
    #Abilities effects
    def apply_ability_effects(self):
        if self.NAME is TELEPORT_BLUR:
            self.use_teleport_blur_ability()
        elif self.NAME is SUMMON_MONSTER:
            self.use_summon_monster_ability()

    def set_blur_visual_effects(self):
        self.monster_original_image.blit(self.monster.image, (0,0))
        self.monster_1_blur_image.blit(self.monster.image, (0,0))
        self.monster_2_blur_image.blit(self.monster.image, (0,0))
        self.monster_3_blur_image.blit(self.monster.image, (0,0))
        self.monster_4_blur_image.blit(self.monster.image, (0,0))
        self.monster_5_blur_image.blit(self.monster.image, (0,0))
        self.monster_1_blur_image.set_alpha(80)
        self.monster_2_blur_image.set_alpha(80)
        self.monster_3_blur_image.set_alpha(80)
        self.monster_4_blur_image.set_alpha(80)
        self.monster_5_blur_image.set_alpha(80)

        self.monster_current_pos = self.monster.map_position
        self.monster_1_frame_back_pos = self.monster.map_position
        self.monster_2_frame_back_pos = self.monster.map_position
        self.monster_3_frame_back_pos = self.monster.map_position
        self.monster_4_frame_back_pos = self.monster.map_position
        self.monster_5_frame_back_pos = self.monster.map_position

    def apply_blur_visual_effect(self):
        self.monster_5_frame_back_pos = self.monster_4_frame_back_pos
        self.monster_4_frame_back_pos = self.monster_3_frame_back_pos
        self.monster_3_frame_back_pos = self.monster_2_frame_back_pos
        self.monster_2_frame_back_pos = self.monster_1_frame_back_pos
        self.monster_1_frame_back_pos = self.monster_current_pos
        self.monster_current_pos = self.monster.map_position
        self.monster.IMAGE_DISPLAY_CORRECTION = 38

        new_image_surf = pygame.Surface((161, 145), SRCALPHA)

        x_1_delta = self.monster_1_frame_back_pos[0]-self.monster_current_pos[0]
        x_2_delta = self.monster_2_frame_back_pos[0]-self.monster_current_pos[0]
        x_3_delta = self.monster_3_frame_back_pos[0]-self.monster_current_pos[0]
        x_4_delta = self.monster_4_frame_back_pos[0]-self.monster_current_pos[0]
        x_5_delta = self.monster_5_frame_back_pos[0]-self.monster_current_pos[0]
        y_1_delta = self.monster_1_frame_back_pos[1]-self.monster_current_pos[1]
        y_2_delta = self.monster_2_frame_back_pos[1]-self.monster_current_pos[1]
        y_3_delta = self.monster_3_frame_back_pos[1]-self.monster_current_pos[1]
        y_4_delta = self.monster_4_frame_back_pos[1]-self.monster_current_pos[1]
        y_5_delta = self.monster_5_frame_back_pos[1]-self.monster_current_pos[1]
        blur_1_pos = 35+x_1_delta, 35+y_1_delta
        blur_2_pos = 35+x_2_delta, 35+y_2_delta
        blur_3_pos = 35+x_3_delta, 35+y_3_delta
        blur_4_pos = 35+x_4_delta, 35+y_4_delta
        blur_5_pos = 35+x_5_delta, 35+y_5_delta

        if y_1_delta <= 0:
            if self.use_speed_timer <= self.use_speed-0.0167*5:
                new_image_surf.blit(self.monster_2_blur_image,(blur_5_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*4:
                new_image_surf.blit(self.monster_1_blur_image,(blur_4_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*3:
                new_image_surf.blit(self.monster_1_blur_image,(blur_3_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*2:
                new_image_surf.blit(self.monster_2_blur_image,(blur_2_pos))
            if self.use_speed_timer <= self.use_speed-0.0167:
                new_image_surf.blit(self.monster_1_blur_image,(blur_1_pos))
            new_image_surf.blit(self.monster_original_image,(35,35))
        else:
            new_image_surf.blit(self.monster_original_image,(35,35))
            if self.use_speed_timer <= self.use_speed-0.0167:
                new_image_surf.blit(self.monster_1_blur_image,(blur_1_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*2:
                new_image_surf.blit(self.monster_2_blur_image,(blur_2_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*3:
                new_image_surf.blit(self.monster_1_blur_image,(blur_3_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*4:
                new_image_surf.blit(self.monster_1_blur_image,(blur_4_pos))
            if self.use_speed_timer <= self.use_speed-0.0167*5:
                new_image_surf.blit(self.monster_2_blur_image,(blur_5_pos))

        self.monster.image = new_image_surf

    def use_teleport_blur_ability(self):
        self.set_blur_visual_effects()

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
        self.travel_speed = travel_speed
        self.monster.speed_vector = travel_speed
        
        sound_player.play_ability_use_sound(self.NAME)

    def use_summon_monster_ability(self):
        summon_name = random.choice([ETTIN,DARK_BISHOP])
        summon_monster = entity_manager.get_new_monster(summon_name)
        summon_tile = self.get_summon_tile(summon_monster)
        if summon_tile:
            entity_manager.summon_new_monster(summon_name,summon_tile)

    #Getters
    def get_summon_tile(self, summon_monster):
        idices_matrix = self.monster.direct_proximity_index_matrix
        possible_summon_tiles = []
        for row in idices_matrix:
            for cell in row:
                legal_tile = True
                
                for entity in entity_manager.all_entity_and_shadow_sprite_group_matrix[cell[0]][cell[1]]:
                    if entity.sprite.TYPE is ITEM and entity.sprite.NAME in [FLAME_PEDESTAL1, SCULPTURE1, STALAG_S, STALAG_L, RUBY_PEDESTAL_EMPTY]:
                        legal_tile = False
                        break
                
                if legal_tile:
                    if FLYING in summon_monster.abilities and entity_manager.level_sprites_matrix[cell[0]][cell[1]].TYPE not in WALL_LIKE:
                        possible_summon_tiles.append(cell)
                
                    elif entity_manager.level_sprites_matrix[cell[0]][cell[1]].TYPE not in IMPASSABLE_TILES:
                        possible_summon_tiles.append(cell)

        if self.monster.tile_index in possible_summon_tiles:
            possible_summon_tiles.remove(self.monster.tile_index)
        
        return random.choice(possible_summon_tiles)


    #Timers
    def increment_use_speed_timer(self):
        if self.use_speed_timer >= self.use_speed:
            self.is_being_used = False
            self.monster.monster_ai.is_using_ability = False
            self.use_speed_timer = 0
            if self.NAME is TELEPORT_BLUR:
                self.monster.IMAGE_DISPLAY_CORRECTION = self.monster_original_img_disp_corr
                self.monster.image = self.monster_original_image
                self.monster.can_collide_with_player = True
        self.use_speed_timer += 0.0167

    def increment_cooldown_timer(self):
        if self.cooldown_timer >= self.cooldown:
            self.is_ready_to_use = True
            self.cooldown_timer = 0
        self.cooldown_timer += 0.0167