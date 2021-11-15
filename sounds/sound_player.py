import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
punch_sound = pygame.mixer.Sound('sounds/atack/PUNCHMIS.wav')
punch_sound.set_volume(0.1)