import pygame
import time

green = (0,220,0)
red = (220,0,0)
green2 = (0,240,0)
red2 = (240,0,0)

def text_objects(text,font,colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def loose_screen(gameDisplay,display_width,display_height,clock,white,black,score):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        large_text = pygame.font.Font(None,190)
        normal_text = pygame.font.Font(None, 75)
        small_text = pygame.font.Font(None, 40)
        TextSurf, TextRect = text_objects('Game Over', large_text, white)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Score: '+str(score), normal_text, white)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 150 and mouse[0] < 350 and mouse[1] > 350 and mouse[1] < 420:
            pygame.draw.rect(gameDisplay,green2,(150,350,200,70))
            if click[0] == 1:
                return(1)
        else:
            pygame.draw.rect(gameDisplay,green,(150,350,200,70))
        if mouse[0] > 950 and mouse[0] < 1150 and mouse[1] > 350 and mouse[1] < 420:
            pygame.draw.rect(gameDisplay,red2,(950,350,200,70))
            if click[0] == 1:
                return(2)
        else:
            pygame.draw.rect(gameDisplay,red,(950,350,200,70))
        TextSurf, TextRect = text_objects('Retry', normal_text, white)
        TextRect.center = (250,385)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Quit', normal_text, white)
        TextRect.center = (1050,385)
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(30)