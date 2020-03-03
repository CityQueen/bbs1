a = float(input('Geben sie wert A an: '))
b = float(input('Geben sie wert B an: '))
c = float(input('Geben sie wert C an: '))

if a == 1:
    erg = (b / 2)**2 - c
    if erg > 0:
        Ostelle = '2'
    elif erg == 0:
        Ostelle = '1'
    elif erg < 0:
        Ostelle = '0'
    else:
        print('ERROR 2')
    print('Diese funktion hat', Ostelle, 'Nullstellen.')
elif a < 1 or a > 1:
    print('für diesen rechner wird A = 1 benötigt')
else:
    print('ERROR 1')