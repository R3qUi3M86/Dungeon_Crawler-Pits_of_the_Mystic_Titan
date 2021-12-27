import pygame
from pygame.constants import DOUBLEBUF, FULLSCREEN, SCALED

starting_new_game = False

#Full screen mode
# screen_width = pygame.display.Info().current_w
# screen_height = pygame.display.Info().current_h
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

#Windowed mode
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height)) #FULLSCREEN
screen_info = pygame.display.Info()
driver = pygame.display.get_driver()
#print(screen_info)
#print(driver)

far_matrix_offset_x = 7
far_matrix_offset_y = 6

player_position = screen_width//2, screen_height//2

pygame.display.set_caption("Pits of the Mystic Titan")
pygame_icon = pygame.image.load('images/icon_small.png')
pygame.display.set_icon(pygame_icon)
pygame.mouse.set_visible(False)

