import pygame
import random
from Starting_screen import *
from Tutorial_map import *
from map_1 import *
from loose_screen import *

pygame.init()
display_width = 1280
display_height = 720
black = (0,0,0)
white = (255,255,255)
Moved_Right = False
Moved_Left = False
Moved_Up = False
Moved_Down = False
First = True
Tutorial = True
score = 0
Loop_stop = False
Hardmode = 0
lose = False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Labyrinthion')
clock = pygame.time.Clock()
        
while not Loop_stop:
    level_number = random.randint(1,1)
    if First == True:
        First = False
        Hardmode = starting_screen(gameDisplay,display_width,display_height,clock,white,black,Hardmode)
    elif Tutorial == True:
        Tutorial = False
        tutorial_loop(clock,Moved_Up,Moved_Down,Moved_Right,Moved_Left,black,gameDisplay,display_width,display_height,Hardmode)
        list_clear()
    elif lose == True:
        retry = loose_screen(gameDisplay,display_width,display_height,clock,white,black,score)
        First = True
        Tutorial = True
        if retry == 1:
            score = 0
        elif retry == 2:
            Loop_stop = True
    if Tutorial == False and First == False and level_number == 1:
        won = map_1_loop(clock,Moved_Up,Moved_Down,Moved_Right,Moved_Left,black,gameDisplay,display_width,display_height,Hardmode)
        list_clear()
        if won == 1:
            score += 1
        elif won == 2:
            lose = True
pygame.quit()
quit()