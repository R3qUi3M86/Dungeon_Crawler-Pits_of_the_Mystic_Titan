import pygame

#Full screen mode
# screen_width = pygame.display.Info().current_w
# screen_height = pygame.display.Info().current_h
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

#Windowed mode
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

far_matrix_offset_x = 6
far_matrix_offset_y = 7

player_position = screen_width//2, screen_height//2

pygame.display.set_caption("Pits of the Mystic Titan")
pygame_icon = pygame.image.load('images/icon_small.png')
pygame.display.set_icon(pygame_icon)
pygame.mouse.set_visible(False)

