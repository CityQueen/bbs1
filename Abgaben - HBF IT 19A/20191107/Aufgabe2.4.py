z1 = int(input("Geben Sie die erste Zahl ein: "))
z2 = int(input("Geben Sie die zweite Zahl ein: "))

print("Die Summe ist" , z1 + z2)
if z1 > z2:
    print("Die Differenz ist:" , z1 - z2)
elif z2 > z1:
    print("Die Differenz ist:" , z2 - z1)
    
print("Das Produkt ist:" , z1 * z2)
if z1 > z2:
    print("Der Quotient ist:" , z1 / z2)
elif z2 > z1:
    print("Der Quotient ist:" , z2 / z1)