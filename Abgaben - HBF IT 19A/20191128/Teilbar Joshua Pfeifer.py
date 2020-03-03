z0 = int(input("Gebe ein wie viele Zahlen du eingeben willst: "))

gerade = []
ungerade = []

for i in range (0, z0):
    z1 = int(input("Bitte gebe eine Zahl ein: "))
    
    if(z1 % 2 == 0):
        gerade.append(z1)
        
    elif(z1 // 2 != 0):
        ungerade.append(z1)
        
gerade.sort()
ungerade.sort()

print(gerade)
print(ungerade)