z1 = int(input("Bitte gebe ein wie viele Zahlen du eingeben willst:"))

l1 = []

for i in range(0, z1):
    z1 = int(input("Bitte gebe eine Zahl ein: "))
    l1.append(z1)
    
l1.reverse()

print(l1)