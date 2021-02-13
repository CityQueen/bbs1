# Shane,Basti und Leon "NEANDERTALER"

from random import randint

print('Neandertaler lost in cave')
print('Lets go')

du_bist_ein_Neandertaler = True
score = 0

while du_bist_ein_Neandertaler:
    baerenhoehle = randint(1, 3)
    #fallenhoele = randint(4, 6)
    print(' ')
    print('Du hast die Wahl zwichen 3 Höhleneingängen.')
    print('In einer Höhle ist ein Bär.')
    #print('In einer Höhle ist eine Falle.')
    print('Welchen Eingang wählst du?')
    eingang = input('1, 2 oder 3? ')
    eingang_nummer = int(eingang)
    #eingang2 = input('4, 5 oder 6?')
    #eingang_nummer2 = int(eingang2)
    
    if eingang_nummer == baerenhoehle:
        print('!!Bär!!')
        print('Lauf du Neandertaler!')
        du_bist_ein_Neandertaler = False
        
    #elif eingang_nummer2 == fallenhoehle:
        #print('!!Falle!!')
        #print('Du bist verletzt aber dennoch weiter!')
        #du_bist_ein_Neandertaler = False
        #score = score -1
        
    else:
        print('Kein Bär!')
        print('Du hast dich verlaufen finde einen neuen Weg.')
        score = score + 1

print(' ')
print('Game over! Deine Punkte: ', score)


# Wir haben uns beiunserem Spiel 'NEANDERTALER' an dem von ihnen vorgegebene
# Geisterspiel orientiert.
# Mit der elif Bedingung haben wir noch ein kleines Problem vielleicht können
# Sie uns noch im nachhinein einen entscheidenen Tipp für die Lösung des
# Problems geben:))