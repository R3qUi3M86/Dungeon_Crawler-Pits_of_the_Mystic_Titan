import pygame
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

player_pain_sound = pygame.mixer.Sound('sounds/player/FGTPAIN.wav')
player_death_sound = pygame.mixer.Sound('sounds/player/FGTDDTH.wav')
player_overkill_sound1 = pygame.mixer.Sound('sounds/player/FGTXDTH1.wav')
player_overkill_sound2 = pygame.mixer.Sound('sounds/player/FGTXDTH2.wav')
player_overkill_sound3 = pygame.mixer.Sound('sounds/player/FGTXDTH3.wav')

ettin_growl_sound = pygame.mixer.Sound('sounds/ettin/GROWL.wav')
ettin_pain_sound = pygame.mixer.Sound('sounds/ettin/PAIN.wav')
ettin_death_sound = pygame.mixer.Sound('sounds/ettin/DEATH.wav')
ettin_overkill_sound = pygame.mixer.Sound('sounds/ettin/OVERKILL.wav')

player_overkill_sounds = [player_overkill_sound1, player_overkill_sound2, player_overkill_sound3]
all_sounds = [weapon_pickup, ammo_pickup, hero_melee_miss_sound,hero_melee_hit_sound,monster_melee_miss_sound,monster_melee_hit_sound,crossbow_attack_sound,crossbow_bolt_hit_sound,player_pain_sound,player_death_sound,player_overkill_sound1,player_overkill_sound2,player_overkill_sound3,ettin_growl_sound,ettin_pain_sound,ettin_death_sound,ettin_overkill_sound]

RANGED_WEAPON_SOUNDS_DICT = {EMERALD_CROSSBOW:crossbow_attack_sound}
PROJECTILE_HIT_SOUNDS_DICT = {CROSSBOW_BOLT:crossbow_bolt_hit_sound}

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

def play_ranged_attack_sound(weapon_name):
    RANGED_WEAPON_SOUNDS_DICT[weapon_name].play()

def play_projectile_impact_sound(projectile_name):
    PROJECTILE_HIT_SOUNDS_DICT[projectile_name].play()