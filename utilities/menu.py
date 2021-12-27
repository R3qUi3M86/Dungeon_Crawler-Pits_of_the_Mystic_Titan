import random
import pygame
import math
import settings
from sys import exit
from entities import cursor
from images.menu.menu_images import *
from sounds import sound_player
from utilities import ui_elements

pygame.init()
clock = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT])

#Global variables
game_won = False
main_menu = True
settings_menu = False
pause_menu = False
yes_or_no_menu = False
scores_menu = False
selected_button = None

in_game = False
entering_game = False
going_to_main_menu = False

#Background image
menu_background_image = pygame.transform.scale(menu_background,(1480,854))
background_pos = -100,-67
background_velocity = 0,0
angle = 0

#Text images
title_img = game_title_text
title_rect = title_img.get_rect()
title_rect.center = (screen_width//2, 134)

settings_text_img = settings_text
settings_text_rect = settings_text_img.get_rect()
settings_text_rect.center = (screen_width//2, 134)

game_paused_img = game_paused_text
game_paused_rect = game_paused_img.get_rect()
game_paused_rect.center = (screen_width//2, 134)

sound_volume_img = sound_volume_text
sound_volume_rect = sound_volume_img.get_rect()
sound_volume_rect.center = (screen_width//2+100, 280)

leave_question_img = leave_question_text
leave_question_rect = leave_question_img.get_rect()
leave_question_rect.center = (screen_width//2, 300)

quit_question_img = quit_question_text
quit_question_rect = quit_question_img.get_rect()
quit_question_rect.center = (screen_width//2, 280)

scores_img = scores_text
scores_rect = scores_img.get_rect()
scores_rect.center = (screen_width//2, screen_height//2)

#Button images and rects
new_game_button_img = new_game_button[0]
new_game_rect = new_game_button_img.get_rect()
new_game_rect.center = (screen_width//2,310)

settings_button_img = settings_button[0]
settings_rect = settings_button_img.get_rect()
settings_rect.center = (screen_width//2,400)

quit_button_img = quit_button[0]
quit_rect = quit_button_img.get_rect()
quit_rect.center = (screen_width//2,490)

effects_button_img = effects_button[0]
effects_rect = effects_button_img.get_rect()
effects_rect.center = (screen_width//2-400,380)

music_button_img = music_button[0]
music_rect = music_button_img.get_rect()
music_rect.center = (screen_width//2-400,470)

back_button_img = back_button[0]
back_rect = back_button_img.get_rect()
back_rect.center = (screen_width-120,screen_height-80)

resume_button_img = resume_button[0]
resume_rect = resume_button_img.get_rect()
resume_rect.center = (screen_width//2,310)

leave_game_button_img = leave_game_button[0]
leave_game_rect = leave_game_button_img.get_rect()
leave_game_rect.center = (screen_width//2,490)

yes_button_img = yes_button[0]
yes_rect = yes_button_img.get_rect()
yes_rect.center = (screen_width//2-120,440)

no_button_img = no_button[0]
no_rect = no_button_img.get_rect()
no_rect.center = (screen_width//2+150,440)

#Button animation
new_game_button_index = 0
settings_button_index = 0
quit_button_index = 0
back_button_index = 0
resume_button_index = 0
leave_game_button_index = 0
effects_button_index = 0
music_button_index = 0
yes_button_index = 0
no_button_index = 0

ASCENDING = "ascending"
DESCENDING = "descending"

BUTTON_IMAGES = {NEW_GAME_BUTTON:new_game_button_img, 
                 SETTINGS_BUTTON:settings_button_img, 
                 QUIT_BUTTON: quit_button_img, 
                 BACK_BUTTON:back_button_img,
                 RESUME_BUTTON:resume_button_img,
                 LEAVE_GAME_BUTTON:leave_game_button_img,
                 EFFECTS_BUTTON:effects_button_img,
                 MUSIC_BUTTON:music_button_img,
                 YES_BUTTON:yes_button_img,
                 NO_BUTTON:no_button_img}

BUTTON_ANIM_INDICES = {NEW_GAME_BUTTON:new_game_button_index,
                       SETTINGS_BUTTON:settings_button_index, 
                       QUIT_BUTTON: quit_button_index,
                       BACK_BUTTON:back_button_index,
                       RESUME_BUTTON:resume_button_index,
                       LEAVE_GAME_BUTTON:leave_game_button_index,
                       EFFECTS_BUTTON:effects_button_index,
                       MUSIC_BUTTON:music_button_index,
                       YES_BUTTON:yes_button_index,
                       NO_BUTTON:no_button_index}

#Slider
sfx_slider_bar = slider_bar
sfx_slider_bar_rect = slider_bar.get_rect()
sfx_slider_bar_rect.center = effects_rect.center[0]+500, effects_rect.center[1]+2

sfx_slider_fill = None

dragging_sfx_pip = False
sfx_slider_pip = slider_pip
SFX_PIP = "sfx pip"
sfx_slider_pip_rect = slider_pip.get_rect()
sfx_slider_pip_rect.center = sfx_slider_bar_rect.center

dragging_music_pip = False
music_slider_bar = slider_bar
MUSIC_PIP = "music pip"
music_slider_bar_rect = slider_bar.get_rect()
music_slider_bar_rect.center = music_rect.center[0]+500, music_rect.center[1]+2

music_slider_fill = None

music_slider_pip = slider_pip
music_slider_pip_rect = slider_pip.get_rect()
music_slider_pip_rect.center = music_slider_bar_rect.center

#Drawing
def draw_menu_elements():
    screen.blit(menu_background_image,(background_pos))

    if main_menu:
        screen.blit(title_img,title_rect)
        draw_main_menu_buttons()
    
    elif settings_menu:
        screen.blit(settings_text_img,settings_text_rect)
        draw_settings_menu_elements()
    
    elif yes_or_no_menu:
        if in_game:
            screen.blit(leave_question_img,leave_question_rect)
        else:
            screen.blit(quit_question_img,quit_question_rect)
        draw_yes_no_menu_buttons()
    
    elif pause_menu:
        screen.blit(game_paused_img,game_paused_rect)
        draw_pause_menu_buttons()

    elif scores_menu:
        screen.blit(scores_img,scores_rect)
        draw_scores_menu_buttons()

def draw_main_menu_buttons():
    screen.blit(BUTTON_IMAGES[NEW_GAME_BUTTON],new_game_rect)
    screen.blit(BUTTON_IMAGES[SETTINGS_BUTTON],settings_rect)
    screen.blit(BUTTON_IMAGES[QUIT_BUTTON],quit_rect)

def draw_settings_menu_elements():
    screen.blit(sound_volume_img,sound_volume_rect)
    screen.blit(BUTTON_IMAGES[EFFECTS_BUTTON],effects_rect)
    screen.blit(BUTTON_IMAGES[MUSIC_BUTTON],music_rect)
    screen.blit(BUTTON_IMAGES[BACK_BUTTON],back_rect)
    
    mask_slider_fill(sfx_slider_fill)
    mask_slider_fill(music_slider_fill)
    screen.blit(sfx_slider_bar,sfx_slider_bar_rect)
    screen.blit(music_slider_bar,music_slider_bar_rect)
    screen.blit(sfx_slider_fill,sfx_slider_bar_rect)
    screen.blit(music_slider_fill,music_slider_bar_rect)
    sfx_slider_pip_rect.center = get_slider_pip_rect_pos(SFX_PIP)
    music_slider_pip_rect.center = get_slider_pip_rect_pos(MUSIC_PIP)
    screen.blit(sfx_slider_pip,sfx_slider_pip_rect)
    screen.blit(music_slider_pip,music_slider_pip_rect)

def draw_yes_no_menu_buttons():
    screen.blit(BUTTON_IMAGES[YES_BUTTON],yes_rect)
    screen.blit(BUTTON_IMAGES[NO_BUTTON],no_rect)

def draw_pause_menu_buttons():
    screen.blit(BUTTON_IMAGES[RESUME_BUTTON],resume_rect)
    screen.blit(BUTTON_IMAGES[SETTINGS_BUTTON],settings_rect)
    screen.blit(BUTTON_IMAGES[LEAVE_GAME_BUTTON],leave_game_rect)

def draw_scores_menu_buttons():
    screen.blit(BUTTON_IMAGES[BACK_BUTTON], back_rect)

def animate_button(button_name, direction):
    index = BUTTON_ANIM_INDICES[button_name]
        
    if direction == ASCENDING:
        index += 0.5
        if index >= len(MENU_BUTTON_IMGAGE_SETS[button_name]):
            index = len(MENU_BUTTON_IMGAGE_SETS[button_name]) - 1

    elif direction == DESCENDING:
        index -= 0.5
        if index < 0:
            index = 0

    BUTTON_ANIM_INDICES[button_name] = index
    BUTTON_IMAGES[button_name] = MENU_BUTTON_IMGAGE_SETS[button_name][int(index)]

def descend_animation_on_not_selected_buttons(m_x, m_y):
    if not new_game_rect.collidepoint(m_x, m_y) and not selected_button == NEW_GAME_BUTTON:
        animate_button(NEW_GAME_BUTTON, DESCENDING)

    if not settings_rect.collidepoint(m_x, m_y) and not selected_button == SETTINGS_BUTTON:
        animate_button(SETTINGS_BUTTON,DESCENDING)

    if not quit_rect.collidepoint(m_x, m_y) and not selected_button == QUIT_BUTTON:
        animate_button(QUIT_BUTTON, DESCENDING)

    if not back_rect.collidepoint(m_x, m_y) and not selected_button == BACK_BUTTON:
        animate_button(BACK_BUTTON, DESCENDING)

    if not effects_rect.collidepoint(m_x, m_y) and not selected_button == EFFECTS_BUTTON:
        animate_button(EFFECTS_BUTTON,DESCENDING)

    if not music_rect.collidepoint(m_x, m_y) and not selected_button == MUSIC_BUTTON:
        animate_button(MUSIC_BUTTON, DESCENDING)  

    if not resume_rect.collidepoint(m_x, m_y) and not selected_button == RESUME_BUTTON:
        animate_button(RESUME_BUTTON, DESCENDING)

    if not leave_game_rect.collidepoint(m_x, m_y) and not selected_button == LEAVE_GAME_BUTTON:
        animate_button(LEAVE_GAME_BUTTON, DESCENDING)

    if not yes_rect.collidepoint(m_x, m_y) and not selected_button == YES_BUTTON:
        animate_button(YES_BUTTON,DESCENDING)

    if not no_rect.collidepoint(m_x, m_y) and not selected_button == NO_BUTTON:
        animate_button(NO_BUTTON, DESCENDING)  

def animate_background():
    global background_pos
    global background_velocity
    global angle

    if background_velocity[0] == 0 and background_velocity[1] == 0:
        if background_pos[0] == 0 and background_pos[1] == 0:
            angle = random.choice(range(270,361))
        elif background_pos[0] == 0 and -134 < background_pos[1] < 0:
            angle = random.choice([random.choice(range(90)),random.choice(range(270,360))])
        elif background_pos[0] == 0 and background_pos[1] == -134:
            angle = random.choice(range(91))
        elif -200 < background_pos[0] < 0 and background_pos[1] == -134:
            angle = random.choice(range(181))
        elif background_pos[0] == -200 and background_pos[1] == -134:
            angle = random.choice(range(90,181))
        elif background_pos[0] == -200 and -134 < background_pos[1] < 0:
            angle = random.choice(range(90,271))
        elif background_pos[0] == -200 and background_pos[1] == 0:
            angle = random.choice(range(180,271))
        elif -200 < background_pos[0] < 0 and background_pos[1] == 0: 
            angle = random.choice(range(180,361))
        elif -200 < background_pos[0] < 0 and -134 < background_pos[1] < 0:
            angle = random.choice(range(0,361))
 
    x_vel_factor = math.cos(math.radians(angle))
    y_vel_factor = -math.sin(math.radians(angle))

    dist_x = 0
    dist_y = 0

    if x_vel_factor > 0:
        dist_x = 200+background_pos[0]
    elif x_vel_factor < 0:
        dist_x = -background_pos[0]

    if y_vel_factor > 0:
        dist_y = 134+background_pos[1]
    elif y_vel_factor < 0:
        dist_y = -background_pos[1]

    if 2 < dist_x <= 5:
        delta_vel_x = -0.01
        delta_vel_y = -0.01
    elif dist_x <= 2:
        delta_vel_x = 0
    else:
        delta_vel_x = 0.001

    if 2 < dist_y <= 5:
        delta_vel_y = -0.01
        delta_vel_x = -0.01
    elif dist_y <= 2:
        delta_vel_y = 0
    else:
        delta_vel_y = 0.001

    speed_x = background_velocity[0]+x_vel_factor*delta_vel_x
    speed_y = background_velocity[1]+y_vel_factor*delta_vel_y

    if speed_x >= 0.15:
        speed_x = 0.15
    elif speed_x <= -0.15:
        speed_x = -0.15
    
    if speed_y >= 0.15:
        speed_y = 0.15
    elif speed_y <= -0.15:
        speed_y = -0.15
    
    if x_vel_factor > 0 and speed_x < 0.02:
        speed_x = 0.02
    elif x_vel_factor < 0 and speed_x > -0.02:
        speed_x = -0.02

    if y_vel_factor > 0 and speed_y < 0.02:
        speed_y = 0.02
    elif y_vel_factor < 0 and speed_y > -0.02:
        speed_y = -0.02

    background_velocity = speed_x,speed_y
    background_pos = background_pos[0] - background_velocity[0], background_pos[1] - background_velocity[1]
    if int(background_pos[0]) == -200 and int(dist_x) == 0:
        background_pos = -200, background_pos[1]
        background_velocity = 0, 0
    elif int(background_pos[0]) == 0 and int(dist_x) == 0:
        background_pos = 0, background_pos[1]
        background_velocity = 0, 0
    if int(background_pos[1]) == -134 and int(dist_y) == 0:
        background_pos = background_pos[0], -134
        background_velocity = 0, 0
    elif int(background_pos[1]) == 0 and int(dist_y) == 0:
        background_pos = background_pos[0], 0
        background_velocity = 0, 0

def mask_slider_fill(slider_type):
    global sfx_slider_fill
    global music_slider_fill

    if slider_type == sfx_slider_fill:
        x_position = sound_player.SFX_VOLUME*665+25-695
        sfx_slider_fill = pygame.Surface(slider_bar.get_size(), pygame.SRCALPHA)
        sfx_slider_fill.blit(slider_fill,(x_position,0))
        sfx_slider_fill.blit(slider_mask,(0,0))
        sfx_slider_fill.set_colorkey((0,0,255))
    elif slider_type == music_slider_fill:
        x_position = sound_player.MUSIC_VOLUME*665+25-695
        music_slider_fill = pygame.Surface(slider_bar.get_size(), pygame.SRCALPHA)
        music_slider_fill.blit(slider_fill,(x_position,0))
        music_slider_fill.blit(slider_mask,(0,0))
        music_slider_fill.set_colorkey((0,0,255))

def get_slider_pip_rect_pos(slider_pip):
    if slider_pip == SFX_PIP:
        position = sfx_slider_bar_rect.center[0]+sound_player.SFX_VOLUME*665+25-695+335, sfx_slider_pip_rect.center[1]
    elif slider_pip == MUSIC_PIP:
        position = music_slider_bar_rect.center[0]+sound_player.MUSIC_VOLUME*665+25-695+335, music_slider_pip_rect.center[1]

    return position

#Menu movement
def cycle_options_up():
    global selected_button

    if main_menu:
        if selected_button == None:
            selected_button = NEW_GAME_BUTTON
        else:
            index = MAIN_MENU_BUTTONS.index(selected_button)
            if index < len(MAIN_MENU_BUTTONS) - 1:
                selected_button = MAIN_MENU_BUTTONS[index+1]
            else:
                selected_button = MAIN_MENU_BUTTONS[0]
    
    elif settings_menu:
        if selected_button == None:
            selected_button = EFFECTS_BUTTON
        else:
            index = SETTINGS_MENU_BUTTONS.index(selected_button)
            if index < len(SETTINGS_MENU_BUTTONS) - 1:
                selected_button = SETTINGS_MENU_BUTTONS[index+1]
            else:
                selected_button = SETTINGS_MENU_BUTTONS[0]
    
    elif pause_menu:
        if selected_button == None:
            selected_button = RESUME_BUTTON
        else:
            index = PAUSE_MENU_BUTTONS.index(selected_button)
            if index < len(PAUSE_MENU_BUTTONS) - 1:
                selected_button = PAUSE_MENU_BUTTONS[index+1]
            else:
                selected_button = PAUSE_MENU_BUTTONS[0]
    
    elif yes_or_no_menu:
        if selected_button == None:
            selected_button = NO_BUTTON
        else:
            index = YES_NO_MENU_BUTTONS.index(selected_button)
            if index < len(YES_NO_MENU_BUTTONS) - 1:
                selected_button = YES_NO_MENU_BUTTONS[index+1]
            else:
                selected_button = YES_NO_MENU_BUTTONS[0]

def cycle_options_down():
    global selected_button

    if main_menu:
        if selected_button == None:
            selected_button = NEW_GAME_BUTTON
        else:
            index = MAIN_MENU_BUTTONS.index(selected_button)
            selected_button = MAIN_MENU_BUTTONS[index-1]
    
    elif settings_menu:
        if selected_button == None:
            selected_button = EFFECTS_BUTTON
        else:
            index = SETTINGS_MENU_BUTTONS.index(selected_button)
            selected_button = SETTINGS_MENU_BUTTONS[index-1]

    elif pause_menu:
        if selected_button == None:
            selected_button = RESUME_BUTTON
        else:
            index = PAUSE_MENU_BUTTONS.index(selected_button)
            selected_button = PAUSE_MENU_BUTTONS[index-1]

    elif yes_or_no_menu:
        if selected_button == None:
            selected_button = NO_BUTTON
        else:
            index = YES_NO_MENU_BUTTONS.index(selected_button)
            selected_button = YES_NO_MENU_BUTTONS[index-1]

def increment_option(m_x,m_y):
    if selected_button == EFFECTS_BUTTON or effects_rect.collidepoint(m_x,m_y):
        sound_player.increment_effects_volume()
    elif selected_button == MUSIC_BUTTON or music_rect.collidepoint(m_x,m_y):
        sound_player.increment_music_volume()

def decrement_option(m_x,m_y):
    if selected_button == EFFECTS_BUTTON or effects_rect.collidepoint(m_x,m_y):
        sound_player.decrement_effects_volume()
    elif selected_button == MUSIC_BUTTON or music_rect.collidepoint(m_x,m_y):
        sound_player.decrement_music_volume()

def go_back_or_quit_prompt():
    if main_menu:
        enter_selected_option(QUIT_BUTTON)
    
    elif settings_menu:
        enter_selected_option(BACK_BUTTON)
    
    elif pause_menu:
        enter_selected_option(RESUME_BUTTON)

    elif yes_or_no_menu:
        enter_selected_option(NO_BUTTON)

def enter_selected_option(used_button):
    global main_menu
    global pause_menu
    global settings_menu
    global yes_or_no_menu
    global scores_menu
    global in_game
    global entering_game
    global going_to_main_menu
    global game_won

    if used_button == NEW_GAME_BUTTON:
        sound_player.play_menu_push_sound(new_game=True)
    else:
        sound_player.play_menu_push_sound()

    if used_button == SETTINGS_BUTTON:
        main_menu = False
        settings_menu = True
    
    elif used_button == QUIT_BUTTON:
        main_menu = False
        yes_or_no_menu = True
    
    elif used_button == NEW_GAME_BUTTON:
        sound_player.fadeout_music()
        settings.starting_new_game = True
        ui_elements.fading_out = True
        game_won = False
        entering_game = True
        in_game = True
    
    elif used_button == BACK_BUTTON:
        settings_menu = False
        scores_menu = False
        game_won = False
        
        if not in_game:
            main_menu = True
        else:
            pause_menu = True
    
    elif used_button == RESUME_BUTTON:
        settings.starting_new_game = False
        entering_game = True

    elif used_button == LEAVE_GAME_BUTTON:
        pause_menu = False
        yes_or_no_menu = True

    elif used_button == NO_BUTTON:
        if in_game:
            pause_menu = True
            yes_or_no_menu = False
        else:
            yes_or_no_menu = False
            main_menu = True

    elif used_button == YES_BUTTON:
        if in_game:
            sound_player.fadeout_music()
            in_game = False
            going_to_main_menu = True
            ui_elements.fading_out = True
        else:
            pygame.quit()
            exit()

def menu():
    global selected_button
    global dragging_sfx_pip
    global dragging_music_pip
    global entering_game
    global going_to_main_menu
    global pause_menu
    global main_menu
    global yes_or_no_menu

    while True:
        m_x, m_y = pygame.mouse.get_pos()
        cursor.cursor.update()
        
        #Events
        click = False
        rclick = False

        if entering_game and ui_elements.fading_out == False:
            entering_game = False
            pause_menu = True
            main_menu = False
            break

        if going_to_main_menu and ui_elements.fading_out == False:
            sound_player.play_music(-1)
            going_to_main_menu = False
            yes_or_no_menu = False
            main_menu = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if not ui_elements.fading_out:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        cycle_options_up()
                    elif event.key == pygame.K_DOWN:
                        cycle_options_down()
                    elif event.key == pygame.K_RIGHT:
                        increment_option(m_x,m_y)
                    elif event.key == pygame.K_LEFT:
                        decrement_option(m_x,m_y)
                    elif event.key == pygame.K_ESCAPE:
                        go_back_or_quit_prompt()
                    elif event.key == pygame.K_RETURN:
                        if selected_button:
                            enter_selected_option(selected_button)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if sfx_slider_pip_rect.collidepoint(m_x,m_y):
                            dragging_sfx_pip = True
                        elif music_slider_pip_rect.collidepoint(m_x,m_y):
                            dragging_music_pip = True
                    elif event.button == 3:
                        rclick = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        dragging_sfx_pip = False
                        dragging_music_pip = False

        #Buttons animation
        if not ui_elements.fading_out:
            if main_menu:
                if new_game_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[NEW_GAME_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(NEW_GAME_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(NEW_GAME_BUTTON)

                elif settings_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[SETTINGS_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(SETTINGS_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(SETTINGS_BUTTON)

                elif quit_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[QUIT_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(QUIT_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(QUIT_BUTTON)

            elif settings_menu:
                if effects_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[EFFECTS_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(EFFECTS_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        sound_player.increment_effects_volume()
                    elif rclick:
                        sound_player.decrement_effects_volume()

                elif music_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[MUSIC_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(MUSIC_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        sound_player.increment_music_volume()
                    elif rclick:
                        sound_player.decrement_music_volume()

                elif back_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[BACK_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(BACK_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(BACK_BUTTON)    

            elif pause_menu:
                if resume_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[RESUME_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(RESUME_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(RESUME_BUTTON) 

                elif settings_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[SETTINGS_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(SETTINGS_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(SETTINGS_BUTTON)

                elif leave_game_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[LEAVE_GAME_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(LEAVE_GAME_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(LEAVE_GAME_BUTTON)

            elif yes_or_no_menu:
                if yes_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[YES_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(YES_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(YES_BUTTON) 

                elif no_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[NO_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(NO_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(NO_BUTTON)

            elif scores_menu:
                if back_rect.collidepoint(m_x, m_y):
                    if BUTTON_ANIM_INDICES[BACK_BUTTON] == 0:
                        sound_player.play_menu_select_sound()
                    animate_button(BACK_BUTTON, ASCENDING)
                    selected_button = None
                    if click:
                        enter_selected_option(BACK_BUTTON)    

            if dragging_sfx_pip or dragging_music_pip:
                zero_volume_pos = sfx_slider_bar_rect.center[0]-665/2
                volume = (m_x - zero_volume_pos)/665
                if volume < 0:
                    volume = 0
                elif volume > 1:
                    volume = 1            
                
                if dragging_sfx_pip:
                    sound_player.SFX_VOLUME = volume
                    sound_player.set_volume_for_all_sfx(volume)
                elif dragging_music_pip:
                    sound_player.MUSIC_VOLUME = volume
                    sound_player.set_music_volume(volume)

        if selected_button:
            if BUTTON_ANIM_INDICES[selected_button] == 0:
                sound_player.play_menu_select_sound()
            animate_button(selected_button, ASCENDING)
        
        descend_animation_on_not_selected_buttons(m_x,m_y)

        #Background animation
        if not ui_elements.fading_out:
            animate_background()

        #Drawing
        draw_menu_elements()
        cursor.cursor.draw(screen)
        if ui_elements.fading_out:
            ui_elements.fade_out()
        elif ui_elements.fading_in:
            ui_elements.fade_in()

        #Other
        pygame.display.flip()
        clock.tick(60)