zahl1 = [12.4,23.4,45,67.4,23,1,9,0.1928,0.9882]
zahl2 = [1,2,3,4,4,5,6,7,7,8,9,10,12,21,23,9,8,7]
zahl3 = [0.23,0.34,2.34,21.234,90.34,23.02,33.94]
worte1 = ["Hier","sind","nur","Worte","enthalten"]
worte2 = ["Hier","haben wir","einzelne","und","mehrere Worte","in der Liste"]
saetze1 =["Das ist Satz eins.","Das ist Satz zwei","Und das ist Satz drei"]

def Definition(art,wert,liste):
    if art == 0:
        for i in range(0,len(liste)):
            wert += liste[i]
        wert /= len(liste)
        print(wert)
    elif art == 1:
        for i in liste:
            if(len(i) > len(wert)):
                wert = i
        print(wert)
            
Definition(0,0,zahl1)
Definition(0,0,zahl2)
Definition(0,0,zahl3)
Definition(1,'',worte1)
Definition(1,'',worte2)
Definition(1,'',saetze1)