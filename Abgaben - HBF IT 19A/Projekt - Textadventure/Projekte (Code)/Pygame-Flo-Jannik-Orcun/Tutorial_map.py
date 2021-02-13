import pygame
from utilities_Labyrinthion_movement import *
from map_assets import *
from Hide_map import *

def tutorial_loop(clock,Moved_Up,Moved_Down,Moved_Right,Moved_Left,black,gameDisplay,display_width,display_height,Hardmode):
    player_x = 80 * 1
    player_y = 80 * 4
    goal_x = 80 * 13
    goal_y = 80 * 7
    Move_Right = False
    Move_Left = False
    Move_Up = False
    Move_Down = False
    global Map_game
    global player_square
    player_square = pygame.image.load('Pics/player.png').convert_alpha()
    game_map = pygame.image.load('Pics/Tutorial_Level.png').convert_alpha()
    Fog = pygame.image.load('Pics/Fog.png').convert_alpha()
    black_square = pygame.image.load('Pics/black.png').convert_alpha()
    goal_square = pygame.image.load('Pics/goal.png').convert_alpha()

    gameExit = False
    while not gameExit:
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
            if player_x == 560 and player_y > 80 and player_y <= 560:
                player_y += -5
        elif Move_Up == False and Moved_Up == True and Move_Down == False:
            player_y = Move_Up_stop(player_y, display_height)
            Moved_Up = Moved_Up_stop()
        if Move_Down == True and (player_y + 80) < display_height and Move_Up == False:
            if player_x == 560 and player_y >= 80 and player_y < 560:
                player_y += 5
        elif Move_Up == False and Moved_Down == True and Move_Down == False:
            player_y = Move_Down_stop(player_y, display_height)
            Moved_Down = Moved_Down_stop()
        if Move_Left == True and player_x > 0 and Move_Right == False:
            if player_y == 80 and player_x > 240:
                player_x += -5
            if player_y == 320 and player_x > 80:
                player_x += -5
            if player_y == 560 and player_x > 240:
                player_x += -5
        elif Move_Left == False and Moved_Left == True and Move_Right == False:
            player_x = Move_Left_stop(player_x, display_width)
            Moved_Left = Moved_Left_stop()
        if Move_Right == True and (player_x + 80) < display_width and Move_Left == False:
            if player_y == 80 and player_x < 880:
                player_x += 5
            if player_y == 320 and player_x < 880:
                player_x += 5
            if player_y == 560 and player_x < 1040:
                player_x += 5
        elif Move_Left == False and Moved_Right == True and Move_Right == False:
            player_x = Move_Right_stop(player_x, display_width)
            Moved_Right = Moved_Right_stop()
        if player_x == goal_x and player_y == goal_y:
            gameExit = True
        
        gameDisplay.fill(black)
        Map_asset(game_map,gameDisplay)
        goal_asset(goal_x,goal_y,goal_square,gameDisplay)
        Hide_map(black_square,gameDisplay,Hardmode,Fog,player_x,player_y,black)
        Player_character(player_square,player_x,player_y,gameDisplay)

        pygame.display.update()
        clock.tick(60)