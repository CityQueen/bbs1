zahl1 = [12.4,23.4,45,67.4,23,1,9,0.1928,0.9882]
zahl2 = [1,2,3,4,4,5,6,7,7,8,9,10,12,21,23,9,8,7]
zahl3 = [0.23,0.34,2.34,21.234,90.34,23.02,33.94]
worte1 = ["Hier","sind","nur","Worte","enthalten"]
worte2 = ["Hier","haben wir","einzelne","und","mehrere Worte","in der Liste"]
saetze1 =["Das ist Satz eins.","Das ist Satz zwei","Und das ist Satz drei"]


def nummern(zahlenliste):
    mwert = 0
    for i in range(0,len(zahlenliste)):
        mwert += zahlenliste[i]
    mwert /= len(zahlenliste)
    print('Der Mittelwert ist: ', mwert)
    
    minimum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if minimum > zahlenliste[i]:
            minimum = zahlenliste[i]
    print('Der Minimumwert ist: ', minimum)
    
    maximum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if maximum < zahlenliste[i]:
            maximum = zahlenliste[i]
    print('Der Maximumwert ist: ', maximum)

def woerter(wortliste):
    longest = ""
    for wort in wortliste:
        if len(longest) < len(wort):
            longest = wort
    print('Der längste String ist: ',longest)

nummern(zahl1)
nummern(zahl2)
nummern(zahl3)

woerter(worte1)
woerter(worte2)
woerter(saetze1)