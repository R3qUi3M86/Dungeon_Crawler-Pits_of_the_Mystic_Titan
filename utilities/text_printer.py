import pygame

pygame.init()
runic1_font = pygame.font.Font("fonts/ComicRunes.ttf",30)
runic2_font = pygame.font.Font("fonts/Dalek-7ZBB.ttf",30)
runic3_font = pygame.font.Font("fonts/DsRunenglish2-nR5O.ttf",30)
runic4_font = pygame.font.Font("fonts/NorseBold-2Kge.otf",30)
runic5_font = pygame.font.Font("fonts/Norse-KaWl.otf",30)


def display_runic1_text(text, color, x = 10, y = 10):
    display_surf = pygame.display.get_surface()
    text_surf = runic1_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    display_surf.blit(text_surf,text_rect)

def display_runic2_text(text, color, x = 10, y = 10):
    display_surf = pygame.display.get_surface()
    text_surf = runic2_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    display_surf.blit(text_surf,text_rect)

def display_runic3_text(text, color, x = 10, y = 10):
    display_surf = pygame.display.get_surface()
    text_surf = runic3_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    display_surf.blit(text_surf,text_rect)

def display_runic4_text(text, color, x = 10, y = 10):
    display_surf = pygame.display.get_surface()
    text_surf = runic4_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    display_surf.blit(text_surf,text_rect)

def display_runic5_text(text, color, x = 10, y = 10):
    display_surf = pygame.display.get_surface()
    text_surf = runic5_font.render(text,True,color)
    text_rect = text_surf.get_rect(center = (x,y))
    display_surf.blit(text_surf,text_rect)