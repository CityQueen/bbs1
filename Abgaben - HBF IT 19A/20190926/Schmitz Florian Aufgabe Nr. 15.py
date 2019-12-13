print('Dies ist ein Niederschlagsberechner. Bitte geben sie den Nieder schlag von 3 Monaten an')

var1 = int(input("Bitte geben Sie den Niederschlag vom 1. Monat an"))
var2 = int(input("Bitte geben Sie den Niederschlag vom 2. Monat an"))
var3 = int(input("Bitte geben Sie den Niederschlag vom 3. Monat an"))

print('Nun werden wir den Durchschnitt berechnen')

var4 = var1 + var2 + var3
var5 = var4 / 3

print('Der Durchschnitt vom Niederschlag beträgt', (var5))