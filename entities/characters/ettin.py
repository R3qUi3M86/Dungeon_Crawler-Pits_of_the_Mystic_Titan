import pygame
import random
from settings import *
from sounds import sound_player
from utilities import util
from utilities import combat_manager
from utilities import collision_manager
from utilities import entity_manager
from utilities import level_painter
from utilities import monster_ai
from utilities.constants import *
from images.characters.ettin_images import *
from entities.characters import unique_player_object
from entities.shadow import Shadow
from entities.colliders.collider import Collider

class Ettin(pygame.sprite.Sprite):
    def __init__(self,tile_index):
        super().__init__()
        ###Constants###
        self.SPRITE_DISPLAY_CORRECTION = 12
        self.NAME = ETTIN
        self.TYPE = MONSTER

        ###Position variables###
        self.tile_index = tile_index
        self.position = level_painter.get_tile_position(tile_index)
        self.map_position = round(self.position[0]-player_position[0]+unique_player_object.HERO.tile_index[0],2), round(self.position[1]-player_position[1]+unique_player_object.HERO.tile_index[1],2)
        self.sprite_position = self.position[0], self.position[1] + self.SPRITE_DISPLAY_CORRECTION
        
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
        self.entity_collider_nw = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_NW)
        self.entity_collider_ne = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_NE)
        self.entity_collider_sw = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_SW)
        self.entity_collider_se = Collider(self.position, self.id, ENTITY_SECTOR, SECTOR_SE)
        self.entity_collider_omni = Collider(player_position, self.id, ENTITY_OMNI)
        self.pathfinding_collider = Collider(self.position, self.id, SQUARE)

        #Melee sectors
        self.melee_collider_e  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_E)
        self.melee_collider_ne = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_NE)
        self.melee_collider_n  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_N)
        self.melee_collider_nw = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_NW)
        self.melee_collider_w  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_W)
        self.melee_collider_sw = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_SW)
        self.melee_collider_s  = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_S)
        self.melee_collider_se = Collider(self.position, self.id, MELEE_SECTOR, SECTOR_SE)

        #Shadow
        self.shadow = Shadow(self.position, self.id, SIZE_MEDIUM)
        
        #Sprite lists
        self.entity_collider_sprites     = [self.entity_collider_omni,self.entity_collider_nw,self.entity_collider_ne,self.entity_collider_sw,self.entity_collider_se,self.pathfinding_collider]
        self.entity_melee_sector_sprites = [self.melee_collider_e,self.melee_collider_ne,self.melee_collider_n,self.melee_collider_nw,self.melee_collider_w,self.melee_collider_sw,self.melee_collider_s,self.melee_collider_se]
        self.entity_auxilary_sprites     = [[self.shadow],self.entity_melee_sector_sprites,self.entity_collider_sprites]

        ###Initial sprite definition###
        self.image = self.character_walk[self.character_walk_index[0]][self.character_walk_index[1]]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))

        ###General variables###
        #Status flags
        self.is_monster = True
        self.is_attacking = False
        self.is_living = True
        self.is_dying = False
        self.is_overkilled = False
        self.is_in_pain = False
        self.is_dead = False
        self.is_corpse = False
        self.has_los = False
        
        #Character properties
        self.health = 10
        self.maxhealth = 10
        self.damage = 0
        self.attack_interruption_chance = 50
        self.attack_can_be_interrupted = True
        self.can_shoot = False
        self.projectile_type = None
        self.abilities = []
        self.facing_direction = SECTOR_S
        self.speed = 1.4,1
        self.speed_vector = 0,0
        self.monster_ai = monster_ai.Ai(self, collision_manager.pathfinding_matrix, tile_index)

    #Update functions
    def update(self):
        self.position = round((self.position[0] + self.speed_vector[0]),2),round((self.position[1] + self.speed_vector[1]),2)
        self.map_position = round(self.position[0]+unique_player_object.HERO.map_position[0]-player_position[0],2), round(self.position[1]+unique_player_object.HERO.map_position[1]-player_position[1],2)
        self.tile_index = int(self.map_position[1])//level_painter.TILE_SIZE[1] , int(self.map_position[0])//level_painter.TILE_SIZE[0]
        self.sprite_position = self.position[0], self.position[1] + self.SPRITE_DISPLAY_CORRECTION
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.update_owned_sprites()
        
        if not self.is_dead:
            self.update_decisions()
            self.update_animation()
        elif not self.is_corpse: 
            entity_manager.kill_entity_colliders_and_melee_entities(id)

    def update_position(self, vector):
        self.position = round((self.position[0]-vector[0]),2),round((self.position[1] - vector[1]),2)
        self.sprite_position = self.position[0], self.position[1] + self.SPRITE_DISPLAY_CORRECTION
        self.tile_index = int(self.map_position[1])//level_painter.TILE_SIZE[1] , int(self.map_position[0])//level_painter.TILE_SIZE[0]
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.update_owned_sprites_position()

    def update_map_position_by_vector(self,vector):
        self.map_position = self.map_position[0]+vector[0], self.map_position[1]+vector[1]
        self.tile_index = int(self.map_position[1])//level_painter.TILE_SIZE[1] , int(self.map_position[0])//level_painter.TILE_SIZE[0]
    
    def update_decisions(self):
        if  unique_player_object.HERO.is_living == False:
            self.speed_vector = 0,0

        if self.is_living == True:
            if self.monster_ai.monster_can_melee_attack_player():
                self.speed_vector = 0,0
                self.facing_direction = util.get_facing_direction(self.position,player_position)
                self.monster_ai.increment_attack_decision_timer()
                self.monster_ai.reset_obstacle_avoidance_flags()
                self.monster_ai.end_pathfinding()
                
                if self.is_attacking and self.is_in_pain:
                    if self.attack_can_be_interrupted and self.attack_interupted():
                        self.interrupt_attack()
            
            else:
                if not self.monster_ai.is_following_path and not self.monster_ai.is_path_finding:
                    self.monster_ai.increment_direction_change_decision_timer()
                    self.set_speed_vector()
                
                else:
                    if self.monster_ai.is_path_finding and not self.monster_ai.is_following_path:
                        self.monster_ai.pathfinder.update(self.tile_index, True)
                        self.monster_ai.pathfinder.create_path()
                        self.monster_ai.is_path_finding = False
                        self.monster_ai.is_following_path = True
                        self.monster_ai.pathfinder.update(self.tile_index, True)
                
                    elif self.monster_ai.is_following_path and len(self.monster_ai.pathfinder.path) != 0:
                        self.monster_ai.pathfinder.update(self.tile_index, True)
                        self.monster_ai.change_to_next_point_direction()

        elif self.is_dying and not self.is_dead:
            self.interrupt_attack()
            self.is_in_pain = False
            self.speed_vector = 0,0
            self.monster_ai.reset_obstacle_avoidance_flags()
            self.monster_ai.end_pathfinding()

        elif self.is_overkilled and not self.is_dead:
            self.interrupt_attack()
            self.is_in_pain = False
            self.is_dying = False
            self.speed_vector = 0,0
            self.monster_ai.reset_obstacle_avoidance_flags()
            self.monster_ai.end_pathfinding()

    def update_animation(self):
        self.set_facing_direction_indices()
        self.image = character_walk[int(self.character_walk_index[0])][int(self.character_walk_index[1])]
        self.character_walk_forward_animation()

        if self.is_attacking == True:
            self.character_attack_animation()

        if self.is_in_pain == True:
            self.character_pain_animation()
        
        if self.is_dying == True:
            self.character_death_animation()

        if self.is_overkilled == True:
            self.character_overkill_animation()

    def set_facing_direction_indices(self):
        self.set_character_animation_direction_indices()
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
    
    def update_owned_sprites_position(self):
        self.pathfinding_collision_rect = pygame.Rect((self.position[0] - 2, self.position[1] -2),(4,4))

        for auxilary_sprites_row in self.entity_auxilary_sprites:
            for auxilary_sprite in auxilary_sprites_row:
                auxilary_sprite.position = self.position
                auxilary_sprite.update_position(self.position)
    
    def update_owned_sprites(self):
        for auxilary_sprites_row in self.entity_auxilary_sprites:
            for auxilary_sprite in auxilary_sprites_row:
                auxilary_sprite.position = self.position
                auxilary_sprite.update()

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

    #Walk speed vector setting
    def set_speed_vector(self):
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
    def take_damage(self, damage):
        self.health -= damage
        print("damage")
        
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

            entity_manager.fix_all_dead_objects_to_pixel_accuracy()
            entity_manager.fix_all_tiles_to_pixel_accuracy()
            entity_manager.fix_player_position_to_pixel_accuracy()
            
            if -(self.maxhealth//2) >= self.health:
                sound_player.ettin_death_sound.stop()
                random.choice(sound_player.player_overkill_sounds).play()
                self.is_living = False
                self.is_in_pain = False
                self.is_dying = False
                self.is_overkilled = True

                entity_manager.fix_all_dead_objects_to_pixel_accuracy()
                entity_manager.fix_all_tiles_to_pixel_accuracy()
                entity_manager.fix_player_position_to_pixel_accuracy()

    def interrupt_attack(self):
        self.is_attacking = False
        self.character_attack_index[1] = 0

    def attack_interupted(self):
        if random.choice(range(1,101)) <= self.attack_interruption_chance:
            return True
        self.attack_can_be_interrupted = False
        return False