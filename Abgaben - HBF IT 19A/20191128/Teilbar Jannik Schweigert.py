z1 = int(input('Gib eine zahl ein:'))
z2 = int(input('Gib eine zahl ein:'))
z3 = int(input('Gib eine zahl ein:'))
z4 = int(input('Gib eine zahl ein:'))
z5 = int(input('Gib eine zahl ein:'))
z6 = int(input('Gib eine zahl ein:'))
z7 = int(input('Gib eine zahl ein:'))
z8 = int(input('Gib eine zahl ein:'))
z9 = int(input('Gib eine zahl ein:'))
z10 = int(input('Gib eine zahl ein:'))

gerade =[]
ungerade =[]

if z1 % 2 == 0:
    gerade.append(z1)
else:
    ungerade.append(z1)
if z2 % 2 == 0:
    gerade.append(z2)
else:
    ungerade.append(z2)
if z3 % 2 == 0:
    gerade.append(z3)
else:
    ungerade.append(z3)
if z4 % 2 == 0:
    gerade.append(z4)
else:
    ungerade.append(z4)
if z5 % 2 == 0:
    gerade.append(z5)
else:
    ungerade.append(z5)
if z6 % 2 == 0:
    gerade.append(z6)
else:
    ungerade.append(z6)
if z7 % 2 == 0:
    gerade.append(z7)
else:
    ungerade.append(z7)
if z8 % 2 == 0:
    gerade.append(z8)
else:
    ungerade.append(z8)
if z9 % 2 == 0:
    gerade.append(z9)
else:
    ungerade.append(z9)
if z10 % 2 == 0:
    gerade.append(z10)
else:
    ungerade.append(z10)

gerade.sort()
ungerade.sort()
print(gerade)
print(ungerade)