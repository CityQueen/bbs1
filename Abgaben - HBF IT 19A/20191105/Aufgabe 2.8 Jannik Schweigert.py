a = float(input('Geben sie wert A an: '))
b = float(input('Geben sie wert B an: '))
c = float(input('Geben sie wert C an: '))

if a > 0:
    öffnung = 'nach oben geöfnet'
elif a < 0:
    öffnung = 'nach unten geöfnet'
elif a == 0:
    print('a kan nicht 0 sein')
else:
    print('ERROR 1')

if a > 1:
    richtung = 'und sie ist gestreckt.'
elif a < 1:
    richtung = 'und sie ist gestaucht.'
elif a == 1:
    richtung = 'und es ist eine normalparabel.'
else:
    print('ERROR 2')

Ostelle = (b/(2*a))**2-(c/a)
if Ostelle > 0:
    Ost = '2'
elif Ostelle == 0:
    Ost = '1'
elif Ostelle < 0:
    Ost = '0'
print('Diese Quadratische Fuktion ist', öffnung, richtung, ' Sie hat auserdem', Ost, 'Nullstellen.')