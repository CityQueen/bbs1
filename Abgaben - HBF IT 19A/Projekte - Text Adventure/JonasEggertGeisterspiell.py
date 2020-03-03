from random import randint
aw = 0
z = 0
gt = randint(1, 3)
while aw != gt :
    aw = int(input("Hinter welcher Tür verbirgt sich der Geist?! Welche Tür wählst du, 1, 2 oder 3? "))
    if aw != gt :
        gt = randint(1, 3)
        z = z+1
        aw = 0
        print("Kein Geist! Du bist ein Zimmer weiter!")
    else :
        print("GEIST! LAUF SCHNELL WEG!!!")
print("GAME OVER! Dein Score:",z )
