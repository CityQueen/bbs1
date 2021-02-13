import random
import time

#Einleitung
print('+-------------------------+'); time.sleep(0.3)
print('| SCHERE | STEIN | PAPIER |'); time.sleep(0.3)
print('+-------------------------+\n\n'); time.sleep(0.3)

#Variablen
figuren = ('Schere','Stein','Papier')
spielen = True

while spielen:
    
    #Spielerfigur auswählen
    spielerauswahl = 0
    while spielerauswahl not in (1,2,3):
        spielerauswahl = int(input('[1]Schere [2]Stein [3]Papier\n'))
    spielerfigur = figuren[spielerauswahl - 1]
    
    #Computerfigur auswählen
    computerfigur = figuren[random.randint(0,2)]
    
    #Sieger ermitteln
    if spielerfigur == computerfigur:
        print('Unentschieden! Computer wählte', computerfigur)
    else :
        if spielerfigur == 'Schere':
            if computerfigur == 'Stein':
                print('Verloren! Computer wählte', computerfigur)
            else:
                print('Gewonnen! Computer wählte', computerfigur)
        if spielerfigur == 'Stein':
            if computerfigur == 'Schere':
                print('Gewonnen! Computer wählte', computerfigur)
            else:
                print('Verloren! Computer wählte', computerfigur)
                
        if spielerfigur == 'Papier':
            if computerfigur == 'Schere':
                print('Verloren! Computer wählte', computerfigur)
            else:
                print('Gewonnen! Computer wählte', computerfigur)
                
    #Restart
    time.sleep(1)
    entscheidung = ''
    while entscheidung not in ('j','n'):
        entscheidung = input('\nNochmal spielen? (j)Ja (n)Nein')
    
    if(entscheidung == 'n'):
        spielen = False