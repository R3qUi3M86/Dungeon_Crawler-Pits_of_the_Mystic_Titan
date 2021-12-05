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
from sounds import sound_player

PROJECTILE_SPEED_DICT = {CROSSBOW_BOLT:13, MAGIC_MISSILE:6}
PROJECTILE_SIZE_DICT = {CROSSBOW_BOLT:(15, 8), MAGIC_MISSILE:(13, 7)}
PROJECTILE_STATIC_IMG_DICT = {CROSSBOW_BOLT:emerald_crossbow_bolt_shot[0], MAGIC_MISSILE:bishop_magic_missile_shot[0]}
PROJECTILE_DYNAMIC_IMG_DICT = {CROSSBOW_BOLT:emerald_crossbow_bolt_shot, MAGIC_MISSILE:bishop_magic_missile_shot}
PROJECTILE_DESTRUCT_IMG_DICT = {CROSSBOW_BOLT:emerald_crossbow_bolt_destruct, MAGIC_MISSILE:bishop_magic_missile_destruct}
PROJECTILE_GLOW_DICT = {CROSSBOW_BOLT:GREEN_GLOW, MAGIC_MISSILE:GREEN_GLOW}
PROJECTILE_SHADOW_SIZE_DICT = {CROSSBOW_BOLT:SIZE_SMALL, MAGIC_MISSILE:SIZE_MEDIUM}

class Projectile(pygame.sprite.Sprite):
    def __init__(self, tile_index, position, map_pos, damage, angle, name, launched_by):
        super().__init__()
        ###Constants###
        self.IMAGE_DISPLAY_CORRECTION = -30
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
        self.speed = PROJECTILE_SPEED_DICT[self.NAME]
        self.size = PROJECTILE_SIZE_DICT[self.NAME]
        self.travel_speed = self.get_travel_speed()
        self.image = self.get_image_and_set_collider_image()
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.effects = []

    #Updates
    def update(self):
        if self.leaving_far_proximity_matrix_margin() or self.is_destroyed:
            entity_manager.remove_projectile_from_from_matrices_and_lists(self)
        
        elif self.has_impacted:
            self.has_impacted = False
            self.is_disintegrating = True
            self.travel_speed = 0,0
            entity_manager.remove_entity_shadow_from_the_game(self)
            sound_player.play_projectile_impact_sound(self.NAME)
        
        elif self.is_disintegrating:
             self.disintegration_animation()
        
        else:
            #Relative speed projectile
            if self.speed != -1:
                self.map_position = round((self.map_position[0] + self.travel_speed[0]),2), round((self.map_position[1] + self.travel_speed[1]),2)
                self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
                self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
                self.rect = self.image.get_rect(midbottom = (self.image_position))
                self.update_owned_sprites_position()
                self.tile_index = util.get_tile_index(self.map_position)

                if self.is_outside_of_map():
                    self.has_impacted = True

                if self.tile_index != self.prevous_tile_index:
                    self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
                    self.direct_proximity_wall_like_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, WALL_LIKE)
                    self.direct_proximity_characters = self.get_direct_proximity_characters_list()
                    entity_manager.move_entity_in_all_matrices(self.id, PROJECTILE, self.prevous_tile_index, self.tile_index)
                    self.prevous_tile_index = self.tile_index

                if len(self.projectile_dynamic_images) >= 2:
                    self.travel_animation()
            
            #Light speed projectile
            else:
                while not self.has_impacted:
                    self.map_position = round((self.map_position[0] + self.travel_speed[0]),2), round((self.map_position[1] + self.travel_speed[1]),2)
                    self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
                    self.update_owned_sprites_position()
                    self.tile_index = util.get_tile_index(self.map_position)

                    if self.tile_index != self.prevous_tile_index:
                        self.direct_proximity_index_matrix = util.get_vicinity_matrix_indices_for_index(self.tile_index)
                        self.direct_proximity_wall_like_tiles = entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, WALL_LIKE)
                        self.direct_proximity_characters = self.get_direct_proximity_characters_list()
                        entity_manager.move_entity_in_all_matrices(self.id, PROJECTILE, self.prevous_tile_index, self.tile_index)
                        self.prevous_tile_index = self.tile_index
                
                    self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION
                    self.rect = self.image.get_rect(midbottom = (self.image_position))
                    collision_manager.projectile_vs_entity_collision(self)
                    collision_manager.projectile_vs_level_collision(self)
                    if self.leaving_far_proximity_matrix_margin():
                        self.has_impacted = True
                        entity_manager.remove_projectile_from_from_matrices_and_lists(self)

                self.image = self.projectile_destuction_image_list[int(self.projectile_destruction_index)]

    def update_position(self, vector=None):
        self.position = round(self.map_position[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(self.map_position[1] - entity_manager.hero.map_position[1] + player_position[1],2)
        self.image_position = self.position[0], self.position[1] + self.IMAGE_DISPLAY_CORRECTION       
        self.rect = self.image.get_rect(midbottom = (self.image_position))
        self.update_owned_sprites_position()

    def update_owned_sprites_position(self):
        for auxilary_sprite in self.entity_auxilary_sprites:
            auxilary_sprite.update_position(self.position)

    #Getters
    def get_image_and_set_collider_image(self):
        total_travel_speed = math.sqrt((self.travel_speed[0]*self.travel_speed[0])+(self.travel_speed[1]*self.travel_speed[1]))
        scaling_factor = total_travel_speed/self.speed
        
        static_image_width = self.projectile_static_image.get_width()
        static_image_height = self.projectile_static_image.get_height()
        scaled_image = pygame.transform.scale(self.projectile_static_image,(static_image_width*scaling_factor,static_image_height))
        
        final_image = pygame.transform.rotate(scaled_image,self.angle)

        self.set_collider_image_and_mask(scaling_factor)

        return final_image

    def set_collider_image_and_mask(self, scaling_factor):
        self.projectile_collider.image = pygame.transform.scale(self.projectile_collider.image, (self.projectile_collider.image.get_width()*scaling_factor,self.projectile_collider.image.get_height()))
        self.projectile_collider.image = pygame.transform.rotate(self.projectile_collider.image, self.angle)
        self.projectile_collider.mask = pygame.mask.from_surface(self.projectile_collider.image)
        self.projectile_collider.rect = self.projectile_collider.image.get_rect(center = (self.position))

    def get_travel_speed(self):
        x_factor = math.cos(math.radians(self.angle))
        y_factor = 0.55*math.sin(math.radians(self.angle))

        x_factored_speed = x_factor*self.speed
        y_factored_speed = y_factor*self.speed

        total_factored_speed = math.sqrt((x_factored_speed*x_factored_speed) + (y_factored_speed*y_factored_speed))

        x_factor_travel = math.cos(math.radians(self.angle))
        y_factor_travel = math.sin(math.radians(self.angle))

        travel_speed = x_factor_travel*total_factored_speed, -y_factor_travel*total_factored_speed

        return travel_speed

    def get_direct_proximity_characters_list(self):
        if self.launched_by is PLAYER:
            return entity_manager.get_direct_proximity_objects_list(self.direct_proximity_index_matrix, MONSTER)
        else:
            return [entity_manager.hero]
    
    #Animations
    def travel_animation(self):
        if int(self.projectile_dynamic_index) == len(self.projectile_dynamic_images):
            self.projectile_dynamic_index = 0
        else:
            self.image = self.projectile_dynamic_images[int(self.projectile_dynamic_index)]
            self.projectile_dynamic_index += 0.075
        #self.rect = self.image.get_rect(midbottom = (self.image_position))

    def disintegration_animation(self):
        if int(self.projectile_destruction_index) == len(self.projectile_destuction_image_list):
            self.is_destroyed = True
        else:
            self.image = self.projectile_destuction_image_list[int(self.projectile_destruction_index)]
            self.projectile_destruction_index += 0.075
        self.rect = self.image.get_rect(midbottom = (self.image_position))

    
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