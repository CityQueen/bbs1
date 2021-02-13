import pygame
import random
import time
from utilities_Labyrinthion_movement import *
from map_assets import *
from Hide_map import *

def map_1_loop(clock,Moved_Up,Moved_Down,Moved_Right,Moved_Left,black,gameDisplay,display_width,display_height,Hardmode):
    player_x = 80 * 15
    player_y = 80 * 7
    goal = random.randint(1,2)
    if goal == 1:
        goal_x = 80 * 1
        goal_y = 80 * 0
    elif goal == 2:
        goal_x = 80 * 2
        goal_y = 80 * 6
    Move_Right = False
    Move_Left = False
    Move_Up = False
    Move_Down = False
    global Map_game
    global player_square
    player_square = pygame.image.load('Pics/player.png').convert_alpha()
    game_map = pygame.image.load('Pics/Level_1.png').convert_alpha()
    Fog = pygame.image.load('Pics/Fog.png').convert_alpha()
    black_square = pygame.image.load('Pics/black.png').convert_alpha()
    goal_square = pygame.image.load('Pics/goal.png').convert_alpha()
    GFix_1 = pygame.image.load('Pics/GFix_1/GFix_1.png').convert_alpha()
    GFix1if = False
    GFix_2 = pygame.image.load('Pics/GFix_1/GFix_2.png').convert_alpha()
    GFix2if = False
    GFix_3 = pygame.image.load('Pics/GFix_1/GFix_3.png').convert_alpha()
    GFix3if = False
    GFix_4 = pygame.image.load('Pics/GFix_1/GFix_4.png').convert_alpha()
    GFix4if = False
    vergangene_zeit = 0
    vergangene_zeit = time.time()
    while True:
        vergangene_zeit += -time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Move_Up = True
                if event.key == pygame.K_LEFT:
                    Move_Left = True
                if event.key == pygame.K_DOWN:
                    Move_Down = True
                if event.key == pygame.K_RIGHT:
                    Move_Right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    Move_Up = False
                    Moved_Up = True
                    Moved_Down = False
                if event.key == pygame.K_DOWN:
                    Move_Down = False
                    Moved_Down = True
                    Moved_Up = False
                if event.key == pygame.K_LEFT:
                    Move_Left = False
                    Moved_Left = True
                    Moved_Right = False
                if event.key == pygame.K_RIGHT:
                    Move_Right = False
                    Moved_Right = True
                    Moved_Left = False
        if Move_Up == True and player_y > 0 and Move_Down == False:
            if player_x == 0 and player_y != 480:
                player_y += -5
            if player_x == 240 and player_y <= 320:
                player_y += -5
            if player_x == 320 and player_y > 560:
                player_y += -5
            if player_x == 480 and player_y > 240:
                player_y += -5
            if player_x == 720:
                player_y += -5
            if player_x == 960 and player_y > 80:
                player_y += -5
            if player_x == 1200 and player_y > 80:
                player_y += -5
        elif Move_Up == False and Moved_Up == True and Move_Down == False:
            player_y = Move_Up_stop(player_y, display_height)
            Moved_Up = Moved_Up_stop()
        if Move_Down == True and (player_y + 80) < display_height and Move_Up == False:
            if player_x == 0 and player_y != 240:
                player_y += 5
            if player_x == 240 and player_y < 320:
                player_y += 5
            if player_x == 320 and player_y >= 560:
                player_y += 5
            if player_x == 480 and player_y > 160:
                player_y += 5
            if player_x == 720:
                player_y += 5
            if player_x == 960 and player_y < 560:
                player_y += 5
            if player_x == 1200 and player_y < 560:
                player_y += 5
        elif Move_Up == False and Moved_Down == True and Move_Down == False:
            player_y = Move_Down_stop(player_y, display_height)
            Moved_Down = Moved_Down_stop()
        if Move_Left == True and player_x > 0 and Move_Right == False:
            if player_y == 0 and player_x != 240:
                player_x += -5
            if player_y == 80 and player_x > 960:
                player_x += -5
            if player_y == 240 and player_x < 320:
                player_x += -5
            if player_y == 320 and player_x > 240 and player_x < 560:
                player_x += -5
            if player_y == 480 and player_x <= 160:
                player_x += -5
            if player_y == 560:
                if player_x > 320 and player_x <= 480:
                    player_x += -5
                if player_x > 720 and player_x <= 960:
                    player_x += -5
            if player_y == 640 and player_x != 480:
                player_x += -5
        elif Move_Left == False and Moved_Left == True and Move_Right == False:
            player_x = Move_Left_stop(player_x, display_width)
            Moved_Left = Moved_Left_stop()
        if Move_Right == True and (player_x + 80) < display_width and Move_Left == False:
            if player_y == 0 and player_x != 80 and player_x != 720:
                player_x += 5
            if player_y == 80 and player_x >= 960:
                player_x += 5
            if player_y == 240 and player_x < 240:
                player_x += 5
            if player_y == 320 and player_x >= 240 and player_x < 480:
                player_x += 5
            if player_y == 480 and player_x < 160:
                player_x += 5
            if player_y == 560:
                if player_x >= 320 and player_x < 480:
                    player_x += 5
                if player_x >= 720 and player_x < 960:
                    player_x += 5
            if player_y == 640 and player_x != 320 and player_x != 720:
                player_x += 5
        elif Move_Left == False and Moved_Right == True and Move_Right == False:
            player_x = Move_Right_stop(player_x, display_width)
            Moved_Right = Moved_Right_stop()
        if Hardmode == 1 and vergangene_zeit <= -3000000000000:
            return(2)
        if Hardmode == 2 and vergangene_zeit <= -2500000000000:
            return(2)
        if Hardmode == 3 and vergangene_zeit <= -2000000000000:
            return(2)
        if player_x > 0 and player_x <= 80 and player_y == 480:
            GFix1if = True
        if player_x > 80 and player_x <= 160 and player_y == 480:
            GFix2if = True
            GFix4if = True
        if player_x > 0 and player_x <= 80 and player_y == 0:
            GFix3if = True
        if player_x == goal_x and player_y == goal_y:
            return(1)
        
        gameDisplay.fill(black)
        Map_asset(game_map,gameDisplay)
        if GFix1if == False:
            Map_asset(GFix_1,gameDisplay)
        if GFix2if == False:
            Map_asset(GFix_2,gameDisplay)
        if GFix3if == False:
            Map_asset(GFix_3,gameDisplay)
        if GFix4if == False:
            Map_asset(GFix_4,gameDisplay)
        goal_asset(goal_x,goal_y,goal_square,gameDisplay)
        Hide_map(black_square,gameDisplay,Hardmode,Fog,player_x,player_y,black)
        Player_character(player_square,player_x,player_y,gameDisplay)

        pygame.display.update()
        clock.tick(60)