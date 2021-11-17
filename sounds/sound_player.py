import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
hero_melee_miss_sound = pygame.mixer.Sound('sounds/attack/PUNCHMIS.wav')
hero_melee_miss_sound.set_volume(0.1)
hero_melee_hit_sound = pygame.mixer.Sound('sounds/attack/hit/ETHIT1.wav')
hero_melee_hit_sound.set_volume(0.1)
monster_melee_miss_sound = pygame.mixer.Sound('sounds/attack/WTRSWIP.wav')
monster_melee_miss_sound.set_volume(0.1)

player_pain_sound = pygame.mixer.Sound('sounds/player/FGTPAIN.wav')
player_pain_sound.set_volume(0.1)
player_death_sound = pygame.mixer.Sound('sounds/player/FGTDDTH.wav')
player_death_sound.set_volume(0.1)

ettin_pain_sound = pygame.mixer.Sound('sounds/attack/monster_pain/CENT1.wav')
ettin_pain_sound.set_volume(0.1)
ettin_death_sound = pygame.mixer.Sound('sounds/attack/monster_pain/CNTDTH1.wav')
ettin_death_sound.set_volume(0.1)