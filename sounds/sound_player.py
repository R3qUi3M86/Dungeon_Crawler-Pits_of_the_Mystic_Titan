import pygame

VOLUME = 0.1

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
hero_melee_miss_sound = pygame.mixer.Sound('sounds/attack/PUNCHMIS.wav')
hero_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/ETHIT1.wav')
monster_melee_miss_sound = pygame.mixer.Sound('sounds/attack/WTRSWIP.wav')
monster_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/MUMPUN5.wav')

player_pain_sound = pygame.mixer.Sound('sounds/player/FGTPAIN.wav')
player_death_sound = pygame.mixer.Sound('sounds/player/FGTDDTH.wav')
player_overkill_sound1 = pygame.mixer.Sound('sounds/player/FGTXDTH1.wav')
player_overkill_sound2 = pygame.mixer.Sound('sounds/player/FGTXDTH2.wav')
player_overkill_sound3 = pygame.mixer.Sound('sounds/player/FGTXDTH3.wav')

ettin_pain_sound = pygame.mixer.Sound('sounds/attack/monster_pain/CENT1.wav')
ettin_death_sound = pygame.mixer.Sound('sounds/attack/monster_pain/CNTDTH1.wav')

player_overkill_sounds = [player_overkill_sound1, player_overkill_sound2, player_overkill_sound3]
all_sounds = [hero_melee_miss_sound,hero_melee_hit_sound,monster_melee_miss_sound,monster_melee_hit_sound,player_pain_sound,player_death_sound,player_overkill_sound1,player_overkill_sound2,player_overkill_sound3,ettin_pain_sound,ettin_death_sound]

def set_volume_for_all_sounds(volume):
    for sound in all_sounds:
        sound.set_volume(volume)