import pygame
from settings import *
from entities import shadow
from sounds import sound_player

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        hero_walk_front1 = pygame.image.load("images/characters/hexen/fighter/front_01.png").convert_alpha()
        hero_walk_front2 = pygame.image.load("images/characters/hexen/fighter/front_02.png").convert_alpha()
        hero_walk_front3 = pygame.image.load("images/characters/hexen/fighter/front_03.png").convert_alpha()
        hero_walk_front4 = pygame.image.load("images/characters/hexen/fighter/front_04.png").convert_alpha()
        self.hero_walk_front = [hero_walk_front1,hero_walk_front2,hero_walk_front3,hero_walk_front4]
        self.hero_walk_front_index = 0
        
        hero_attack_front1 = pygame.image.load("images/characters/hexen/fighter/front_attack_01.png").convert_alpha()
        hero_attack_front2 = pygame.image.load("images/characters/hexen/fighter/front_attack_02.png").convert_alpha()
        self.hero_attack_front = [hero_attack_front1,hero_attack_front2]
        self.hero_attack_front_index = 0
        
        self.atack = False

        self.image = self.hero_walk_front[self.hero_walk_front_index]
        self.rect = self.image.get_rect(midbottom = (PLAYER_POSITION))

    def hero_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_s] and pygame.mouse.get_pressed()[0] == False:
            self.hero_front_walk_animation()
        
        if pygame.mouse.get_pressed()[0] or self.atack == True:
            self.atack = True
            self.hero_front_attack_animation()

    def update(self):
        self.hero_input()

    def hero_front_walk_animation(self):
        self.hero_walk_front_index += 0.1
        if int(self.hero_walk_front_index) == 4:
            self.hero_walk_front_index = 0
        self.image = self.hero_walk_front[int(self.hero_walk_front_index)]

    def hero_front_attack_animation(self):
        if self.atack:
            print("initialized")
            self.image = self.hero_attack_front[int(self.hero_attack_front_index)]
            self.rect = self.image.get_rect(midbottom = (PLAYER_POSITION))

            self.hero_attack_front_index += 0.05
            print(self.hero_attack_front_index)
            if round(self.hero_attack_front_index,2) == 1.00:
                sound_player.punch_sound.play()
            if int(self.hero_attack_front_index) == 2:
                print(self.hero_attack_front_index)
                self.atack = False
                self.hero_attack_front_index = 0
                self.image = self.hero_walk_front[0]
                self.rect = self.image.get_rect(midbottom = (PLAYER_POSITION))
    
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

hero = pygame.sprite.Group()
hero.add(Hero())
hero.add(shadow.Shadow(PLAYER_POSITION))







