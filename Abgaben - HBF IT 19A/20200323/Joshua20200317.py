from random import randint

zahlenliste = []

for zahl in range (randint(5, 5)):
    zahlenliste.append(randint(1, 100000))
    
zahlenliste.sort()

print(zahlenliste)

if len(zahlenliste) == 5:
    print("\nDie kleinste Zahl ist die: ", zahlenliste[0])
    print("\nDie mittlere Zahl ist die: ", zahlenliste[2])
    print("\nDie größte Zahl ist die: ", zahlenliste[4])
    
# Aufgabe b hab ich versucht aber nicht geschafft