zahl1 = [12.4,23.4,45,67.4,23,1,9,0.1928,0.9882]
zahl2 = [1,2,3,4,4,5,6,7,7,8,9,10,12,21,23,9,8,7]
zahl3 = [0.23,0.34,2.34,21.234,90.34,23.02,33.94]
worte1 = ["Hier","sind","nur","Worte","enthalten"]
worte2 = ["Hier","haben wir","einzelne","und","mehrere Worte","in der Liste"]
saetze1 =["Das ist Satz eins.","Das ist Satz zwei","Und das ist Satz drei"]


def CalculateNumbers(zahlenliste):
    # Berechne Mittelwert und gebe ihn aus
    mwert = 0
    for i in range(0,len(zahlenliste)):
        mwert += zahlenliste[i]
    mwert /= len(zahlenliste)
    print('Mittelwert: ', mwert)
    
    # Berechne Minimum und gebe es aus
    minimum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if minimum > zahlenliste[i]:
            minimum = zahlenliste[i]
    print('Minimum: ', minimum)
    
    # Berechne Maximum und gebe es aus
    maximum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if maximum < zahlenliste[i]:
            maximum = zahlenliste[i]
    print('Maximum: ', maximum)

def CalculateStrings(wortliste):
    # Bestimme den längsten String und gebe ihn aus
    longest = ""
    for wort in wortliste:
        if len(longest) < len(wort):
            longest = wort
    print('Längster String: ',longest)

CalculateNumbers(zahl1)
CalculateNumbers(zahl2)
CalculateNumbers(zahl3)

CalculateStrings(worte1)
CalculateStrings(worte2)
CalculateStrings(saetze1)