zahl1 = [12.4,23.4,45,67.4,23,1,9,0.1928,0.9882]
zahl2 = [1,2,3,4,4,5,6,7,7,8,9,10,12,21,23,9,8,7]
zahl3 = [0.23,0.34,2.34,21.234,90.34,23.02,33.94]
worte1 = ["Hier","sind","nur","Worte","enthalten"]
worte2 = ["Hier","haben wir","einzelne","und","mehrere Worte","in der Liste"]
saetze1 =["Das ist Satz eins.","Das ist Satz zwei","Und das ist Satz drei"]

def pillepalle (welcheliste):
    mwert1 = 0
    for i in range(0, len(welcheliste)):
        mwert1 += welcheliste[i]
    mwert1 /= len(welcheliste)
    print(mwert1)

def pallepille (welcheliste):
    long1 = ""
    for wort in welcheliste:
        if (len(wort) > len(long1)):
            long1 = wort
    print(long1)
pillepalle(zahl1)
pillepalle(zahl2)
pillepalle(zahl3)
pallepille(worte1)
pallepille(worte2)
pallepille(saetze1)