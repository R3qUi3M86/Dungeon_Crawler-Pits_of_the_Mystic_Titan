import pygame

# Emerald crossbow bolt
emerald_crossbow_bolt_shot_01 = pygame.image.load("images/projectiles/emerald_crossbow/shot_01.png").convert_alpha()
emerald_crossbow_bolt_destruct_01 = pygame.image.load("images/projectiles/emerald_crossbow/destruct_01.png").convert_alpha()
emerald_crossbow_bolt_destruct_02 = pygame.image.load("images/projectiles/emerald_crossbow/destruct_02.png").convert_alpha()
emerald_crossbow_bolt_destruct_03 = pygame.image.load("images/projectiles/emerald_crossbow/destruct_03.png").convert_alpha()
emerald_crossbow_bolt_destruct_04 = pygame.image.load("images/projectiles/emerald_crossbow/destruct_04.png").convert_alpha()
emerald_crossbow_bolt_shot = [emerald_crossbow_bolt_shot_01]
emerald_crossbow_bolt_destruct = [emerald_crossbow_bolt_destruct_01, emerald_crossbow_bolt_destruct_02, emerald_crossbow_bolt_destruct_03, emerald_crossbow_bolt_destruct_04]

# Necrolight ball
necrolight_ball_shot_01 = pygame.image.load("images/projectiles/necro_ball/shot_01.png").convert_alpha()
necrolight_ball_shot_02 = pygame.image.load("images/projectiles/necro_ball/shot_02.png").convert_alpha()
necrolight_ball_destruct_01 = pygame.image.load("images/projectiles/necro_ball/destruct_01.png").convert_alpha()
necrolight_ball_destruct_02 = pygame.image.load("images/projectiles/necro_ball/destruct_02.png").convert_alpha()
necrolight_ball_destruct_03 = pygame.image.load("images/projectiles/necro_ball/destruct_03.png").convert_alpha()
necrolight_ball_destruct_04 = pygame.image.load("images/projectiles/necro_ball/destruct_04.png").convert_alpha()
necrolight_ball_destruct_05 = pygame.image.load("images/projectiles/necro_ball/destruct_05.png").convert_alpha()
necrolight_ball_shot = [necrolight_ball_shot_01, necrolight_ball_shot_02]
necrolight_ball_destruct = [necrolight_ball_destruct_01, necrolight_ball_destruct_02, necrolight_ball_destruct_03, necrolight_ball_destruct_04, necrolight_ball_destruct_05]

# Bishop magic missile
bishop_magic_missile_shot_01 = pygame.image.load("images/projectiles/bishop_magic_missile/shot_01.png").convert_alpha()
bishop_magic_missile_shot_02 = pygame.image.load("images/projectiles/bishop_magic_missile/shot_02.png").convert_alpha()
bishop_magic_missile_destruct_01 = pygame.image.load("images/projectiles/bishop_magic_missile/destruct_01.png").convert_alpha()
bishop_magic_missile_destruct_02 = pygame.image.load("images/projectiles/bishop_magic_missile/destruct_02.png").convert_alpha()
bishop_magic_missile_destruct_03 = pygame.image.load("images/projectiles/bishop_magic_missile/destruct_03.png").convert_alpha()
bishop_magic_missile_destruct_04 = pygame.image.load("images/projectiles/bishop_magic_missile/destruct_04.png").convert_alpha()
bishop_magic_missile_destruct_05 = pygame.image.load("images/projectiles/bishop_magic_missile/destruct_05.png").convert_alpha()
bishop_magic_missile_destruct_06 = pygame.image.load("images/projectiles/bishop_magic_missile/destruct_06.png").convert_alpha()
bishop_magic_missile_shot = [bishop_magic_missile_shot_01,bishop_magic_missile_shot_02]
bishop_magic_missile_destruct = [bishop_magic_missile_destruct_01, bishop_magic_missile_destruct_02, bishop_magic_missile_destruct_03, bishop_magic_missile_destruct_04, bishop_magic_missile_destruct_05, bishop_magic_missile_destruct_06]

# Whirlwind
whirlwind_01 = pygame.image.load("images/projectiles/whirlwind/whirlwind_01.png").convert_alpha()
whirlwind_02 = pygame.image.load("images/projectiles/whirlwind/whirlwind_02.png").convert_alpha()
whirlwind_03 = pygame.image.load("images/projectiles/whirlwind/whirlwind_03.png").convert_alpha()
whirlwind_destruct_01 = pygame.image.load("images/projectiles/whirlwind/destruct_01.png").convert_alpha()
whirlwind_destruct_02 = pygame.image.load("images/projectiles/whirlwind/destruct_02.png").convert_alpha()
whirlwind_destruct_03 = pygame.image.load("images/projectiles/whirlwind/destruct_03.png").convert_alpha()
whirlwind_destruct_04 = pygame.image.load("images/projectiles/whirlwind/destruct_04.png").convert_alpha()
whirlwind = [whirlwind_01, whirlwind_02, whirlwind_03]
whirlwind_destruct = [whirlwind_destruct_01, whirlwind_destruct_02, whirlwind_destruct_03, whirlwind_destruct_04]

#Spike ball
spike_ball_01 = pygame.image.load("images/projectiles/spike_ball/spike_ball_01.png").convert_alpha()
spike_ball_02 = pygame.image.load("images/projectiles/spike_ball/spike_ball_02.png").convert_alpha()
spike_ball_03 = pygame.image.load("images/projectiles/spike_ball/spike_ball_03.png").convert_alpha()
spike_ball_destruct_01 = pygame.image.load("images/projectiles/spike_ball/destruct_01.png").convert_alpha()
spike_ball_destruct_02 = pygame.image.load("images/projectiles/spike_ball/destruct_02.png").convert_alpha()
spike_ball_destruct_03 = pygame.image.load("images/projectiles/spike_ball/destruct_03.png").convert_alpha()
spike_ball_destruct_04 = pygame.image.load("images/projectiles/spike_ball/destruct_04.png").convert_alpha()
spike_ball = [spike_ball_01, spike_ball_02, spike_ball_03]
spike_ball_destruct = [spike_ball_destruct_01, spike_ball_destruct_02, spike_ball_destruct_03, spike_ball_destruct_04]

#Spike shard
spike_shard_01 = pygame.image.load("images/projectiles/spike_shard/shard_01.png").convert()
spike_shard_01.set_colorkey((255,0,0))
spike_shard_destruct = pygame.image.load("images/projectiles/spike_shard/destruct_01.png").convert_alpha()
spike_shard = [spike_shard_01]

#Red orb
red_orb_01 = pygame.image.load("images/projectiles/red_orb/red_orb_01.png").convert_alpha()
red_orb_02 = pygame.image.load("images/projectiles/red_orb/red_orb_02.png").convert_alpha()
red_orb_03 = pygame.image.load("images/projectiles/red_orb/red_orb_03.png").convert_alpha()
red_orb_04 = pygame.image.load("images/projectiles/red_orb/red_orb_04.png").convert_alpha()
red_orb_05 = pygame.image.load("images/projectiles/red_orb/red_orb_05.png").convert_alpha()
red_orb_destruct_01 = pygame.image.load("images/projectiles/red_orb/destruct_01.png").convert_alpha()
red_orb_destruct_02 = pygame.image.load("images/projectiles/red_orb/destruct_02.png").convert_alpha()
red_orb_destruct_03 = pygame.image.load("images/projectiles/red_orb/destruct_03.png").convert_alpha()
red_orb_destruct_04 = pygame.image.load("images/projectiles/red_orb/destruct_04.png").convert_alpha()
red_orb_destruct_05 = pygame.image.load("images/projectiles/red_orb/destruct_05.png").convert_alpha()
red_orb_destruct_06 = pygame.image.load("images/projectiles/red_orb/destruct_06.png").convert_alpha()
red_orb_destruct_07 = pygame.image.load("images/projectiles/red_orb/destruct_07.png").convert_alpha()
red_orb_destruct_08 = pygame.image.load("images/projectiles/red_orb/destruct_08.png").convert_alpha()
red_orb_destruct_09 = pygame.image.load("images/projectiles/red_orb/destruct_09.png").convert_alpha()
red_orb = [red_orb_01, red_orb_02, red_orb_03, red_orb_04, red_orb_05]
red_orb_destruct = [red_orb_destruct_01, red_orb_destruct_02, red_orb_destruct_03, red_orb_destruct_04, red_orb_destruct_05, red_orb_destruct_06, red_orb_destruct_07, red_orb_destruct_08, red_orb_destruct_09]