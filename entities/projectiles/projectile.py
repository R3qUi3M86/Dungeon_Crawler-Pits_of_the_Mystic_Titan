import random
import pygame
import math
from images.projectiles.projectile_images import *
from entities.shadow import Shadow
from entities.colliders.collider import Collider
from utilities.constants import *
from utilities import util
from utilities import level_painter
from utilities import collision_manager
from utilities.level_painter import TILE_SIZE
from utilities import entity_manager
from utilities import combat_manager
from utilities import t_ctrl
from sounds import sound_player

PROJECTILE_DISPLAY_CORRECTION = {CROSSBOW_BOLT:-30, NECRO_BALL:-5, MAGIC_MISSILE:-30, SPIKE_BALL:-15, SPIKE_SHARD:-30, WHIRLWIND:0, RED_ORB:-5}
PROJECTILE_SPEED_DICT = {CROSSBOW_BOLT:13, NECRO_BALL:8, MAGIC_MISSILE:6, SPIKE_BALL:8, SPIKE_SHARD:13, WHIRLWIND:4, RED_ORB:5}
PROJECTILE_SIZE_DICT = {CROSSBOW_BOLT:(15, 8), NECRO_BALL:(20, 11), MAGIC_MISSILE:(13, 7), SPIKE_BALL:(15, 8), SPIKE_SHARD:(9, 5), WHIRLWIND:(60, 34), RED_ORB:(18, 10)}
PROJECTILE_STATIC_IMG_DICT = {CROSSBOW_BOLT:emerald_crossbow_bolt_shot[0], NECRO_BALL:necrolight_ball_shot[0], MAGIC_MISSILE:bishop_magic_missile_shot[0], SPIKE_BALL:spike_ball[0], SPIKE_SHARD:spike_shard[0], WHIRLWIND:whirlwind[0], RED_ORB:red_orb[0]}
PROJECTILE_DYNAMIC_IMG_DICT = {CROSSBOW_BOLT:emerald_crossbow_bolt_shot, NECRO_BALL:necrolight_ball_shot, MAGIC_MISSILE:bishop_magic_missile_shot, SPIKE_BALL:spike_ball, SPIKE_SHARD:spike_shard, WHIRLWIND:whirlwind, RED_ORB:red_orb}
PROJECTILE_DESTRUCT_IMG_DICT = {CROSSBOW_BOLT:emerald_crossbow_bolt_destruct, NECRO_BALL:necrolight_ball_destruct, MAGIC_MISSILE:bishop_magic_missile_destruct, SPIKE_BALL:spike_ball_destruct, SPIKE_SHARD:[spike_shard_destruct], WHIRLWIND:whirlwind_destruct, RED_ORB:red_orb_destruct}
PROJECTILE_GLOW_DICT = {CROSSBOW_BOLT:GREEN_GLOW, NECRO_BALL:RED_GLOW, MAGIC_MISSILE:GREEN_GLOW, SPIKE_BALL:BLUE_GLOW, SPIKE_SHARD:BLUE_GLOW, WHIRLWIND:None, RED_ORB:RED_GLOW}
PROJECTILE_SHADOW_SIZE_DICT = {CROSSBOW_BOLT:SIZE_SMALL, NECRO_BALL:SIZE_MEDIUM, MAGIC_MISSILE:SIZE_MEDIUM, SPIKE_BALL:SIZE_MEDIUM, SPIKE_SHARD:SIZE_TINY, WHIRLWIND:SIZE_TINY, RED_ORB:SIZE_LARGE}

class Projectile(pygame.sprite.Sprite):
    def __init__(self, tile_index, position, map_pos, damage, angle, name, launched_by):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = PROJECTILE_DISPLAY_CORRECTION[name]
        self.NAME = name
        self.TYPE = PROJECTILE

        ###Position variables###
        self.launched_by = launched_by
        self.tile_index = tile_index
        self.prevous_tile_index = tile_index
        self.position = position
        self.map_position = map_pos
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION
        self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
        self.direct_proximity_wall_like_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, WALL_LIKE)
        self.direct_proximity_characters = self.get_direct_proximity_characters_list()
        self.direct_proximity_coolidable_items = self.get_direct_proximity_colidable_items()

        ###Object ID###
        self.id = util.generate_entity_id()
        
        ###Animations###
        #Static image assets
        self.projectile_static_image = PROJECTILE_STATIC_IMG_DICT[self.NAME]

        #Dynamic image assets
        self.projectile_dynamic_images = PROJECTILE_DYNAMIC_IMG_DICT[self.NAME]
        self.projectile_dynamic_index = 0

        #Destruction assets
        self.projectile_destuction_image_list = PROJECTILE_DESTRUCT_IMG_DICT[self.NAME]
        self.projectile_destruction_index = 0

        ###Owned sprites###
        #Colliders
        self.projectile_collider = Collider(self.position, self.id, PROJECTILE)

        #Shadow
        self.shadow = Shadow(self.position, self.map_position, self.id, PROJECTILE_SHADOW_SIZE_DICT[name], self.tile_index, PROJECTILE_GLOW_DICT[name])

        #Sprite lists
        self.entity_auxilary_sprites = [self.projectile_collider, self.shadow]

        #####General variables#####
        ###Status flags###
        self.has_impacted = False
        self.is_disintegrating = False
        self.is_destroyed = False

        ###Projectile properties###
        #General
        self.angle = angle
        self.damage = damage
        self.damage_ticks = self.get_damage_ticks()
        self.tick_cooldown = 0
        self.tick_cooldown_limit = self.get_tick_cooldown_limit()
        self.speed = PROJECTILE_SPEED_DICT[self.NAME]
        self.size = PROJECTILE_SIZE_DICT[self.NAME]
        
        if self.NAME is not SPIKE_SHARD:
            self.travel_speed = util.get_travel_speed(self.angle, self.speed)
        else:
            self.travel_speed = util.get_elipse_travel_speed(self.angle, self.speed)
        
        self.delta_travel_speed = 0,0
        self.image = self.get_image_and_set_collider_image()
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.effects = []

    #Updates
    def update(self):
        if self.NAME is WHIRLWIND:
            self.rotate_speed_vector()

        if self.leaving_far_proximity_matrix_margin() or self.is_destroyed:
            entity_manager.remove_projectile_from_from_matrices_and_lists(self)
        
        elif self.has_impacted:
            self.tick_cooldown += 0.0167 * t_ctrl.dt
            if self.NAME is WHIRLWIND:
                self.travel_animation()
                self.pull_player_into_whirlwind()
            
            if self.tick_cooldown >= self.tick_cooldown_limit:
                self.damage_ticks -= 1
                self.has_impacted = False
                self.tick_cooldown = 0
            
            if self.damage_ticks == 0:
                self.has_impacted = False
                self.is_disintegrating = True
                self.travel_speed = 0,0
                self.delta_travel_speed = 0,0
                entity_manager.remove_entity_shadow_from_the_game(self)
                sound_player.play_projectile_impact_sound(self.NAME)
                if self.NAME is SPIKE_BALL:
                    self.launch_spike_shards()
                elif self.NAME is RED_ORB or self.NAME is NECRO_BALL:
                    self.deal_aoe_damage()
        
        elif self.is_disintegrating:
             self.disintegration_animation()
        
        else:
            traveled_distance_x = 0
            traveled_distance_y = 0
            frame_travel_x = (self.travel_speed[0] + self.delta_travel_speed[0]) * t_ctrl.dt
            frame_travel_y = (self.travel_speed[1] + self.delta_travel_speed[1]) * t_ctrl.dt
            x_travel = self.travel_speed[0] + self.delta_travel_speed[0]
            y_travel = self.travel_speed[1] + self.delta_travel_speed[1]

            if abs(x_travel) > 25 and abs(x_travel) > abs(y_travel):
                proportion = y_travel/x_travel
                if x_travel > 0:
                    x_travel = 25
                else:
                    x_travel = -25
                y_travel = x_travel * proportion
            
            elif abs(y_travel) > 15 and abs(y_travel) > abs(x_travel):
                proportion = x_travel/y_travel
                if y_travel > 0:
                    y_travel = 15
                else:
                    y_travel = -15
                x_travel = y_travel * proportion
            
            while not self.has_impacted and (abs(traveled_distance_x) < abs(frame_travel_x) or abs(traveled_distance_y) < abs(frame_travel_y)):
                if abs(frame_travel_x) - abs(traveled_distance_x) <= abs(x_travel):
                    x_travel = frame_travel_x - traveled_distance_x
                if abs(frame_travel_y) - abs(traveled_distance_y) <= abs(y_travel):
                    y_travel = frame_travel_y - traveled_distance_y

                traveled_distance_x += x_travel
                traveled_distance_y += y_travel

                self.map_position = round(self.map_position[0] + x_travel,2), round(self.map_position[1] + y_travel,2)
                self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
                self.update_owned_sprites_position()
                self.tile_index = util.get_tile_index(self.map_position)

                if self.tile_index != self.prevous_tile_index:
                    self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
                    self.direct_proximity_wall_like_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, WALL_LIKE)
                    self.direct_proximity_characters = self.get_direct_proximity_characters_list()
                    self.direct_proximity_coolidable_items = self.get_direct_proximity_colidable_items()
                    entity_manager.move_entity_in_all_matrices(self.id, PROJECTILE, self.prevous_tile_index, self.tile_index)
                    self.prevous_tile_index = self.tile_index
              
                if self.leaving_far_proximity_matrix_margin():
                    self.has_impacted = True
                    entity_manager.remove_projectile_from_from_matrices_and_lists(self)

                collision_manager.projectile_vs_entity_collision(self)
                collision_manager.projectile_vs_level_collision(self)

            if len(self.projectile_dynamic_images) >= 2:
                self.travel_animation()
            
            self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
            self.rect.midbottom = self.image_position

    def update_position(self, vector=None):
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
        self.rect.midbottom = self.image_position
        self.update_owned_sprites_position()

    def update_owned_sprites_position(self):
        for auxilary_sprite in self.entity_auxilary_sprites:
            auxilary_sprite.update_position(self.position)

    #Getters
    def get_image_and_set_collider_image(self):
        total_travel_speed = math.sqrt((self.travel_speed[0]*self.travel_speed[0])+(self.travel_speed[1]*self.travel_speed[1]))
        scaling_factor = total_travel_speed/self.speed
        self.set_collider_image_and_mask(scaling_factor)
        
        if self.NAME in [CROSSBOW_BOLT, SPIKE_SHARD]:
            static_image_width = self.projectile_static_image.get_width()
            static_image_height = self.projectile_static_image.get_height()
            scaled_image = pygame.transform.scale(self.projectile_static_image,(static_image_width*scaling_factor,static_image_height))
            
            final_image = pygame.transform.rotate(scaled_image,self.angle)

            return final_image
    
        else:
            return self.projectile_static_image

    def set_collider_image_and_mask(self, scaling_factor):
        self.projectile_collider.image = pygame.transform.scale(self.projectile_collider.image, (self.projectile_collider.image.get_width()*scaling_factor,self.projectile_collider.image.get_height()))
        self.projectile_collider.image = pygame.transform.rotate(self.projectile_collider.image, self.angle)
        self.projectile_collider.mask = pygame.mask.from_surface(self.projectile_collider.image)
        self.projectile_collider.rect = self.projectile_collider.image.get_rect(center = (self.position))

    def get_direct_proximity_characters_list(self):
        if self.launched_by is PLAYER:
            return entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, MONSTER)
        else:
            return [entity_manager.hero]
    
    def get_direct_proximity_colidable_items(self):
        items_list = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, ITEM)
        filtered_item_list = []
        for item in items_list:
            if item.can_collide and not item.is_pickable and not item.is_falling_apart and not item.is_destroyed:
                filtered_item_list.append(item)

        return filtered_item_list

    def get_damage_ticks(self):
        if self.NAME is WHIRLWIND:
            return 5
        else:
            return 1

    def get_tick_cooldown_limit(self):
        if self.NAME is WHIRLWIND:
            return 0.2
        else:
            return 0

    #Animations
    def travel_animation(self):
        self.projectile_dynamic_index += 0.075 * t_ctrl.dt
        if self.projectile_dynamic_index >= len(self.projectile_dynamic_images):
            self.projectile_dynamic_index = 0
        self.image = self.projectile_dynamic_images[int(self.projectile_dynamic_index)]            
        #self.rect = self.image.get_rect(midbottom = (self.image_position))

    def disintegration_animation(self):
        if self.projectile_destruction_index >= len(self.projectile_destuction_image_list):
            self.is_destroyed = True
        else:
            self.image = self.projectile_destuction_image_list[int(self.projectile_destruction_index)]
            if self.NAME is RED_ORB:
                image_size = self.image.get_size()
                self.image = pygame.transform.scale(self.image,(2*image_size[0], 2*image_size[1]))
            self.projectile_destruction_index += 0.075 * t_ctrl.dt
        self.rect = self.image.get_rect(midbottom = (self.image_position))

    #Special behaviours
    def launch_spike_shards(self):
        for i in range(72):
            combat_manager.launch_projectile(self.tile_index,self.position,self.map_position,i*5,self,MONSTER,-3)

    def deal_aoe_damage(self):
        if not entity_manager.hero.is_dead and not entity_manager.hero.is_overkilled and util.elipses_intersect(self.map_position,entity_manager.hero.map_position,(80,44), entity_manager.hero.size):
            entity_manager.hero.take_damage(self.damage//2)
        for character in entity_manager.far_proximity_character_sprites_list:
            if character is not entity_manager.hero and not character.is_dead and not character.is_overkilled:
                 if util.elipses_intersect(self.map_position,character.map_position,(100,55), character.size):
                    character.take_damage(self.damage//2)

        for item in self.direct_proximity_coolidable_items:
            if item.is_destructible:
                item.destroy_item()

    def rotate_speed_vector(self):
        self.angle+= random.choice(range(10))*t_ctrl.dt
        self.delta_travel_speed = util.get_travel_speed(self.angle,5)

    def pull_player_into_whirlwind(self):
        if util.elipses_intersect(self.map_position,entity_manager.hero.map_position,self.size,entity_manager.hero.size):
            angle = util.get_total_angle(entity_manager.hero.map_position, self.map_position)
            pull_vector = util.get_travel_speed(angle,6)
            entity_manager.hero.speed_scalar=(entity_manager.hero.speed_scalar[0]+pull_vector[0]*t_ctrl.dt), (entity_manager.hero.speed_scalar[1]+pull_vector[1]*t_ctrl.dt)


    #Conditions
    def leaving_far_proximity_matrix_margin(self):
        hero_tile_index = entity_manager.hero.tile_index
        tile_row_offset = screen_height//2//TILE_SIZE[Y]+far_matrix_offset_y//3
        tile_col_offset = screen_width//2//TILE_SIZE[X]+far_matrix_offset_x//3
        if abs(self.tile_index[0]-hero_tile_index[0]) > tile_row_offset or abs(self.tile_index[1]-hero_tile_index[1]) > tile_col_offset:
            return True
        return False

    def is_outside_of_map(self):
        if self.tile_index[0] < 0 or self.tile_index[0]+1 >= len(level_painter.level_layout) or self.tile_index[1] < 0 or self.tile_index[1]+1 > len(level_painter.level_layout[0]):
            return True