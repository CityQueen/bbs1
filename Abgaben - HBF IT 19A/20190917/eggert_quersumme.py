Zahl =int(input("Bitte eine ganze Zahl eingeben"))
Zahl_als_String = str(Zahl)
quersumme = sum([int(i) for i in Zahl_als_String])

print(quersumme)
