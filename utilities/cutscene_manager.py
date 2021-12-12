from utilities import level_painter
from utilities import entity_manager
from utilities.constants import *
from sounds import sound_player
from images.misc.cutscenes import *

narrator_text = ["You have played this game too long mortal!","Are you ready to die???", "(Spell Chanting)"]

playing_cutscene = False

narrator_voice_lines = [sound_player.game_too_long_sound, sound_player.ready_to_die_sound, sound_player.spell_chant_sound]
voice_line_timer = 0

init_cutscene_animation = False

cutscene_tile_index = None
cutscene_position = None
cutscene_map_pos = None

portal_animation_index = 0
portal_animation_timer = 0
portal_animation_timer_limit = 1

boss_entry_animation_index = 0
boss_entry_animation_timer = 0
boss_entry_animation_timer_limit = 5

portal_tick = 0
portal_animation_rect = portal_animation[0].get_rect()

portal_is_opening = True
portal_is_closing = False
boss_entering = False
boss_has_entered_game = False

def play_cutscene(cutscene_type):
    if cutscene_type == BOSS_ENTRY:
        play_boss_entry_cutscene()

def play_boss_entry_cutscene():
    global narrator_text

    global playing_cutscene
    global init_cutscene_animation
    global voice_line_timer

    global portal_tick
    global boss_entering

    global cutscene_tile_index
    global cutscene_position
    global cutscene_map_pos

    global portal_animation_index
    global portal_animation_timer

    global boss_entry_animation_index
    global boss_entry_animation_timer

    global portal_is_opening
    global portal_is_closing

    global portal_animation_rect  

    if init_cutscene_animation == False:
        if voice_line_timer == 0:
            sound_player.fadeout_music()
            deactivate_all_monsters()
            narrator_voice_lines[0].play()
        elif 4.0167 > round(voice_line_timer,4) >= 4: 
            narrator_voice_lines[1].play()
        elif 7.0167 > round(voice_line_timer,4) >= 7: 
            narrator_voice_lines[2].play()
        elif voice_line_timer >= 10:
            init_cutscene_animation = True
        voice_line_timer += 0.0167

    else:
        if portal_animation_timer == 0 and portal_is_opening ==  True:
            sound_player.portal_open_sound.play()
            sound_player.play_music(4)

        if cutscene_tile_index == None:
            cutscene_tile_index = level_painter.cutscene_place_index
            cutscene_map_pos = entity_manager.level_sprites_matrix[cutscene_tile_index[0]][cutscene_tile_index[1]].map_position
            cutscene_map_pos = cutscene_map_pos[0], cutscene_map_pos[1]+14
            cutscene_position = round(cutscene_map_pos[0] - entity_manager.hero.map_position[0] + player_position[0],2), round(cutscene_map_pos[1] - entity_manager.hero.map_position[1] + player_position[1],2)
            portal_animation_rect.midbottom = cutscene_position

        if portal_is_opening:
            screen.blit(portal_animation[int(portal_animation_index)],(portal_animation_rect))
            portal_animation_timer += 0.0167
            portal_animation_index = (len(portal_animation)-1)*portal_animation_timer/portal_animation_timer_limit
            if portal_animation_index >= len(portal_animation):
                portal_is_opening = False
                portal_animation_index = 0
                portal_animation_timer = 0

        elif not portal_is_opening and not portal_is_closing and not boss_entering:
            screen.blit(portal_open_animation[int(portal_animation_index)],(portal_animation_rect))
            portal_animation_timer += 0.0167
            portal_animation_index = (len(portal_open_animation)-1)*portal_animation_timer/0.6
            if portal_animation_index >= len(portal_open_animation) and portal_tick < 3:
                portal_tick += 1
                portal_animation_timer = 0
                portal_animation_index = 0
            elif portal_tick >= 3:
                boss_entering = True

        elif boss_entering and not portal_is_closing:
            screen.blit(boss_entry_animation[int(boss_entry_animation_index)],portal_animation_rect)
            boss_entry_animation_timer += 0.0167
            boss_entry_animation_index = (len(boss_entry_animation)-1)*boss_entry_animation_timer/boss_entry_animation_timer_limit
            if boss_entry_animation_timer >= boss_entry_animation_timer_limit:
                entity_manager.summon_new_monster(IRON_LICH,(cutscene_tile_index[0], cutscene_tile_index[1]),BOSS_ENTRY)
                deactivate_all_monsters()
                portal_animation_index = len(portal_animation)-1
                portal_animation_timer = portal_animation_timer_limit
                portal_is_closing = True
        
        elif portal_is_closing:
            screen.blit(portal_animation[int(portal_animation_index)],(portal_animation_rect))
            portal_animation_timer -= 0.0167
            portal_animation_index = (len(portal_animation)-1)*portal_animation_timer/portal_animation_timer_limit
            if portal_animation_index < 0:
                playing_cutscene = False
                init_cutscene_animation = False
                portal_is_opening = True
                portal_is_closing = False
                cutscene_tile_index = None
                cutscene_position = None
                cutscene_map_pos = None
                portal_animation_index = 0
                portal_animation_timer = 0
                boss_entry_animation_index = 0
                boss_entry_animation_timer = 0
                voice_line_timer = 0
                portal_tick = 0
                narrator_text = ["You have played this game too long mortal!","Are you ready to die???", "(Spell Chanting)"]

def deactivate_all_monsters():
    for monster in entity_manager.far_proximity_character_sprites_list:
        monster.deactivate()

def overkill_kill_all_monsters():
    for monster in entity_manager.far_proximity_character_sprites_list:
        if not monster.is_dead:
            monster.take_damage(2*monster.maxhealth)

def destroy_all_projectiles():
    for projectile in entity_manager.far_proximity_projectile_sprites_list:
        if not projectile.is_disintegrating:
            projectile.is_disintegrating = True