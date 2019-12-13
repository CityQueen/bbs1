print('Bitte geben sie Länge, Breite und Tiefe vom Schwimmbecken an um die Wassermenge zu berechnen')

Länge = float(input('Bitte geben sie die Länge an'))
Breite = float(input('Bitte geben sie die Breite an'))
Tiefe = float(input('Bitte geben sie die Tiefe an'))

var1 = Länge * Breite
var2 = var1 * Tiefe

print('Sie brauchen', var2 "Liter Wasser")