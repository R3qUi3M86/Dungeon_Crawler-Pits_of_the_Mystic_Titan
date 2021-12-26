import pygame, time
from pygame.constants import BLEND_ALPHA_SDL2
from utilities.text_printer import *
from utilities.constants import *
from utilities import entity_manager
from utilities import collision_manager
from utilities import level_painter
from utilities import util
from utilities import ui_elements
from utilities import menu
from utilities import cutscene_manager
from utilities import t_ctrl
from sys import exit
import settings
from entities import cursor
from sounds.sound_player import *
from utilities.profile import profile

pygame.init()
clock = pygame.time.Clock()
mouse_input_pause = False
mouse_input_pause_timer = 0
playing_cutscene = False
wall_drawing_mode = VISIBLE
game_won_delay = 0
game_won_delay_limit = 2

set_volume_for_all_sfx(SFX_VOLUME)
set_music_volume(MUSIC_VOLUME)
pygame.event.set_allowed([pygame.QUIT])

#Player inputs
def get_player_wsad_input():
    keys = pygame.key.get_pressed()

    if entity_manager.hero.is_living and not collision_manager.moving_to_next_level and not cutscene_manager.playing_cutscene:
        if keys[pygame.K_s] and entity_manager.hero.speed_scalar[Y] < 30.0:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]+1 * t_ctrl.dt

        if (not keys[pygame.K_s] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[Y] > 0:
            if entity_manager.hero.speed_scalar[Y] < 3 * t_ctrl.dt:
                entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],0
            else:
                entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]-3 * t_ctrl.dt
        
        if keys[pygame.K_w] and entity_manager.hero.speed_scalar[Y] > -30.0:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]-1 * t_ctrl.dt

        if (not keys[pygame.K_w] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[Y] < 0:
            if entity_manager.hero.speed_scalar[Y] > -3 * t_ctrl.dt:
                entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],0
            else:
                entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X],entity_manager.hero.speed_scalar[Y]+3 * t_ctrl.dt

        if keys[pygame.K_a] and entity_manager.hero.speed_scalar[X] > -30.0:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]-1 * t_ctrl.dt,entity_manager.hero.speed_scalar[1]

        if (not keys[pygame.K_a] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[X] < 0:
            if entity_manager.hero.speed_scalar[X] > -3 * t_ctrl.dt:
                entity_manager.hero.speed_scalar = 0,entity_manager.hero.speed_scalar[Y]
            else:
                entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]+3 * t_ctrl.dt,entity_manager.hero.speed_scalar[Y]
        
        if keys[pygame.K_d] and entity_manager.hero.speed_scalar[X] < 30.0:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]+1 * t_ctrl.dt,entity_manager.hero.speed_scalar[Y]

        if (not keys[pygame.K_d] or entity_manager.hero.is_attacking) and entity_manager.hero.speed_scalar[X] > 0:
            if entity_manager.hero.speed_scalar[X] < 3 * t_ctrl.dt:
                entity_manager.hero.speed_scalar = 0,entity_manager.hero.speed_scalar[Y]
            else:
                entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X]-3 * t_ctrl.dt,entity_manager.hero.speed_scalar[Y]

        if entity_manager.hero.speed_scalar[X] > 21.2 and entity_manager.hero.speed_scalar[Y] > 22.54:
            entity_manager.hero.speed_scalar = 21.2,22.54
        elif entity_manager.hero.speed_scalar[X] > 21.2 and entity_manager.hero.speed_scalar[Y] < -22.54:
            entity_manager.hero.speed_scalar = 21.2,-22.54
        elif entity_manager.hero.speed_scalar[X] < -21.2 and entity_manager.hero.speed_scalar[Y] > 22.54:
            entity_manager.hero.speed_scalar = -21.2,22.54
        elif entity_manager.hero.speed_scalar[X] < -21.2 and entity_manager.hero.speed_scalar[Y] < -22.54:
            entity_manager.hero.speed_scalar = -21.2,-22.54

        if entity_manager.hero.speed_scalar[X] > 30.0:
            entity_manager.hero.speed_scalar = 30.0, entity_manager.hero.speed_scalar[Y]
        elif entity_manager.hero.speed_scalar[X] < -30.0:
            entity_manager.hero.speed_scalar = -30.0, entity_manager.hero.speed_scalar[Y]
        if entity_manager.hero.speed_scalar[Y] > 30.0:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X], 30.0
        elif entity_manager.hero.speed_scalar[Y] < -30.0:
            entity_manager.hero.speed_scalar = entity_manager.hero.speed_scalar[X], -30.0

        entity_manager.hero.speed_scalar = round(entity_manager.hero.speed_scalar[0],2),round(entity_manager.hero.speed_scalar[1],2)
        entity_manager.hero.speed_vector = round((entity_manager.hero.speed_scalar[X]/30)*entity_manager.hero.speed,2), round((entity_manager.hero.speed_scalar[Y]/30)*entity_manager.hero.speed*0.55,2)
    
    else:
        entity_manager.hero.speed_scalar = 0,0
        entity_manager.hero.speed_vector = 0,0
    
def get_player_mouse_input():
    global mouse_input_pause
    global mouse_input_pause_timer

    mouse_pos = pygame.mouse.get_pos()
    entity_manager.hero.facing_direction = util.get_facing_direction(player_position,mouse_pos)
    
    if pygame.mouse.get_pressed()[0] and not mouse_input_pause and not cutscene_manager.playing_cutscene:
        if entity_manager.hero.is_living == True:
            entity_manager.hero.is_in_pain = False
            entity_manager.hero.is_attacking = True

    if mouse_input_pause:
        mouse_input_pause_timer += 1 * t_ctrl.dt
        if mouse_input_pause_timer >= 10:
            mouse_input_pause_timer = 0
            mouse_input_pause = False

def toggle_wall_drawing_mode():
    global wall_drawing_mode

    if wall_drawing_mode is VISIBLE:
        wall_drawing_mode = HIDDEN
    else:
        wall_drawing_mode = VISIBLE

def switch_weapon(weapon_index):
    weapon_name = HERO_WEAPONS[weapon_index]
    if entity_manager.hero.weapons[weapon_name] and entity_manager.hero.is_attacking == False:
        entity_manager.hero.selected_weapon = HERO_WEAPONS[weapon_index]
        if weapon_name in MELEE_WEAPONS:
            entity_manager.hero.character_attack_index[1] = 0
        else:
            entity_manager.hero.character_attack_index[1] = 1

def use_consumable():
    if entity_manager.hero.selected_consumable and entity_manager.hero.consumables[entity_manager.hero.selected_consumable].is_ready_to_use and entity_manager.hero.is_living:
        entity_manager.use_consumable_item()

def pause_mouse_input():
    global mouse_input_pause

    mouse_input_pause = True

def resurrect_player():
    if not entity_manager.hero.is_living:
        entity_manager.hero.is_living = True
        entity_manager.hero.is_dying = False
        entity_manager.hero.is_overkilled = False
        entity_manager.hero.is_in_pain = False
        entity_manager.hero.is_dead = False
        entity_manager.hero.is_corpse = False
        entity_manager.hero.health = entity_manager.hero.maxhealth

def check_next_level_travel():
    if collision_manager.moving_to_next_level and not ui_elements.fading_out and not ui_elements.fading_in:
        ui_elements.fading_out = True
    elif collision_manager.moving_to_next_level and ui_elements.fading_in:
        collision_manager.moving_to_next_level = False
        start_next_level()

def check_win_conditions():
    global game_won_delay

    if menu.game_won and not ui_elements.fading_out and not ui_elements.fading_in:
        if game_won_delay >= game_won_delay_limit:
            ui_elements.fading_out = True
            game_won_delay = 0
            fadeout_music()
        else:
            if game_won_delay == 0:
                cutscene_manager.overkill_kill_all_monsters()
                cutscene_manager.destroy_all_projectiles()
            game_won_delay += 0.0167 * t_ctrl.dt

    elif menu.game_won and ui_elements.fading_in:
        play_music(-1)
        menu.pause_menu = False
        menu.scores_menu = True
        menu.in_game = False
        menu.menu()
        if settings.starting_new_game:
            start_new_game()

#Visuals drawing and sorting
def increment_sprite_sorting_timer():
    entity_manager.sorting_timer += 1 * t_ctrl.dt
    if entity_manager.sorting_timer >= entity_manager.sorting_timer_limit:
        entity_manager.order_sprites()
        entity_manager.sorting_timer = 0


def draw_sprites():
    translation_vector = level_painter.get_level_surface_translation_vector()
    screen.blit(level_painter.level_surface, (0,0), (-translation_vector[0],-translation_vector[1],screen_width,screen_height))

    for tile in entity_manager.far_proximity_level_liquids_sprites_list:
        if tile.is_animated:
            tile.update()
            screen.blit(tile.image,tile.disp_rect)

    if wall_drawing_mode == VISIBLE:
        for tile in entity_manager.far_proximity_primary_wall_sprites_list:
            screen.blit(tile.image,tile.disp_rect)

    for shadow in entity_manager.far_proximity_shadow_sprite_group_list:
        #shadow.draw(screen)
        #screen.blit(shadow.sprite.image,shadow.sprite.position, special_flags=BLEND_RGB_ADD)
        screen.blit(shadow.sprite.image,shadow.sprite.rect, special_flags=BLEND_ALPHA_SDL2)

    if cutscene_manager.playing_cutscene:
        cutscene_manager.play_cutscene(BOSS_ENTRY)

    for row in entity_manager.sorted_entity_matrix: 
        for entity in row:
            entity.draw(screen)
            # if entity.sprite.TYPE is PROJECTILE:
            #     img = entity.sprite.projectile_collider.image
            #     screen.blit(img, entity.sprite.projectile_collider.rect)

    if wall_drawing_mode == VISIBLE:
        for tile in entity_manager.far_proximity_secondary_wall_sprites_list:
            if tile.is_hiding_player_prim:
                screen.blit(tile.alpha_image1,tile.disp_rect)
            elif tile.is_hiding_player_sec:
                screen.blit(tile.alpha_image2,tile.disp_rect)
            elif tile.is_hiding_player_tert:
                screen.blit(tile.alpha_image3,tile.disp_rect)
            else:
                screen.blit(tile.image,tile.disp_rect)

              
def draw_ui():
    screen.blit(ui_elements.central_light,(0,0))
    ui_elements.draw_damage_overlay()
    ui_elements.draw_health_bar()
    ui_elements.draw_weapon_ammo_counter()
    ui_elements.draw_consumable_counter()
    if entity_manager.boss and entity_manager.boss.health > 0:
        ui_elements.draw_boss_hp_bar()

    if len(entity_manager.picked_up_item_names) != 0 and not cutscene_manager.playing_cutscene:
        ui_elements.display_pickup_text()
    elif len(cutscene_manager.narrator_text) != 0 and cutscene_manager.playing_cutscene:
        ui_elements.display_narrator_text()

    if ui_elements.fading_in:
        ui_elements.fade_in()
    elif ui_elements.fading_out:
        ui_elements.fade_out()

#Game initialization
def start_new_game():
    global game_won_delay

    cutscene_manager.reset_cutscene_flags()
    game_won_delay = 0
    entity_manager.clear_all_lists()
    entity_manager.create_new_player()
    play_music(0)
    level_painter.level_layout = level_painter.levels[0] #level_painter.test_map #
    level_painter.cutscene_place_index = CUTSCENE_PLACE_INDEX
    level_painter.cutscene_tile_indices = CUTSCENE_TILE_INDICES
    entity_manager.initialize_game()
    t_ctrl.last_time = time.time()
    main_game_loop()

def start_next_level():
    entity_manager.clear_all_lists()
    currenet_level_index = level_painter.levels.index(level_painter.level_layout)
    next_level_index = currenet_level_index + 1
    level_painter.level_layout = level_painter.levels[next_level_index]
    play_music(next_level_index)
    entity_manager.initialize_game()
    t_ctrl.last_time = time.time()
    main_game_loop()

#Main game loop
def main_game_loop():
    while 1:
        #Inputs
        get_player_wsad_input()
        get_player_mouse_input()

        #Updates
        cursor.cursor.update()
        entity_manager.update_all_objects_position_in_far_proximity()
        entity_manager.update_all_objects_in_far_proximity()
        collision_manager.wall_hider_collision()

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN and not collision_manager.moving_to_next_level and not menu.game_won:
                if event.key == pygame.K_TAB:
                    toggle_wall_drawing_mode()
                elif event.key == pygame.K_1:
                    switch_weapon(0)
                elif event.key == pygame.K_2:
                    switch_weapon(1)
                elif event.key == pygame.K_3:
                    switch_weapon(2)
                elif event.key == pygame.K_f:
                    entity_manager.use_puzzle()
                elif event.key == pygame.K_SPACE:
                    use_consumable()
                elif event.key == pygame.K_p:
                    resurrect_player()
                elif event.key == pygame.K_ESCAPE:
                    menu.menu()
                    pause_mouse_input()
                    if settings.starting_new_game:
                        start_new_game()
        
        check_win_conditions()
        check_next_level_travel()
        
        #Drawing
        increment_sprite_sorting_timer()
        draw_sprites()
        draw_ui()
        cursor.cursor.draw(screen)

        ################
        ####Debuging####
        ################
        debug_text(f"{entity_manager.hero.map_position}")
        debug_text(f"{entity_manager.hero.tile_index}",x = 10, y = 30)
        #debug_text(f"109 pos: {entity_manager.hero.direct_proximity_collision_tiles[1].map_position}",x = 10, y = 30)
        #debug_text(f"{entity_manager.hero.tile_index}", x=10, y=30)
        #debug_text(f"hero map pos: {entity_manager.hero.map_position}",x = 10, y = 45)
        #debug_text(f"mon 0 pos: {entity_manager.get_entity_sprite_by_id(1).position}",x = 10, y = 45)
        #debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(1).map_position}",x = 10, y = 60)
        #debug_text(f"mon 0 tile_index: {entity_manager.get_entity_sprite_by_id(1).tile_index}", x=10, y=75)
        #debug_text(f"mon 0 current_tile_map_pos: {entity_manager.get_entity_sprite_by_id(1).map_position}",x = 10, y = 75)s
        # debug_text(f"mon 0 prvous_tile_map_pos: {entity_manager.get_entity_sprite_by_id(0).previous_tile_position}",x = 10, y = 75)
        # debug_text(f"mon 0 map_pos: {entity_manager.get_entity_sprite_by_id(0).map_position}",x = 10, y = 90)
        # debug_text(f"mon 1 map_pos: {entity_manager.get_entity_sprite_by_id(1).tile_index}",x = 10, y = 90)

        #util.increment_print_matrix_timer(entity_manager.far_proximity_level_sprite_matrix, "S")
        #util.increment_print_matrix_timer(entity_manager.level_sprites_matrix, "S", True)
        #util.increment_print_matrix_timer(entity_manager.far_proximity_entity_sprite_group_matrix, "S")

        #Other
        t_ctrl.adjust_delta_time()
        increment_ambient_sound_timer()
        pygame.display.flip()
        clock.tick(60)
        if entity_manager.hero.tile_index in level_painter.cutscene_tile_indices and level_painter.level_layout is level_painter.level_04_map and not cutscene_manager.playing_cutscene:
            cutscene_manager.playing_cutscene = True
            level_painter.cutscene_tile_indices = []

def main():
    play_music(-1)
    menu.menu()
    start_new_game()

main()