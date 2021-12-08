import pygame
from utilities.constants import *

menu_background = pygame.image.load("images/menu/main.png").convert()

#Slider
slider_pip = pygame.image.load("images/menu/slider/slider_pip.png").convert_alpha()
slider_bar = pygame.image.load("images/menu/slider/slider_bar.png").convert_alpha()
slider_fill = pygame.image.load("images/menu/slider/slider_fill.png").convert_alpha()
slider_mask = pygame.image.load("images/menu/slider/slider_mask.png").convert_alpha()

#Texts
game_title = pygame.image.load("images/menu/title.png").convert_alpha()
game_paused = pygame.image.load("images/menu/game_paused.png").convert_alpha()
settings = pygame.image.load("images/menu/settings.png").convert_alpha()
sound_volume = pygame.image.load("images/menu/sound_volume.png").convert_alpha()
leave_question = pygame.image.load("images/menu/leave_game_question.png").convert_alpha()
quit_question = pygame.image.load("images/menu/quit_question.png").convert_alpha()

#Buttons
new_game_button_01 = pygame.image.load("images/menu/buttons/new_game/new_game_01.png").convert_alpha()
new_game_button_02 = pygame.image.load("images/menu/buttons/new_game/new_game_02.png").convert_alpha()
new_game_button_03 = pygame.image.load("images/menu/buttons/new_game/new_game_03.png").convert_alpha()
new_game_button_04 = pygame.image.load("images/menu/buttons/new_game/new_game_04.png").convert_alpha()
new_game_button_05 = pygame.image.load("images/menu/buttons/new_game/new_game_05.png").convert_alpha()
new_game_button_06 = pygame.image.load("images/menu/buttons/new_game/new_game_06.png").convert_alpha()
new_game_button_07 = pygame.image.load("images/menu/buttons/new_game/new_game_07.png").convert_alpha()
new_game_button_08 = pygame.image.load("images/menu/buttons/new_game/new_game_08.png").convert_alpha()
new_game_button_09 = pygame.image.load("images/menu/buttons/new_game/new_game_09.png").convert_alpha()
new_game_button_10 = pygame.image.load("images/menu/buttons/new_game/new_game_10.png").convert_alpha()

new_game_button = [new_game_button_01,new_game_button_02,new_game_button_03,new_game_button_04,new_game_button_05,
                   new_game_button_06,new_game_button_07,new_game_button_08,new_game_button_09,new_game_button_10]

settings_button_01 = pygame.image.load("images/menu/buttons/settings/settings_01.png").convert_alpha()
settings_button_02 = pygame.image.load("images/menu/buttons/settings/settings_02.png").convert_alpha()
settings_button_03 = pygame.image.load("images/menu/buttons/settings/settings_03.png").convert_alpha()
settings_button_04 = pygame.image.load("images/menu/buttons/settings/settings_04.png").convert_alpha()
settings_button_05 = pygame.image.load("images/menu/buttons/settings/settings_05.png").convert_alpha()
settings_button_06 = pygame.image.load("images/menu/buttons/settings/settings_06.png").convert_alpha()
settings_button_07 = pygame.image.load("images/menu/buttons/settings/settings_07.png").convert_alpha()
settings_button_08 = pygame.image.load("images/menu/buttons/settings/settings_08.png").convert_alpha()
settings_button_09 = pygame.image.load("images/menu/buttons/settings/settings_09.png").convert_alpha()
settings_button_10 = pygame.image.load("images/menu/buttons/settings/settings_10.png").convert_alpha()

settings_button = [settings_button_01,settings_button_02,settings_button_03,settings_button_04,settings_button_05,
                   settings_button_06,settings_button_07,settings_button_08,settings_button_09,settings_button_10]

quit_button_01 = pygame.image.load("images/menu/buttons/quit/quit_01.png").convert_alpha()
quit_button_02 = pygame.image.load("images/menu/buttons/quit/quit_02.png").convert_alpha()
quit_button_03 = pygame.image.load("images/menu/buttons/quit/quit_03.png").convert_alpha()
quit_button_04 = pygame.image.load("images/menu/buttons/quit/quit_04.png").convert_alpha()
quit_button_05 = pygame.image.load("images/menu/buttons/quit/quit_05.png").convert_alpha()
quit_button_06 = pygame.image.load("images/menu/buttons/quit/quit_06.png").convert_alpha()
quit_button_07 = pygame.image.load("images/menu/buttons/quit/quit_07.png").convert_alpha()
quit_button_08 = pygame.image.load("images/menu/buttons/quit/quit_08.png").convert_alpha()
quit_button_09 = pygame.image.load("images/menu/buttons/quit/quit_09.png").convert_alpha()
quit_button_10 = pygame.image.load("images/menu/buttons/quit/quit_10.png").convert_alpha()

quit_button = [quit_button_01,quit_button_02,quit_button_03,quit_button_04,quit_button_05,
               quit_button_06,quit_button_07,quit_button_08,quit_button_09,quit_button_10]

effects_01 = pygame.image.load("images/menu/buttons/sfx/effects_01.png").convert_alpha()
effects_02 = pygame.image.load("images/menu/buttons/sfx/effects_02.png").convert_alpha()
effects_03 = pygame.image.load("images/menu/buttons/sfx/effects_03.png").convert_alpha()
effects_04 = pygame.image.load("images/menu/buttons/sfx/effects_04.png").convert_alpha()
effects_05 = pygame.image.load("images/menu/buttons/sfx/effects_05.png").convert_alpha()
effects_06 = pygame.image.load("images/menu/buttons/sfx/effects_06.png").convert_alpha()
effects_07 = pygame.image.load("images/menu/buttons/sfx/effects_07.png").convert_alpha()
effects_08 = pygame.image.load("images/menu/buttons/sfx/effects_08.png").convert_alpha()
effects_09 = pygame.image.load("images/menu/buttons/sfx/effects_09.png").convert_alpha()
effects_10 = pygame.image.load("images/menu/buttons/sfx/effects_10.png").convert_alpha()

effects_button = [effects_01,effects_02,effects_03,effects_04,effects_05,
                  effects_06,effects_07,effects_08,effects_09,effects_10]

music_01 = pygame.image.load("images/menu/buttons/music/music_01.png").convert_alpha()
music_02 = pygame.image.load("images/menu/buttons/music/music_02.png").convert_alpha()
music_03 = pygame.image.load("images/menu/buttons/music/music_03.png").convert_alpha()
music_04 = pygame.image.load("images/menu/buttons/music/music_04.png").convert_alpha()
music_05 = pygame.image.load("images/menu/buttons/music/music_05.png").convert_alpha()
music_06 = pygame.image.load("images/menu/buttons/music/music_06.png").convert_alpha()
music_07 = pygame.image.load("images/menu/buttons/music/music_07.png").convert_alpha()
music_08 = pygame.image.load("images/menu/buttons/music/music_08.png").convert_alpha()
music_09 = pygame.image.load("images/menu/buttons/music/music_09.png").convert_alpha()
music_10 = pygame.image.load("images/menu/buttons/music/music_10.png").convert_alpha()

music_button = [music_01,music_02,music_03,music_04,music_05,
                music_06,music_07,music_08,music_09,music_10]

yes_01 = pygame.image.load("images/menu/buttons/yes/yes_01.png").convert_alpha()
yes_02 = pygame.image.load("images/menu/buttons/yes/yes_02.png").convert_alpha()
yes_03 = pygame.image.load("images/menu/buttons/yes/yes_03.png").convert_alpha()
yes_04 = pygame.image.load("images/menu/buttons/yes/yes_04.png").convert_alpha()
yes_05 = pygame.image.load("images/menu/buttons/yes/yes_05.png").convert_alpha()
yes_06 = pygame.image.load("images/menu/buttons/yes/yes_06.png").convert_alpha()
yes_07 = pygame.image.load("images/menu/buttons/yes/yes_07.png").convert_alpha()
yes_08 = pygame.image.load("images/menu/buttons/yes/yes_08.png").convert_alpha()
yes_09 = pygame.image.load("images/menu/buttons/yes/yes_09.png").convert_alpha()
yes_10 = pygame.image.load("images/menu/buttons/yes/yes_10.png").convert_alpha()

yes_button = [yes_01,yes_02,yes_03,yes_04,yes_05,
              yes_06,yes_07,yes_08,yes_09,yes_10]

no_01 = pygame.image.load("images/menu/buttons/no/no_01.png").convert_alpha()
no_02 = pygame.image.load("images/menu/buttons/no/no_02.png").convert_alpha()
no_03 = pygame.image.load("images/menu/buttons/no/no_03.png").convert_alpha()
no_04 = pygame.image.load("images/menu/buttons/no/no_04.png").convert_alpha()
no_05 = pygame.image.load("images/menu/buttons/no/no_05.png").convert_alpha()
no_06 = pygame.image.load("images/menu/buttons/no/no_06.png").convert_alpha()
no_07 = pygame.image.load("images/menu/buttons/no/no_07.png").convert_alpha()
no_08 = pygame.image.load("images/menu/buttons/no/no_08.png").convert_alpha()
no_09 = pygame.image.load("images/menu/buttons/no/no_09.png").convert_alpha()
no_10 = pygame.image.load("images/menu/buttons/no/no_10.png").convert_alpha()

no_button = [no_01,no_02,no_03,no_04,no_05,
             no_06,no_07,no_08,no_09,no_10]

back_01 = pygame.image.load("images/menu/buttons/back/back_01.png").convert_alpha()
back_02 = pygame.image.load("images/menu/buttons/back/back_02.png").convert_alpha()
back_03 = pygame.image.load("images/menu/buttons/back/back_03.png").convert_alpha()
back_04 = pygame.image.load("images/menu/buttons/back/back_04.png").convert_alpha()
back_05 = pygame.image.load("images/menu/buttons/back/back_05.png").convert_alpha()
back_06 = pygame.image.load("images/menu/buttons/back/back_06.png").convert_alpha()
back_07 = pygame.image.load("images/menu/buttons/back/back_07.png").convert_alpha()
back_08 = pygame.image.load("images/menu/buttons/back/back_08.png").convert_alpha()
back_09 = pygame.image.load("images/menu/buttons/back/back_09.png").convert_alpha()
back_10 = pygame.image.load("images/menu/buttons/back/back_10.png").convert_alpha()

back_button = [back_01,back_02,back_03,back_04,back_05,
               back_06,back_07,back_08,back_09,back_10]

resume_01 = pygame.image.load("images/menu/buttons/resume/resume_01.png").convert_alpha()
resume_02 = pygame.image.load("images/menu/buttons/resume/resume_02.png").convert_alpha()
resume_03 = pygame.image.load("images/menu/buttons/resume/resume_03.png").convert_alpha()
resume_04 = pygame.image.load("images/menu/buttons/resume/resume_04.png").convert_alpha()
resume_05 = pygame.image.load("images/menu/buttons/resume/resume_05.png").convert_alpha()
resume_06 = pygame.image.load("images/menu/buttons/resume/resume_06.png").convert_alpha()
resume_07 = pygame.image.load("images/menu/buttons/resume/resume_07.png").convert_alpha()
resume_08 = pygame.image.load("images/menu/buttons/resume/resume_08.png").convert_alpha()
resume_09 = pygame.image.load("images/menu/buttons/resume/resume_09.png").convert_alpha()
resume_10 = pygame.image.load("images/menu/buttons/resume/resume_10.png").convert_alpha()

resume_button = [resume_01,resume_02,resume_03,resume_04,resume_05,
                 resume_06,resume_07,resume_08,resume_09,resume_10]

leave_game_01 = pygame.image.load("images/menu/buttons/leave_game/leave_game_01.png").convert_alpha()
leave_game_02 = pygame.image.load("images/menu/buttons/leave_game/leave_game_02.png").convert_alpha()
leave_game_03 = pygame.image.load("images/menu/buttons/leave_game/leave_game_03.png").convert_alpha()
leave_game_04 = pygame.image.load("images/menu/buttons/leave_game/leave_game_04.png").convert_alpha()
leave_game_05 = pygame.image.load("images/menu/buttons/leave_game/leave_game_05.png").convert_alpha()
leave_game_06 = pygame.image.load("images/menu/buttons/leave_game/leave_game_06.png").convert_alpha()
leave_game_07 = pygame.image.load("images/menu/buttons/leave_game/leave_game_07.png").convert_alpha()
leave_game_08 = pygame.image.load("images/menu/buttons/leave_game/leave_game_08.png").convert_alpha()
leave_game_09 = pygame.image.load("images/menu/buttons/leave_game/leave_game_09.png").convert_alpha()
leave_game_10 = pygame.image.load("images/menu/buttons/leave_game/leave_game_10.png").convert_alpha()

leave_game_button = [leave_game_01,leave_game_02,leave_game_03,leave_game_04,leave_game_05,
                     leave_game_06,leave_game_07,leave_game_08,leave_game_09,leave_game_10]

NEW_GAME_BUTTON = "new game button"
SETTINGS_BUTTON = "settings button"
QUIT_BUTTON = "quit button"
EFFECTS_BUTTON = "effects button"
MUSIC_BUTTON = "music button"
YES_BUTTON = "yes button"
NO_BUTTON = "no button"
BACK_BUTTON = "back button"
RESUME_BUTTON = "resume button"
LEAVE_GAME_BUTTON = "leave game button"

MAIN_MENU_BUTTONS = [QUIT_BUTTON,SETTINGS_BUTTON,NEW_GAME_BUTTON]
SETTINGS_MENU_BUTTONS = [EFFECTS_BUTTON,MUSIC_BUTTON,BACK_BUTTON]
PAUSE_MENU_BUTTONS = [LEAVE_GAME_BUTTON,RESUME_BUTTON]
YES_NO_MENU_BUTTONS = [YES_BUTTON,NO_BUTTON]
MENU_BUTTON_IMGAGE_SETS = {NEW_GAME_BUTTON:new_game_button, SETTINGS_BUTTON:settings_button, QUIT_BUTTON:quit_button}