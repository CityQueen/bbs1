VariableZa1 = [12.4,23.4,45,67.4,23,1,9,0.1928,0.9882]
VariableZa2 = [1,2,3,4,4,5,6,7,7,8,9,10,12,21,23,9,8,7]
VariableZa3 = [0.23,0.34,2.34,21.234,90.34,23.02,33.94]
VariableWo1 = ["Hier","sind","nur","Worte","enthalten"]
VariableWo2 = ["Hier","haben wir","einzelne","und","mehrere Worte","in der Liste"]
VariableSa1 =["Das ist Satz eins.","Das ist Satz zwei","Und das ist Satz drei"]


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

CalculateNumbers(VariableZa1)
CalculateNumbers(VariableZa2)
CalculateNumbers(VariableZa3)

CalculateStrings(VariableWo1)
CalculateStrings(VariableWo2)
CalculateStrings(VariableSa1)