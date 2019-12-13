print('1 für Addition')
print('2 für Subtraktion')
print('3 für Multiplikation')
print('4 für Division')
rechenart = input('Gib eine rechenart an:')
if rechenart == '1':
    zahl1 = float(input('Gib die erste zahl der gewünschten rechenart an:'))
    zahl2 = float(input('Nun die zweite:'))
    Ergebnis = zahl1+zahl2
    print(Ergebnis)
elif rechenart == '2':
    zahl1 = float(input('Gib die erste zahl der gewünschten rechenart an:'))
    zahl2 = float(input('Nun die zweite:'))
    Ergebnis = zahl1-zahl2
    print(Ergebnis)
elif rechenart == '3':
    zahl1 = float(input('Gib die erste zahl der gewünschten rechenart an:'))
    zahl2 = float(input('Nun die zweite:'))
    Ergebnis = zahl1*zahl2
    print(Ergebnis)
elif rechenart == '4':
    zahl1 = float(input('Gib die erste zahl der gewünschten rechenart an:'))
    zahl2 = float(input('Nun die zweite:'))
    Ergebnis = zahl1/zahl2
    print(Ergebnis)
else:
    print('Dies ist keine der zur verfügung stehenden rechenarten')