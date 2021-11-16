import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
hero_melee_miss_sound = pygame.mixer.Sound('sounds/atack/PUNCHMIS.wav')
hero_melee_miss_sound.set_volume(0.1)
monster_melee_miss_sound = pygame.mixer.Sound('sounds/atack/WTRSWIP.wav')
monster_melee_miss_sound.set_volume(0.1)