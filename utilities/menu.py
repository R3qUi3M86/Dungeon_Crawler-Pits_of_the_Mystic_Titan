import random
import pygame
import math
from sys import exit
from settings import *
from entities import cursor
from images.menu.menu_images import *
from sounds.sound_player import play_menu_push_sound, play_menu_select_sound

pygame.init()
clock = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT])

#Global variables
main_menu = True
settings_menu = False
pause_menu = False
quit_menu = False
start_game = False
selected_button = None

fading_out = False
fade_out_overlay = pygame.Surface(screen.get_size())
fade_out_overlay.fill((0,0,0))

#Background image
menu_background_image = pygame.transform.scale(menu_background,(1400,934))
background_pos = -100,-67
background_velocity = 0,0
angle = 0

#Button images and rects
title_img = game_title
new_game_button_img = new_game_button[0]
settings_button_img = settings_button[0]
quit_button_img = quit_button[0]
title_rect = title_img.get_rect()
title_rect.center = (screen_width//2, 154)
new_game_rect = new_game_button_img.get_rect()
new_game_rect.center = (screen_width//2,330)
settings_rect = settings_button_img.get_rect()
settings_rect.center = (screen_width//2,420)
quit_rect = quit_button_img.get_rect()
quit_rect.center = (screen_width//2,510)

#Button animation
new_game_button_index = 0
settings_button_index = 0
quit_button_index = 0

ASCENDING = "ascending"
DESCENDING = "descending"

BUTTON_IMAGES = {NEW_GAME_BUTTON:new_game_button_img, SETTINGS_BUTTON:settings_button_img, QUIT_BUTTON: quit_button_img}
BUTTON_ANIM_INDICES = {NEW_GAME_BUTTON:new_game_button_index, SETTINGS_BUTTON:settings_button_index, QUIT_BUTTON: quit_button_index}

#Drawing
def draw_menu_elements():
    screen.blit(menu_background_image,(background_pos))
    screen.blit(title_img,title_rect)

    if main_menu:
        draw_main_menu_buttons()
    elif settings_menu:
        draw_settings_menu_elements()
    elif quit_menu:
        draw_quit_menu_buttons()
    elif pause_menu:
        draw_pause_menu_buttons()

def draw_main_menu_buttons():
    screen.blit(BUTTON_IMAGES[NEW_GAME_BUTTON],new_game_rect)
    screen.blit(BUTTON_IMAGES[SETTINGS_BUTTON],settings_rect)
    screen.blit(BUTTON_IMAGES[QUIT_BUTTON],quit_rect)

def draw_settings_menu_elements():
    pass

def draw_quit_menu_buttons():
    pass

def draw_pause_menu_buttons():
    pass

#Menu effects
def fade_out_and_start_game():
    pass

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

#Menu movement
def cycle_options_up():
    global selected_button

    if selected_button == None:
        selected_button = NEW_GAME_BUTTON
    else:
        index = MENU_BUTTONS.index(selected_button)
        if index < len(MENU_BUTTONS) - 1:
            selected_button = MENU_BUTTONS[index+1]
        else:
            selected_button = MENU_BUTTONS[0]

def cycle_options_down():
    global selected_button

    if selected_button == None:
        selected_button = NEW_GAME_BUTTON
    else:
        index = MENU_BUTTONS.index(selected_button)
        selected_button = MENU_BUTTONS[index-1]

def increment_option():
    pass

def decrement_option():
    pass

def go_back_or_quit_prompt():
    pass

def enter_selected_option():
    global main_menu
    global pause_menu
    global settings_menu
    global quit_menu
    global fading_out

    play_menu_push_sound()
    if selected_button == SETTINGS_BUTTON:
        main_menu = False
        settings_menu = True
    elif selected_button == QUIT_BUTTON:
        main_menu = False
        quit_menu = True
    elif selected_button == NEW_GAME_BUTTON:
        main_menu = False
        pause_menu = True
        fading_out = True

def menu():
    global selected_button

    while True:
        m_x, m_y = pygame.mouse.get_pos()
        cursor.cursor.update()
        
        #Events
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cycle_options_up()
                elif event.key == pygame.K_DOWN:
                    cycle_options_down()
                elif event.key == pygame.K_RIGHT:
                    increment_option()
                elif event.key == pygame.K_LEFT:
                    decrement_option()
                elif event.key == pygame.K_ESCAPE:
                    go_back_or_quit_prompt()
                elif event.key == pygame.K_RETURN:
                    if selected_button:
                        enter_selected_option()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #Buttons animation
        if new_game_rect.collidepoint(m_x, m_y):
            if BUTTON_ANIM_INDICES[NEW_GAME_BUTTON] == 0:
                play_menu_select_sound()
            animate_button(NEW_GAME_BUTTON, ASCENDING)
            selected_button = None
            if click:
                enter_selected_option()

        elif settings_rect.collidepoint(m_x, m_y):
            if BUTTON_ANIM_INDICES[SETTINGS_BUTTON] == 0:
                play_menu_select_sound()
            animate_button(SETTINGS_BUTTON, ASCENDING)
            selected_button = None
            if click:
                enter_selected_option()

        elif quit_rect.collidepoint(m_x, m_y):
            if BUTTON_ANIM_INDICES[QUIT_BUTTON] == 0:
                play_menu_select_sound()
            animate_button(QUIT_BUTTON, ASCENDING)
            selected_button = None
            if click:
                enter_selected_option()

        if selected_button:
            if BUTTON_ANIM_INDICES[selected_button] == 0:
                play_menu_select_sound()
            animate_button(selected_button, ASCENDING)
        descend_animation_on_not_selected_buttons(m_x,m_y)

        #Background animation
        animate_background()

        #Drawing
        draw_menu_elements()
        cursor.cursor.draw(screen)

        #Other
        pygame.display.update()
        clock.tick(60)