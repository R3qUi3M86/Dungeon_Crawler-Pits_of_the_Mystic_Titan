import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

player_position = screen_width//2, screen_height//2

pygame.display.set_caption("Pits of the Mystic Titan")
pygame_icon = pygame.image.load('images/icon_small.png')
pygame.display.set_icon(pygame_icon)
pygame.mouse.set_visible(False)

