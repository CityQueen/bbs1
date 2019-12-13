z1 = int(input("Bitte gebe die Erste Zahl ein"))
z2 = int(input("Bitte gebe die Zweite Zahl ein"))
z3 = int(input("Bitte gebe die Dritte Zahl ein"))
z4 = int(input("Bitte gebe die Vierte Zahl ein"))

if (z1 < z2 and z1 < z3 and z1 < z4):
    print(z1, "Die Erste Zahl ist die Kleinste")

if (z2 < z1 and z2 < z3 and z2 < z4):
    print(z2, "Die Zweite Zahl ist die Kleinste")
    
if (z3 < z1 and z3 < z2 and z3 < z4):
    print(z3, "Die Dritte Zahl ist die Kleinste")
    
if (z4 < z1 and z4 < z2 and z4 < z3):
    print(z4, "Die Vierte Zahl ist die Kleinste")