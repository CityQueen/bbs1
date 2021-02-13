liste1 = [1,4,78,3,56,89,3]
liste2 = [2,4,8,34,5,9,3,76,23,9]
liste3 = ['Halli','Hallu','Hallo']
liste4 = ['Nope','Dope','Hope']
liste5 = ['Use what i have','and you dont','a functining liver','depth perception and a pulse']
liste6 = ['you are an amateur','and a fool']
try:
    if liste1[0] == int(liste1[0]):
        Var = int((((int(len(liste1))/2)-0.5)))
        print('Erstes:',liste1[0],'  Mittleres:',liste1[Var],'  Letztes',liste1[(len(liste1)-1)])
except ValueError:
    count = -1
    Var = 0
    for i in range(0,len(liste1)):
        count += 1
        Var1 = liste1[i]
        if Var < len(Var1):
            Var = len(Var1)
            count1 = count
    print(liste1[count1])
try:
    if liste2[0] == int(liste2[0]):
        Var = int((((int(len(liste2))/2)-0.5)))
        print('Erstes:',liste2[0],'  Mittleres:',liste2[Var],'  Letztes',liste2[(len(liste2)-1)])
except ValueError:
    count = -1
    Var = 0
    for i in range(0,len(liste2)):
        count += 1
        Var1 = liste2[i]
        if Var < len(Var1):
            Var = len(Var1)
            count1 = count
    print(liste2[count1])
try:
    if liste3[0] == int(liste3[0]):
        Var = int((((int(len(liste3))/2)-0.5)))
        print('Erstes:',liste3[0],'  Mittleres:',liste3[Var],'  Letztes',liste3[(len(liste1)-1)])
except ValueError:
    count = -1
    Var = 0
    for i in range(0,len(liste3)):
        count += 1
        Var1 = liste3[i]
        if Var < len(Var1):
            Var = len(Var1)
            count1 = count
    print(liste3[count1])
try:
    if liste4[0] == int(liste4[0]):
        Var = int((((int(len(liste4))/2)-0.5)))
        print('Erstes:',liste4[0],'  Mittleres:',liste4[Var],'  Letztes',liste4[(len(liste1)-1)])
except ValueError:
    count = -1
    Var = 0
    for i in range(0,len(liste4)):
        count += 1
        Var1 = liste4[i]
        if Var < len(Var1):
            Var = len(Var1)
            count1 = count
    print(liste4[count1])
try:
    if liste5[0] == int(liste5[0]):
        Var = int((((int(len(liste5))/2)-0.5)))
        print('Erstes:',liste5[0],'  Mittleres:',liste5[Var],'  Letztes',liste5[(len(liste1)-1)])
except ValueError:
    count = -1
    Var = 0
    for i in range(0,len(liste5)):
        count += 1
        Var1 = liste5[i]
        if Var < len(Var1):
            Var = len(Var1)
            count1 = count
    print(liste5[count1])
try:
    if liste6[0] == int(liste6[0]):
        Var = int((((int(len(liste6))/2)-0.5)))
        print('Erstes:',liste6[0],'  Mittleres:',liste6[Var],'  Letztes',liste6[(len(liste1)-1)])
except ValueError:
    count = -1
    Var = 0
    for i in range(0,len(liste6)):
        count += 1
        Var1 = liste6[i]
        if Var < len(Var1):
            Var = len(Var1)
            count1 = count
    print(liste6[count1])
