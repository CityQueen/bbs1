zahl1 = [55,0.3215,2.854,25,0.7896,98,0.9998877,0.54]
zahl2 = [9,5,8,7,4,1,2,3,5,4,88,5,1,4,5,8,6,5,2,5]
zahl3 = [2.28,5.54,7.4,88.254,100.54,57.521,55.51]
def CalculateNumbers(zahlenliste):
    wert = 0
    for i in range(0,len(zahlenliste)):
        wert += zahlenliste[i]
    wert /= len(zahlenliste)
    print('Mittelwert: ', wert)
    
    mini = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if mini > zahlenliste[i]:
            mini = zahlenliste[i]
    print('Minimum: ', mini)
    
    maxi = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if maxi < zahlenliste[i]:
            maxi = zahlenliste[i]
    print('Maximum: ', maxi)
worte1 = ["Hier","sind","nur","Vokabel"]
worte2 = ["Hier sind","einzelne","und","mehrere Vokabeln"]
saetze1 =["Das ist Satz,"," das ist Satz andere,"," und das ist letzte"]
def CalculateStrings(wortl):
    longest = ""
    for wort in wortl:
        if len(longest) < len(wort):
            longest = wort
    print('Längster String: ',longest)

CalculateNumbers(zahl1)
CalculateNumbers(zahl2)
CalculateNumbers(zahl3)

CalculateStrings(worte1)
CalculateStrings(worte2)
CalculateStrings(saetze1)