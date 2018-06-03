# -*- coding: utf-8 -*-
"""
@namespace JogoDoPiano

    Load everything


Copyright 2007, NATE-LSI-EPUSP

Piano Game is developed in Brazil at Escola Politécnica of 
Universidade de São Paulo. NATE is part of LSI (Integrable
Systems Laboratory) and stands for Learning, Work and Entertainment
Research Group. Visit our web page: 
www.lsi.usp.br/nate
Suggestions, bugs and doubts, please email sautchuk@lsi.usp.br

Piano Game is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation version 2 of 
the License.

Piano Game is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with Oficina; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, 
Boston, MA  02110-1301  USA.
The copy of the GNU General Public License is found in the 
COPYING file included in the source distribution.


Author:
Nathalia Sautchuk Patrício          (nathalia.sautchuk@gmail.com)

Group Manager:
Irene Karaguilla Ficheman           (irene@lsi.usp.br)

Cientific Coordinator:
Roseli de Deus Lopes                (roseli@lsi.usp.br)

"""

#import the pygame modules package and Piano Game archives
import sys, pygame
from pygame.locals import *
from Cursor import Cursor
from Key import Key
from Screen import Screen
from Stick import Stick
from Lamp import Lamp
from Game import Game
from Challenge import Challenge
from Label import Label
from Stone import Stone
from Help import Help
from Ball import Ball
from Image import Image
from gettext import gettext as _
#start these modules
pygame.init()

class JogoDoPiano(object):
    run = True    
    
    def loop(self):
        """
        The main loop

        	@param self -- the JogoDoPiano
	    
        """
        sc = Screen()
        screen = sc.getScreen()

        statusBar = Label(10, 805, [(0,0), (1,1), (0,1)])
        statusBarRight = Label(1100, 805, [(0,0), (1,1), (0,1)])
        #statusBar = Label(10, 10, [(0,0), (1,1), (0,1)])

        lampCursor = Cursor("lamp", 0, 0, [(0,0), (1,1), (0,1)])
        earCursor = Cursor("ear", 0, 0, [(0,0), (1,1), (0,1)])
        lamp = Lamp("lamp", 825, 709, [(836, 721), (868, 721), (836, 779), (868, 779)], lampCursor)
	    #lamp = Lamp("lamp", 825, 709, [(0, 0), (0, 20), (20, 20), (20, 0)], lampCursor)
        game = Game()

        buttons = [Key("1", -36, 507, [(28, 508), (0, 566), (0, 639), (31, 649), (49, 602), (30, 595), (58, 514)], game),
        Key("2", 31, 510, [(60, 512), (30, 595), (58, 603), (89, 518)], game), 
        Key("3", 19, 516, [(89, 518), (59, 603), (49, 602), (34, 649), (88, 664), (100, 615), (84, 610), (104, 520)], game), 
        Key("4", 85, 517, [(106, 520), (84, 610), (113, 615), (133, 524)], game), 
        Key("5", 75, 524, [(134, 524), (113, 615), (100, 614), (87, 663), (137, 672), (158, 527)], game), 
        Key("6", 131, 527, [(160, 527), (138, 671), (196, 677), (200, 624), (184, 621), (196, 532)], game), 
        Key("7", 187, 529, [(194, 532), (184, 621), (213, 623), (221, 536)], game), 
        Key("8", 190, 535, [(221, 536), (215, 623), (201, 624), (196, 680), (254, 677), (253, 628), (232, 626), (237, 538)], game), 
        Key("9", 234, 534, [(236, 536), (232, 625), (263, 626), (262, 539)], game), 
        Key("10", 243, 538, [(262, 539), (263, 626), (252, 627), (254, 676), (303, 675), (296, 627), (284, 626), (279, 538)], game), 
        Key("11", 282, 532, [(279, 538), (285, 625), (312, 625), (301, 538)], game), 
        Key("12", 295, 540, [(302, 540), (312, 625), (297, 627), (301, 676), (344, 670), (317, 539)], game), 
        Key("13", 320, 537, [(317, 539), (344, 671), (389, 662), (378, 625), (367, 624), (342, 538)], game), 
        Key("14", 342, 532, [(342, 538), (367, 623), (387, 621), (358, 535)], game),
        Key("15", 358, 535, [(358, 535), (387, 620), (378, 625), (389, 661), (432, 651), (418, 618), (407, 619), (376, 534)], game), 
        Key("16", 377, 526, [(376, 534), (406, 618), (424, 614), (394, 530)], game), 
        Key("17", 393, 529, [(394, 531), (424, 613), (418, 618), (431, 653), (473, 639), (411, 529)], game), 
        Key("18", 413, 524, [(413, 530), (474, 639), (511, 628), (496, 603), (484, 605), (434, 525)], game), 
        Key("19", 436, 516, [(435, 526), (483, 604), (503, 599), (456, 521)], game), 
        Key("20", 455, 520, [(455, 522), (503, 599), (496, 603), (511, 629), (548, 615), (532, 592), (522, 593), (474, 520)], game), 
        Key("21", 475, 508, [(473, 520), (522, 592), (542, 585), (493, 514)], game), 
        Key("22", 494, 512, [(493, 514), (541, 585), (532, 591), (548, 616), (585, 600), (568, 579), (559, 580), (507, 512)], game), 
        Key("23", 510, 502, [(508, 512), (559, 580), (577, 574), (526, 507)], game), 
        Key("24", 526, 506, [(527, 508), (577, 574), (569, 582), (585, 602), (621, 586), (538, 504)], game), 
        Key("25", 539, 496, [(538, 504), (622, 588), (661, 571), (639, 550), (626, 553), (572, 496)], game), 
        Key("26", 572, 485, [(572, 496), (627, 553), (644, 546), (595, 494)], game), 
        Key("27", 595, 492, [(596, 493), (645, 546), (639, 551), (662, 572), (698, 562), (672, 538), (664, 539), (610, 491)], game), 
        Key("28", 611, 481, [(610, 492), (664, 539), (679, 534), (632, 488)], game), 
        Key("29", 632, 488, [(633, 489), (679, 534), (672, 539), (698, 562), (729, 553), (646, 488)], game), 
        Key("30", 647, 485, [(645, 488), (731, 556), (763, 550), (739, 531), (728, 531), (671, 485)], game), 
        Key("31", 672, 478, [(670, 485), (728, 530), (742, 527), (690, 484)], game), 
        Key("32", 690, 483, [(693, 484), (742, 528), (739, 532), (763, 551), (796, 545), (778, 530), (769, 529), (714, 482)], game), 
        Key("33", 715, 474, [(714, 483), (770, 529), (784, 525), (734, 481)], game), 
        Key("34", 735, 481, [(736, 481), (784, 524), (777, 529), (797, 547), (829, 543), (810, 527), (802, 525), (748, 481)], game), 
        Key("35", 746, 472, [(749, 481), (802, 525), (817, 521), (771, 480)], game), 
        Key("36", 771, 482, [(773, 481), (818, 522), (810, 527), (830, 543), (869, 541), (793, 481)], game), 
        Key("37", 794, 481, [(793, 481), (869, 540), (902, 539), (879, 520), (866, 518), (821, 480)], game), 
        Key("38", 823, 472, [(820, 480), (866, 519), (881, 516), (843, 480)], game), 
        Key("39", 843, 480, [(843, 480), (881, 518), (878, 520), (902, 539), (936, 537), (909, 515), (899, 516), (852, 480)], game),
        Stick("2", _("Aleluia - Handel - 4 notes"), 892, 241, [(1022, 330), (1017, 325), (1011, 327), (1005, 319), (1008, 315), (1010, 301), (1008, 296), (1004, 289), (993, 284), (984, 277), (983, 257), (988, 248), (998, 247), (1007, 247), (1013, 249), (1018, 257), (1020, 269), (1016, 277), (1010, 282), (1007, 285), (1009, 295), (1016, 295), (1021, 326)], game),
        Stick("1", _("Silent Night - Christmas Song - 4 notes"), 885, 271, [(1006, 343), (1001, 338), (1006, 330), (1000, 322), (994, 325), (984, 324), (976, 319), (970, 308), (973, 296), (982, 288), (992, 285), (1003, 290), (1008, 299), (1009, 309), (1004, 321), (1010, 327), (1017, 325), (1038, 351)], game), 
        Stick("3", _("Save me - Hanson - 4 notes"), 917, 222, [(1039, 351), (1027, 338), (1024, 278), (1031, 276), (1030, 265), (1026, 262), (1019, 256), (1015, 246), (1016, 233), (1026, 229), (1036, 226), (1046, 231), (1049, 238), (1049, 252), (1044, 262), (1036, 266), (1037, 276), (1046, 276), (1049, 352), (1037, 352)], game),
        Stick("4", _("Every breath you take - Sting - 5 notes"), 944, 213, [(1050, 233), (1054, 223), (1063, 218), (1071, 218), (1084, 223), (1087, 235), (1083, 247), (1079, 253), (1070, 250), (1061, 249), (1055, 249), (1053, 248)], game),       
        Stick("5", _("Aquarela - Toquinho - 6 notes"), 950, 247, [(1061, 353), (1055, 302), (1063, 299), (1062, 289), (1055, 283), (1048, 276), (1047, 263), (1053, 254), (1059, 250), (1070, 250), (1082, 257), (1086, 271), (1081, 278), (1074, 282), (1070, 289), (1070, 299), (1078, 301), (1081, 351)], game),
        Stick("6", _("Wedding March - Felix Mendelssohn - 7 notes"), 969, 202, [(1091, 233), (1091, 239), (1094, 248), (1100, 257), (1108, 257), (1116, 257), (1125, 252), (1128, 242), (1129, 234), (1128, 226), (1122, 222), (1111, 219), (1102, 221), (1096, 226)], game),
        Stick("7", _("Amor Maior - Jota Quest - 8 notes"), 977, 251, [(1081, 352), (1079, 324), (1086, 304), (1093, 308), (1097, 296), (1094, 291), (1090, 283), (1089, 275), (1091, 267), (1096, 263), (1104, 261), (1109, 260), (1114, 262), (1119, 266), (1126, 272), (1126, 279), (1124, 290), (1119, 295), (1108, 298), (1102, 299), (1101, 303), (1098, 311), (1105, 313), (1091, 351)], game), 
        Stick("8", _("Greenleaves - Anonymous - 9 notes"), 1014, 211, [(1108, 346), (1118, 296), (1124, 292), (1125, 286), (1127, 279), (1127, 274), (1124, 266), (1129, 267), (1133, 257), (1127, 252), (1128, 251), (1129, 242), (1130, 238), (1130, 230), (1128, 222), (1133, 219), (1136, 217), (1144, 217), (1149, 220), (1155, 226), (1158, 234), (1158, 245), (1152, 252), (1143, 258), (1136, 263), (1135, 267), (1133, 271), (1136, 286), (1134, 278), (1138, 291), (1140, 293), (1140, 301), (1132, 301), (1129, 301), (1126, 316), (1120, 328), (1114, 339), (1111, 344)], game),
        Stick("9", _("Velha Infancia - Tribalistas - 5 notes"), 985, 219, [(1113, 344), (1130, 303), (1139, 303), (1143, 294), (1139, 288), (1136, 282), (1135, 273), (1138, 266), (1140, 262), (1146, 259), (1157, 259), (1167, 260), (1170, 269), (1173, 278), (1171, 286), (1165, 293), (1157, 295), (1149, 297), (1148, 298), (1146, 307), (1151, 309), (1139, 339), (1113, 345)], game),
        Stick("10", _("Jingle Bells - Christmas Song - 11 notes"), 883, 496, [(1009, 604), (1002, 560), (1009, 558), (1009, 547), (1004, 545), (996, 543), (991, 533), (990, 526), (995, 513), (997, 510), (1007, 507), (1016, 507), (1021, 511), (1025, 518), (1027, 528), (1024, 536), (1019, 545), (1014, 546), (1014, 557), (1023, 557), (1028, 609)], game),
        Stick("11", _("Habanera - Georges Bizet - 8 notes"), 927, 479, [(1039, 612), (1034, 536), (1040, 533), (1040, 521), (1034, 519), (1029, 515), (1024, 509), (1024, 499), (1026, 490), (1030, 487), (1039, 485), (1048, 484), (1059, 490), (1062, 498), (1062, 509), (1056, 515), (1047, 521), (1046, 523), (1047, 534), (1054, 534), (1059, 612)], game),
        Stick("12", _("Yellow Submarine - Beatles - 10 notes"), 954, 497, [(1060, 609), (1059, 589), (1062, 571), (1066, 552), (1071, 551), (1074, 541), (1068, 537), (1062, 526), (1064, 513), (1071, 504), (1085, 503), (1087, 504), (1096, 512), (1099, 520), (1096, 532), (1089, 539), (1080, 543), (1078, 553), (1086, 556), (1074, 614)], game),
        Stick("13", _("Jesu, Joy of Man's Desiring - J. S. Bach - 12 notes"), 995, 495, [(1087, 612), (1105, 549), (1113, 550), (1114, 538), (1110, 533), (1104, 522), (1105, 515), (1112, 506), (1118, 504), (1126, 501), (1134, 503), (1139, 509), (1143, 519), (1139, 533), (1129, 541), (1122, 543), (1117, 553), (1126, 554), (1108, 608)], game), 
        Stick("14", _("Symphony No. 9 - Beethoven - 15 notes"), 1027, 515, [(1113, 605), (1133, 566), (1138, 569), (1145, 560), (1142, 551), (1139, 544), (1139, 536), (1145, 529), (1152, 525), (1160, 526), (1169, 529), (1176, 539), (1174, 553), (1169, 560), (1158, 565), (1151, 564), (1146, 572), (1151, 578), (1138, 600)], game),
        lampCursor,
        earCursor,
        lamp,
        statusBar,
        statusBarRight]
        
        helps = [Help("re", 370, 500, [(0,0), (1,1), (0,1)]),
        Help("re_sust", 380, 458, [(0,0), (1,1), (0,1)]),
        Help("mi", 415, 490, [(0,0), (1,1), (0,1)]),
        Help("fa", 450, 478, [(0,0), (1,1), (0,1)]),
        Help("fa_sust", 455, 435, [(0,0), (1,1), (0,1)]),
        Help("sol", 490, 470, [(0,0), (1,1), (0,1)]),
        Help("sol_sust", 490, 425, [(0,0), (1,1), (0,1)]),
        Help("la", 525, 460, [(0,0), (1,1), (0,1)]),
        Help("la_sust", 530, 417, [(0,0), (1,1), (0,1)]),
        Help("si", 565, 445, [(0,0), (1,1), (0,1)]),
        Help("do", 595, 430, [(0,0), (1,1), (0,1)]),
        Help("do_sust", 600, 395, [(0,0), (1,1), (0,1)]),
        Help("re", 640, 420, [(0,0), (1,1), (0,1)]),
        Help("re_sust", 630, 380, [(0,0), (1,1), (0,1)]),
        Help("mi", 675, 405, [(0,0), (1,1), (0,1)]),
        Help("fa", 708, 402, [(0,0), (1,1), (0,1)]),
        Help("fa_sust", 695, 370, [(0,0), (1,1), (0,1)]),
        Help("sol", 742, 398, [(0,0), (1,1), (0,1)])
        ]

        game.setButtons(buttons, helps)
                
        stones = [Stone("stone", 115, 187, [(116, 188), (159, 188), (159, 234), (116, 234)], game),
        Stone("stone", 163, 187, [(164, 188), (207, 188), (207, 234), (164, 234)], game),
        Stone("stone", 211, 187, [(212, 188), (255, 188), (255, 234), (212, 234)], game),
        Stone("stone", 259, 187, [(260, 188), (303, 188), (303, 234), (260, 234)], game),
        Stone("stone", 307, 187, [(308, 188), (351, 188), (351, 234), (308, 234)], game),
        Stone("stone", 355, 187, [(356, 188), (399, 188), (399, 234), (356, 234)], game),
        Stone("stone", 403, 187, [(404, 188), (447, 188), (447, 234), (404, 234)], game),
        Stone("stone", 451, 187, [(452, 188), (495, 188), (495, 234), (452, 234)], game),
        Stone("stone", 498, 187, [(500, 188), (543, 188), (543, 234), (500, 234)], game),
        Stone("stone", 546, 187, [(548, 188), (591, 188), (591, 234), (548, 234)], game),
        Stone("stone", 594, 187, [(596, 188), (639, 188), (639, 234), (596, 234)], game),
        Stone("stone", 642, 187, [(644, 188), (687, 188), (687, 234), (644, 234)], game),
        Stone("stone", 690, 187, [(692, 188), (735, 188), (735, 234), (692, 234)], game),
        Stone("stone", 738, 187, [(740, 188), (783, 188), (783, 234), (740, 234)], game),
        Stone("stone", 786, 187, [(788, 188), (831, 188), (831, 234), (788, 234)], game)]
        
        animation = [Ball("bar", 80, 287, [(0,0), (1,1), (0,1)], game),
        Ball("redBall", 10, 247, [(8, 247), (100, 247), (100, 338), (8, 338)], game),
        Ball("greenBall", 10, 247, [(8, 247), (100, 247), (100, 338), (8, 338)], game),
        Ball("blueBall", 10, 247, [(8, 247), (100, 247), (100, 338), (8, 338)], game),
        Ball("yellowBall", 10, 247, [(8, 247), (100, 247), (100, 338), (8, 338)], game),
        Ball("rightBall", 850, 267, [(0,0), (1,1), (0,1)], game)
        ]

        game.addChallenge(Challenge("noitefeliz", [20, 22, 20, 17], buttons[40], stones, [5, 7, 5, 2], animation[1], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("aleluia", [27, 22, 24, 22], buttons[39], stones, [12, 7, 9, 7], animation[3], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("saveme", [16, 17, 24, 17], buttons[41], stones, [1, 2, 9, 2], animation[2], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("everybreath", [26, 27, 26, 24, 22], buttons[42], stones, [11, 12, 11, 9, 7], animation[3], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("aquarela", [15, 15, 20, 20, 19, 17], buttons[43], stones, [0, 0, 5, 5, 4, 2], animation[4], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("marchanupcial", [25, 24, 19, 22, 20, 18, 15], buttons[44], stones, [10, 9, 4, 7, 5, 3, 0], animation[1], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("amormaior", [22, 23, 22, 25, 27, 22, 20, 18], buttons[45], stones, [7, 8, 7, 10, 12, 7, 5, 3], animation[2], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("greenleaves", [17, 20, 22, 24, 25, 24, 22, 19, 15], buttons[46], stones, [], animation[4], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("velhainfancia", [19, 22, 19, 22, 29], buttons[47], stones, [4, 7, 4, 7, 14], animation[1], animation[0], animation[5], "easy", game))
        game.addChallenge(Challenge("jinglebells", [24, 24, 24, 24, 24, 24, 24, 27, 20, 22, 24], buttons[48], stones, [9, 9, 9, 9, 9, 9, 9, 12, 5, 7, 9], animation[1], animation[0], animation[5], "difficult", game))
        game.addChallenge(Challenge("habanera", [27, 26, 25, 25, 25, 24, 23, 22], buttons[49], stones, [12, 11, 10, 10, 10, 9, 8, 7], animation[2], animation[0], animation[5], "difficult", game))
        game.addChallenge(Challenge("yellow", [27, 27, 27, 27, 29, 24, 22, 22, 22, 22], buttons[50], stones, [12, 12, 12, 12, 14, 9, 7, 7, 7, 7], animation[3], animation[0], animation[5], "difficult", game))
        game.addChallenge(Challenge("jesusalegria", [20, 22, 24, 27, 25, 25, 29, 27, 27, 32, 31, 32], buttons[51], stones, [5, 7, 9, 12, 10, 10, 14, 12, 12, 17, 16, 17], animation[0], animation[4], animation[5], "difficult", game))
        game.addChallenge(Challenge("nonasinfonia", [19, 19, 20, 22, 22, 20, 19, 17, 15, 15, 17, 19, 19, 17, 17], buttons[52], stones, [4, 4, 5, 7, 7, 5, 4, 2, 0, 0, 2, 4, 4, 2, 2], animation[3], animation[0], animation[5], "difficult", game))

        keyboard = pygame.image.load("image/keyboard.png")
        
        bigBar = pygame.image.load("image/bigBar.png")
        bigBar.set_alpha(None) # disable alpha.
        bigBar.convert()
        bigBar.set_colorkey( ( 255, 0, 255 ) ) # magenta
        
        frame = pygame.image.load("image/frame.png")
        frame.set_alpha(None) # disable alpha.
        frame.convert()
        frame.set_colorkey( ( 255, 0, 255 ) ) # magenta
        
        bucket1 = pygame.image.load("image/bucket1.png")
        bucket1.set_alpha(None) # disable alpha.
        bucket1.convert()
        bucket1.set_colorkey( ( 255, 0, 255 ) ) # magenta
        
        bucket2 = pygame.image.load("image/bucket2.png")
        bucket2.set_alpha(None) # disable alpha.
        bucket2.convert()
        bucket2.set_colorkey( ( 255, 0, 255 ) ) # magenta

        clock = pygame.time.Clock()
        FPS = 20

        while self.run:  
        	for event in pygame.event.get():
        		if event.type == pygame.QUIT:
        			sys.exit()
        		else:
        			for button in buttons:
        				button.parseEvent(event)
    				for stone in stones:
        				stone.parseEvent(event)
    				for help in helps:
        				help.parseEvent(event)
    				for thing in animation:
        				thing.parseEvent(event)
        			if event.type == MOUSEMOTION:
        		    		posicao = (event.pos[0],event.pos[1])
        		    		#pygame.display.set_caption(str(posicao[0])+" x "+str(posicao[1]))	

        	screen.blit(keyboard, (0, -1))

        	for button in buttons:
        		button.draw(screen)
            		
    		for stone in stones:
    		    stone.draw(screen)
    		    
		    for thing in animation:
		        thing.draw(screen)

        	screen.blit(frame, (-39, 470))
        	screen.blit(bigBar, (114, 274))
        	
        	for help in helps:
    		    help.draw(screen)
        	
        	screen.blit(bucket1, (988, 338))
        	screen.blit(bucket2, (987, 597))
        	
        	lampCursor.draw(screen)
        	earCursor.draw(screen)
        	
        	#update the surface in the screen
        	pygame.display.flip()

		    #control number of frames per second
        	clock.tick(FPS)
		    #print "Quadros por segundo: " , clock.get_fps ()
    	
def main():
    """
    Load the main loop
    
    """
    jogodopiano = JogoDoPiano()
    jogodopiano.loop()


if __name__== '__main__':
    main()
