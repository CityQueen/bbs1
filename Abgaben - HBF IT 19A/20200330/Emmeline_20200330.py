zahl1 = [12.4,23.4,45,67.4,23,1,9,0.1928,0.9882]
zahl2 = [1,2,3,4,4,5,6,7,7,8,9,10,12,21,23,9,8,7]
zahl3 = [0.23,0.34,2.34,21.234,90.34,23.02,33.94]
worte1 = ["Hier","sind","nur","Worte","enthalten"]
worte2 = ["Hier","haben wir","einzelne","und","mehrere Worte","in der Liste"]
saetze1 =["Das ist Satz eins.","Das ist Satz zwei","Und das ist Satz drei"]

def Zahlenwerte (zahl) :
    print("\nVon der Liste:",zahl)
    mwert = 0
    for i in range(0,len(zahl)):
        mwert += zahl[i]
        mwert /= len(zahl)
    print("Mittelwert:",mwert)
    
    minw = zahl[0]
    for i in range(0,len(zahl)):
        if minw > zahl[i]:
            minw = zahl[i]
    print("Kleinste Zahl:", minw)
    
    maxw = zahl[0]
    for i in range(0,len(zahl)):
        if maxw < zahl[i]:
            maxw = zahl[i]
    print("Größte Zahl:", maxw)
    
def Wortwerte (worte):
    print("\nVon der Liste:",worte)
    long = ""
    for wort in worte:
        if(len(wort) > len(long)):
            long = wort
    print("Längstes Wort/Satz:",long)

Zahlenwerte (zahl1)
Zahlenwerte (zahl2)
Zahlenwerte (zahl3)
Wortwerte (worte1)
Wortwerte (worte2)
Wortwerte (saetze1)