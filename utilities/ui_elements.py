from time import time
import pygame
from settings import *
from images.ui import ui
from utilities.constants import *
from utilities import entity_manager
from utilities.text_printer import *
from utilities import cutscene_manager
from utilities import t_ctrl

pickup_text_display_timer = 0
pickup_text_display_timer_limit = 210

narrator_text_display_timer = 0
narrator_text_display_timer_limit = 240

consumable_use_image_index = 0

fading_in = False
fading_out = False
fade_overlay = pygame.Surface(screen.get_size())
fade_overlay.fill((0,0,0))
fade_overlay.set_alpha(0)

PALE_WHITE_COLOR = (180,200,200)
PALE_ORANGE_COLOR = (210,200,150)

HEALTH_BAR_POS = 273,740
HEALTH_BAR_SIZE = 654,35
HEALTH_LENGTH = 644
EMPTY_HEALH_BAR_X_POS = -654

health_surface = pygame.Surface(HEALTH_BAR_SIZE)
health_surface.set_colorkey((0,0,255))
ui.health_bar_health_mask.set_colorkey((0,255,0))
ui.health_bar_empty.set_colorkey((0,0,255))

BOSS_HP_BAR_POS = screen_width//2, 35
BOSS_HP_BAR_SIZE = 734, 46
BOSS_HP_LENGTH = 666

boss_health_surface = pygame.Surface(BOSS_HP_BAR_SIZE, pygame.SRCALPHA)

boss_hp_bar_rect = ui.boss_hp_bar_empty.get_rect()
boss_hp_bar_rect.center = BOSS_HP_BAR_POS

AMMO_COUNTER_BOX_SIZE = 108, 82
AMMO_COUNTER_BOX_POS = screen_width - AMMO_COUNTER_BOX_SIZE[0], screen_height - AMMO_COUNTER_BOX_SIZE[1]
AMMO_WEAP_IMAGE_SIZE = 27, 47
AMMO_WEAP_IMAGE_OFFSET = 22, 17
AMMO_WEAP_IMAGE_POS = AMMO_COUNTER_BOX_POS[0] + AMMO_WEAP_IMAGE_OFFSET[0], AMMO_COUNTER_BOX_POS[1] + AMMO_WEAP_IMAGE_OFFSET[1]
AMMO_NUMBER_OFFSET = 31, 0
AMMO_NUMBER_POS = AMMO_WEAP_IMAGE_POS[0] + AMMO_NUMBER_OFFSET[0], AMMO_WEAP_IMAGE_POS[1] + AMMO_NUMBER_OFFSET[1]
AMMO_INF_POS = AMMO_NUMBER_POS[0], AMMO_NUMBER_POS[1]+13

CONSUMABLE_COUNTER_BOX_SIZE = 108, 82
CONSUMABLE_COUNTER_BOX_POS = 0, screen_height - CONSUMABLE_COUNTER_BOX_SIZE[1]
CONSUMABLE_IMAGE_SIZE = 35, 35
CONSUMABLE_IMAGE_OFFSET = 54, 23
CONSUMABLE_IMAGE_POS = CONSUMABLE_COUNTER_BOX_POS[0] + CONSUMABLE_IMAGE_OFFSET[0], CONSUMABLE_COUNTER_BOX_POS[1] + CONSUMABLE_IMAGE_OFFSET[1]
CONSUMABLE_NUMBER_OFFSET = -39, -6
CONSUMABLE_NUMBER_POS = CONSUMABLE_IMAGE_POS[0] + CONSUMABLE_NUMBER_OFFSET[0], CONSUMABLE_IMAGE_POS[1] + CONSUMABLE_NUMBER_OFFSET[1]

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

central_light = ui.central_light6
damage_overlay = ui.damage_overaly

def draw_damage_overlay():
    if entity_manager.hero.has_taken_damage == True:
        index = int(entity_manager.hero.damage_timer/(entity_manager.hero.damage_timer_limit/4))
        screen.blit(damage_overlay[index],(0,0))
        entity_manager.hero.damage_timer += 0.0167 * t_ctrl.dt
    if entity_manager.hero.damage_timer >= entity_manager.hero.damage_timer_limit:
        entity_manager.hero.damage_timer = 0
        entity_manager.hero.has_taken_damage = False

def draw_health_bar():
    health_step = HEALTH_LENGTH / (entity_manager.hero.maxhealth)
    missing_health = entity_manager.hero.maxhealth - entity_manager.hero.health

    health_surface.fill((0,0,255))
    health_surface.blit(ui.health_bar_health,(-health_step*missing_health,0))
    health_surface.blit(ui.health_bar_health_mask,(0,0))
    screen.blit(ui.outer_shadow, HEALTH_BAR_POS)
    screen.blit(ui.health_bar_empty, HEALTH_BAR_POS)
    screen.blit(health_surface, HEALTH_BAR_POS)
    screen.blit(ui.inner_shadow,HEALTH_BAR_POS)

def draw_boss_hp_bar():
    health_step = BOSS_HP_LENGTH / (entity_manager.boss.maxhealth)
    missing_health = entity_manager.boss.maxhealth - entity_manager.boss.health

    boss_health_surface.fill((0,0,255))
    boss_health_surface.blit(ui.boss_hp_bar_health,(-health_step*missing_health,0))
    boss_health_surface.blit(ui.boss_hp_bar_mask,(0,0))
    boss_health_surface.set_colorkey((0,0,255))
    screen.blit(ui.boss_hp_bar_empty, boss_hp_bar_rect)
    screen.blit(boss_health_surface, boss_hp_bar_rect)

def draw_weapon_ammo_counter():
    screen.blit(ui.ammo_counter_overlay2, AMMO_COUNTER_BOX_POS)
    screen.blit(get_selected_weapon_image(), AMMO_WEAP_IMAGE_POS)
    ammo = entity_manager.hero.ammo[entity_manager.hero.selected_weapon]
    ammo_text = format_ammo_text(ammo)
    if ammo_text != "INF":
        display_ammo_runic_text(ammo_text, PALE_WHITE_COLOR, AMMO_NUMBER_POS[0], AMMO_NUMBER_POS[1])
    else:
        screen.blit(ui.infinity_sign, AMMO_INF_POS)

def draw_consumable_counter():
    global consumable_use_image_index

    screen.blit(ui.consumable_counter_overlay, CONSUMABLE_COUNTER_BOX_POS)
    selected_consumable_image = get_selected_consumable_image()
    if selected_consumable_image:
        cooldown = entity_manager.hero.consumables[entity_manager.hero.selected_consumable].use_cooldown
        cooldown_limit = entity_manager.hero.consumables[entity_manager.hero.selected_consumable].use_cooldown_limit
        if cooldown == 0:
            selected_consumable_image.set_alpha(255)
        else:
            selected_consumable_image.set_alpha(int(255*cooldown/cooldown_limit))

        consumable_use_image = ui.consumable_use[int(consumable_use_image_index)]

        screen.blit(selected_consumable_image, CONSUMABLE_IMAGE_POS)
        if cooldown != 0 and cooldown < 0.4:
            consumable_use_image_index += 0.1667 * t_ctrl.dt
            screen.blit(consumable_use_image, CONSUMABLE_IMAGE_POS)
        else:
            consumable_use_image_index = 0

        consumable = entity_manager.hero.consumables[entity_manager.hero.selected_consumable]
        uses = consumable.quantity
        consumable_text = format_consumable_text(uses)
        display_ammo_runic_text(consumable_text, PALE_WHITE_COLOR, CONSUMABLE_NUMBER_POS[0], CONSUMABLE_NUMBER_POS[1])

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
        pickup_text_display_timer += 1 * t_ctrl.dt
    
    else:
        pickup_text_display_timer = 0
        del entity_manager.picked_up_item_names[0]
    
def display_narrator_text():
    global narrator_text_display_timer

    text = cutscene_manager.narrator_text[0]

    if narrator_text_display_timer < narrator_text_display_timer_limit:
        display_pickup_runic_text(text, PALE_ORANGE_COLOR, PICKUP_TEXT_POS[0], PICKUP_TEXT_POS[1])
        narrator_text_display_timer += 1 * t_ctrl.dt
    
    else:
        narrator_text_display_timer = 0
        del cutscene_manager.narrator_text[0]

def get_selected_weapon_image():
    weapon = entity_manager.hero.selected_weapon
    return ui.inventory_weapons[HERO_WEAPONS.index(weapon)]

def get_selected_consumable_image():
    consumable = entity_manager.hero.selected_consumable
    if consumable:
        return ui.inventory_consumables[CONSUMABLES.index(consumable)]

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

def format_consumable_text(uses):
    if len(str(uses)) == 1:
        return " "+str(uses)
    elif len(str(uses)) == 2:
        return str(uses)

def fade_in():
    global fading_in
    global fade_overlay

    alpha = fade_overlay.get_alpha()

    if alpha == 0:
        fading_in = False
    else:
        alpha = alpha - int(5*t_ctrl.dt)
        if alpha < 0:
            alpha = 0
        fade_overlay.set_alpha(alpha)
  
    screen.blit(fade_overlay,(0,0))

def fade_out():
    global fading_out
    global fading_in
    global fade_overlay

    alpha = fade_overlay.get_alpha()

    if alpha == 255:
        fading_out = False
        fading_in = True
    else:
        alpha = alpha + int(5*t_ctrl.dt)
        if alpha > 255:
            alpha = 255
        fade_overlay.set_alpha(alpha+int(5*t_ctrl.dt))
  
    screen.blit(fade_overlay,(0,0))