gerade = []
ungerade = []
for i in range(10):
    a = int(input("Geben sie Bitte eine Ganze Zahl ein"))
    if a % 2 == 0:
        gerade.append(a)
    else:
        ungerade.append(a)
print(len(ungerade))
print(len(gerade))
fliesskomma = []
for i in range(10):
    a = float(input("Geben sie bitte eine Fließkommazahl ein"))
    fliesskomma.append(a)
fliesskomma.sort()
print(fliesskomma)
istrichtigestelle = []
ganzzahl = []
for i in range(15):
    a = int(input("Geben sie bitte eine ganze Zahl zwischen 0 und 14 ein"))
    ganzzahl.append(a)
    if ganzzahl[a] == a:
        a = str(a)
        a = (a," ist an ",a,"ter Stelle")
    else:
        a = str(a)
        a = (a,"ist nicht an ",a,"ter Stelle")
    istrichtigestelle.append(a)
    print(istrichtigestelle[i])
negativezahlen = []
positivezahlen = []
nullen = []
for i in range(10):
    a = float(input("Geben sie bitte eine Zahl ein (negativ oder positiv)"))
    if a > 0:
        positivezahlen.append(a)
    elif a < 0:
        negativezahlen.append(a)
    else:
        nullen.append(a)
if len(positivezahlen) > len(negativezahlen):
    print("Sie haben mehr positive Zahlen eingegeben")
elif len(positivezahlen) < len(negativezahlen):
    print("Sie haben mehr negative Zahlen eingegeben")
else:
    print("Sie haben gleich viele negative wie positive Zahlen eingegeben")

