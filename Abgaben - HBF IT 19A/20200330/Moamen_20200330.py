zahl1 = [95,5.145,8,8.965,7.6,5.98,7452,25.51]
zahl2 = [5.41,8.2,51.252,7.465,6.652,352.3652]
zahl3 = [5,4,2,1,8,25,2,65,89,875,5,8,57,81,6,4,3,45]
def CalculateNumbers(liste):
    mw = 0
    for i in range(0,len(liste)):
        mw += liste[i]
    mw /= len(liste)
    print('Mittelwert: ',mw)
    min = liste[0]
    for i in range(0,len(liste)):
        if min > liste[i]:
            min = liste[i]
    print('Minimum: ', min)
    max = liste[0]
    for i in range(0,len(liste)):
        if max < liste[i]:
            max = liste[i]
    print('Maximum: ', max)
CalculateNumbers(zahl1)
CalculateNumbers(zahl2)
CalculateNumbers(zahl3)    
worte = ["Hallo","Hi","Wort","Wörte"]
saetze =["Ich heiße Moamen","Wie heißt du?"]
worteS =["Hallo","Wie grhts dir?","gut","und","wie gehts dir?","auch gut danke"]
def CalculateStrings(wortliste):
    longest = ""
    for wort in wortliste:
        if len(longest) < len(wort):
            longest = wort
    print('Längster String: ',longest)
CalculateStrings(worte)
CalculateStrings(worteS)
CalculateStrings(saetze)