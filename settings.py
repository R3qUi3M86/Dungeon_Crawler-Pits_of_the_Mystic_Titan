import pygame
from pygame.constants import DOUBLEBUF

starting_new_game = False

#Full screen mode
# screen_width = pygame.display.Info().current_w
# screen_height = pygame.display.Info().current_h
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

#Windowed mode
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
screen_info = pygame.display.Info()
driver = pygame.display.get_driver()
print(screen_info)
print(driver)

far_matrix_offset_x = 4
far_matrix_offset_y = 5

player_position = screen_width//2, screen_height//2

pygame.display.set_caption("Pits of the Mystic Titan")
pygame_icon = pygame.image.load('images/icon_small.png')
pygame.display.set_icon(pygame_icon)
pygame.mouse.set_visible(False)

