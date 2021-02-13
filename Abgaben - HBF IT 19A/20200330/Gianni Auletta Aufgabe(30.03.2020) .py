zahl1 = [1,2.4,32,23.6,23,45.0,0.22234,32,34.036257,00.3389832]
zahl2 = [32.323,23,24335.232,35.2424,24423,424,46,3,43.553,24,4]
zahl3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
worte1 = ['Hallo','mir','geht','es','gut']
worte2 = ['hey','mir','geht es','gut','und dir?']
saetze1 = ['hallo how are you?','I am fine and you?']

def CalculateNumbers(zahlenliste):
    # Berechne Mittelwert und gebe ihn aus
    mwert = 0
    for i in range(0,len(zahlenliste)):
        mwert +=zahlenliste[i]
    mwert /=len(zahlenliste)
    print('Mittelwert:',mwert)
    
    #Berechne Minimum und gebe es aus
    minimum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if minimum > zahlenliste[i]:
            minimum = zahlenliste[i]
    print('Minimum:',minimum)
    
    #Berechne Maximum und gebe es aus
    maximum = zahlenliste[0]
    for i in range(0,len(zahlenliste)):
        if maximum < zahlenliste[i]:
            maximum = zahlenliste[i]
    print('Maximum:',maximum)
    
def CalculateStrings(wortliste):
    #Bestimme den längsten String und gebe ihn aus
    longest = ''
    for wort in wortliste:
        if len(longest) < len(wort):
            longest = wort
    print('Längster String:',longest)
    
CalculateNumbers(zahl1)
CalculateNumbers(zahl2)
CalculateNumbers(zahl3)

CalculateStrings(worte1)
CalculateStrings(worte2)
CalculateStrings(saetze1)