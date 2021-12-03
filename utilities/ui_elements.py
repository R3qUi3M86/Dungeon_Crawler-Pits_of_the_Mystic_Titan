import pygame
from settings import *
from images.ui import ui
from utilities.constants import *
from utilities import entity_manager
from utilities.entity_manager import hero
from utilities.text_printer import *

pickup_text_display_timer = 0
pickup_text_display_timer_limit = 210

PALE_WHITE_COLOR = (180,200,200)
PALE_ORANGE_COLOR = (210,200,150)

HEALTH_BAR_POS = 273,740
HEALTH_BAR_SIZE = 654,35
HEALTH_LENGTH = 644
EMPTY_HEALH_BAR_X_POS = -654

AMMO_COUNTER_BOX_SIZE = 108, 82
AMMO_COUNTER_BOX_POS = screen_width - AMMO_COUNTER_BOX_SIZE[0], screen_height - AMMO_COUNTER_BOX_SIZE[1]
AMMO_WEAP_IMAGE_SIZE = 27, 47
AMMO_WEAP_IMAGE_OFFSET = 22, 17
AMMO_WEAP_IMAGE_POS = AMMO_COUNTER_BOX_POS[0] + AMMO_WEAP_IMAGE_OFFSET[0], AMMO_COUNTER_BOX_POS[1] + AMMO_WEAP_IMAGE_OFFSET[1]
AMMO_NUMBER_OFFSET = 31, 0
AMMO_NUMBER_POS = AMMO_WEAP_IMAGE_POS[0] + AMMO_NUMBER_OFFSET[0], AMMO_WEAP_IMAGE_POS[1] + AMMO_NUMBER_OFFSET[1]
AMMO_INF_POS = AMMO_NUMBER_POS[0], AMMO_NUMBER_POS[1]+13

PICKUP_TEXT_POS = screen_width//2, HEALTH_BAR_POS[1] - 25
PICKUP_TEXT = "You have found "

# DARK_COLOR = (30,30,30)
# fog = pygame.Surface((screen_width,screen_height))
# fog.fill(DARK_COLOR)
# light_mask = ui.central_light5
# light_rect = light_mask.get_rect()
# fog.blit(light_mask,light_rect)

# light_surface = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA)
# light_surface.blit(ui.central_light6,(0,0))

# wall_hider_surf = pygame.Surface((296,288), pygame.SRCALPHA, 16)
# wall_hider_surf.fill((0,0,0))
# wall_hider_mask = ui.wall_hider_mask
# wall_hider_mask2 = ui.wall_hider_mask2
# wall_hider_mask_rect = wall_hider_mask.get_rect(center = WALL_HIDER_POSITION)
# wall_hider_surf.blit(wall_hider_mask,(0,0))

central_ligtht = ui.central_light6

def draw_health_bar():
    screen.blit(ui.health_bar_empty, HEALTH_BAR_POS)
    health_surface = pygame.Surface(HEALTH_BAR_SIZE, pygame.SRCALPHA)

    health_step = HEALTH_LENGTH // (hero.maxhealth)
    missing_health = hero.maxhealth - hero.health

    health_surface.blit(ui.health_bar_health,(-health_step*missing_health,0))
    health_surface.blit(ui.health_bar_health_mask,(0,0))
    health_surface.set_colorkey((0,0,255,255))
    screen.blit(ui.health_bar_empty, HEALTH_BAR_POS)
    screen.blit(health_surface, HEALTH_BAR_POS)
    screen.blit(ui.inner_shadow,HEALTH_BAR_POS)

def draw_weapon_ammo_counter():
    screen.blit(ui.ammo_counter_overlay2, AMMO_COUNTER_BOX_POS)
    screen.blit(get_selected_weapon_image(), AMMO_WEAP_IMAGE_POS)
    ammo = hero.ammo[hero.selected_weapon]
    ammo_text = format_ammo_text(ammo)
    if ammo_text != "INF":
        display_ammo_runic_text(ammo_text, PALE_WHITE_COLOR, AMMO_NUMBER_POS[0], AMMO_NUMBER_POS[1])
    else:
        screen.blit(ui.infinity_sign, AMMO_INF_POS)

def display_pickup_text():
    global pickup_text_display_timer

    item_name = entity_manager.picked_up_item_names[0]
    displayed_text = PICKUP_TEXT + item_name
    if item_name in WEAPONS:
        displayed_text += "!"
    else:
        displayed_text += "."

    if pickup_text_display_timer < pickup_text_display_timer_limit:
        display_pickup_runic_text(displayed_text, PALE_ORANGE_COLOR, PICKUP_TEXT_POS[0], PICKUP_TEXT_POS[1])
        pickup_text_display_timer += 1
    
    else:
        pickup_text_display_timer = 0
        del entity_manager.picked_up_item_names[0]
    

def get_selected_weapon_image():
    weapon = hero.selected_weapon
    return ui.inventory_weapons[HERO_WEAPONS.index(weapon)]

def format_ammo_text(ammo):
    if ammo != -1:
        if len(str(ammo)) == 1:
            return "  "+str(ammo)
        elif len(str(ammo)) == 2:
            return " "+str(ammo)
        else:
            return str(ammo)
    else:
        return "INF"
        