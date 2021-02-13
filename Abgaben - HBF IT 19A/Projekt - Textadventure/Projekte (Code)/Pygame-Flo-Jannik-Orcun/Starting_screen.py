import pygame
import time

green = (0,220,0)
yellow = (220,220,0)
red = (220,0,0)
green2 = (0,240,0)
yellow2 = (240,240,0)
red2 = (240,0,0)

def text_objects(text,font,colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def starting_screen(gameDisplay,display_width,display_height,clock,white,black, Hardmode):
    time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        large_text = pygame.font.Font(None,190)
        normal_text = pygame.font.Font(None, 75)
        small_text = pygame.font.Font(None, 40)
        TextSurf, TextRect = text_objects('Labyrintion', large_text, white)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 150 and mouse[0] < 350 and mouse[1] > 350 and mouse[1] < 600:
            pygame.draw.rect(gameDisplay,green2,(150,350,200,250))
            if click[0] == 1:
                return(1)
        else:
            pygame.draw.rect(gameDisplay,green,(150,350,200,250))
        if mouse[0] > 550 and mouse[0] < 750 and mouse[1] > 350 and mouse[1] < 600:
            pygame.draw.rect(gameDisplay,yellow2,(550,350,200,250))
            if click[0] == 1:
                return(2)
        else:
            pygame.draw.rect(gameDisplay,yellow,(550,350,200,250))
        if mouse[0] > 950 and mouse[0] < 1150 and mouse[1] > 350 and mouse[1] < 600:
            pygame.draw.rect(gameDisplay,red2,(950,350,200,250))
            if click[0] == 1:
                return(3)
        else:
            pygame.draw.rect(gameDisplay,red,(950,350,200,250))
        TextSurf, TextRect = text_objects('EASY', normal_text, white)
        TextRect.center = (250,385)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Time: 30s', small_text, white)
        TextRect.center = (220,450)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('View: seen', small_text, white)
        TextRect.center = (227,500)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Normal', normal_text, white)
        TextRect.center = (650,385)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Time: 25s', small_text, white)
        TextRect.center = (620,450)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('View: Fog', small_text, white)
        TextRect.center = (623,500)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Hard', normal_text, white)
        TextRect.center = (1050,385)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Time: 20s', small_text, white)
        TextRect.center = (1020,450)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('View: Blind', small_text, white)
        TextRect.center = (1030,500)
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(30)