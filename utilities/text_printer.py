import pygame
from settings import *

pygame.init()
standard_font = pygame.font.Font(None,20)
runic1_font = pygame.font.Font("fonts/ComicRunes.ttf",34)
runic2_font = pygame.font.Font("fonts/Dalek-7ZBB.ttf",30)
runic3_font = pygame.font.Font("fonts/DsRunenglish2-nR5O.ttf",30)
runic4_font = pygame.font.Font("fonts/NorseBold-2Kge.otf",30)
runic5_font = pygame.font.Font("fonts/Norse-KaWl.otf",30)

def debug_text(text,color="Black", x = 10, y = 10):
    text_surf = standard_font.render(text,True,color)
    text_rect = text_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(screen,"White",text_rect)
    screen.blit(text_surf,text_rect)

def display_runic1_text(text, color="Red", x = 10, y = 10):
    text_surf = runic1_font.render(text,True,color)
    text_rect = text_surf.get_rect(topleft = (x,y))
    screen.blit(text_surf,text_rect)

def display_runic2_text(text, color="Red", x = 10, y = 10):
    text_surf = runic2_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    screen.blit(text_surf,text_rect)

def display_runic3_text(text, color="Red", x = 10, y = 10):
    text_surf = runic3_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    screen.blit(text_surf,text_rect)

def display_runic4_text(text, color="Red", x = 10, y = 10):
    text_surf = runic4_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    screen.blit(text_surf,text_rect)

def display_runic5_text(text, color="Red", x = 10, y = 10):
    text_surf = runic5_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    screen.blit(text_surf,text_rect)

