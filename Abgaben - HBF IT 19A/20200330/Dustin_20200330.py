zahl1 = [12.3,221.4,3.5,237.4,204,1,29,0.19228,0.91882]
zahl2 = [31,22,0.3,4,4,5,6,7,7,8,9,10,12,21,23,39,0.28,7]
zahl3 = [0.23,0.44,2.324,121.234,20.34,63.02,13.94]
worte1 = ["Test12","Test123","Test1234","Test12345","Test1234567"]
worte2 = ["No Sad","No Bad","Days","in","LA","Killy underrated"]
saetze1 =["Balenci","Balenci Balenci","Balenci Balenci Balenci Balenci"]


def CalculateNumbers(zahlenliste):

    mwert = 0
    for i in range(0,len(zahlenliste)):
        mwert += zahlenliste[i]
    mwert /= len(zahlenliste)
    print('Mittelwert: ', mwert)
    
    
    minimum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if minimum > zahlenliste[i]:
            minimum = zahlenliste[i]
    print('Minimum: ', minimum)
    
    
    maximum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if maximum < zahlenliste[i]:
            maximum = zahlenliste[i]
    print('Maximum: ', maximum)

def CalculateStrings(wortliste):
   
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