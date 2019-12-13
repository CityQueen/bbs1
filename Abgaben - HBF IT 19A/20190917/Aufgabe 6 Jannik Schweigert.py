import time
print('Gib Länge A an')
LängeA = int(input('Länge A:'))
print('Gib Länge B an')
LängeB = int(input('Länge B:'))
print('Was wllst du berechnen?')
Art = input('Umfang oder Flächeninhalt:')
if Art == 'Umfang':
    Umfang = (LängeA*(2))+(LängeB*(2))
    print(Umfang)
    time.sleep(3)
    quit()
elif Art == 'Flächeninhalt':
    Flächeninhalt = LängeA*LängeB
    print(Flächeninhalt)
    time.sleep(3)
    quit()
else:
    print('FEHLER 404: Inteligenz nicht gefunden')
    print('Beende Prozess...')
    time.sleep(3)
    quit()