def Quersumme(zahl):
    result = 0
    while zahl: # solange Zahl nicht Null ist
        result += zahl % 10 # Zahl modulo 10 zum Ergebnis
        zahl = int(zahl / 10) # Zahl durch 10 Dividieren
    return result # Ergebnis zurueckgeben


eingabe = int(input("Zahl eingeben: "))
q = Quersumme(eingabe)
q = Quersumme(q)
print("Die Quersumme von ", eingabe, 'ist:', q)