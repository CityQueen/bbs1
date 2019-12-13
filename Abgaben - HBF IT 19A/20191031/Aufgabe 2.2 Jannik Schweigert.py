z1 = float(input('Geben sie eine zahl ein:'))
z2 = float(input('Geben sie eine zahl ein:'))

if z1 > 0 or z1 < 0 and z2 > 0 or z2 < 0:
    gros = max(z1,z2)
    klein = min(z1,z2)
    
    erg = gros / klein
    print(erg, 'ist das Ergebnis')
else:
    print('es darf keine 0 vorhanden sein')