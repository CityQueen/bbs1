z1 = int(input("Geben Sie eine Zahl ein: "))
z2 = int(input("Geben Sie noch eine Zahl ein: "))
z3 = int(input("Geben Sie nun noch eine Zahl ein: "))

if z1 > z2 and z1 > z3 and z2 > z3:
    print("Die großeste Zahl ist" , z1 , ", die mittlere zahl ist" , z2 , "und die kleineste Zahl ist" , z3 ,)
elif z1 > z2 and z1 > z3 and z3 > z2:
    print("Die großeste Zahl ist" , z1 , ", die mittlere zahl ist" , z3 , "und die kleineste Zahl ist" , z2 ,)
elif z2 > z1 and z2 > z3 and z1 > z3:
    print("Die großeste Zahl ist:" , z2 , ", die mittlere zahl ist:" , z1 , "und die kleineste Zahl ist:" , z3 ,)
elif z2 > z1 and z2 > z3 and z3 > z1:
    print("Die großeste Zahl ist:" , z2 , ", die mittlere zahl ist:" , z3 , "und die kleineste Zahl ist:" , z1 ,)
elif z3 > z1 and z3 > z2 and z1 > z2:
    print("Die großeste Zahl ist:" , z3 , ", die mittlere zahl ist:" , z1 , "und die kleineste Zahl ist:" , z2 ,)
elif z3 > z1 and z3 > z2 and z2 > z1:
    print("Die großeste Zahl ist:" , z3 , ", die mittlere zahl ist:" , z2 , "und die kleineste Zahl ist:" , z1 ,)
    