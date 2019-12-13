z1 = int(input("Bitte gebe die erste Zahl ein"))
print("plus +")
print("minus -")
print("mal *")
print("geteilt /")
Z1 = str(input("Bitte gebe eines dieser Zeichen ein"))

z2 = int(input("Bitte gebe die zweite Zahl ein"))

if (Z1 == "+"):
    e1 = z1 + z2
    print("Das Ergebnis ist", e1) 

if (Z1 == "-"):
    e2 = z1 - z2
    print("Das Ergebnis ist", e2)
    
if (Z1 == "/"):
    e3 = z1 / z2
    print("Das Ergebnis ist", e3)
    
if (Z1 == "*"):
    e4 = z1 * z2
    print("Das Ergebnis ist", e4)