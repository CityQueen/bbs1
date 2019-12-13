import time
modus = input('Wähle den modus: Taschenrechner, Potenzrechner')
if modus == 'Taschenrechner':
    print('Gib zahl 1 an')
    zahl1 = int(input('Zahl 1:'))
    print('Gib zahl 2 an')
    zahl2 = int(input('Zahl 2:'))
    print('Gib zahl 3 an')
    time.sleep(0.2)
    print('Wenn diese zahl nicht benötigt wird, gib 0 für Plus und Minus an, und 1 für Mahl und Geteilt.')
    zahl3 = int(input('Zahl 3:'))
    print('Wähle deine Rechenart. (Plus, Minus, Mahl, Geteilt')
    rechenart = input('Rechenart:')
    if rechenart == 'Plus':
        Ergebnis = zahl1+zahl2+zahl3
        print(Ergebnis)
        time.sleep(3)
        quit()
    elif rechenart == 'Minus':
        Ergebnis = zahl1-zahl2-zahl3
        print(Ergebnis)
        time.sleep(3)
        quit()
    elif rechenart == 'Mahl':
        Ergebnis = zahl1*zahl2*zahl3
        print(Ergebnis)
        time.sleep(3)
        quit()
    elif rechenart == 'Geteilt':
        Ergebnis = zahl1/zahl2/zahl3
        print(Ergebnis)
        time.sleep(3)
        quit()
    else:
        print('FEHLER 404: Inteligenz nicht gefunden')
        print('Beende Prozess...')
        time.sleep(3)
        quit()
elif modus == 'Potenzrechner':
    Basis = int(input('Gib die Basis an'))
    Potenz = int(input('Gib die Potenz an'))
    Ergebnis = Basis**Potenz
    print(Ergebnis)
    time.sleep(3)
    quit()
else:
    print('FEHLER 101: Inteligenz nicht gefunden')
    print('Beende Prozess...')
    time.sleep(3)
    quit()