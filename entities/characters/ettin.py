import pygame
import random
from settings import *
from sounds import sound_player
from entities import shadow
from entities import melee_range
from utilities import util
from utilities import combat_manager
from utilities import collision_manager
from utilities import entity_manager
from utilities import level_painter
from utilities import monster_ai
from utilities.text_printer import *
from utilities.constants import *
from images.characters.ettin_images import *
from entities.characters import unique_player_object

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
        self.entity_collision_mask_nw = shadow.Shadow(self.position, self.id, SIZE_SMALL, True, SECTOR_NW)
        self.entity_collision_mask_ne = shadow.Shadow(self.position, self.id, SIZE_SMALL, True, SECTOR_NE)
        self.entity_collision_mask_sw = shadow.Shadow(self.position, self.id, SIZE_SMALL, True, SECTOR_SW)
        self.entity_collision_mask_se = shadow.Shadow(self.position, self.id, SIZE_SMALL, True, SECTOR_SE)
        self.entity_collision_mask    = shadow.Shadow(player_position, self.id, SIZE_SMALL, True)

        #Melee sectors
        self.entity_melee_e_sector  = melee_range.Melee(self.position, SECTOR_E)
        self.entity_melee_ne_sector = melee_range.Melee(self.position, SECTOR_NE)
        self.entity_melee_n_sector  = melee_range.Melee(self.position, SECTOR_N)
        self.entity_melee_nw_sector = melee_range.Melee(self.position, SECTOR_NW)
        self.entity_melee_w_sector  = melee_range.Melee(self.position, SECTOR_W)
        self.entity_melee_sw_sector = melee_range.Melee(self.position, SECTOR_SW)
        self.entity_melee_s_sector  = melee_range.Melee(self.position, SECTOR_S)
        self.entity_melee_se_sector = melee_range.Melee(self.position, SECTOR_SE)

        #Shadow
        self.shadow = shadow.Shadow(self.position, self.id, SIZE_MEDIUM, True)
        
        #Sprite lists
        self.entity_collision_mask_sprites = [self.entity_collision_mask_nw,self.entity_collision_mask_ne,self.entity_collision_mask_sw,self.entity_collision_mask_se]
        self.entity_melee_sector_sprites   = [self.entity_melee_e_sector,self.entity_melee_ne_sector,self.entity_melee_n_sector,self.entity_melee_nw_sector,self.entity_melee_w_sector,self.entity_melee_sw_sector,self.entity_melee_s_sector,self.entity_melee_se_sector]
        self.entity_auxilary_sprites       = [[self.shadow],self.entity_collision_mask_sprites,self.entity_melee_sector_sprites]

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
        self.has_los = False
        
        #Character properties
        self.health = 10
        self.maxhealth = 10
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
        self.map_position = round(self.position[0]-player_position[0]+unique_player_object.HERO.tile_index[0],2), round(self.position[1]-player_position[1]+unique_player_object.HERO.tile_index[1],2)
        self.tile_index = int(self.map_position[1])//level_painter.TILE_SIZE[1] , int(self.map_position[0])//level_painter.TILE_SIZE[0]
        self.sprite_position = self.position[0], self.position[1] + self.sprite_display_correction
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.update_owned_sprites_position()
        self.update_decisions()
        self.update_animation()

    def update_position(self, vector):
        self.position = round((self.position[0]-vector[0]),2),round((self.position[1] - vector[1]),2)
        self.sprite_position = self.position[0], self.position[1] + self.sprite_display_correction
        self.rect = self.image.get_rect(midbottom = (self.sprite_position))
        self.update_owned_sprites_position()

    def update_map_position_by_vector(self,vector):
        self.map_position = self.map_position[0]+vector[0], self.map_position[1]+vector[1]
        self.tile_index = int(self.map_position[1])//level_painter.TILE_SIZE[1] , int(self.map_position[0])//level_painter.TILE_SIZE[0]
    
    def update_decisions():
        pass

    def update_animation(self):
        if self.is_living == True:
            if self.monster_ai.monster_can_melee_attack_player() == False and self.is_attacking == False and self.monster_ai.is_following_path == False:
                self.monster_ai.increment_direction_change_decision_timer()
            elif self.monster_ai.is_following_path == False:
                self.facing_direction = self.monster_ai.player_direction_sector

            if self.is_attacking == False and self.is_in_pain == False:
                self.set_facing_direction()
        
            elif self.is_path_finding == True and self.is_following_path == False:
                print("creating path")
                self.is_path_finding = False
                self.is_following_path = True
                self.pathfinder.update(self.monster.tile_index, True)
                self.pathfinder.create_path()
                self.pathfinder.update(self.monster.tile_index, True)
                
            elif self.is_following_path == True and self.pathfinder.path:
                print("following path")
                self.pathfinder.update(self.monster.tile_index, True)
                self.change_to_next_point_direction()
            
            if self.monster_ai.monster_can_melee_attack_player():
                self.monster_ai.finish_avoiding_obstacle()
                self.monster_ai.finish_pathfinding()
                self.monster_ai.increment_attack_decision_timer()

            if self.is_attacking == False and self.is_in_pain == False and unique_player_object.HERO.is_living == True:
                self.set_speed_vector()
                if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
                    self.character_walk_forward_animation()
            
            elif self.is_attacking == True and self.is_in_pain == True:
                self.speed_vector = 0,0
                if self.attack_can_be_interrupted and self.attack_interupted():
                    self.interrupt_attack()

            if self.is_in_pain == True and self.is_attacking == False:
                self.speed_vector = 0,0
                self.character_pain_animation()

            elif self.is_attacking == True:
                self.speed_vector = 0,0
                self.character_attack_animation()
        
        elif self.is_dying == True:
            self.interrupt_attack()
            self.is_in_pain = False
            self.speed_vector = 0,0
            self.character_death_animation()

        if  unique_player_object.HERO.is_living == False:
            self.speed_vector = 0,0

    def set_facing_direction(self):
        self.set_character_animation_direction_indices()
        self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]
    
    def update_owned_sprites_position(self):
        self.pathfinding_collision_rect = pygame.Rect((self.position[0] - 2, self.position[1] -2),(4,4))

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
        if self.is_overkilled == False:
            self.character_death_index += 0.1
            if int(self.character_death_index) == 7:
                self.character_death_index = 6
                self.is_dying == False
            self.image = self.character_death[int(self.character_death_index)]

    def character_overkill_animation(self):
        self.character_overkill_index += 0.1
        if int(self.character_overkill_index) == 10:
            self.character_overkill_index = 9
            self.is_overkilled == False
        self.image = self.character_overkill[int(self.character_overkill_index)]       

    def character_walk_forward_animation(self):
        if self.speed_vector[0] != 0 or self.speed_vector[1] != 0:
            self.character_walk_index[1] += 0.1
            if int(self.character_walk_index[1]) == 4:
                self.character_walk_index[1] = 0
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

    def character_attack_animation(self):
        self.character_attack_index[1] += 0.1
        if round(self.character_attack_index[1],2) == 2.00:
            combat_manager.attack_player_with_melee_attack(self)
        self.image = self.character_attack[self.character_attack_index[0]][int(self.character_attack_index[1])]
        
        if int(self.character_attack_index[1]) == 3:
            self.interrupt_attack()
            self.image = self.character_walk[self.character_walk_index[0]][int(self.character_walk_index[1])]

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
        if self.health <= 0:
            sound_player.ettin_death_sound.play()
            self.is_living = False
            self.is_dying = True
            self.speed_vector = 0,0
            entity_manager.kill_entity_colliders_and_melee_entities(self.id)
            entity_manager.fix_all_dead_objects_to_pixel_accuracy()
            entity_manager.fix_all_tiles_to_pixel_accuracy()
            entity_manager.fix_player_position_to_pixel_accuracy()
        else:
            self.is_in_pain = True
            if random.choice(range(4)) == 0:
                sound_player.ettin_pain_sound.play()

    def interrupt_attack(self):
        self.is_attacking = False
        self.character_attack_index[1] = 0

    def attack_interupted(self):
        if random.choice(range(1,101)) <= self.attack_interruption_chance:
            return True
        self.attack_can_be_interrupted = False
        return False