z1 = int(input("Geben Sie bitte ein zahl ein: "))
z2 = int(input("Geben Sie bitte noch ein zahl ein: "))
z3 = int(input("Geben Sie noch ein zahl ein: "))
z4 = int(input("Und geben Sie noch ein zahl ein: "))

if z1 < z2 and z1 < z3 and z1 < z4:
    print("Die kleinste zahl ist " , z1)
elif z2 < z1 and z2 < z3 and z2 < z4:
    print("Die kleinste zahl ist " , z2)
elif z3 < z1 and z3 <z2 and z3 < z4:
    print("Die kleinste zahl ist " , z3)
elif z4 < z1 and z4 < z2 and z4 < z3:
    print("Die kleinste zahl ist " , z4)