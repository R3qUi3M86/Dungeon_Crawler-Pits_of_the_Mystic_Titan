from settings import *
from utilities.constants import BANNER, CORPSE1, CORPSE2, DARK_BISHOP, EMERALD_CROSSBOW, EMERALD_CROSSBOW_BOLTS, EMERALD_CROSSBOW_QUIVER, ETTIN, FLAME_PEDESTAL1, IRON_LICH, LICH_EYE, NECRO_LARGE_AMMO, NECRO_SMALL_AMMO, NECROLIGHT, QUARTZ_FLASK, RUBY_PEDESTAL_EMPTY, RUBY_PEDESTAL_FULL, SCULPTURE1, SECTOR_E, SECTOR_N, SECTOR_NE, SECTOR_NW, SECTOR_S, SECTOR_SE, SECTOR_SW, SECTOR_W, STALAG_L, STALAG_S, VASE, WALL_TORCH

test_map = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                                              XX",
"X          XXXXXXXX                                             X",
"X          XXXXXXXX                                             X",
"X          XXXXXXXX                                             X",
"X          XXXXXXXX                                             X",
"X          XXXXXXXX                                             X",
"X          XXXXXXXX                                             X",
"X                                                               X",
"X                                                               X",
"X                                                               X",
"X                                                               X",
"X                                                               X",
"X                                                               X",
"X                      XX                                       X",
"X                      XXXX                                     X",
"X                      XXXX                                     X",
"X                                                               X",
"X                                                               X",
"X                     XXXXX        ~~                           X",
"X                     XEEEX        ~~                           X",
"X                     XEEEX                                     X",
"X                                                               X",
"X                          XX                                   X",
"X                         ~XXXX                                 X",    
"X                         ~XXXX~                                X",
"X                         ~~XX~~                                X",
"X                         ~XXX                                  X",
"X                         ~XX                                   X",
"X                         ~~                                    X",
"X                                                              XX",
"X                                                              XX",
"X                                                               X",
"X                                                               X",
"X                                                               X",
"X                                                               X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

test_map_items = [[(25,19), STALAG_S],[(25,17), STALAG_L], [(25,16), RUBY_PEDESTAL_EMPTY], [(23,17), RUBY_PEDESTAL_FULL], [(26,17), CORPSE1], [(26,21), CORPSE2], [(26,20), BANNER], [(24,22), LICH_EYE], [(24,25),EMERALD_CROSSBOW]]
test_map_monsters = [[(3,13),ETTIN,SECTOR_W], [(21,12),IRON_LICH,SECTOR_W]]


level_01_map = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXEEEXXXXX       XX        XX         ~~~~XXX~~~~XXXX",
"XXXEEEXXXXX    *  XX     O             ~~~~~~~~~~~XX X",
"XX     XX         XX             XX     *~~~~~~~  XX X",
"X          XX           XX       XX               XX X",
"XX  *    XXXX           XX                      ``   X",
"XX       XXXX         XXXX                      ``XXXX",
"XX                    XXXX         XXXX           XXXX",
"XX              XX *           *   XXXX      O   *XXXX",
"X   *           XX                ~~XX            XXXX",
"X       XXX     XX       ``       ~~XX               X",
"X   O   XXXXX        ~~  ``       XXXX         ~~~   X",
"XX      XXXXX~~~~   ~~~~          XXXX        ~~~~~~~X",
"XX   XXXXXXX~~~~~~~~~~~~~~~~~~      XXXX      ~~~~~XXX",
"XXXXXXXXXXXX~~~~~~~~~~~~~~XXXXXXXXXXXXXXX        ~~XXX",
"XXXXXX  ~~~~~~      ~~    XXXXXXXXXXXXXXX    O    XXXX", 
"X   XX                              ~~    *       XXXX",
"X  XXX     ``XXX~~~~XXXXXXXXXX                 XXXXXXX",
"X  XX      ``XXXX~~~XXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXX",
"X  XX        XXXX~~~XXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXX",
"X            XXXX~~~                    XXXXXXXX``   X",
"X   XX  XX                                      ``  XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

level_01_items = [[(5,2), WALL_TORCH],[(5,6), WALL_TORCH],[(9,11), WALL_TORCH],[(3,14), WALL_TORCH],[(3,24), WALL_TORCH],[(10,23), WALL_TORCH],[(3,34), WALL_TORCH],[(18,38), WALL_TORCH],[(18,28), WALL_TORCH],[(17,6), WALL_TORCH],[(18,2), WALL_TORCH],[(23,14), WALL_TORCH],[(22,23), WALL_TORCH],[(22,29), WALL_TORCH],[(22,35), WALL_TORCH],[(22,48), WALL_TORCH],[(22,52), WALL_TORCH],
                  [(9,10), VASE],[(9,12), VASE],[(10,22), VASE],[(10,25), VASE],[(11,38), VASE],[(12,38), VASE],[(13,38), VASE],[(14,38), VASE],[(17,6), VASE],[(18,3), VASE],
                  [(15,35), QUARTZ_FLASK],[(4,52), QUARTZ_FLASK],
                  [(18,1), EMERALD_CROSSBOW_BOLTS],
                  [(7,16),BANNER],[(7,43),BANNER],[(13,28),STALAG_S]]

level_01_monsters = [[(3,20),ETTIN,SECTOR_S],[(12,28),ETTIN,SECTOR_W],[(9,32),ETTIN,SECTOR_SW],[(4,37),ETTIN,SECTOR_SW],[(6,52),ETTIN,SECTOR_S],[(11,44),ETTIN,SECTOR_N],[(20,6),ETTIN,SECTOR_W],[(21,9),ETTIN,SECTOR_N],[(18,2),ETTIN,SECTOR_S],[(22,50),ETTIN,SECTOR_S]]



level_02_map = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXXXXX",
"XXXXX                     XXXXXXXX    XXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          XXX",
"XXXX    ~~~~~~      ``  ``              XXXXXXXXX       ``   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          ``   X",
"XXX     ~~~~~~      ``* ``  XXXXXXXXX         XX   XX   ``  XXXXXXXXXXXXXXXXXXXXXXXXXXXX              ``   X",
"XXX       ~~       *        XXXXXXXXXXXXX         XXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXX    XXXXXX",
"XXXX                           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXX    XXXXXX",
"XXXXXXX   XXXXXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXX     XXXX",
"XXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXX    XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXX`` XXXXXXXXXXXX       XXXXXXXXXXXXXXXXXX   XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXX     *       XXXXXXXX       XXXXXXXXXXXXXXXXXXXXX   XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXX        ~~~~~~     ~~~~        XXXXXXXXXXXXXXXXXXXXXX   XXXX",
"XXXXXXX    XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXX         ~~~~~~~~~~~              XXXXXXXXXXX  *   XXXXX   XXXX",
"XXXXXX  ``   XXXXXXXXXXXXXXXXXX    XXXXXXX       ~~~~~~~~~~~~~~~~~~~~            XXXXXXXX     *  XXXX   XXXX",
"XXXX    ``    XXXXXXXXXXXXXXXXXXX     XXXX     ~~~~~~~~~~~~~~~~~~~~~~~~    O      XXXXXXXXX       XXX   XXXX",
"XXX   XXXXXX  XXXXXX   XXXXXXXXXXXX   XX       ~~~~~~~~~~~~~~~~~~~~~~~~          XXXXXXXXXXXXXXX      ``XXXX",
"XXX  XXXXXXX  XXXXXX  *XXXXXXXXXXXXX           ~~~~~~~~~~   ~~~~~~~~~~~        XXXXXXXXXXXXXXXXXXXXX  `` XXX",
"XX   XXXXX      XX      XXXXXXXXXXXX~       ~~~~~~~~~~~~     ~~~~~~~~~~       XXXXXXXXXXXXXXXXXXXXXXXXX  XXX",
"X    XXXXXXXX       XXXXXXXXXXXXXX~~~      ~~~~~~~~~~~~~     ~~~~~~~~~        XXXXXXXXXXXXXXXXXXXXXXXXXX  XX",
"X    XXXXXXXXXXX    XXXXXXXXXXXXXX        ~~~~~~~~~~~~~~~   ~~~~~~~~~~~      ``XXXXXXXXXXXXXXXXX     XXXX  X",
"XX      XXXXXXXXXX  XXXXXXXXXXXXXX     O  ~~~~~~~~~~~~~~~  ~~~~~~~~~~~~      ``*XXXXXXXXXXXXXXX  XX    XX  X",
"XX      XXXXXXXXXX   XXXXXXXXXXXXXX        ~~~~~~~~~~~~~~  ~~~~~~~~~~~        XXXXXXXXXXXXXXXXX  XXXX     XX",
"XXX         XXX        XXXXXXXXXXXX         ~~~~~~~~~~~~   ~~~~~~~~~~       XXXXXXXXXXXXXXXXXX  XXXXXX   XXX",
"XXX    XX               XXXXXXXXXX          ~~~~~~~~~~~   ~~~~~~~~~~~       XXXXXXXXXXXXXXXXXX  XXXXXXXXXXXX",
"XX   XXXXXXXXX           XXXXXXXXX    O        ~~~~~~~   ~~~~~~~~~~       XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXX",
"XX   XXXXXXXXXXXXXXXX        XXXX                 ~~~   ~~~~~~~~~        XXXXXXXXXXXXXXXXXX       XXXXXXXXXX",
"XX    XXXXXXXXXXXXXXXXXXX     XXX                       ~~~~~~           XXXXXXXXXXXXXXXX    ~~~    XXXXXXXX",
"XXXX    ``    XXXXXXXXXXXX    XXX   XXX                            ~~~~XXXXXXXXXXXXXXX      ~~~~     XXXXXXX",
"XXXX    ``   XXXXXXXXXXXXX          XXXXXXX                    ~~~~~~XXXXXXXXXXXXXXXX    ~~~~~~~~     XXXXXX",
"XXX          XXXXXXXXXXXXXXXXXXX    XXXXXXXXXX    ~~           ~~XXXXXXXXXXXXXXXXXXXXX   ~~~~~~~~    XXXXXXX",
"XXXX   XXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ~~           ~~XXXXXXXXXXXXXXXXXXXXXX     ~~~      XXXXXXX",
"XXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXX     O               XXXXXXXXXXXXXXXXX          O  XXXXXXXX",
"XXXXXXXXXXXXXXX           XXXXXXXXXEEEXXXXXXXXXXX                     XXXXXXXXXXXXXXXXXXX           XXXXXXXX",
"XXXXXXXXXXXXXXXXXX   XX     XXXXXXXEEEXXXXXXXXXXXXX                  XXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXX  XXXXX   XXXXX       XXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXX",
"XXXXXX  XXXXXX  *   XXXXXX   XX         XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXX",
"XXXX      XXXX     XXXXXXX  *           XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXX",
"XXX        XXXXXXXXXXXXXXX      XXXXX   *XXXXXXXXXXXXXX     XXXXXXXXX    *XXXXXXXXXXXXXXXXXXXXXXX       XXXX",
"X           XXXXXXXXXXX      XXXXXXXX     XXXXXXXXXXXX      XXXX  ``           XXXXXXXXXXXXXXXXXX      XXXXX",
"X     ``    XXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ``      XXXXXXXXX     XXXXX",
"XX    ``       XXX       XXXXXXXXXXXXXXXXXXXXXXXXXX                   XXX                 XXXXXXXX  ``  XXXX",
"XX                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXX          XXXX     ``   XXX",
"XXXXX             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ``  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX              XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",]

level_02_items = [[(35,34), WALL_TORCH],[(35,38), WALL_TORCH],[(34,27), WALL_TORCH],[(39,24), WALL_TORCH],[(41,13), WALL_TORCH],[(36,6), WALL_TORCH],[(36,7), WALL_TORCH],[(36,15), WALL_TORCH],[(32,16), WALL_TORCH],[(21,6), WALL_TORCH],[(23,15), WALL_TORCH],[(13,8), WALL_TORCH],[(26,27), WALL_TORCH],[(28,9), WALL_TORCH],[(16,21), WALL_TORCH],[(12,49), WALL_TORCH],[(14,43), WALL_TORCH],[(11,58), WALL_TORCH],[(12,66), WALL_TORCH],[(12,71), WALL_TORCH],[(13,32), WALL_TORCH],[(3,7), WALL_TORCH],[(3,15), WALL_TORCH],[(3,23), WALL_TORCH],[(4,30), WALL_TORCH],[(5,43), WALL_TORCH],[(3,35), WALL_TORCH],[(3,36), WALL_TORCH],[(3,53), WALL_TORCH],[(3,55), WALL_TORCH],[(7,29), WALL_TORCH],[(38,55), WALL_TORCH],[(41,52), WALL_TORCH],[(40,62), WALL_TORCH],[(38,71), WALL_TORCH],[(40,80), WALL_TORCH],[(40,87), WALL_TORCH],[(42,95), WALL_TORCH],[(38,102), WALL_TORCH],[(32,67), WALL_TORCH],[(27,98), WALL_TORCH],[(27,89), WALL_TORCH],[(20,98), WALL_TORCH],[(13,93), WALL_TORCH],[(8,102), WALL_TORCH],[(3,103), WALL_TORCH],[(3,99), WALL_TORCH],[(4,93), WALL_TORCH],[(8,83), WALL_TORCH],
                  [(36,6), VASE],[(36,7), VASE],[(37,6), VASE],[(37,7), VASE],[(39,2), VASE],[(40,2), VASE],[(40,1), VASE],[(28,13), VASE],[(15,4), VASE],[(13,10), VASE],[(18,10), VASE],[(27,29), VASE],[(26,28), VASE],[(15,81), VASE],[(3,5), VASE],[(4,5), VASE],[(4,4), VASE],[(5,3), VASE],[(5,4), VASE],[(5,5), VASE],[(6,3), VASE],[(6,4), VASE],[(6,5), VASE],[(7,4), VASE],[(7,5), VASE],[(3,34), VASE],[(3,35), VASE],[(3,36), VASE],[(3,37), VASE],[(7,30), VASE],[(41,52), VASE],[(42,95), VASE],[(32,67), VASE],
                  [(39,1), QUARTZ_FLASK],[(16,21), QUARTZ_FLASK],[(10,53), QUARTZ_FLASK],[(10,54), QUARTZ_FLASK],[(3,54), QUARTZ_FLASK],[(14,89), QUARTZ_FLASK],[(4,106), QUARTZ_FLASK],
                  [(39,39), EMERALD_CROSSBOW_BOLTS],[(36,15), EMERALD_CROSSBOW_BOLTS],[(16,20), EMERALD_CROSSBOW_BOLTS],[(16,22), EMERALD_CROSSBOW_BOLTS],[(14,80), EMERALD_CROSSBOW_BOLTS],[(38,71), EMERALD_CROSSBOW_BOLTS],[(26,91), EMERALD_CROSSBOW_BOLTS],[(26,92), EMERALD_CROSSBOW_BOLTS],
                  [(18,57), EMERALD_CROSSBOW_QUIVER],[(18,59), EMERALD_CROSSBOW_QUIVER],[(8,8), EMERALD_CROSSBOW_QUIVER],
                  [(17,58), EMERALD_CROSSBOW],
                  [(17,57),FLAME_PEDESTAL1],[(17,59),FLAME_PEDESTAL1],
                  [(5,19),STALAG_L],[(36,38),STALAG_L],[(14,72),STALAG_L],[(33,63),STALAG_L],
                  [(41,12),BANNER],[(43,12),BANNER],
                  [(14,92),CORPSE1],[(36,36),CORPSE1],
                  [(32,90),CORPSE2]]

level_02_monsters = [[(40,4),ETTIN,SECTOR_E],[(38,8),ETTIN,SECTOR_S],[(30,4),ETTIN,SECTOR_E],[(14,8),ETTIN,SECTOR_S],[(26,3),ETTIN,SECTOR_S],[(6,7),ETTIN,SECTOR_E],[(5,7),ETTIN,SECTOR_E],[(7,7),ETTIN,SECTOR_E],[(3,10),ETTIN,SECTOR_SE],[(3,14),ETTIN,SECTOR_SE],[(7,13),ETTIN,SECTOR_E],[(24,36),ETTIN,SECTOR_S],[(26,39),ETTIN,SECTOR_W],[(41,83),ETTIN,SECTOR_W],[(42,54),ETTIN,SECTOR_NE],[(14,93),ETTIN,SECTOR_E],[(3,99),ETTIN,SECTOR_S],[(3,103),ETTIN,SECTOR_S],
                     [(19,57),DARK_BISHOP,SECTOR_S],[(19,59),DARK_BISHOP,SECTOR_S],[(4,56),DARK_BISHOP,SECTOR_W],[(40,100),DARK_BISHOP,SECTOR_S],[(28,90),DARK_BISHOP,SECTOR_SE],[(29,99),DARK_BISHOP,SECTOR_W],[(3,101),DARK_BISHOP,SECTOR_S]]

level_03_map = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XX               XXXXXXXXXXXXXXXXXX                                     X",
"X           ``    XXXXXXXXXXXXXXXXX                                     X",
"X     *       O    XXXXXXXXXXXXXXXX   XXX  XXXXXXXXXXXXXX  XXXXXXXXXXXXXX",
"X        XX         XXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXX",
"XX       XX     *    XXXXXXXXXXXXXX   XXXXXXX                           X",
"XX                   XXXXXXXXXXXXXX   XXXXXXX                           X",
"XX                   XXXXXXXXXXXXXX   XXXXXXX                           X",
"XX   ``    ~~~       XXXXXXXXXXXXXX   XXXXXXX   XX                 XX   X",
"XXX  ``    ~~~~     XXXXXXXXXXXXXXX   XXXXXXX   XX                 XX   X",
"XXXX        ~~~    XXXXXXXXXXXXXXXX   XXXXXXX                           X",
"XXXX         ~~    XXXXXXXXXXXXXXXX   XXXXXXX                           X",
"XXX     O          XXXXXXXXXXXXXXXX   XXXXXXX                           X",
"XXX                   XXXXXXXXXXXXX   XXXXXXX                           X",
"XXXX         ~~    XXXXXXXXXXXXXXX     XXXXXX                           X",
"XXXX         ~~    XXXXXXXXXXXXXXXX   XXXXXXX                           X",
"XXXX         ~~    XXXXXXXXXXXXXXXX   XXXXXXX                           X",
"XXX     O          XXXXXXXXXXXXXXXX   XXXXXXX                           X",
"XXX                   XXXXXXXXXXXXX   XXXXXXX                           X",
"XXX        ~~        XXXXXXXXXXXXXX   XXXXXXX   XX                 XX   X",
"XX      XXXX~    O   XXXXXXXXXXXXXX   XXXXXXX   XX                 XX   X",
"X       XXXX         XXXXXXXXXXXXXX   XXXXXXX                           X",
"X       ~~~~        XXXXXXXXXXXXXXX   XXXXXXX                           X",
"X                   XXXXXXXXXXXXXXX   XXXXXXX                           X",
"XX            `    XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXX",
"XX    *            XXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXX",
"XX             `  XXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXX",
"XX       *       XXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXX",
"XXX             XXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXX",
"XXXXX           XXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXX",
"XXXXXXX        XXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXX  XXXXEEEXXXXXXX",
"XXXXXXXX      XXXXXX            XXX   XXXXXXXXXXXXXXXXXXX  XXXXEEEXXXXXXX",
"XXXXXXXX      XXX                     XXXXXXXXXXXXXXXXXX              XXX",
"XXXXXXXXX             XXXXXXXX         XXXXXXXXXXXXXXXXX               XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",]

level_03_items = [[(34,66), WALL_TORCH],[(34,62), WALL_TORCH],[(28,60), WALL_TORCH],[(23,48), WALL_TORCH],[(23,49), WALL_TORCH],[(23,67), WALL_TORCH],[(23,68), WALL_TORCH],[(12,48), WALL_TORCH],[(12,49), WALL_TORCH],[(12,67), WALL_TORCH],[(12,68), WALL_TORCH],[(7,48), WALL_TORCH],[(7,55), WALL_TORCH],[(7,60), WALL_TORCH],[(7,68), WALL_TORCH],[(3,48), WALL_TORCH],[(3,55), WALL_TORCH],[(3,60), WALL_TORCH],[(3,68), WALL_TORCH],[(3,41), WALL_TORCH],[(6,34), WALL_TORCH],[(16,38), WALL_TORCH],[(16,34), WALL_TORCH],[(15,20), WALL_TORCH],[(27,38), WALL_TORCH],[(27,34), WALL_TORCH],[(33,30), WALL_TORCH],[(34,33), WALL_TORCH],[(3,4), WALL_TORCH],[(3,8), WALL_TORCH],[(8,9), WALL_TORCH],[(8,10), WALL_TORCH],[(33,21), WALL_TORCH],
                  [(3,71), VASE],[(4,71), VASE],[(3,70), VASE],[(4,70), VASE],[(3,69), VASE],[(4,69), VASE],[(3,68), VASE],[(4,68), VASE],[(3,67), VASE],[(4,67), VASE],[(3,66), VASE],[(4,66), VASE],[(3,65), VASE],[(4,65), VASE],[(3,64), VASE],[(4,64), VASE],[(3,63), VASE],[(4,63), VASE],[(3,62), VASE],[(4,62), VASE],
                  [(30,60), QUARTZ_FLASK],[(28,60), QUARTZ_FLASK],[(29,60), QUARTZ_FLASK],[(5,41), QUARTZ_FLASK],[(5,42), QUARTZ_FLASK],
                  [(34, 69), EMERALD_CROSSBOW_QUIVER],
                  [(16,58),NECROLIGHT],
                  [(15,58),NECRO_LARGE_AMMO],[(17,58),NECRO_LARGE_AMMO],[(16,57),NECRO_LARGE_AMMO],[(16,59),NECRO_LARGE_AMMO],[(15,20),NECRO_LARGE_AMMO],
                  [(16,56),NECRO_SMALL_AMMO],[(16,60),NECRO_SMALL_AMMO],[(14,58),NECRO_SMALL_AMMO],[(18,58),NECRO_SMALL_AMMO],[(15,57),NECRO_SMALL_AMMO],[(15,59),NECRO_SMALL_AMMO],[(17,57),NECRO_SMALL_AMMO],[(17,59),NECRO_SMALL_AMMO],[(6,34),NECRO_SMALL_AMMO],[(16,38),NECRO_SMALL_AMMO],[(16,34),NECRO_SMALL_AMMO],[(27,38),NECRO_SMALL_AMMO],[(27,34),NECRO_SMALL_AMMO],
                  [(13,51),FLAME_PEDESTAL1],[(13,65),FLAME_PEDESTAL1],[(19,51),FLAME_PEDESTAL1],[(19,65),FLAME_PEDESTAL1],[(20,58),FLAME_PEDESTAL1],[(12,58),FLAME_PEDESTAL1],[(16,50),FLAME_PEDESTAL1],[(16,66),FLAME_PEDESTAL1],
                  [(16,55),CORPSE1],[(15,60),CORPSE1],[(17,61),CORPSE1],[(8,15),CORPSE1],
                  [(27,6),CORPSE2],[(26,16),CORPSE2],[(17,7),CORPSE2],[(15,14),CORPSE2],
                  [(31,7),BANNER],[(31,14),BANNER],
                  [(20,19),STALAG_L],
                  [(7,7),STALAG_S],]

level_03_monsters = [[(4,3),ETTIN,SECTOR_S],[(4,5),ETTIN,SECTOR_S],[(4,7),ETTIN,SECTOR_S],[(4,9),ETTIN,SECTOR_S],[(4,11),ETTIN,SECTOR_S],[(4,13),ETTIN,SECTOR_S],[(13,16),ETTIN,SECTOR_S],[(22,14),ETTIN,SECTOR_S],[(22,15),ETTIN,SECTOR_S],[(25,5),ETTIN,SECTOR_SE],[(27,10),ETTIN,SECTOR_S],[(34,26),ETTIN,SECTOR_E],[(35,36),ETTIN,SECTOR_N],[(31,36),ETTIN,SECTOR_N],[(30,35),ETTIN,SECTOR_N],[(30,37),ETTIN,SECTOR_N],[(26,36),ETTIN,SECTOR_N],[(25,35),ETTIN,SECTOR_N],[(25,37),ETTIN,SECTOR_N],[(19,36),ETTIN,SECTOR_N],[(18,35),ETTIN,SECTOR_N],[(18,37),ETTIN,SECTOR_N],[(14,36),ETTIN,SECTOR_N],[(13,35),ETTIN,SECTOR_N],[(13,37),ETTIN,SECTOR_N],[(9,36),ETTIN,SECTOR_N],[(8,35),ETTIN,SECTOR_N],[(8,37),ETTIN,SECTOR_N],[(21,54),ETTIN,SECTOR_N],[(21,62),ETTIN,SECTOR_N],[(11,54),ETTIN,SECTOR_S],[(11,62),ETTIN,SECTOR_S],[(14,68),ETTIN,SECTOR_W],[(18,68),ETTIN,SECTOR_W],[(14,48),ETTIN,SECTOR_E],[(18,48),ETTIN,SECTOR_E],
                     [(9,5),DARK_BISHOP,SECTOR_S],[(9,7),DARK_BISHOP,SECTOR_S],[(9,9),DARK_BISHOP,SECTOR_S],[(9,11),DARK_BISHOP,SECTOR_S],[(9,13),DARK_BISHOP,SECTOR_S],[(9,15),DARK_BISHOP,SECTOR_S],[(13,8),DARK_BISHOP,SECTOR_S],[(17,6),DARK_BISHOP,SECTOR_SE],[(17,10),DARK_BISHOP,SECTOR_SE],[(17,16),DARK_BISHOP,SECTOR_S],[(22,36),DARK_BISHOP,SECTOR_N],[(21,35),DARK_BISHOP,SECTOR_N],[(21,37),DARK_BISHOP,SECTOR_N],[(14,51),DARK_BISHOP,SECTOR_E],[(15,51),ETTIN,SECTOR_E],[(17,51),ETTIN,SECTOR_E],[(15,51),DARK_BISHOP,SECTOR_E],[(17,51),DARK_BISHOP,SECTOR_E],[(15,65),DARK_BISHOP,SECTOR_W],[(17,65),DARK_BISHOP,SECTOR_W],[(12,60),DARK_BISHOP,SECTOR_S],[(12,56),DARK_BISHOP,SECTOR_S],[(20,60),DARK_BISHOP,SECTOR_N],[(20,56),DARK_BISHOP,SECTOR_N]]

level_04_map = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXvvvvvvvvvvvvvvvvvvvvvvvvvvvvvXXX",
"XXvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvXX",
"Xvvvv                         vvvvX",
"Xvvv          O     O          vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvv    XXX             XXX    vvvX",
"Xvvv    XXX             XXX    vvvX",
"Xvvv    XXX             XXX    vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvvv    *     `` ``     *    vvvvX",
"Xvvvvvvvv      `` ``      vvvvvvvvX",
"Xvvvvvvvv  ``    *   ``   vvvvvvvvX",
"Xvvvvvvvv      `` ``      vvvvvvvvX",
"Xvvvv    *     `` ``     *    vvvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"Xvvv    XXX             XXX    vvvX",
"Xvvv    XXX             XXX    vvvX",
"Xvvv    XXX             XXX    vvvX",
"Xvvv                           vvvX",
"Xvvv                           vvvX",
"XXvvv         O     O         vvvXX",
"XXXvvv                       vvvXXX",
"XXXXXXXXX      XXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXX      XXXXXXXXXXXXXXEEEXXX",
"XXXXXXXX        XXXXXXXXXXXXXEEEXXX",
"XX                               XX",
"X                                 X",
"XX       XXXXXX                  XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

level_04_items = [[(12,9), WALL_TORCH],[(12,25), WALL_TORCH],[(28,9), WALL_TORCH],[(28,25), WALL_TORCH],[(35,3), WALL_TORCH],[(35,6), WALL_TORCH],[(35,21), WALL_TORCH],[(35,28), WALL_TORCH],[(35,32), WALL_TORCH],
                  [(34,8), VASE],[(34,15), VASE],
                  [(36,2), QUARTZ_FLASK],[(33,9), QUARTZ_FLASK],[(33,14), QUARTZ_FLASK],[(6,29), QUARTZ_FLASK],[(6,5), QUARTZ_FLASK],[(30,29), QUARTZ_FLASK],[(30,5), QUARTZ_FLASK],
                  [(36,33), EMERALD_CROSSBOW_QUIVER],[(36,1), EMERALD_CROSSBOW_QUIVER],[(35,2), EMERALD_CROSSBOW_QUIVER],[(37,2), EMERALD_CROSSBOW_QUIVER],
                  [(13,13), EMERALD_CROSSBOW_BOLTS],[(14,12), EMERALD_CROSSBOW_BOLTS],[(13,21), EMERALD_CROSSBOW_BOLTS],[(14,22), EMERALD_CROSSBOW_BOLTS],[(23,21), EMERALD_CROSSBOW_BOLTS],[(22,22), EMERALD_CROSSBOW_BOLTS],[(22,12), EMERALD_CROSSBOW_BOLTS],[(23,13), EMERALD_CROSSBOW_BOLTS],
                  [(6,17), NECRO_LARGE_AMMO],
                  [(28,9), NECRO_SMALL_AMMO],[(28,25), NECRO_SMALL_AMMO],[(12,9), NECRO_SMALL_AMMO],[(12,25), NECRO_SMALL_AMMO],
                  [(7,6), FLAME_PEDESTAL1],[(7,28), FLAME_PEDESTAL1],[(29,6), FLAME_PEDESTAL1],[(29,28), FLAME_PEDESTAL1],[(14,13), FLAME_PEDESTAL1],[(14,21), FLAME_PEDESTAL1],[(22,13), FLAME_PEDESTAL1],[(22,21), FLAME_PEDESTAL1],
                  [(15,14), SCULPTURE1],[(15,20), SCULPTURE1],[(21,14), SCULPTURE1],[(21,20), SCULPTURE1],
                  [(10,17),RUBY_PEDESTAL_EMPTY],
                  [(18,19),CORPSE1],[(17,15),CORPSE1]]

level_04_monsters = []

TEST_MAP = "test_map"
LEVEL_01 = "level_01"
LEVEL_02 = "level_02"
LEVEL_03 = "level_03"
LEVEL_04 = "level_04"

LEVEL_LAYOUT_DICT = {LEVEL_01: level_01_map, LEVEL_02: level_02_map, LEVEL_03: level_03_map, LEVEL_04: level_04_map, TEST_MAP:test_map}
LEVEL_ITEMS_DICT = {LEVEL_01:level_01_items, LEVEL_02:level_02_items, LEVEL_03:level_03_items, LEVEL_04:level_04_items, TEST_MAP:test_map_items}
LEVEL_MONSTERS_DICT = {LEVEL_01:level_01_monsters, LEVEL_02:level_02_monsters, LEVEL_03:level_03_monsters, LEVEL_04:level_04_monsters, TEST_MAP:test_map_monsters}

# Legend
ENTRANCE = "E" 
EXIT = "N"
WALL = "X"
WATER = "~"
LAVA = "v"
FLOOR = " "
FLOOR_PIT = "O"
SIMPLE_CRACK = "*"
CORNER_CRACK = "`"