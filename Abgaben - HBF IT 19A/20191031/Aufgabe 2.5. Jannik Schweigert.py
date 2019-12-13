z1 = float(input('Geben sie zahl 1 ein:'))
z2 = float(input('Geben sie zahl 2 ein:'))
z3 = float(input('Geben sie zahl 3 ein:'))
# die gröste zahl herausfinden
if z1 > z2 and z1 > z3:
    gros = z1
elif z2 > z1 and z2 > z3:
    gros = z2
elif z3 > z1 and z3 > z2:
    gros = z3
else:
    print('ERROR')
# die kleinste zahl herausfinden
if z1 < z2 and z1 < z3:
    klein = z1
elif z2 < z1 and z2 < z3:
    klein = z2
elif z3 < z1 and z3 < z2:
    klein = z3
else:
    print('ERROR')
# die mittlere zahl herausfinden
if z1 > z2 and z1 < z3 or z1 < z2 and z1 > z3:
    mittel = z1
elif z2 > z1 and z2 < z3 or z2 < z1 and z2 > z3:
    mittel = z2
elif z3 > z1 and z3 < z2 or z3 < z1 and z3 > z2:
    mittel = z3
else:
    print('ERROR')
print(klein, mittel, gros)