import pygame
import random
from utilities.constants import *

VOLUME = 0.1

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

weapon_pickup = pygame.mixer.Sound('sounds/pickups/SAMPLE11.wav')
ammo_pickup = pygame.mixer.Sound('sounds/pickups/PICUP5.wav')

hero_melee_miss_sound = pygame.mixer.Sound('sounds/attack/PUNCHMIS.wav')
hero_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/ETHIT1.wav')
monster_melee_miss_sound = pygame.mixer.Sound('sounds/attack/WTRSWIP.wav')
monster_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/MUMPUN5.wav')

crossbow_attack_sound = pygame.mixer.Sound('sounds/attack/BOWSHT.wav')
crossbow_bolt_hit_sound = pygame.mixer.Sound('sounds/attack/hit/FIREDHIT.wav')
bishop_magic_missile_attack_sound = pygame.mixer.Sound('sounds/attack/BSHHIT2.wav')
bishop_magic_missile_hit_sound = pygame.mixer.Sound('sounds/attack/hit/IMPACT3.wav')

player_pain_sound = pygame.mixer.Sound('sounds/player/FGTPAIN.wav')
player_death_sound = pygame.mixer.Sound('sounds/player/FGTDDTH.wav')
player_overkill_sound1 = pygame.mixer.Sound('sounds/player/FGTXDTH1.wav')
player_overkill_sound2 = pygame.mixer.Sound('sounds/player/FGTXDTH2.wav')
player_overkill_sound3 = pygame.mixer.Sound('sounds/player/FGTXDTH3.wav')

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

player_overkill_sounds = [player_overkill_sound1, player_overkill_sound2, player_overkill_sound3]
all_sounds = [weapon_pickup, ammo_pickup, hero_melee_miss_sound,hero_melee_hit_sound,monster_melee_miss_sound,monster_melee_hit_sound,crossbow_attack_sound,crossbow_bolt_hit_sound,player_pain_sound,player_death_sound,player_overkill_sound1,player_overkill_sound2,player_overkill_sound3,ettin_noise1_sound,ettin_pain_sound,ettin_death_sound,ettin_overkill_sound, bishop_magic_missile_attack_sound,bishop_magic_missile_hit_sound,bishop_noise1_sound,bishop_noise2_sound,bishop_pain_sound,bishop_death_sound,bishop_overkill_sound,bishop_atkprep_sound,bishop_tele_blur_sound]

MONSTER_NOISE_SOUNDS = {ETTIN:[ettin_noise1_sound], DARK_BISHOP:[bishop_noise1_sound,bishop_noise2_sound]}
MONSTER_PAIN_SOUND = {ETTIN:ettin_pain_sound, DARK_BISHOP:bishop_pain_sound}
MONSTER_DEATH_SOUND = {ETTIN:ettin_death_sound, DARK_BISHOP:bishop_death_sound}
MONSTER_OVERKILL_SOUND = {ETTIN:ettin_overkill_sound, DARK_BISHOP:bishop_overkill_sound}
MONSTER_ATKPREP_SOUNDS = {ETTIN:None, DARK_BISHOP:bishop_atkprep_sound}

RANGED_WEAPON_SOUNDS_DICT = {EMERALD_CROSSBOW:crossbow_attack_sound, BISHOP_MAGIC_MISSILE:bishop_magic_missile_attack_sound}
PROJECTILE_HIT_SOUNDS_DICT = {CROSSBOW_BOLT:crossbow_bolt_hit_sound, MAGIC_MISSILE:bishop_magic_missile_hit_sound}

def play_item_picked_sound(self):
    if self.is_weapon:
        weapon_pickup.play()
    elif self.is_ammo:
        ammo_pickup.play()

def set_volume_for_all_sounds(volume):
    for sound in all_sounds:
        sound.set_volume(volume)

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

def play_ranged_attack_sound(weapon_name):
    RANGED_WEAPON_SOUNDS_DICT[weapon_name].play()

def play_projectile_impact_sound(projectile_name):
    PROJECTILE_HIT_SOUNDS_DICT[projectile_name].play()

def play_monster_noise_sound(monster_name):
    random.choice(MONSTER_NOISE_SOUNDS[monster_name]).play()

def play_monster_atk_prep_sound(monster_name):
    if MONSTER_ATKPREP_SOUNDS[monster_name]:
        MONSTER_ATKPREP_SOUNDS[monster_name].play()