import pygame
import random
from utilities.constants import *

SFX_VOLUME = 0.1
MUSIC_VOLUME = 0.05


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

###Music
the_winnowing_hall = 'sounds/music/The_Winnowing_Hall.mp3'
the_docks = 'sounds/music/The_Docks.mp3'
the_dungeons = 'sounds/music/The_Dungeons.mp3'
the_cathedral = 'sounds/music/The_Cathedral.mp3'
the_crater = 'sounds/music/The_Crater.mp3'
the_boss = 'sounds/music/The_Boss.mp3'

music_tracks = [the_docks,the_dungeons, the_cathedral, the_crater, the_boss, the_winnowing_hall]

###Sound Effects
blank_sound = pygame.mixer.Sound('sounds/attack/hit/BLANK.wav')

#Menu
menu_select = pygame.mixer.Sound('sounds/menu/KEYS2A.wav')
menu_push = pygame.mixer.Sound('sounds/menu/SWITCH.wav')
menu_new_game = pygame.mixer.Sound('sounds/menu/NEW_GAME.wav')

#Pickups
weapon_pickup = pygame.mixer.Sound('sounds/pickups/SAMPLE11.wav')
ammo_pickup = pygame.mixer.Sound('sounds/pickups/PICUP5.wav')
coin_01 = pygame.mixer.Sound('sounds/pickups/GOLD_PICKUP_01.wav')
coin_02 = pygame.mixer.Sound('sounds/pickups/GOLD_PICKUP_02.wav')
coin_03 = pygame.mixer.Sound('sounds/pickups/GOLD_PICKUP_03.wav')
consumable_pickup = pygame.mixer.Sound('sounds/pickups/CONSUM_PICUP.wav')
consumable_artifact_use = pygame.mixer.Sound('sounds/pickups/ARTIUSE.wav')
consumable_potion_use = pygame.mixer.Sound('sounds/pickups/ARTACT1.wav')
vase_break = pygame.mixer.Sound('sounds/pickups/POTBRK1.wav')
coin = [coin_01,coin_02,coin_03]

#Melee attacks
hero_melee_miss_sound = pygame.mixer.Sound('sounds/attack/PUNCHMIS.wav')
hero_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/ETHIT1.wav')
monster_melee_miss_sound = pygame.mixer.Sound('sounds/attack/WTRSWIP.wav')
monster_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/MUMPUN5.wav')

#Ranged attacks
crossbow_attack_sound = pygame.mixer.Sound('sounds/attack/BOWSHT.wav')
crossbow_bolt_hit_sound = pygame.mixer.Sound('sounds/attack/hit/FIREDHIT.wav')
necrolight_attack_sound = pygame.mixer.Sound('sounds/attack/NECROLIGHT_ATK.wav')
necrolight_hit_sound = pygame.mixer.Sound('sounds/attack/hit/NECROLIGHT_EXP.wav')
spike_ball_attack_sound = pygame.mixer.Sound('sounds/attack/LICH_ATK1.wav')
spike_ball_hit_sound = pygame.mixer.Sound('sounds/attack/hit/SPIKED_BALL.wav')
spike_shard_hit_sound = pygame.mixer.Sound('sounds/attack/hit/SHARD_HIT.wav')
whirlwind_attack_sound = pygame.mixer.Sound('sounds/attack/LICH_ATK2.wav')
red_orb_attack_sound = pygame.mixer.Sound('sounds/attack/LICH_ATK3.wav')
red_orb_hit_sound = pygame.mixer.Sound('sounds/attack/hit/RED_ORB.wav')
bishop_magic_missile_attack_sound = pygame.mixer.Sound('sounds/attack/BSHHIT2.wav')
bishop_magic_missile_hit_sound = pygame.mixer.Sound('sounds/attack/hit/IMPACT3.wav')

#Player
player_pain_sound = pygame.mixer.Sound('sounds/player/FGTPAIN.wav')
player_death_sound = pygame.mixer.Sound('sounds/player/FGTDDTH.wav')
player_overkill_sound1 = pygame.mixer.Sound('sounds/player/FGTXDTH1.wav')
player_overkill_sound2 = pygame.mixer.Sound('sounds/player/FGTXDTH2.wav')
player_overkill_sound3 = pygame.mixer.Sound('sounds/player/FGTXDTH3.wav')

#Monsters
ettin_noise1_sound = pygame.mixer.Sound('sounds/ettin/NOISE1.wav')
ettin_pain_sound = pygame.mixer.Sound('sounds/ettin/PAIN.wav')
ettin_death_sound = pygame.mixer.Sound('sounds/ettin/DEATH.wav')
ettin_overkill_sound = pygame.mixer.Sound('sounds/ettin/OVERKILL.wav')

bishop_noise1_sound = pygame.mixer.Sound('sounds/bishop/NOISE1.wav')
bishop_noise2_sound = pygame.mixer.Sound('sounds/bishop/NOISE2.wav')
bishop_pain_sound = pygame.mixer.Sound('sounds/bishop/PAIN.wav')
bishop_death_sound = pygame.mixer.Sound('sounds/bishop/DEATH.wav')
bishop_overkill_sound = pygame.mixer.Sound('sounds/bishop/OVERKILL.wav')
bishop_atkprep_sound = pygame.mixer.Sound('sounds/bishop/ATKPREP.wav')
bishop_tele_blur_sound = pygame.mixer.Sound('sounds/bishop/TELE_BLUR.wav')

lich_noise1_sound = pygame.mixer.Sound('sounds/iron_lich/NOISE1.wav')
lich_noise2_sound = pygame.mixer.Sound('sounds/iron_lich/NOISE2.wav')
lich_pain_sound = pygame.mixer.Sound('sounds/iron_lich/PAIN.wav')
lich_death_sound = pygame.mixer.Sound('sounds/iron_lich/DEATH.wav')

#Effects
portal_open_sound = pygame.mixer.Sound('sounds/effects/TPORT1.wav')
spell_chant_sound = pygame.mixer.Sound('sounds/effects/SPELL_CHANT.wav')

#Narrator
game_too_long_sound = pygame.mixer.Sound('sounds/narrator/GAME1.wav')
ready_to_die_sound = pygame.mixer.Sound('sounds/narrator/READY1.wav')

#Ambient
water_drop1_sound = pygame.mixer.Sound('sounds/ambient/drops/DROP1.wav')
water_drop2_sound = pygame.mixer.Sound('sounds/ambient/drops/DROP2.wav')
rocks1_sound = pygame.mixer.Sound('sounds/ambient/rocks/ROCKS1.wav')
rocks2_sound = pygame.mixer.Sound('sounds/ambient/rocks/ROCKS2.wav')

player_overkill_sounds = [player_overkill_sound1, player_overkill_sound2, player_overkill_sound3]
all_sounds = [menu_select, menu_push, menu_new_game, 
              weapon_pickup, ammo_pickup, consumable_pickup, coin_01, coin_02, coin_03, consumable_artifact_use, consumable_potion_use, vase_break, 
              hero_melee_miss_sound,hero_melee_hit_sound,monster_melee_miss_sound,monster_melee_hit_sound,
              crossbow_attack_sound,crossbow_bolt_hit_sound,
              necrolight_attack_sound, necrolight_hit_sound,
              spike_ball_attack_sound, spike_ball_hit_sound,spike_shard_hit_sound,
              whirlwind_attack_sound, blank_sound,
              red_orb_attack_sound, red_orb_hit_sound,
              bishop_magic_missile_attack_sound,bishop_magic_missile_hit_sound,
              player_pain_sound,player_death_sound,player_overkill_sound1,player_overkill_sound2,player_overkill_sound3,
              ettin_noise1_sound,ettin_pain_sound,ettin_death_sound,ettin_overkill_sound, 
              bishop_noise1_sound,bishop_noise2_sound,bishop_pain_sound,bishop_death_sound,bishop_overkill_sound,bishop_atkprep_sound,bishop_tele_blur_sound,
              lich_noise1_sound, lich_noise2_sound, lich_pain_sound, lich_death_sound,
              portal_open_sound, spell_chant_sound,
              game_too_long_sound, ready_to_die_sound,
              water_drop1_sound, water_drop2_sound, rocks1_sound, rocks2_sound]

MONSTER_NOISE_SOUNDS = {ETTIN:[ettin_noise1_sound], DARK_BISHOP:[bishop_noise1_sound,bishop_noise2_sound], IRON_LICH:[lich_noise1_sound, lich_noise2_sound]}
MONSTER_PAIN_SOUND = {ETTIN:ettin_pain_sound, DARK_BISHOP:bishop_pain_sound, IRON_LICH:lich_pain_sound}
MONSTER_DEATH_SOUND = {ETTIN:ettin_death_sound, DARK_BISHOP:bishop_death_sound, IRON_LICH:lich_death_sound}
MONSTER_OVERKILL_SOUND = {ETTIN:ettin_overkill_sound, DARK_BISHOP:bishop_overkill_sound, IRON_LICH:blank_sound}
MONSTER_ATKPREP_SOUNDS = {ETTIN:None, DARK_BISHOP:bishop_atkprep_sound, IRON_LICH:None}

ABILITIES_SOUNDS = {TELEPORT_BLUR:bishop_tele_blur_sound}

RANGED_WEAPON_SOUNDS_DICT = {EMERALD_CROSSBOW:crossbow_attack_sound,
                             NECROLIGHT:necrolight_attack_sound, 
                             BISHOP_MAGIC_MISSILE:bishop_magic_missile_attack_sound,
                             SPIKE_BALL_SPELL:spike_ball_attack_sound,
                             WHIRLWIND_SPELL:whirlwind_attack_sound,
                             RED_ORB_SPELL:red_orb_attack_sound}

PROJECTILE_HIT_SOUNDS_DICT = {CROSSBOW_BOLT:crossbow_bolt_hit_sound, NECRO_BALL:necrolight_hit_sound,
                              MAGIC_MISSILE:bishop_magic_missile_hit_sound, SPIKE_BALL:spike_ball_hit_sound, SPIKE_SHARD:spike_shard_hit_sound, WHIRLWIND:blank_sound, RED_ORB:red_orb_hit_sound}

def increment_effects_volume():
    global SFX_VOLUME

    SFX_VOLUME += 0.025
    if SFX_VOLUME >= 1:
        SFX_VOLUME = 1

    set_volume_for_all_sfx(SFX_VOLUME)

def decrement_effects_volume():
    global SFX_VOLUME

    SFX_VOLUME -= 0.025
    if SFX_VOLUME < 0:
        SFX_VOLUME = 0
         
    set_volume_for_all_sfx(SFX_VOLUME)

def increment_music_volume():
    global MUSIC_VOLUME

    MUSIC_VOLUME += 0.0125
    if MUSIC_VOLUME >= 1:
        MUSIC_VOLUME = 1

    set_music_volume(MUSIC_VOLUME)

def decrement_music_volume():
    global MUSIC_VOLUME

    MUSIC_VOLUME -= 0.0125
    if MUSIC_VOLUME < 0:
        MUSIC_VOLUME = 0
         
    set_music_volume(MUSIC_VOLUME)

def fadeout_music():
    pygame.mixer.music.fadeout(1000)

def play_menu_select_sound():
    menu_select.stop()
    menu_select.play()

def play_menu_push_sound(new_game=False):
    menu_push.stop()
    
    if new_game:
        menu_new_game.play()
    else:
        menu_push.play()

def set_volume_for_all_sfx(volume):
    for sound in all_sounds:
        sound.set_volume(volume)

def set_music_volume(volume):
    pygame.mixer.music.set_volume(volume)

def play_item_picked_sound(item):
    if item.is_weapon:
        weapon_pickup.play()
    elif item.is_ammo:
        ammo_pickup.play()
    elif item.is_consumable:
        consumable_pickup.play()
    elif item.is_currency:
        random.choice(coin).play()

def play_vase_break_sound():
    vase_break.play()

def play_monster_pain_sound(monster_name):
    MONSTER_PAIN_SOUND[monster_name].play()

def stop_monster_pain_sound(monster_name):
    MONSTER_PAIN_SOUND[monster_name].stop()

def play_monster_death_sound(monster_name):
    MONSTER_DEATH_SOUND[monster_name].play()

def stop_monster_death_sound(monster_name):
    MONSTER_DEATH_SOUND[monster_name].stop()

def play_monster_overkill_sound(monster_name):
    MONSTER_OVERKILL_SOUND[monster_name].play()

def play_monster_noise_sound(monster_name):
    random.choice(MONSTER_NOISE_SOUNDS[monster_name]).play()

def play_monster_atk_prep_sound(monster_name):
    if MONSTER_ATKPREP_SOUNDS[monster_name]:
        MONSTER_ATKPREP_SOUNDS[monster_name].play()

def play_melee_attack_sound(attacking_entity_name, hit):
    if hit:
        if attacking_entity_name == PLAYER:
            hero_melee_hit_sound.play()
        elif attacking_entity_name == ETTIN:
            monster_melee_hit_sound.play()
    else:
        if attacking_entity_name == PLAYER:
            hero_melee_miss_sound.play()
        elif attacking_entity_name == ETTIN:
            monster_melee_miss_sound.play()

def play_ranged_attack_sound(weapon_name):
    RANGED_WEAPON_SOUNDS_DICT[weapon_name].play()

def play_projectile_impact_sound(projectile_name):
    PROJECTILE_HIT_SOUNDS_DICT[projectile_name].play()

def play_ability_use_sound(ability_name):
    ABILITIES_SOUNDS[ability_name].play()

def play_consumable_use_sound(consumable_name):
    if consumable_name is QUARTZ_FLASK:
        consumable_potion_use.play()
    else:
        consumable_artifact_use.play()

def play_music(track_no):
    pygame.mixer.music.load(music_tracks[track_no])
    pygame.mixer.music.play(-1)

